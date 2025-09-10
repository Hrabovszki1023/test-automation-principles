---
title: Begriffsklärung der Schlüsselwörter
description: Definitionen und Abgrenzung von abstrakten, elementaren und generischen Schlüsselwörtern im Keyword-basierten Testdesign.
tags: ["begriffe", "schlüsselwörter", "keyword-driven", "grundlagen"]
status: Fertig
type: artikel
sidebar_position: 2
editors:
  - zoltan
created: 2025-09-09
updated: 2025-09-09
rolle: Begriffsklärung
kapitel: Grundlagen
---

# Begriffsklärung: Schlüsselwörter im Keyword-basierten Testdesign

In der Literatur und Praxis kursieren unterschiedliche Begriffe zur Beschreibung von Testschlüsselwörtern.  
Diese Seite klärt, welche Begriffe wir verwenden – und wie sie voneinander abzugrenzen sind.

---

## Abstrakte Schlüsselwörter

**Definition:** Fachlich beschreibende Schlüsselwörter, die auf höherer Ebene Testaktionen ausdrücken (z. B. `Benutzer anlegen`, `Bestellung abschließen`).

- **Zweck:** Verständlichkeit für Fachanwender, Strukturierung von Testfällen
- **Merkmale:** lesbar, sprechend, domänenspezifisch
- **Synonyme in Literatur:** High-Level Keywords, Business Keywords, Scenario Steps
- **Quelle:** [ISTQB Glossary: high-level keyword](https://glossary.istqb.org/)

---

## Elementare Schlüsselwörter

**Definition:** Technisch konkrete Schlüsselwörter, die einzelne GUI-Aktionen repräsentieren (z. B. `SetValue`, `Click`, `Select`).

- **Zweck:** Wiederverwendbare Bausteine für alle Testfälle
- **Merkmale:** generisch, GUI-nah, stabil
- **Mögliche Synonyme:** Low-Level Keywords, Basisschlüsselwörter, generische Schlüsselwörter
- **Anmerkung:** Diese Begriffe werden oft nicht konsistent verwendet – Quellen siehe unten.

---

## Generische Schlüsselwörter

**Definition:** Projektunabhängige Schlüsselwörter, die in vielen GUI-Kontexten verwendbar sind (z. B. `Click`, `VerifyValue`).

- Wird bei uns synonym mit *elementaren Schlüsselwörtern* verwendet
- In einigen Frameworks (z. B. Robot Framework) auch als „Built-in Keywords“ bezeichnet

---

## Technische Schlüsselwörter

**(Optional, falls verwendet)**  
Bezeichnet Schlüsselwörter, die sich primär auf technische Aktionen beziehen (z. B. `Open Browser`, `Start App`, `Log`, `Set Log Level`), aber nicht direkt mit Testfachlichkeit zu tun haben.

---

## Quellen und Referenzen

- ISTQB Glossary: „Keyword-driven testing“, „High-level keyword“, „Low-level keyword“
- Robot Framework User Guide: Built-in Keywords, User-defined Keywords
- Literatur:
  - Graham Bath / Judy McKay: *The Software Test Engineer’s Handbook*
  - Rex Black: *Managing the Testing Process*
  - [TMap NEXT Testing Guide](https://www.tmap.net/)
