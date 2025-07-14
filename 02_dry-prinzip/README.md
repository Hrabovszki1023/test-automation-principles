---
title: DRY-Prinzip – Wiederholung vermeiden, Wartung erleichtern
description: Warum das DRY-Prinzip für nachhaltige Testautomatisierung unverzichtbar ist – und wie man es konkret umsetzt.
tags:
  - dry
  - prinzipien
  - wartbarkeit
  - testautomatisierung
  - technikensammlung
status: fertig
type: kapitel
sidebar_position: 2
editors:
  - zoltan
created: 2025-07-13
updated: 2025-07-13
rolle: Kapitelübersicht
---

# Kapitel: DRY-Prinzip – Wiederholung vermeiden, Wartung erleichtern

> „Don’t Repeat Yourself“ – dieses Prinzip ist mehr als nur ein schlauer Spruch aus der Softwareentwicklung.
> In der Testautomatisierung ist es **der Schlüssel**, um langfristig effizient und stabil zu arbeiten.

Das DRY-Prinzip besagt: **Vermeide Redundanz.**
Informationen, Regeln oder Strukturen sollten **nur an einer Stelle definiert** werden. Wird dasselbe an mehreren Orten wiederholt, entstehen schnell Wartungsprobleme, Inkonsistenzen – und Frust.

In der Testautomatisierung gilt das ganz besonders:
Tests bestehen oft aus ähnlichen Schritten, benutzen dieselben Elemente, prüfen dieselben Dinge – aber wenn man das alles mehrfach „per Hand“ schreibt oder kopiert, dann wird Pflege zur Hölle.

Und genau das passiert in vielen Projekten. DRY wird nicht beachtet – und irgendwann wird fast nur noch gewartet, kaum noch Neues geschaffen.

---

## Warum ist DRY so wichtig für Testautomatisierung?

In klassischen Softwareprojekten hilft DRY, den Code übersichtlich und wartbar zu halten.
In der Testautomatisierung kommt noch eine Besonderheit dazu:

👉 **Tests ändern sich ständig.**
Wenn die Software angepasst wird, müssen oft dutzende, manchmal hunderte Tests mitgezogen werden.
Wenn die gleichen Lokatoren, Testschritte oder Daten an zehn Stellen stehen, dann muss man zehn Stellen ändern.

Mit DRY reduziert sich das auf **eine einzige Stelle** – und alle Tests profitieren automatisch davon.

---

## Und der größte Fehler?

Der größte Fehler ist nicht, das DRY-Prinzip falsch anzuwenden –
sondern zu glauben, dass es **nicht so wichtig** ist.

Manche tun es als „zu theoretisch“ ab, andere halten Copy & Paste für harmlos.
Aber die Quittung kommt später:

> 🔥 Was du heute kopierst, wirst du morgen zehnmal anfassen müssen.

**DRY lässt sich ignorieren – seine Folgen aber nicht.**
Und genau deshalb lohnt es sich, sich einmal bewusst mit dem Prinzip auseinanderzusetzen.
Denn wer DRY ernst nimmt, macht sich das Leben in der Testautomatisierung **spürbar leichter**.

### Und das Perfide daran?

Gerade in der GUI-Testautomatisierung lauert noch eine andere Gefahr:
**Skriptfehler tauchen oft erst zur Laufzeit auf** – und dann meistens **nicht alle auf einmal**, sondern **einer nach dem anderen**.
Der erste Fehler blockiert den Testlauf, verdeckt den nächsten – und das Debugging wird zur Geduldsprobe.

Noch schlimmer:
**Skriptfehler überdecken echte Fehler in der Anwendung.**
Wenn die Tests ständig an ihrer eigenen Instabilität scheitern, dann gehen die tatsächlichen Probleme der SUT einfach unter.

> Die Folge: „Unsere Automatisierung bringt nichts – sie zeigt ja eh nur Skriptfehler.“
> Und plötzlich steht das ganze Projekt auf der Kippe.

Darum gilt in der Praxis:
**Die Anzahl der Skriptfehler muss gegen null gehen.**
Erst dann kann die Automatisierung ihre eigentliche Aufgabe erfüllen – nämlich zuverlässig und frühzeitig Fehler in der Anwendung aufzudecken.

Und genau deshalb ist das DRY-Prinzip so wichtig:
**Je weniger Redundanz, desto weniger Fehlerquellen – und desto robuster die Tests.**

---

## DRY – und dann noch ein Schritt weiter

Das DRY-Prinzip hilft, überflüssige Wiederholungen zu vermeiden.
Aber manchmal geht noch mehr: Man kann Dinge **komplett weglassen**.

> 🧠 **„The best part is no part.“**
> – Elon Musk, bei der Vorstellung des Raptor-3-Triebwerks

Was in der Raumfahrt gilt, lässt sich auch auf Tests übertragen:
**Was du nicht brauchst, kann nicht kaputtgehen.**
Jede unnötige Abhängigkeit, jeder doppelte Schritt, jede manuelle Konfiguration – all das ist eine potenzielle Fehlerquelle.

Deshalb lohnt sich beim Testdesign immer auch die Frage:
*Muss das wirklich sein?*
Oder gibt es eine Möglichkeit, diesen Teil ganz zu eliminieren?

---

## Was dich in diesem Kapitel erwartet

In den folgenden Artikeln zeigen wir, wie sich das DRY-Prinzip konkret in der Testautomatisierung umsetzen lässt – mit Fokus auf:

* Testfallstruktur und Wiederverwendbarkeit
* Reduktion von Pflegeaufwand durch zentrale Definitionen
* Typische Problemstellen wie Lokatoren, Testdaten oder Synchronisation
* Praktische Techniken wie Schlüsselwortnotation und Mapping-Strategien
* ✅ **Eine Sammlung praxiserprobter DRY-Techniken**
  – Methoden, Werkzeuge und Ideen, die helfen, alltägliche Probleme zu lösen.

Denn:
**Jedes Projekt ist anders.**
Was in einem Setup funktioniert, kann in einem anderen scheitern – weil das Tooling, die Prozesse oder das Team anders sind.
**DRY ist kein starres Rezept, sondern ein Werkzeugkasten.** Und dieses Kapitel hilft dir, genau die Werkzeuge zu finden, die in *deinem* Projekt funktionieren.
