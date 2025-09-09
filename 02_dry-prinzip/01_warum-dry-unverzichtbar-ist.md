---
title: Warum DRY für Testautomatisierung so entscheidend ist
description: Motivation und Praxisnutzen des DRY-Prinzips in der Testautomatisierung – vom Grundsatz bis zur Anwendung in Framework, Testdaten und GUI-Objekten.
tags:
  - dry
  - motivation
  - testautomatisierung
  - wartbarkeit
  - effizienz
status: fertig
type: artikel
rolle: Motivation
kapitel: DRY-Prinzip
sidebar_position: 1
editors:
  - zoltan
created: 2025-09-09
updated: 2025-09-09
---

# Warum DRY für Testautomatisierung so entscheidend ist

Das DRY-Prinzip („Don't Repeat Yourself“) ist einer der **zentralen Hebel**, um den **Wartungsaufwand** in der Testautomatisierung dauerhaft zu reduzieren.

Denn jedes redundante Element – egal ob Testcode, Testdaten, Konfiguration oder Lokatoren – ist eine **potenzielle Fehlerquelle**, die gepflegt werden muss.  
Und jede unnötige Wiederholung erhöht den Aufwand **exponentiell mit jedem neuen Testfall**.

---

## 💡 Was bedeutet DRY konkret in der Testautomatisierung?

Das DRY-Prinzip besagt, dass **jede Information nur einmal im System vorkommen sollte**.  
Das bedeutet: Wiederkehrende Logik, Daten oder Strukturen sollten **zentral definiert** und von überall aus **wiederverwendet** werden.

**Typische Beispiele:**

| Bereich | DRY-Anwendung |
|--------|---------------|
| **Testskripte** | Gemeinsame Schritte in zentrale Schlüsselwörter oder Bibliotheken auslagern |
| **Testdaten** | Zentrale Definition in YAML/CSV/JSON statt hartcodiert im Test |
| **Element-Lokatoren** | Zentrale Objektlisten statt XPath in jedem Skript |
| **Konfiguration** | Eine zentrale Stelle für Timeouts, URLs, Benutzerkonten etc. |
| **Protokollierung** | Gemeinsames Logging-Framework für alle Tests |
| **Testframework** | GUI-Adapter, Assertions, Fehlerbehandlung als wiederverwendbare Module |
| **Testumgebungsaufbau** | SetUp-/TearDown-Logik zentralisiert statt in jedem Testfall dupliziert |

---

## 🚫 Was passiert, wenn DRY ignoriert wird?

Wenn jede Automatisierung „für sich“ gebaut wird:

- entstehen hunderte Kopien derselben Logik,
- müssen Anpassungen mehrfach erfolgen – oft **nicht überall vollständig**,
- schleichen sich Inkonsistenzen, Inkapselungsfehler und „vergessene Stellen“ ein,
- wird die Wartung zur täglichen Qual.

---

## ✅ DRY als Erfolgsfaktor für nachhaltige Automatisierung

Ein gutes DRY-konformes Design sorgt dafür, dass du Änderungen **nur an einer Stelle** machen musst:

> **Ein geänderter Button-Name?**  
> → Nur den zentralen Lokator ändern – alle Tests profitieren.

> **Ein neues Format für Testdaten?**  
> → Parser anpassen – alle Tests nutzen die Änderung automatisch.

> **Ein neuer Login-Prozess?**  
> → `Login`-Schlüsselwort anpassen – keine einzige Testfallzeile muss geändert werden.

---

## 🧱 DRY geht über Code hinaus

Das DRY-Prinzip lässt sich auf **alle Ebenen der Automatisierung** anwenden:

- **Technik:** Wiederverwendbare Schlüsselwörter, Adapter, Logging, Fehlerbehandlung
- **Fachlichkeit:** Abstrakte Schlüsselwörter, zentral gepflegte Testbeschreibungen
- **Testdaten:** Parametrisierte Testdatenquellen, generische Konfigurationen
- **Umgebung:** Zentraler Aufbau von Testsystemen, zentrale Konfigurationsprofile
- **Wartung:** Gemeinsame Standards, Skriptstrukturen, Synchronisationsstrategien

---

## 📎 Siehe auch

- 🔗 [[07_die_Dreifaltigkeit_der_Lokatoren]]
- 🔗 [[Abstrakte und elementare Schlüsselwörter – ein starkes Team]]
- 🔗 [[Wie Schlüsselwörter die Brücke zwischen Fachtest und Automatisierung schlagen]]

---

## Fazit

Das DRY-Prinzip ist **keine theoretische Schönwetterregel** –  
sondern die **praktische Voraussetzung**, um Testautomatisierung **überhaupt wartbar** zu halten.

Je komplexer das System, desto mehr zahlt sich DRY aus:  
**Jede eingesparte Redundanz ist ein Stück Skalierbarkeit.**

