---
title: Adaptive Synchronisation statt fixer Sleeps
description: Warum Sleeps scheitern – und wie ein Readiness-Contract mit Observability & Controllability sie ersetzt.
tags:
  - steuerbarkeit
  - beobachtbarkeit
  - stabilität
  - dry
  - okw
status: In Bearbeitung
type: technik
---

# Adaptive Synchronisation statt fixer Sleeps

**These:** Fixe Wartezeiten sind ein Anti-Pattern. Sie entstehen, wenn **Beobachtbarkeit** (Signale) und **Steuerbarkeit** (Kontrollen) fehlen.

## Warum hier im Kapitel?
- **Beobachtbarkeit**: Wir brauchen belastbare **Readiness-Signale** (UI-ready, Network-idle, Spinner-weg, Visibility/Enabled, DOM-ruhig).
- **Steuerbarkeit**: Wir brauchen Schalter, um die App testbar zu machen (**disable animations**, **fast startup**, **test mode**, Feature-Flags).

> Ergebnis: Keine `Sleep 5s` mehr. Stattdessen **ereignis- und zustandsbasiertes Warten** im Adapter.

## Zielbild (kurz)
- Tests enthalten **keine** Warte-/Sync-Kommandos.  
- Keywords warten **implizit** auf „ready“.  
- Readiness ist **zentral** definiert (pro Widget/Seite), nicht pro Test.

## Readiness-Contract (Was der Adapter garantiert)
- **Page-ready**: Root sichtbar & interaktiv, **kein Spinner**, **network idle** (konfigurierbar).  
- **Widget-ready**: sichtbar, enabled, scrolled into view, stabil (Bounding-Box 2× identisch).  
- **Timeout-Budget** pro Keyword (z. B. 10s, geteilt in Poll-Intervale).  
- **Telemetry**: Wartegrund, Dauer, count der Retries.

### YAML (Beispiel, abstrakt → konkret)
```yaml
TravelExpenses:
  __self__:
    class: okw4robot_web.gui.web.widgets.PageRoot
    locator: { css: '[data-testid="expenses-page"]' }
    readyWhen:
      - no_spinner: '[data-testid="loading-spinner"]'
      - network_idle: true
  Destination:
    class: okw4robot_web.gui.web.widgets.TextField
    locator: { css: '#destination' }
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

### Robot (sauber, nur Fach-Steps)

```robot

*** Test Cases ***
Select Destination
	Open Application      Travel Expenses
	Select Menu           New Expense Report
	Set Value             Destination        Berlin
	Click                 Save
	Verify Value          Status Message     Expense report saved

```

> Die Keywords implementieren den Readiness-Contract. Tests enthalten **keine** Sleeps/Waits.

## Warum fixe Sleeps immer verlieren

- Man wartet **nie „richtig“**: entweder **zu kurz** (flaky) oder **zu lang** (langsamer Lauf).
    
- Latenzen schwanken (Netz, Rendern, GC, Animations-Delays).
    
- Sleeps maskieren echte Ursachen und verteuern die Suite.
    

## DoD & Metriken

- **0** Vorkommen von `Sleep`, `Wait Until Element ...` in Testdateien.
    
- **Wait-Budget p95** < 2s pro Keyword.
    
- **Flake-Rate** < 1% (wöchentlich).
    
- Telemetry: `wait_reason`, `wait_ms`, `retries` werden pro Keyword geloggt.
    

## Steuerbarkeit (Beispiele)

- **Disable animations** (globales Flag)
    
- **Fast-login/Test-Mode** (vorkonfigurierte Nutzer, Seed-Daten)
    
- **Network stubbing** / **Retry-Backoff** konfigurierbar
    
- **Clock control** (Zeit einfrieren, wenn relevant)
    

## Beobachtbarkeit (Signale)

- **Spinner-Selector** bekannt
    
- **Network-idle** (Requests in flight = 0 für X ms)
    
- **UI-ready** (sichtbar+enabled+stabil)
    
- **App-health** (ping/pong, Fehlerbanner, backend reachable)
    

---

### Anti-Pattern (Kontrast)

```robot
# Schlecht
	Sleep    5s
	Click Element    xpath=//div[3]/span[2] 
	Wait Until Element Is Visible    css=.toast-success    10s`
```

### Clean (Adapter macht die Arbeit)

```robot

	Click    Save
	Verify Value    Status Message    Expense report saved`
```
---