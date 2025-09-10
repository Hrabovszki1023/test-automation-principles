---
title: Vergleich klassisch vs Schluesselwoerter
sidebar_position: 4
beschreibung:
tags:
  - schlüsselwörter
  - abstraction
  - dry
  - wiederverwendung
status: in Bearbeitung
type: artikel
editors:
  - zoltan
created: 2025-08-12
updated: 2025-08-12
rolle: Technik-Erläuterung
kapitel: DRY-Prinzip
kapitel_nummer: 2
---


| Aspekt                                 | Klassischer Ansatz                          | Schlüsselwort-Notation (DRY)                          |
|----------------------------------------|---------------------------------------------|-------------------------------------------------------|
| **Testfallbeschreibung**              | Prosatext (z. B. Word, Jira, Excel)         | Strukturierte Schlüsselwörter                        |
| **Automatisierungsschritt**           | Manuelle Übersetzung durch technischen Tester | Direkt ausführbar durch Framework                   |
| **Fehlerpotenzial**                   | Hoch – zwei Übersetzungen, viele Missverständnisse | Niedrig – keine zweite Übersetzung notwendig    |
| **Wiederverwendbarkeit**              | Gering – jeder Testfall ist individuell     | Hoch – durch Bibliotheken & abstrakte Schlüsselwörter |
| **Werkzeugabhängigkeit**             | Hoch – Testfälle sind an Tool gebunden      | Gering – Technik ist im Framework gekapselt          |
| **Lesbarkeit für Fachtester**         | Niedrig – technischer Code                  | Hoch – durch sprechende Begriffe in Fachsprache      |
| **Wartbarkeit bei Änderungen**        | Aufwendig – viele Stellen betroffen         | Minimal – Änderung an einer zentralen Stelle         |
| **Pflege von Lokatoren & Logik**      | Direkt im Testcode                          | Zentral im Framework                                 |
| **GUI-Technologie-Wechsel möglich?** | Nur mit kompletter Neuentwicklung           | Ja – durch Adapter im Framework                     |
| **Testfallstruktur**                  | Unstrukturiert, oft lang und unklar         | Klar, modular, drehbuchartig                         |
