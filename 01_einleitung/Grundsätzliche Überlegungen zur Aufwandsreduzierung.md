---
title: Grundsätzliche Überlegung
description:                # Kurzbeschreibung (1–2 Sätze), erscheint z. B. in GitBook als Summary
tags: []                    # Freie Stichworte, mehrere erlaubt. z. B.: ["dry", "lokatoren", "steuerbarkeit"]

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
kapitel_nummer: 1.1

# Optional: Position in der Sidebar (numerisch, für Sortierung in GitBook)
# Beispiele: 1, 2, 3.5 (Zahl mit Dezimalstelle = Zwischenposition)
sidebar_position: 1.1

# Wer hat an diesem Artikel gearbeitet?
# Auch mehrere Einträge möglich
editors:
  - zoltan

# Automatisch vom Templater gesetzt
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

# Rolle im Buchkontext (Meta-Ebene)
# Mögliche Werte:
# - Kapitelübersicht
# - Technik-Erläuterung
# - Praxisbeispiel
# - Denkmodell
# - Werkzeugbeschreibung
rolle: Denkmodell

# Zugehöriges Hauptkapitel
# Mögliche Werte (Stand heute):
# - Einleitung
# - DRY-Prinzip
# - Beobachtbarkeit & Steuerbarkeit
# - Test-Denkmodelle
# - GUI-Strategien
kapitel: Einleitung
---
---

## Aufwand? Kommt drauf an, _wo_ du änderst

Wenn sich an der Software etwas ändert, stellt sich immer die gleiche Frage:  
**Wie viele Stellen in den Tests muss ich jetzt anfassen?**

Im Idealfall lautet die Antwort:

> **Genau eine.** 🎯

Denn je mehr Stellen du anfassen musst, desto größer ist der Aufwand.  
Und desto wahrscheinlicher ist es, dass du irgendwo was vergisst – oder dass etwas kaputtgeht.

---

## Reduktion auf _eine Stelle_ ist möglich!

Auch wenn’s paradox klingt:  
Ja, **jeder Testfall ist ein Einzelfall**.  
Und ja, man muss jeden Test irgendwie spezifizieren.

Aber:  
Wenn du bestimmte Prinzipien und Techniken (wie z. B. **Abstraktion**, **Vererbung**, **Parametrisierung** oder das **DRY-Prinzip**) richtig einsetzt,  
dann ist eine saubere Reduktion auf **eine Änderungsstelle pro Aspekt** möglich.

Konkret heißt das:

- Eine Änderung am UI? → Nur den Lokator ändern – nicht jeden Test.
- Eine neue Berechnung? → Nur die Prüflogik anpassen.
- Ein anderer Testdatenwert? → In der zentralen Testdatenquelle ändern.

Das ist keine Utopie – es ist machbar.  
Man muss es nur **von Anfang an konsequent durchziehen**.

---

## Ohne Struktur wird’s wild

Ein häufiger Aufwandstreiber ist auch das Testumfeld selbst.  
Wenn dort Wildwuchs herrscht – unklare Strukturen, schlecht benannte Objekte, fehlende Synchronisation –  
dann brauchst du für jede kleine Änderung gleich ein Großreinemachen.

Daher lohnt es sich, auch bei „Nebensächlichkeiten“ wie

- guter **Benennung** (von Klassen, Methoden, Schritten), 
- klarer **Skriptstruktur**
- und durchdachter **Synchronisation** der Testumgebung
- auf **Lesbarkeit und Nachvollziehbarkeit** zu achten.  

Denn Tests müssen nicht nur laufen – sie müssen **verständlich wartbar** sein.

---

### Fazit

Die Frage ist also nicht _ob_ du Aufwand hast –  
sondern **ob du ihn jedes Mal neu hast oder nur ein einziges Mal**.

Und genau hier liegt der Schlüssel zur effizienten Testautomatisierung.

---
