---
title: <% tp.file.title %>  # Automatisch der Dateiname (in Obsidian per Templater eingefügt)
description:                # Kurzbeschreibung (1–2 Sätze), erscheint z. B. in GitBook als Summary
tags: []                    # Freie Stichworte, mehrere erlaubt. z. B.: ["dry", "lokatoren", "steuerbarkeit"]

# Status im Lebenszyklus der Seite (für Arbeitsorganisation)
# Mögliche Werte:
# - Entwurf
# - In Bearbeitung
# - Zur Prüfung
# - Fertig
# - Archiviert
status: Entwurf

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
kapitel_nummer: 2.3

# Optional: Position in der Sidebar (numerisch, für Sortierung in GitBook)
# Beispiele: 1, 2, 3.5 (Zahl mit Dezimalstelle = Zwischenposition)
sidebar_position: 2.3

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
kapitel: DRY-Prinzip
---

