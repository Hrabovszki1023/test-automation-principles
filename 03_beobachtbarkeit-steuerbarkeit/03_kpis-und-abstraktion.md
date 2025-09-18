---
title: KPIs für Stabilität & Geschwindigkeit – warum nur mit Abstraktion
description: Ohne abstrakte Lokatoren und abstrakte Interaktionen gibt es keine belastbaren KPIs. Diese Seite erklärt das Warum und den Rahmen.
tags: [steuerbarkeit, beobachtbarkeit, kpi, telemetry, okw, dry]
status: In Bearbeitung
type: artikel 
---


# KPIs für Stabilität & Geschwindigkeit – warum nur mit Abstraktion

**These:** Sinnvolle KPIs (p95-Dauer, Timeout-Rate, Flake-Rate, Retry-Intensität) sind nur möglich, wenn wir **abstrakte Lokatoren** und **abstrakte Interaktionen** verwenden. Technikdetails bleiben in der Adapter-Schicht.

## Begriffe (kurz)

| Ebene | Abstrakt (fachlich) | Konkret (technisch) |
|---|---|---|
| **Lokator** | `Destination`, `Save`, `Status Message` (funktionale Namen) | `css:#destination`, `css:button.save` |
| **Interaktion** | `Click`, `Set Value`, `Verify Value`, `Select Menu` (Intent) | WebDriver-Calls, JS-Snippets, Low-Level Waits |

- **Abstrakte Lokatoren** sind **stabile Identitäten** im Sinne der Domäne.  
- **Abstrakte Interaktionen** beschreiben **Was** passiert, nicht **Wie**.  
- Das **Wie** gehört in die **Adapter/Keyword-Bibliothek** (Ready-Checks, Selektoren, Wait-Strategien).

## Warum ohne Abstraktion nichts messbar ist

- **Identität fehlt:** Reine CSS/XPath im Test zerfallen bei jedem UI-Refactor → keine Zeitreihen möglich.  
- **Aggregation scheitert:** Synonym-Befehle („Click Element“, „DoClick“, „Tap“) zerschießen p95/p99-Metriken.  
- **Kein Drilldown:** Ohne Taxonomie (Seite, Kategorie, Widget-Name) gibt’s keine Heatmaps („Top-Slow Buttons“).  
- **Anti-DRY:** Jede Änderung erfordert Massen-Edits; KPIs messen Refactoring statt Verhalten.

## Messvoraussetzungen (Definition of Ready für KPIs)

1. **Taxonomie:** `page`, `locator_name`, `locator_category` (z. B. `Button`, `Field`, `MenuItem`), `keyword`.  
2. **Eindeutige Namen/IDs:** Lokator-Namen sind stabil; optional feste IDs (`button.save`).  
3. **Einheitliche Keywords:** `Open Application`, `Select Menu`, `Set Value`, `Click`, `Verify Value`.  
4. **Telemetry im Adapter:** Jedes Keyword emittiert ein Event mit Dauer, Budget, Wait-Breakdown, Ergebnis.  
5. **SLO/SLA definiert:** z. B. _PageReady p95 < 1 000 ms_; Poll-Intervall passend zum Ziel (≈ ≤ 0,2 × Zielzeit).

## Heilige Dreifaltigkeit (Was–Wie–Tut)

- **Was:** Abstrakter Lokator (z. B. `"Destination"`).  
- **Tut:** Abstrakte Interaktion (`Set Value`, `Click`, `Verify Value`, `Select Menu`).  
- **Wie:** Adapter löst Technik (Ready-Signale, Selektoren, Timeouts, Polling, Network-Idle).

**Ergebnis:** Tests bleiben fachlich & lesbar, KPIs werden **vergleichbar und steuerbar**.
