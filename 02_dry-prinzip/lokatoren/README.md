---
title: DRY bei Lokatoren
description: Warum stabile Test-IDs und Kontext-Scoping der Schlüssel zu wartbarer Testautomatisierung sind.
tags: ["dry", "lokatoren", "steuerbarkeit"]
status: Entwurf
type: kapitel
---

# DRY bei Lokatoren

**Heilige Dreifaltigkeit (Orientierung):**  
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

Lokatoren sind das Fundament jeder GUI-Testautomatisierung.  
Und genau hier passieren die größten **DRY-Verstöße**:  
- gleiche XPath-Schnipsel an zig Stellen,  
- fragile CSS-Klassen-Namen als Erkennungsmerkmal,  
- oder Fenster-IDs, die in jedem Kindobjekt dupliziert werden.  

Das Ergebnis: **hohe Wartungskosten und instabile Tests**.

Dieses Unterkapitel zeigt, wie man das DRY-Prinzip bei Lokatoren konsequent anwendet:

- [Mindestkriterien für Test-IDs](./test-ids-checkliste.md) – die kurze 5-Punkte-Checkliste  
- [Eigenschaften guter Test-IDs](./test-ids-eigenschaften.md) – ausführlich & mit Anti-Patterns  
- [Kontext-Scoping (Übersicht)](./kontext-scoping/README.md) – Einstieg ins Thema  
  - [Prinzip](./kontext-scoping/prinzip.md) – Grundmuster „Fenster setzen, Kinder relativ suchen“  
  - [Umsetzung](./kontext-scoping/umsetzung.md) – Detail mit `Select Window` und `.//`-Notation  
- [Generator-Prinzip](./generator-prinzip.md) – Fenster einmal definieren, Kinder automatisch ableiten  
- [Beispiele aus Swing & Web](./beispiele.md) – konkrete Codeausschnitte zum Anfassen  

---

## Einordnung in die „Heilige Dreifaltigkeit“

> 💡 **Infokasten**: Die Testautomatisierungs-Trinität  
>
> 1. **Abstrakter Bezeichner** – der **Vater**: gibt dem Objekt seinen Namen (fachlich/funktional).  
> 2. **Konkreter Lokator** – der **Sohn**: die „Fleischwerdung“ des Abstrakten, sichtbar und greifbar in der technischen Welt (XPath, `data-testid`, Swing-`setName`, …).  
> 3. **Widget/Adapter-Klasse** – der **Heilige Geist**: kapselt die Interaktion für den jeweiligen GUI-Objekttyp (Click, SetValue, Verify …).  
>
> 👉 Mit diesem Dreiklang bleibt die Verantwortung klar getrennt –  
> und das Test-Design heilig DRY. ✝️😇

---

## Weiterführend

- [Kritik am Auto-Healing von Lokatoren](./auto-healing-kritik.md) –  
  warum KI-basierte „Wunderheilungen“ nur Symptome kaschieren und DRY brechen.  

---

👉 Ziel: Lokatoren **eindeutig, stabil und sprechend** gestalten –  
und dabei **einmal definieren, überall nutzen**.
