---
title: Kontext-Scoping bei Lokatoren
description: Warum Fenster/Dialoge als Suchkontext gewählt werden sollten und wie das DRY spart.
tags: ["dry", "lokatoren", "scoping"]
status: Entwurf
type: kapitel
---

# Kontext-Scoping bei Lokatoren

**Heilige Dreifaltigkeit (Orientierung):**  
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

---

## Motivation

Ohne Scoping werden GUI-Elemente oft mit **globalen XPaths oder CSS-Ketten** gesucht.  
Das führt zu:

- **Redundanz**: Fenster-Locator steckt in jedem Kindobjekt.  
- **Fragilität**: Kleine Layout-Änderungen brechen viele Tests.  
- **Verwirrung**: Unklar, in welchem Fenster gesucht wird.

👉 **Lösung:** Fenster/Dialoge/Container als **Kontext** wählen und Kindobjekte **relativ** suchen.  

---

## Inhalte dieses Abschnitts

- [Prinzip: Kontext wählen](./prinzip.md)  
  → Überblick über das Grundmuster „Fenster setzen, Kinder relativ suchen“.  

- [Umsetzung im Detail](./umsetzung.md)  
  → Technische Umsetzung mit `Select Window`, `.//`-Notation und Adapter-Logik.  

---

## Merksatz

**Kontext-Scoping = Fenster einmal wählen, Kinder nur noch relativ suchen.**  
So bleibt das Testdesign DRY und robust.
