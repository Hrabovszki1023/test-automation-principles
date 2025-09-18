---
title: Test-Hooks & Controllability
description: Wie wir die App gezielt steuerbar machen (Disable Animations, Fast-Login, Clock-Control, Network-Stubs) – für stabile, schnelle Tests ohne Sleeps.
tags: [steuerbarkeit, beobachtbarkeit, hooks, testmode, okw, robotframework]
status: In Bearbeitung
type: technik
---

# Test-Hooks & Controllability

**Ziel:** Die Anwendung so **steuerbar** machen, dass Keywords zuverlässig **ereignis-/zustandsbasiert** arbeiten – ohne harte Sleeps und ohne Testfall-Tricks.

Bezug zur Heiligen Dreifaltigkeit (Was–Wie–Tut):
- **Was:** Abstrakte Lokatoren (funktionale Namen)
- **Tut:** Abstrakte Interaktionen (`Click`, `Set Value`, `Verify Value`, `Select Menu`)
- **Wie:** **Test-Hooks** und Adapter sorgen für **Readiness**, Stabilität und Geschwindigkeit

---

## 1) Designprinzipien für Hooks

- **Expliziter Test-Modus:** App erkennt `APP_TEST_MODE=true` (Env, Config, Query-Param `?e2e=1`) und aktiviert testfreundliches Verhalten.
- **Idempotent & reversibel:** Jeder Hook lässt sich aktivieren/deaktivieren, vorzugsweise pro Session.
- **Sicherheitsgeländer:** Test-Modus **nicht** in Produktion aktivierbar (Env-Schalter, Whitelist der Test-Hosts).
- **Konfiguration zentral:** Flags & Parameter in YAML/Config, nicht quer in Testfällen.
- **Telemetry:** Jeder Hook darf gemessen werden (aktiv? Dauer? Effekt auf KPIs?).

---

## 2) Hook-Katalog (Überblick)

| Hook | Zweck | Typische Umsetzung |
|---|---|---|
| **Disable Animations** | Eliminierte UI-Verzögerungen → weniger Wartezeit | CSS-Injection, `prefers-reduced-motion`, Framework-Flags |
| **Fast Login** | Login überspringen/beschleunigen | Token-/Cookie-Injection, Test-Login-Endpoint |
| **Clock Control** | Zeit deterministisch machen | `Date.now`/Timer faken, Time-Travel |
| **Network Stubbing** | Externe/instabile Calls neutralisieren | Fetch/XHR-Monkeypatch, DevTools/Playwright, Backend-Flags |
| **Data Seeding** | Reproduzierbare Ausgangszustände | Test-APIs/Fixtures, idempotente Seeds |
| **Feature Flags** | Funktionen gezielt an/aus | Test-Konfiguration, serverseitige Flags |

---

## 3) Zentrale Konfiguration (YAML)

```yaml
_defaults:
  hooks:
    disable_animations: true
    fast_login:
      enabled: true
      method: cookie         # cookie | header | endpoint
      endpoint: /api/test/login
      user_cookie_name: session
    clock:
      freeze: null           # ISO-Zeit oder null für „live“
    network:
      stub:
        - pattern: "/analytics"
          action: "block"    # block | respond_204 | delay
      quiet_ms: 300          # für "network idle"
TravelExpenses:
  __self__:
    class: okw4robot_web.gui.web.widgets.PageRoot
    locator: { css: '[data-testid="expenses-page"]' }
    hooks:
      disable_animations: true
      clock:
        freeze: "2025-05-12T10:00:00Z"
````

> Die Adapter-Schicht liest diese Flags beim Start einer Session und aktiviert die entsprechenden Hooks.

---

## 4) Robot-Beispiele (Bordmittel-Demo)

> In der Praxis implementiert ihr das in **OKW4Robot** außerhalb der `.robot`-Dateien. Hier nur **parse-fähige** Beispiele zum Verständnis.

```robot
*** Settings ***
Library           SeleniumLibrary
Library           RequestsLibrary
Library           DateTime
Library           Collections

*** Variables ***
${BASE_URL}                 https://example.app
${TEST_LOGIN_EP}            /api/test/login
${SESSION_COOKIE}           session

${PAGE_READY}               15s
${WIDGET_READY}             5s
${POST_CLICK_SETTLE}        2s
${FAST_LOGIN_READY}         7s          # Budget: nach Reload bis Ready
${POLL_INTERVAL}            100ms
${NET_IDLE_QUIET}           300ms
${SPINNER}                  css:[data-testid="loading-spinner"]
${PAGE_ROOT}                css:[data-testid="expenses-page"]

&{LOCATORS}                 Destination=css:#destination
...                         Save=css:button.save

*** Test Cases ***
Create New Expense Report (with Hooks)
    Enable Test Mode
    Fast Login As       alice        # ← enthält implizit Page-Ready
    Select Menu         New Expense Report
    Set Value           Destination    Berlin
    Click               Save
    Verify Value        Status Message    Expense report saved

*** Keywords ***
Enable Test Mode
    Go To    ${BASE_URL}?e2e=1
    Disable Animations

Disable Animations
    ${css}=    Catenate    SEPARATOR=\n
    ...    * { transition: none !important; animation: none !important; }
    ...    html, body { scroll-behavior: auto !important; }
    Execute Javascript    var s=document.createElement('style'); s.innerHTML=arguments[0]; document.head.appendChild(s);    ${css}

Fast Login As
    [Arguments]    ${username}    ${password}=secret
    # 1) Test-Endpoint aufrufen → Token holen
    Create Session    fast    ${BASE_URL}
    ${resp}=    POST On Session    fast    ${TEST_LOGIN_EP}    json={"user":"${username}","password":"${password}"}
    Should Be Equal As Integers    ${resp.status_code}    200
    ${token}=    Set Variable    ${resp.json()['token']}
    # 2) Cookie setzen + Reload
    Add Cookie    ${SESSION_COOKIE}    ${token}
    Reload Page
    # 3) Implizit auf Ready warten (Budget für Fast-Login)
    Wait Until Page Ready    ${FAST_LOGIN_READY}

Wait Until Page Ready
    [Arguments]    ${budget}=${PAGE_READY}
    ${deadline}=    Compute Deadline    ${budget}
    WHILE    ${True}
        ${ok1}=    No Spinner Visible    ${SPINNER}    ${PAGE_ROOT}
        ${ok2}=    Network Is Idle       ${NET_IDLE_QUIET}
        ${ok3}=    Run Keyword And Return Status    Element Should Be Visible    ${PAGE_ROOT}
        Run Keyword If    ${ok1} and ${ok2} and ${ok3}    Exit For Loop
        Run Keyword If    Is After Deadline    ${deadline}    Fail    Page not ready in ${budget}
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
    Click Element       ${loc}
    Wait Until Keyword Succeeds    ${POST_CLICK_SETTLE}    ${POLL_INTERVAL}    Network Is Idle    ${NET_IDLE_QUIET}

# --- Helpers ---
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
    # Stub für Bordmittel; im Framework durch echten Idle-Check ersetzen
    Sleep    ${quiet_ms}
    [Return]    ${True}

```

**Hinweise**

- `Fast Login As` nutzt `RequestsLibrary`, um einen **Test-Login-Endpoint** aufzurufen und das Session-Cookie zu setzen. Alternativ: Token über Header/LocalStorage.
- `Freeze Clock` wirkt **nur client-seitig** (für viele UI-Fälle ausreichend). Serverseitige Zeitpunkte benötigen Backend-Support.
- `Stub Network Pattern` ist bewusst simpel. Für echte Stubs: Playwright (`route`), Chrome DevTools Protocol oder serverseitige Flags.
    

---

## 5) Zusammenspiel mit Observability

Hooks + Observability ergeben den **Readiness-Contract**:

- `Disable Animations` → **weniger künstliche Wartezeit**, Ready schneller messbar.
- `Fast Login` → Startzustand reproduzierbar, **weniger Varianz**.
- `Clock Control` → deterministische Zeitlogik; **keine Flakes** durch „00:00-Rollover“ etc.
- `Network Stubs` → eliminiert nicht-deterministische Drittsysteme (Analytics, Ads, langsame Partner).
    

---

## 6) KPIs für Hooks

|KPI|Ziel|Interpretation|
|---|---|---|
|**PageReady p95**|↓ nach `disable_animations=true`|Bestätigung, dass Animationen Wartezeit trieben|
|**Flake-Rate**|< 1 %|Sinkt, wenn `fast_login` & Seeds sauber sind|
|**Timeout-Rate**|< 0.5 %|Fällt, wenn `network.stub` störende Calls blockt|
|**Retry-Intensität**|< 3|Niedriger bei stabilen Readiness-Signalen|

> Telemetry-Events sollten ein Feld `hooks_active` enthalten (z. B. `{"disable_animations":true,"fast_login":true}`), um Effekte kausal auszuwerten.

---

## 7) Sicherheits- & Betriebs-Geländer

- **Nicht in Prod:** Test-Mode nur in Test-Umgebungen aktivierbar (ENV-Guard).
    
- **Auth-Bypass nur gezielt:** `Fast Login` nur für synthetische Testnutzer; keine Admin-Shortcuts ohne Whitelist.
    
- **Auditing:** Hook-Nutzung in Logs markieren; bei Missbrauch nachvollziehbar.
    
- **Fail-Safe:** Falls Hook scheitert, darf die App normal funktionieren (kein Hard-Crash).
    

---

## 8) Do/Don’t-Checkliste

**Do**

- Hooks **zentral konfigurieren**, **früh** aktivieren (vor dem ersten Testschritt).
- Telemetry für Hook-Effekte erfassen.
- Clean-Up: pro Test neue Session oder explizit zurücksetzen.
    

**Don’t**

- Hooks „heimlich“ im Testfall verstreuen.
- Test-Mode ohne Umgebungs-Schutz deployen.
- Auf Client-Clock-Freeze für Server-Zeitlogik verlassen.
    

---

## 9) Mini-Ablauf (Beispiel)

```robot
*** Test Cases ***
Create New Expense Report (with Hooks)
    Enable Test Mode
    Fast Login As       alice
    Wait Until Page Ready
    Select Menu         New Expense Report
    Set Value           Destination        Berlin
    Click               Save
    Verify Value        Status Message     Expense report saved
```

**Ergebnis:** Steuerbarer, messbarer und **schneller** Ablauf – ohne einen einzigen `Sleep`.
