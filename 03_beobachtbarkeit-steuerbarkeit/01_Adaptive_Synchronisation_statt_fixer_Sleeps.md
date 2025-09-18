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

voll gut — ich hab dir den Text **bereinigt, straffer gegliedert und GitBook-kompatibel** formatiert (inkl. sauberem Formel-Block und Codefences). Du kannst das 1:1 ersetzen.

---

# Adaptive Synchronisation statt fixer Sleeps

**These:** Fixe Wartezeiten sind ein Anti-Pattern. Sie entstehen, wenn **Beobachtbarkeit** (Signale) und **Steuerbarkeit** (Kontrollen) fehlen.

## Warum hier im Kapitel?

- **Beobachtbarkeit:** belastbare **Readiness-Signale** (UI ready, Network idle, Spinner weg, sichtbar/enabled, DOM ruhig).
    
- **Steuerbarkeit:** Schalter für Testbarkeit (**disable animations**, **fast startup**, **test mode**, Feature-Flags).
    

> Ergebnis: Keine `Sleep 5s` mehr. Stattdessen **ereignis-/zustandsbasiertes Warten** in der Adapter-/Keyword-Schicht.

## Zielbild (kurz)

- Tests enthalten **keine** Warte-/Sync-Kommandos.
    
- Keywords warten **implizit** auf „ready“.
    
- Readiness ist **zentral** definiert (pro Widget/Seite), nicht pro Test.
    

---

# Warum fixe Wartezeiten nichts im Testfall zu suchen haben

**Kernproblem:** Jede feste Wartezeit im Testfall **multipliziert** sich mit  
(a) der Anzahl betroffener Stellen, (b) der Anzahl Testfälle und (c) der Laufhäufigkeit.  
Und sie ist **nie „richtig“**: mal zu kurz (flaky), mal zu lang (Zeitverschwendung).

## Skalierungsformel

$$Verschwendete Zeit (s)=w⋅n⋅T⋅R\text{Verschwendete Zeit (s)} = w \cdot n \cdot T \cdot R$$

- $$w$$ = feste Wartezeit pro Vorkommen (Sekunden)
    
- $$n$$ = Warte-Vorkommen pro Test
    
- $$T$$ = Anzahl Tests pro Lauf
    
- $$R$$R = Anzahl Läufe im Zeitraum
    

> Zusätzlich: Flakes erzeugen Re-Runs → $$**nn**$$ wächst faktisch, ohne irgendeine Verbesserung.

## Rechenbeispiele (typische Szenarien)

|Szenario|Annahmen|Verschwendung pro Lauf|
|---|---|---|
|**Login-Sleep**|w=10w=10 s, n=1n=1, T=5,000T=5{,}000|10×1×5,000=50,00010 \times 1 \times 5{,}000 = 50{,}000 s → **13 h 53 m 20 s**|
|**Drei kleine Sleeps**|w=2w=2 s, n=3n=3, T=5,000T=5{,}000|2×3×5,000=30,0002 \times 3 \times 5{,}000 = 30{,}000 s → **8 h 20 m**|
|**Viele Mini-Sleeps**|w=1w=1 s, n=10n=10, T=5,000T=5{,}000|1×10×5,000=50,0001 \times 10 \times 5{,}000 = 50{,}000 s → **13 h 53 m 20 s**|

> Parallelisierung senkt nur die **Wandzeit**; **Kosten** und **Queue-Zeit** bleiben: die Sekunden werden nur auf mehr Maschinen verteilt.

## „Man wartet nie richtig“

- **Zu kurz** → Flaky-Fehler, Re-Runs, unzuverlässige Signale.
    
- **Zu lang** → lineare Verschwendung, skaliert mit $$n,T,Rn, T, R.$$
    
- Latenzen schwanken (UI/Netz/Rendern/Animationen) → feste Zahl passt selten.
    
- Jede Anpassung (z. B. 5 s → 7 s) erfordert **alle Vorkommen** zu ändern → Anti-DRY.
    

## Konsequenz

- **Warten gehört in die Keyword-/Adapter-Schicht**, nicht in den Testfall.
    
- Testfälle beschreiben **Intent** (Was/Tut), die Bibliothek garantiert **Readiness** (Wie).
    

---

## Ersatz: Readiness statt Sleeps

- **Adapter-Policy:** `Click`/`Set Value` warten **implizit** auf _sichtbar, enabled, im Viewport, stabil, network idle_.
    
- **Konfiguration zentral:** Timeout-Budgets, Poll-Intervalle, Spinner-Selektor, „disable animations“.
    
- **Telemetry pro Keyword:** Grund, Dauer, Retries → messbare Stabilität statt Ratespiel.
    

---

## Readiness-Contract (Was der Adapter garantiert)

- **Page-ready:** Root sichtbar & interaktiv, **kein Spinner**, **Network idle** (konfigurierbar).
    
- **Widget-ready:** sichtbar, enabled, „in view“, stabil (Bounding-Box 2× identisch).
    
- **Timeout-Budget** pro Keyword (z. B. 10 s, in Poll-Intervalle geteilt).
    
- **Telemetry:** `wait_reason`, `wait_ms`, `retries`.
    

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

---

## Anti-Pattern (Kontrast)

```robot
# Schlecht
Sleep    5s
Click Element    xpath=//div[3]/span[2]
Wait Until Element Is Visible    css=.toast-success    10s
```

## Clean (Adapter macht die Arbeit)

```robot
Click           Save
Verify Value    Status Message    Expense report saved
```

---

## DoD & Metriken

- **0** Vorkommen von `Sleep`/`Wait Until Element ...` in Testdateien.
    
- **Wait-Budget p95** < 2 s pro Keyword.
    
- **Flake-Rate** < 1 % (wöchentlich).
    
- Telemetry: `wait_reason`, `wait_ms`, `retries` pro Keyword geloggt.
    

---

> Tipp für GitBook: Math funktioniert mit `$$…$$` (wie oben). Falls Math deaktiviert ist, schreib die Formel alternativ in einer Codezeile:  
> `Verschwendete Zeit (s) = w * n * T * R`

Wenn du willst, packe ich dir dazu noch eine **Mini-Grafik** (PlantUML/mermaid) „Kosten explodieren linear mit w, n, T, R“.