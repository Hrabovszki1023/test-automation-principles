---
title: DRY-Prinzip im modellbasierten Testen (MBT)
description: Wie modellbasiertes Testen das DRY-Prinzip automatisch unterstützt – und was das für Design und Wartbarkeit bedeutet.
tags:
  - dry
  - mbt
  - testdesign
  - wiederverwendung
status: in Bearbeitung
type: artikel
editors:
  - zoltan
created: 2025-09-09
updated: 2025-09-09
rolle: Anwendungsbeispiel
kapitel: DRY-Prinzip
---

# DRY-Prinzip im modellbasierten Testen (MBT)

Modellbasiertes Testen (MBT) und das DRY-Prinzip (Don’t Repeat Yourself) sind natürliche Partner:

> Ein gutes MBT-Modell ist die zentrale Quelle –  
> aus der viele Testfälle **automatisch und konsistent** abgeleitet werden.

Das bedeutet: **Redundanz wird systematisch vermieden**, sowohl im Testdesign als auch in der Automatisierung.  
Wartung, Erweiterung und Wiederverwendung profitieren direkt davon.

---

## Wo MBT konkret DRY umsetzt

1. **Zentrale Modelle statt mehrfacher Testfallbeschreibungen**
Anstatt ähnliche Testschritte immer wieder in Prosatestfällen zu beschreiben,  
werden **einmalig Modelle definiert**, die dann viele Varianten automatisch generieren.

2. **Parametrisierte Modelle**
Durch Eingangsgrößen, Bedingungen und Übergänge können Modelle **dynamisch angepasst** werden –  
ohne, dass der zugrunde liegende Ablauf dupliziert werden muss.

3. **Wiederverwendbare Modellbausteine**
Häufige Abläufe wie „Login“, „Navigation“ oder „Fehlermeldung anzeigen“ können als **wiederverwendbare Submodelle** gestaltet werden.  
Diese lassen sich in verschiedenen übergeordneten Szenarien einbinden.

4. **Zentrale Testdatenstrategie**
Testdaten werden nicht mehr manuell in jeden Testfall geschrieben, sondern  
kommen aus **zentral verwalteten Datenpools** oder **konfigurierbaren Generatoren**.

5. **Abstraktion der Testaktivitäten**
Die Aktionen, die beim Traversieren des Modells ausgeführt werden, sind oft als **Bibliotheken von Schlüsselwörtern oder Aktionen** gekapselt –  
auch das ist DRY: Der gleiche „Klick“ oder „Eingabeschritt“ wird nur einmal technisch definiert.

---

## Fazit

> Modellbasiertes Testen ist nicht nur ein Testdesign-Ansatz –  
> sondern **ein automatisierter Weg, das DRY-Prinzip in der Praxis umzusetzen**.

Wer MBT nutzt, profitiert automatisch von den DRY-Vorteilen:

- weniger Redundanz
- mehr Wiederverwendung
- konsistentere Tests
- bessere Wartbarkeit

Und wenn sich etwas ändert, muss **nur das Modell angepasst werden** –  
die daraus erzeugten Tests aktualisieren sich automatisch.

---

## Siehe auch

- 📎 [Abstrakte und elementare Schlüsselwörter – ein starkes Team](../elementare-schluesselwoerter/README.md)
- 📎 [Testfallbeschreibung ohne technische Übersetzung](../keine-uebersetzung-noetig/README.md)
