---
title: Mindestkriterien für Test-IDs
description: Die 30-Sekunden-Checkliste für brauchbare Test-IDs (data-testid, automation-id, Swing name).
tags: ["dry", "lokatoren", "checkliste"]
status: Entwurf
type: artikel
---

# Mindestkriterien für Test-IDs

**Heilige Dreifaltigkeit (Orientierung):**
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

Eine Test-ID ist **brauchbar**, wenn sie …

1. **Eindeutig** ist  
   – applikationsweit einmalig, keine Duplikate.

2. **Stabil** bleibt  
   – über Releases unverändert; keine Abhängigkeit von Layout, Reihenfolgen oder Indizes.

3. **Sprechend & domänennah** ist  
   – fachlicher Name statt Technik-Kürzel (`customer.search.submit` statt `btn123`).

4. **Schema-konform** ist  
   – klein geschrieben, punkt-getrennt, `[a-z0-9_.-]`, keine Umlaute/Leerzeichen.

5. **Neutral** gegenüber Sprache & Daten ist  
   – keine Lokalisierung, keine PII/Geheimnisse in der ID.

> **Merksatz:** Die Aufgabe des Lokators ist **nur** die eindeutige Identifikation des Objekts – nicht mehr und nicht weniger.

