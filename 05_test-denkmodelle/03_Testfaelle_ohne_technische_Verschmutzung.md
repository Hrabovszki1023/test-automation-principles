---
title: Testfälle ohne technische Verschmutzung
description: Warum fachliche Testfälle frei von Technik bleiben müssen – und wie wir das konsequent umsetzen.
tags:
  - testdenken
  - prinzipien
  - wartbarkeit
  - dry
  - okw
  - robotframework
status: fertig
type: artikel
---
# Testfälle ohne technische Verschmutzung

**Grundsatz:** Ein Testfall beschreibt **fachliches Verhalten** in **Fachsprache** – mit **abstrakten Schlüsselwörtern** und **abstrakten Lokatoren**.  
**Technische Problemlösungen** (Warten, Synchronisation, wilde Selektoren, Treiber-APIs, Programmierlogik) haben im Testfall nichts zu suchen.

## Zielbild (kurz)

- **Lesbar** für Fachtester:innen
- **Wiederverwendbar** und **DRY**
- **Wartungsarm**, weil Technik zentral gekapselt ist (Bibliothek/Adapter)
    

---

## Was **nicht** in den Testfall gehört (No-Gos)

| Problem                        | Beispiele                                                                         | Warum raus damit                                                            |
| ------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Harte Wartezeiten**          | `Warte 5s`, `Sleep 5000`                                                          | Fragil, verlangsamt Runs, maskiert echte Timing-Probleme.                   |
| **Synchronisationscode**       | Polling-Schleifen, Retry-Basteleien, `Wait Until Element Is Visible` als Pflaster | Sync gehört **zentral** in die Keyword-Bibliothek/Adapter.                  |
| **Wilde/konkrete Lokatoren**   | `xpath=//div[3]/span[2]`, `.app > :nth-child(7)`                                  | Unlesbar & instabil; ersetze durch **funktionale Namen** mit Mapping.       |
| **Programmierlogik**           | `if/else`, Schleifen, Regex-Flows, Variablen-Akrobatik                            | Vermischt Fachlogik mit Technik; erschwert Review & Wartung.                |
| **Treiber-/Framework-Aufrufe** | WebDriver-Calls, HTTP-Clients, Java/Python im Test                                | Bricht Abstraktion; gehört in Adapter/Library – nicht in fachliche Skripte. |

> Diese Punkte sind **technische Probleme** (Timing, Stabilität, Identifikation) und gehören **hinter** die Keyword-Schnittstelle.

---

## Was **in** den Testfall gehört

| Baustein                     | Beispiele                                                                               | Zweck                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Domänen-Keywords**         | `Open Application`, <br>`Select Menu`, <br>`Set Value`, <br>`Click`, <br>`Verify Value` | Beschreiben **Was** passiert (Intent), nicht **Wie**.                           |
| **Abstrakte Lokatoren**      | `Destination`, <br>`Status Message`, <br>`New Expense Report`                           | Benennen **Was** adressiert wird (funktionaler Name), Technik bleibt verborgen. |
| **Fachliche Orchestrierung** | Schrittfolge des Geschäftsprozesses                                                     | Klare, lesbare Abläufe statt Technik-Gerümpel.                                  |
| **Geschäftliche Checks**     | `Verify Value Status Message Expense report saved`                                      | Prüfen **Outcome**, nicht Implementierungsschritte.                             |

---

## Heilige Dreifaltigkeit (Was–Wie–Tut)

- **Was:** Abstrakter Lokator (funktionaler Name) – z. B. `"Destination"`.
    
- **Tut:** Abstraktes Schlüsselwort (Intent) – z. B. `Set Value`, `Click`, `Verify Value`, `Select Menu`.
    
- **Wie:** Bibliothek/Adapter löst die Technik – Mapping zu konkreten Selektoren, Smart-Waits, Retries, Scrolling, Fehlerbilder.
    

→ **Alles Technische** passiert **hinter** der Keyword-Schnittstelle.

---

## Beispiel: vorher → nachher

**Vorher (verschmutzt):**

```robot

*** Test Cases ***
Anti-Pattern Example (Dirty)
    Sleep    5s
	Click Element    xpath=//div[3]/span[2]
	Wait Until Element Is Visible    css=.toast-success    10s
	Run Keyword If    '${status}' == 'OK'    Log    Ready

```

**Nachher (sauber):**

```robot

*** Test Cases ***
Create New Expense Report (Clean)
    [Documentation]    Domain-level steps only; all technical handling is inside keywords.
    Open Application      Travel Expenses
    Select Menu           New Expense Report
    Set Value             Travel Date        2025-05-12
    Set Value             Destination        Berlin
    Click                 Save
    Verify Value          Status Message     Expense report saved
```

_Hinweis:_ `Click New Expense Report` kann je nach Locator-Kategorie intern auf **Menu-Logik** routen. Für Fachtester ist `Select Menu New Expense Report` oft noch klarer.

---

## Lokator-Map (Beispiel, abstrakt → konkret)

```yaml

TravelExpenses:
  __self__:
    class: okw4robot_web.gui.web.widgets.PageRoot
    locator: { css: '[data-testid="expenses-page"]' }

  # Menüeintrag mit Pfad (Sonderrolle: Menu)
  New Expense Report:
    class: okw4robot_web.gui.web.widgets.MenuItem
    path: ["File", "New", "Expense Report"]
    reveal: hover_or_click

  # Felder
  Travel Date:
    class: okw4robot_web.gui.web.widgets.TextField
    locator: { css: "#travelDate" }

  Destination:
    class: okw4robot_web.gui.web.widgets.TextField
    locator: { css: "#destination" }

  # Aktionen / Status
  Save:
    class: okw4robot_web.gui.web.widgets.Button
    locator: { css: "button.save" }

  Status Message:
    class: okw4robot_web.gui.web.widgets.Label
    locator: { css: "#status" }

```

Die **Bibliothek** liest diese Map, löst die funktionalen Namen auf und kümmert sich um Sichtbarkeit, Scroll, Retry, etc.

---

## Definition of Done (Do/Don’t)

**Don’t**

- ❌ `Sleep`, `Wait Until Element Is ...` im Testfall
    
- ❌ `xpath=`, `css=`, `id=` im Testfall
    
- ❌ Treiber-/HTTP-Aufrufe oder Programmiersprache im Testfall
    

**Do**

- ✅ Nur **abstrakte Keywords** & **abstrakte Lokatoren**
    
- ✅ Fachliche Schritte klar & knapp
    
- ✅ Technik (Sync, Stabilität, Selektoren) in **Adapter/Bibliothek**
    

---

## Refactoring-Leitfaden (Bestand säubern)

1. **Lokatoren extrahieren** → funktionale Namen + zentrale Map.
2. **Warte/Sync entfernen** → Smart-Waits/Retry in Bibliothek kapseln.
3. **Programmierlogik tilgen** → domänenspezifische Keywords einführen, Datenvariation via Testdatenquelle.  
4. **Guardrails einziehen** → Lint/CI blockiert No-Gos in `*.robot`.   

---

## Nutzen (warum sich die Disziplin lohnt)

- **Lesbarkeit:** Fachtester verstehen Tests ohne Technik-Handbuch.
    
- **Wartbarkeit:** Änderungen an UI/Timing betreffen primär den Adapter, nicht alle Tests.
    
- **Stabilität:** Zentrale Sync-Strategien statt Flickenteppich.
    
- **DRY:** Ein Ort für Selektoren & Technik – keine Wiederholungen in Tests.