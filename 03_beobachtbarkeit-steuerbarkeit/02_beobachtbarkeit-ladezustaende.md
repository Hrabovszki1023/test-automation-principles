
---
title: Beobachtbarkeit von Ladezuständen (Spinner, Progress, ARIA busy)  
description: Readiness-Signale definieren und zuverlässig prüfen – statt fixer Sleeps.  
tags: [beobachtbarkeit, steuerbarkeit, stabilität, okw, robotframework]  
status: In Bearbeitung  
type: technik
---


# Beobachtbarkeit von Ladezuständen (Spinner, Progress, ARIA busy)

**Ziel:** Klare, messbare **Readiness-Signale** definieren (und prüfen), damit Keywords **ereignis-/zustandsbasiert** warten – ohne Sleeps.

**Bezug zur Heiligen Dreifaltigkeit (Was–Wie–Tut):**

- **Was:** Seite/Widget (abstrakter Lokator, z. B. `TravelExpenses` / `Destination`)
    
- **Tut:** Keyword (`Click`, `Set Value`, `Verify Value`)
    
- **Wie:** Adapter prüft **Readiness** (keine Spinner, network idle, sichtbar/enabled …) und führt aus.
    

---

## 1. Begriffe & Signale

- **Spinner / Busy-Icon / indeterminate progress**  
    Sichtbares Lade-Signal ohne Restdauer. **Ready ⇒** nicht sichtbar / entfernt.
    
- **Determinate Progressbar** (`role="progressbar"` mit Wert)  
    **Ready ⇒** 100 % _oder_ Progressbar nicht sichtbar.
    
- **Overlay/Backdrop** (halbtransparente Sperre)  
    **Ready ⇒** Overlay verschwunden / nicht sichtbar.
    
- **Skeletons** (graue Platzhalter)  
    **Ready ⇒** Skeleton weg **und** echter Content sichtbar.
    
- **ARIA busy** (`aria-busy="true"`)  
    **Ready ⇒** `aria-busy="false"` am relevanten Container.
    
- **Network idle**  
    Keine offenen Requests seit _X_ ms (Quiet-Zeit).
    

> Praxis: Ein **Readiness-Check** kombiniert mehrere Signale (AND/OR) – z. B. „kein Spinner **und** network idle“.

---

## 2. Designrichtlinien (Selektoren & Scopes)

- **Stabile TestIDs** vergeben: `data-testid="loading-spinner"`, `data-testid="app-root"`.
    
- **Scope** setzen: innerhalb des **Seiten-Roots** suchen (z. B. `[data-testid="expenses-page"]`), damit fremde Spinner nicht stören.
    
- **Entfernt vs. versteckt**: Entscheidet, ob Spinner **aus dem DOM entfernt** oder nur **versteckt** wird → entsprechend auf „nicht vorhanden“ **oder** „nicht sichtbar“ prüfen.
    
- **Zugänglichkeit nutzen**: `role="progressbar"`, `aria-busy` sind robuste, technikunabhängige Signale.
    

---

## 3. Defaults & Overrides (YAML)

```yaml
_defaults:
  timeouts:
    page_ready: 15s
    widget_ready: 5s
    post_click_settle: 2s
  poll_interval_ms: 200
  spinner_selector:
    - '[data-testid="loading-spinner"]'
    - '.ant-spin'
    - '.MuiCircularProgress-root'
    - '[role="progressbar"]'
  aria_busy_container: '[data-testid="app-root"]'
  network_idle_quiet_ms: 500

TravelExpenses:
  __self__:
    class: okw4robot_web.gui.web.widgets.PageRoot
    locator: { css: '[data-testid="expenses-page"]' }
    timeouts:
      page_ready: 20s           # Seite darf länger brauchen
    readyWhen:
      - no_spinner: true
      - aria_busy: false
      - network_idle: true

  Destination:
    class: okw4robot_web.gui.web.widgets.TextField
    locator: { css: '#destination' }
    timeouts:
      widget_ready: 3s          # Widget ist schnell erreichbar
    readyWhen:
      - visible: true
      - enabled: true

  Save:
    class: okw4robot_web.gui.web.widgets.Button
    locator: { css: 'button.save' }
    readyWhen:
      - visible: true
      - enabled: true
```

---

## 4. Adapter-Keywords (Robot, gekürzt)

```robot
*** Settings ***
Library           SeleniumLibrary
Library           DateTime
Library           Collections

*** Variables ***
${PAGE_READY}              15s
${WIDGET_READY}            5s
${POST_CLICK_SETTLE}       2s
${POLL_INTERVAL}           200ms
${NETWORK_IDLE_QUIET}      500ms
${SPINNER}                 css:[data-testid="loading-spinner"]
${PAGE_ROOT}               css:[data-testid="expenses-page"]

# Beispielhafte abstrakte Lokatoren → konkrete Selektoren
&{LOCATORS}                Destination=css:#destination
...                        Save=css:button.save

*** Keywords ***
# ------------------------------ Page/Widget Readiness ------------------------------
Wait Until Page Ready
    [Arguments]    ${page}=TravelExpenses
    ${cfg}=    Get Config For Page    ${page}
    ${deadline}=    Compute Deadline    ${cfg.timeouts.page_ready}
    WHILE    ${True}
        ${ok1}=    No Spinner Visible    ${cfg.spinner_selector}    ${cfg.page_root}
        ${ok2}=    Aria Busy Is False    ${cfg.page_root}
        ${ok3}=    Network Is Idle       ${NETWORK_IDLE_QUIET}
        Run Keyword If    ${ok1} and ${ok2} and ${ok3}    Exit For Loop
        Run Keyword If    Is After Deadline    ${deadline}    Fail    Page not ready in ${cfg.timeouts.page_ready}
        Sleep    ${POLL_INTERVAL}
    END

Wait For Widget Ready
    [Arguments]    ${name}
    ${cfg}=    Get Config For Widget    ${name}
    # Wartet innerhalb des Widget-Ready-Budgets mit Poll-Intervallen
    Wait Until Keyword Succeeds    ${cfg.timeouts.widget_ready}    ${POLL_INTERVAL}
    ...    Element Should Be Visible    ${cfg.locator}
    Element Should Be Enabled          ${cfg.locator}

# ------------------------------ Click mit Pre-/Post-Handling ------------------------------
Click
    [Arguments]    ${name}
    ${cfg}=    Get Config For Widget    ${name}
    # PRE: Widget-Readiness (sichtbar, enabled, im Viewport etc.)
    Wait For Widget Ready    ${name}
    # ACTION: Klick auf den konkreten Locator
    Click Element            ${cfg.locator}
    # POST: Settle/Network-Idle innerhalb des Post-Click-Budgets
    # (mit Bordmitteln simuliert – echtes Network-Idle hängt vom Stack ab)
    Wait Until Keyword Succeeds    ${POST_CLICK_SETTLE}    ${POLL_INTERVAL}
    ...    Network Is Idle          ${NETWORK_IDLE_QUIET}

# ------------------------------ Helfer (Minimal-Stubs) ------------------------------
Get Config For Page
    [Arguments]    ${page}
    &{timeouts}=    Create Dictionary    page_ready=${PAGE_READY}
    &{cfg}=         Create Dictionary    timeouts=&{timeouts}    poll_interval=${POLL_INTERVAL}
    ...                               page_root=${PAGE_ROOT}    spinner_selector=${SPINNER}
    [Return]    &{cfg}

Get Config For Widget
    [Arguments]    ${name}
    ${locator}=    Get From Dictionary    ${LOCATORS}    ${name}
    &{timeouts}=   Create Dictionary    widget_ready=${WIDGET_READY}    post_click_settle=${POST_CLICK_SETTLE}
    &{cfg}=        Create Dictionary    locator=${locator}    timeouts=&{timeouts}    poll_interval=${POLL_INTERVAL}
    [Return]    &{cfg}

Compute Deadline
    [Arguments]    ${timeout}
    ${now}=        Get Time    epoch
    ${secs}=       Convert Time    ${timeout}    result_format=number
    ${deadline}=   Evaluate    ${now} + ${secs}
    [Return]    ${deadline}

Is After Deadline
    [Arguments]    ${deadline}
    ${now}=        Get Time    epoch
    ${after}=      Evaluate    ${now} > ${deadline}
    [Return]    ${after}

No Spinner Visible
    [Arguments]    ${selector}    ${scope}=${EMPTY}
    # Einfacher Check: Spinner darf nicht vorhanden/ sichtbar sein
    ${in_scope}=   Set Variable If    '${scope}'!=''    ${scope} >> ${selector}    ${selector}
    ${ok}=         Run Keyword And Return Status    Page Should Not Contain Element    ${in_scope}
    [Return]    ${ok}

Aria Busy Is False
    [Arguments]    ${container}
    ${val}=        Get Element Attribute    ${container}    aria-busy
    ${val}=        Set Variable If    '${val}'==''    false    ${val}
    ${ok}=         Evaluate    str(${val}).lower() != 'true'
    [Return]    ${ok}

Network Is Idle
    [Arguments]    ${quiet_ms}=500ms
    # Platzhalter für Bordmittel: kurze Quiet-Zeit abwarten und „True“ liefern.
    # In OKW4Robot würde hier echter Netz-/Event-Idle geprüft.
    Sleep    ${quiet_ms}
    [Return]    ${True}

```

**Hinweise:**

- **Budgetierung:** `Click` verbraucht sein Budget in zwei Phasen: `widget_ready` (PRE) und `post_click_settle` (POST). In einer echten Lib könntest du das als **Gesamtbudget** messen; hier halten wir’s Bordmittel-einfach.
    
- **Network Is Idle:** ist hier absichtlich ein Stub. Im Framework ersetzt du das durch einen echten Idle-Check (DevTools, Playwright `networkidle`, App-Hook).
    
- **No Spinner Visible:** für Demo simpel gehalten; wenn ihr mehrere Spinner-Selektoren habt, kannst du das leicht erweitern (Liste iterieren).

---

## 5. Network-Idle messen (Hook-Beispiel, Browser/JS)

Falls euer Stack es nicht schon anbietet, könnt ihr Fetch/XHR zählen:

```javascript
// in app test-mode oder via devtools injection
(function () {
  const w = window;
  w.__activeRequests = 0;
  const origFetch = w.fetch;
  w.fetch = function() {
    w.__activeRequests++;
    return origFetch.apply(this, arguments).finally(() => w.__activeRequests--);
  };
  const origOpen = XMLHttpRequest.prototype.open;
  const origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function() { this.__tracked = true; return origOpen.apply(this, arguments); };
  XMLHttpRequest.prototype.send = function() {
    if (this.__tracked) {
      w.__activeRequests++;
      this.addEventListener('loadend', () => w.__activeRequests--, { once: true });
    }
    return origSend.apply(this, arguments);
  };
})();
```

Euer Adapter prüft dann „idle“ so:

```javascript
// Pseudocode aus Adapter
function isNetworkIdle(quietMs = 500) {
  if (window.__activeRequests > 0) return false;
  // zusätzlich: in den letzten quietMs keine Änderung
  // z. B. Zeitstempel der letzten Aktivität tracken
  return true;
}
```

> Alternativen: Playwrights `wait_for_load_state('networkidle')`, Browser-DevTools-Protokoll, App-seitige Events.

---

## 6. Telemetry & KPIs

**Pro Keyword loggen:**  
`keyword`, `locator_name`, `wait_reason` (spinner/network/visibility), `wait_ms`, `retries`, `timeout_budget_ms`, `result`.

**Ziele (Startwerte):**

- p95 `wait_ms` pro Keyword < **2 s**
- **0** Sleeps/explicit Waits in Testdateien
- Flake-Rate < **1 %** pro Woche
    

---

## 7. Anti-Pattern vs. Clean

**Schlecht**

```robot
Sleep    5s
Click Element    xpath=//div[3]/span[2]
Wait Until Element Is Visible    css=.toast-success    10s
```

**Gut (Readiness hinter Keywords)**

```robot
Click           Save
Verify Value    Status Message    Expense report saved
```

---

## 8. Do/Don’t-Checkliste

**Do**

- Readiness-Signale **zentral** definieren (YAML)
- Keywords warten **implizit** (Budget, Poll-Intervalle)
- **Scope** beim Suchen beachten (Page-Root)
- Telemetry & KPIs aktiv auswerten
    

**Don’t**

- Keine `Sleep`/`Wait Until ...` im Testfall
- Keine Spinner-Heuristiken im Testfall 
- Keine konkreten Selektoren in Tests (nur abstrakte Lokatoren)
    

---

