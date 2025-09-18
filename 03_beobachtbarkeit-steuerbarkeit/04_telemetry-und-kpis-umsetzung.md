---
title: Telemetry & KPIs – Umsetzung mit OKW-Style Keywords
description: Event-Schema, Budgets, Polling, Spinner/Busy-Signale, SLOs und CI-Gates. Mit YAML- und Robot-Beispielen.
tags: [telemetry, kpi, okw4robot, robotframework, steuerbarkeit, beobachtbarkeit]
status: In Bearbeitung
type: technik
---

# Telemetry & KPIs – Umsetzung mit OKW-Style Keywords

Ziel: **Messen, nicht raten.** Jedes Keyword liefert Telemetry; KPIs werden pro Seite/Widget/Keyword berechnet und in der CI überwacht.

## 1) Event-Schema (minimal)

| Feld | Beispiel | Zweck |
|---|---|---|
| `run_id`, `suite`, `test` | `2025-09-18T09:10Z-42`, `Expenses Suite`, `Create New Expense Report` | Korrelation |
| `page` | `TravelExpenses` | Scope |
| `keyword` | `Click` | Aktion |
| `locator_name`, `locator_category`, `locator_id` | `Save`, `Button`, `button.save` | Identität |
| `start_ts`, `end_ts`, `duration_ms` | `...`, `...`, `742` | Dauer |
| `timeout_budget_ms` | `2000` | Budget |
| `wait_breakdown_ms` | `{spinner:0, network_idle:350, visibility:180, settle:120}` | Wofür gewartet |
| `retries` | `4` | Poll-Versuche |
| `result`, `error_class` | `PASS`/`TIMEOUT`, `StaleElement` | Outcome |

**Beispiel (JSON-Line):**
```json
{"page":"TravelExpenses","keyword":"Click","locator_name":"Save","locator_category":"Button","duration_ms":742,"timeout_budget_ms":2000,"wait_breakdown_ms":{"network_idle":350,"visibility":180,"settle":120},"retries":4,"result":"PASS"}
```

## 2) Defaults & Overrides (YAML)

```yaml
_defaults:
  timeouts:
    page_ready: 15s
    widget_ready: 5s
    post_click_settle: 2s
  poll_interval_ms: 100              # passend für SLO < 1s
  network_idle_quiet_ms: 300
  spinner_selector:
    - '[data-testid="loading-spinner"]'
    - '.ant-spin'
    - '.MuiCircularProgress-root'

TravelExpenses:
  __self__:
    class: okw4robot_web.gui.web.widgets.PageRoot
    locator: { css: '[data-testid="expenses-page"]' }
    slo:
      page_ready_ms:
        target_p95: 1000
        guard_ms: 100
    readyWhen:
      - no_spinner: true
      - network_idle: true

  Destination:
    id: field.destination
    class: okw4robot_web.gui.web.widgets.TextField
    locator: { css: '#destination' }
    readyWhen: [ { visible: true }, { enabled: true } ]

  Save:
    id: button.save
    class: okw4robot_web.gui.web.widgets.Button
    locator: { css: 'button.save' }
    readyWhen: [ { visible: true }, { enabled: true } ]
```

## 3) Adapter-Keywords (Robot-Bordmittel, Demo)

> In echt gehört die Logik in eure Bibliothek. Hier nur als **parse-fähige** Demo.

```robot 
*** Settings ***
Library    SeleniumLibrary
Library    DateTime
Library    Collections

*** Variables ***
${PAGE_READY}         15s
${WIDGET_READY}       5s
${POST_CLICK_SETTLE}  2s
${POLL_INTERVAL}      100ms
${NET_IDLE_QUIET}     300ms
${SPINNER}            css:[data-testid="loading-spinner"]
${PAGE_ROOT}          css:[data-testid="expenses-page"]
&{LOCATORS}           Destination=css:#destination
...                   Save=css:button.save

*** Keywords ***
Telemetry Start
    [Arguments]    ${keyword}    ${locator_name}    ${budget_ms}
    ${t0}=    Get Time    epoch
    Set Suite Variable    ${__KW}    ${keyword}
    Set Suite Variable    ${__LOC}   ${locator_name}
    Set Suite Variable    ${__BUD}   ${budget_ms}
    Set Suite Variable    ${__T0}    ${t0}
    Set Suite Variable    ${__WB}    &{EMPTY}

Telemetry Add Wait
    [Arguments]    ${reason}    ${ms}
    ${wb}=    Set Variable    ${__WB}
    ${old}=   Get From Dictionary    ${wb}    ${reason}    default=0
    Set To Dictionary    ${wb}    ${reason}    ${old + ${ms}}
    Set Suite Variable    ${__WB}    ${wb}

Telemetry End
    [Arguments]    ${result}=PASS    ${error}=${EMPTY}
    ${t1}=    Get Time    epoch
    ${dur}=   Evaluate    int((${t1}-${__T0})*1000)
    ${evt}=   Create Dictionary    keyword=${__KW}    locator_name=${__LOC}    duration_ms=${dur}
    ...       timeout_budget_ms=${__BUD}    wait_breakdown_ms=${__WB}    result=${result}    error_class=${error}
    ${json}=  Evaluate    __import__('json').dumps(${evt})
    Log To Console    ${json}

Wait Until Page Ready
    ${deadline}=    Compute Deadline    ${PAGE_READY}
    WHILE    ${True}
        ${ok1}=    No Spinner Visible    ${SPINNER}    ${PAGE_ROOT}
        ${ok2}=    Network Is Idle       ${NET_IDLE_QUIET}
        Run Keyword If    ${ok1} and ${ok2}    Exit For Loop
        Run Keyword If    Is After Deadline    ${deadline}    Fail    Page not ready in ${PAGE_READY}
        Sleep    ${POLL_INTERVAL}
    END

Wait For Widget Ready
    [Arguments]    ${name}
    ${locator}=    Get From Dictionary    ${LOCATORS}    ${name}
    Wait Until Keyword Succeeds    ${WIDGET_READY}    ${POLL_INTERVAL}
    ...    Element Should Be Visible    ${locator}
    Element Should Be Enabled          ${locator}
    [Return]    ${locator}

Click
    [Arguments]    ${name}
    ${loc}=   Wait For Widget Ready    ${name}
    Telemetry Start    Click    ${name}    2000
    ${t0}=    Get Time    epoch
    Click Element       ${loc}
    Wait Until Keyword Succeeds    ${POST_CLICK_SETTLE}    ${POLL_INTERVAL}    Network Is Idle    ${NET_IDLE_QUIET}
    ${t1}=    Get Time    epoch
    ${ms}=    Evaluate    int((${t1}-${t0})*1000)
    Telemetry Add Wait   settle    ${ms}
    Telemetry End    PASS

# Helpers
Compute Deadline
    [Arguments]    ${timeout}
    ${now}=     Get Time    epoch
    ${secs}=    Convert Time    ${timeout}    result_format=number
    ${dl}=      Evaluate    ${now}+${secs}
    [Return]    ${dl}

Is After Deadline
    [Arguments]    ${deadline}
    ${now}=     Get Time    epoch
    ${after}=   Evaluate    ${now} > ${deadline}
    [Return]    ${after}

No Spinner Visible
    [Arguments]    ${selector}    ${scope}=${EMPTY}
    ${in_scope}=   Set Variable If    '${scope}'!=''    ${scope} >> ${selector}    ${selector}
    ${ok}=         Run Keyword And Return Status    Page Should Not Contain Element    ${in_scope}
    [Return]    ${ok}

Network Is Idle
    [Arguments]    ${quiet_ms}=300ms
    Sleep    ${quiet_ms}     # Stub; in der Lib durch echten Idle-Check ersetzen
    [Return]    ${True}

```

## 4) KPIs (Definitionen & Gates)

- **Timeout-Rate** = `TIMEOUT-Keywords / alle Keywords` → Ziel **< 0,5 %**
- **Flake-Rate** = `fail→rerun→pass / alle Tests` → Ziel **< 1 %/Woche**
- **p95 Dauer je Keyword** (z. B. `Click Save`) → Ziel **< 2 s**
- **Retry-Intensität** (Ø `retries`) → Ziel **< 3**
    

**CI-Gates (Beispiele):**

- PR failen, wenn `p95(PageReady) ≥ 1 000 ms` **oder** `Timeout-Rate ≥ 0,5 %`.
- Report: „Top-N langsame Keywords“ + „Wait-Mix“ (Anteil network_idle/visibility/settle).
    

## 5) Poll-Intervall ↔ Anforderung

- **Erkennungs-Latenz** ≈ Poll/2.
- Für **< 1 s** Zielzeit → Poll **≤ 100–200 ms** (Guard-Band 10–20 %).
- Quiet-Zeit (Network-Idle) **200–500 ms**; feinjustieren per Telemetry.
    

---

## 6) Ergebnis

- **Messbar:** Jede Wartezeit hat Grund, Dauer, Budget.
- **Vergleichbar:** Zeitreihen über Releases trotz UI-Änderungen (dank Abstraktion).
- **Steuerbar:** Budgets & Polling zentral; Tests bleiben technisch sauber.
    
