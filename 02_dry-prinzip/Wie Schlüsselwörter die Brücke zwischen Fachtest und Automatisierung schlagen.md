---
title: Keine Übersetzung nötig
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
kapitel_nummer: 2.2

# Optional: Position in der Sidebar (numerisch, für Sortierung in GitBook)
# Beispiele: 1, 2, 3.5 (Zahl mit Dezimalstelle = Zwischenposition)
sidebar_position: 2.2

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

## Wie Schlüsselwörter die Brücke zwischen Fachtest und Automatisierung schlagen

Die beste Möglichkeit, Aufwand zu vermeiden?  
**Gar nichts machen müssen.**

Das klingt erstmal nach Faulheit – ist aber in Wahrheit **maximale Effizienz**:  
Denn jede Tätigkeit, die **nicht** anfällt, spart nicht nur Zeit, sondern auch Komplexität und Fehlerquellen.

---

## Ein klassisches Beispiel: Die Übersetzung in Skriptsprache

In vielen Projekten müssen Testfälle – meist von Fachtestern geschrieben – von anderen Personen in Skriptcode „übersetzt“ werden.  
Das kostet Zeit, erfordert viel Abstimmung und ist anfällig für Fehler.

Aber: **Braucht man diese Übersetzung überhaupt?**

---

## Schlüsselwortbasiertes Testen: Schreiben wie ein Mensch, ausführen wie ein Automat

Wenn Testfälle mit **Schlüsselwörtern** (Keywords) beschrieben werden, passiert plötzlich etwas Magisches:

- Fachtester schreiben ihre Testfälle **lesbar und verständlich** – fast wie in Prosa.
- Die Beschreibung ist dabei **strukturiert und formal genug**, dass sie **direkt automatisiert** ausgeführt werden kann.
- Eine zusätzliche Übersetzung durch ein separates Team entfällt komplett.

Der Ablauf der Testfallerstellung mit Schlüsselwörtern, dabei wird die Automatisierung einem geschenkt:

![Ein-Phasen-Übersetzung mit Schlüsselwörtern](../assets/diagrams/dry-prinzip/testfall-ohne-zweite-uebersetzung.svg)

---

## Einmal automatisiert – unendlich oft genutzt

Die Grundidee:  
Ein Testfall besteht aus einer Abfolge von Schlüsselwörtern wie `GibEin`, `PrüfeWert` oder `Klicke`.

Diese Schlüsselwörter werden **einmalig** durch ein Automatisierungsteam implementiert – und stehen dann **beliebig oft** zur Verfügung.

> 👉 Ein Testfall ist dann nur noch eine **Reihung von Bausteinen**, die bereits funktionieren.

Und genau das ist die Essenz des DRY-Prinzips:  
**Einmal machen – überall wiederverwenden.**

## Beispiel für einen schlüsselwortbasierten Testfall

```
ÖffneAnwendung( "Reisekosten" )
WähleAus( "Menü", "Neue Abrechnung" ) 
GibEin( "Reisedatum", "2025-05-12" ) 
GibEin( "Zielort", "Berlin" ) 
Klicke( "Speichern" )
PrüfeWert( "Statusmeldung", "Abrechnung gespeichert" )
```

Jeder Schritt nutzt ein **abstraktes Schlüsselwort** (`GibEin`, `Klicke`, `PrüfeWert`) und einen **abstrakten Lokator** wie `"Zielort"` – also einen funktionalen Namen, der vom Testautor verwendet wird.

> Zur Laufzeit werden diese abstrakten Lokatoren von der Schlüsselwortbibliothek in **konkrete Lokatoren** (z. B. XPath oder CSS-Selektoren) übersetzt – der Fachtester muss sich darum nicht kümmern.

Das Ergebnis:  
Der Test ist **leicht verständlich, wiederverwendbar und wartungsarm**.
## Fazit

Reduktion auf Null heißt:  
**Nicht optimieren, sondern eliminieren.**

Wenn etwas nicht nötig ist – z. B. das manuelle Übersetzen von Testfällen – dann sollte es auch nicht stattfinden.

Schlüsselwortbasierte Tests sind dabei ein mächtiges Werkzeug, um unnötige Arbeit von vornherein zu verhindern – und machen gleichzeitig das Testdesign klarer und verständlicher.

