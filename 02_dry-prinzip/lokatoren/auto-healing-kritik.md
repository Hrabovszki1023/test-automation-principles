---
title: Kritik am Auto-Healing von Lokatoren
description: Warum KI-basierte „Wunderheilungen“ von Lokatoren das Problem auf der falschen Meta-Ebene lösen.
tags: ["dry", "lokatoren", "auto-healing", "kritik"]
status: Entwurf
type: artikel
---

# Kritik am Auto-Healing von Lokatoren

> Kurzfassung: **Heilen** kaschiert, **Gestalten** behebt.  
> Oder: *Don’t fix the fire alarm. Fireproof the building.*

---

## 1) Falsche Meta-Ebene

„Healing“ versucht, brüchige Selektoren (CSS/XPath) nachträglich zu erraten.  
Das eigentliche Problem liegt aber **davor**:  
- fehlende **proaktive Test-IDs** (`data-testid`, `automation-id`, Swing `setName`)  
- und keine **zentrale DRY-Quelle**, aus der Lokatoren generiert werden.

---

## 2) Risiken von Healing

- **Nicht-Determinismus**: ML-Heuristiken finden „irgendwas“ – oft falsch positiv.  
- **Stille Fehlanpassungen**: Tests laufen grün, obwohl am falschen Element.  
- **Traceability bricht**: Warum ein Test nach einer Änderung noch läuft, bleibt undokumentiert.  
- **Verstoß gegen DRY**: Healing erzeugt implizite Logik im Runtime-Pfad statt eine zentrale Quelle zu nutzen.  
- **Kosten & Lock-in**: Pflege, Training, Plattformbindung – statt einfacher Locator-Registry.

---

## 3) Was stattdessen (robust & DRY)

1. **Heilige Dreifaltigkeit einhalten**:  
   👤 Abstrakter Bezeichner (Vater) → ✨ Konkreter Lokator (Sohn/Fleischwerdung) → 🛠️ Widget/Adapter (Heiliger Geist).
2. **Eindeutige, stabile Test-IDs** in der Anwendung verankern.  
3. **Zentrale Registry** (`locator-ids.yaml`) + **Generator** je Plattform.  
4. **Kontext-Scoping** statt globaler Wild-XPaths.  
5. **CI-Linting**: Verbot von index-/layoutbasierten Selektoren, Duplikat-Check, PII-Scan.  
6. **Änderungsprozess mit Alias/Deprecation** für sanfte Migration.

---

## 4) Gibt es legitime Ausnahmefälle?

- **Altsysteme** ohne nachrüstbare IDs: Healing **max. temporär**, sichtbar geloggt, mit **Exit-Datum**.  
- **Migrationsphasen**: Healing als **Übergangsbrücke**, nicht als Dauerlösung.  

> 🚩 **Rote Flagge:** Healing im Produktivlauf ohne Audit-Trail und ohne PR an der Locator-Quelle.

---

## Merksatz

Lokatoren haben **nur eine Aufgabe**: ein GUI-Objekt **eindeutig identifizieren**.  
Wenn das verlässlich und DRY gelöst ist, braucht niemand „Wunderheilungen“.
