---
title: Übliche Vorgehensweise
description:  Warum zwei Übersetzungen pro Testfall Aufwand und Fehlerquellen verursachen – und wie man das vermeiden kann.
tags: ["dry", "testfallstruktur", "übersetzung", "schlüsselwortnotation"]

# Status im Lebenszyklus der Seite (für Arbeitsorganisation)
# Mögliche Werte:
# - Entwurf
# - In Bearbeitung
# - Zur Prüfung
# - Fertig
# - Archiviert
status: Fertig

# Typ der Seite im Inhaltsverzeichnis (steuert Sidebar-Darstellung in GitBook/Obsidian)
# Mögliche Werte:
# - kapitel         → Kapitelübersicht
# - artikel         → Ein normaler Fließtext-Artikel
# - technik         → Detaillierte technische Erklärung oder Pattern
# - beispiel        → Konkretes Beispiel mit Code/Diagramm
# - notiz           → Rohentwurf oder Ideensammlung (nicht für Veröffentlichung gedacht)
type: artikel

# Kapitelnummer zur stabilen Sortierung im Treeview
# Beispiele: 2.3, 2.4, 3.1 (für Haupt- und Unterkapitel)
kapitel_nummer: 2.1

# Optional: Position in der Sidebar (numerisch, für Sortierung in GitBook)
# Beispiele: 1, 2, 3.5 (Zahl mit Dezimalstelle = Zwischenposition)
sidebar_position: 2.1

# Wer hat an diesem Artikel gearbeitet?
# Auch mehrere Einträge möglich
editors:
  - zoltan

# Automatisch vom Templater gesetzt
created: 2025-08-11
updated: 2025-08-11

# Rolle im Buchkontext (Meta-Ebene)
# Mögliche Werte:
# - Kapitelübersicht
# - Technik-Erläuterung
# - Praxisbeispiel
# - Denkmodell
# - Werkzeugbeschreibung
rolle: Inhalt

# Zugehöriges Hauptkapitel
# Mögliche Werte (Stand heute):
# - Einleitung
# - DRY-Prinzip
# - Beobachtbarkeit & Steuerbarkeit
# - Test-Denkmodelle
# - GUI-Strategien
kapitel: DRY-Prinzip
---

## Übliche Vorgehensweise: Zwei Übersetzungen pro Testfall

In vielen Projekten läuft die Testautomatisierung ungefähr so ab:

1. Ein **Fachtester** erstellt einen Testfall in Prosa.
2. Ein **technischer Tester** übersetzt diesen in die Skriptsprache des Automatisierungswerkzeugs.

Klingt erstmal logisch – ist aber mit unnötigem Aufwand und Risiko verbunden.

---

## Zwei Übersetzungen, zwei Problemquellen

Die Umsetzung einer fachlichen Anforderung in ein automatisiertes Testskript umfasst typischerweise **zwei separate Übersetzungsschritte**:

1. **Anforderung → Prosa-Testfallbeschreibung**  
2. **Prosa-Testfallbeschreibung → Automatisierungsskript**

In der Praxis führt das oft zu folgenden Problemen:

- Die Prosa-Testfälle sind **zu ungenau**, z. B. _„Man wählt eine geeignete Person aus.“_
- Es fehlen **konkrete Testdaten** – der Testfall ist rein **abstrakt**.
- Die **Startbedingungen** sind unklar: Welche Daten oder Zustände werden in der Testumgebung vorausgesetzt?

**Jede dieser Übersetzungen ist eine Interpretation – und jede Interpretation ist eine potenzielle Fehlerquelle.**  
Solche Lücken erzeugen Nachfragen, Missverständnisse – oder führen dazu, dass der Testfall gar nicht umgesetzt wird.

## Zwei Übersetzungen = doppelte Fehlerquelle

Ein klassisches Problem in der Testautomatisierung:  
**Ein Testfall wird nicht einmal, sondern zweimal interpretiert – und damit potenziell verfälscht.**

Der Ablauf sieht in vielen Projekten so aus:

![Zwei-Phasen-Übersetzung bei herkömmlicher Testfallautomatisierung](../assets/diagrams/dry-prinzip/testfall-uebersetzungen.svg)

*Jeder Übersetzungsschritt ist eine potenzielle Fehlerquelle.*

Jede Rolle bringt ihre Sichtweise und ihr Verständnis ein – was grundsätzlich gut ist.  
Aber bei mangelnder Struktur oder unklaren Begriffen entstehen **Interpretationsspielräume**, die sich in Bugs oder instabilen Tests niederschlagen.

Die Lösung?  
Ein Notationssystem, das beide Welten zusammenbringt – z. B. durch **abstrakte Lokatoren und Schlüsselwörter**.


---

## Was wäre, wenn diese Übersetzung entfällt?

Zwei Übersetzungen bedeuten doppelten Aufwand – und doppeltes Risiko für Missverständnisse.  
Aber was, wenn man den zweiten Schritt einfach **weglassen** könnte?

Im Kapitel 👉 [DRY-Prinzip: Keine Übersetzung nötig](Wie%20Schlüsselwörter%20die%20Brücke%20zwischen%20Fachtest%20und%20Automatisierung%20schlagen.md) zeigen wir, wie sich dieser Schritt komplett eliminieren lässt –  
**durch schlüsselwortbasierte Testfallbeschreibung**, die direkt automatisierbar ist.
