---
title: Abstrakte und elementare Schlüsselwörter – ein starkes Team
sidebar_position: 3
beschreibung: Wie sich abstrakte und elementare Schlüsselwörter in der Testautomatisierung ergänzen – und warum sie gemeinsam DRY ermöglichen.
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

# Abstrakte und elementare Schlüsselwörter – ein starkes Team

In der Testfall-Notation, insbesondere im Zusammenhang mit Schlüsselwort-basiertem Testen, ist das DRY-Prinzip ein entscheidender Erfolgsfaktor. Es sorgt für Wiederverwendbarkeit, klare Strukturen und reduzierte Wartungskosten. Dabei unterscheidet man zwei Arten von Schlüsselwörtern:

- **Abstrakte Schlüsselwörter**, z. B. `LogIn`, `Benutzer anlegen`, `Rechnung stornieren`
- **Elementare Schlüsselwörter**, z. B. `SetValue`, `Click`, `VerifyValue`

In vielen Projekten sind abstrakte Schlüsselwörter verbreitet – während elementare Schlüsselwörter selten vorkommen. Der Grund: Sie benötigen ein durchdachtes Framework, das sowohl technische als auch fachliche Aspekte trennt – was aufwendig ist, sich aber langfristig lohnt.

Diese beiden Schlüsselworttypen sind **keine Konkurrenz**, sondern **ergänzen sich perfekt**:

- Abstrakte Schlüsselwörter beschreiben **was** fachlich passiert.
- Elementare Schlüsselwörter beschreiben **wie** es an der GUI umgesetzt wird.

---

## 🔧 DRY in der Schlüsselwort-Notation umsetzen

### 🧱 1. Abstrakte Schlüsselwörter strukturieren Testfälle

Ein abstraktes Schlüsselwort ist eine **fachlich verständliche Beschreibung** eines Schritts, z. B. `Artikel in Warenkorb legen`.

Diese können in Bibliotheken zentral definiert werden und sind wiederverwendbar. Sie erleichtern die Zusammenarbeit mit Fachtestern und fördern die Lesbarkeit der Tests.

### 🧰 2. Wiederverwendbare Bibliotheken elementarer Schlüsselwörter

Elementare Schlüsselwörter wie `Click`, `SetValue`, `VerifyValue` bilden die **technische Basis** und werden in wiederverwendbaren Bibliotheken gekapselt.

Diese Kapselung ermöglicht:

- zentrale Behandlung von GUI-Eigenheiten (z. B. bei Dropdowns, Modals)
- saubere Abstraktion vom Automatisierungstool (Selenium, Cypress, etc.)
- hohe Wiederverwendung und Stabilität

> 👷‍♂️ Je öfter ein technisches Schlüsselwort wiederverwendet wird, desto robuster wird es.

### 🔄 3. Kein technischer Zwischenschritt nötig

In klassischen Projekten gibt es oft diesen Ablauf:

- Fachtester schreiben Prosatestfall
- Technische Tester übersetzen ihn in Code

Dieser **Übersetzungsschritt** ist fehleranfällig.  
Mit der Schlüsselwort-Notation entfällt er vollständig:

- Abstrakte Schlüsselwörter bilden die fachliche Sicht
- Das Framework sorgt für technische Ausführung

> 💡 Kein Zwischenschritt = keine zweite Fehlerquelle

### 📦 4. Parameterisierung für maximale Flexibilität

Schlüsselwörter können Parameter enthalten – z. B. `${Suchbegriff}` oder `${Benutzername}` – um sie in unterschiedlichen Kontexten wiederzuverwenden.

Das fördert die Wiederverwendbarkeit und reduziert die Anzahl notwendiger Schlüsselwörter.

---

## 🛠️ Tipps für abstrakte Schlüsselwörter

### 💡 1. Wähle sprechende und eindeutige Bezeichner

- **Kurz**, aber nicht kryptisch
- **Eindeutig**, ohne Interpretationsspielraum
- **Fachlich klar**, im Vokabular der Zielgruppe

> ❗ Unklare Begriffe wie „ausführen“ führen zu Verwirrung – und zu Fehlern.

### 🧱 2. Keine Verschachtelung abstrakter Schlüsselwörter

Ein guter Testfall ist wie ein Drehbuch:

- Eine Anweisung nach der anderen
- Klarer Ablauf
- Keine verschachtelten Logiken

> 👉 Komplexität gehört ins Framework, nicht in den Testfall.

---

## 🚫 Testfälle direkt in Code schreiben?

Natürlich kann man Testfälle auch direkt in Java, JS oder Python schreiben. Aber:

1. Nicht mehr lesbar für Fachtester
2. Technisch stark abhängig vom gewählten Tool
3. Änderung des Tools = kompletter Rewrite
4. Investition in Testbeschreibung ist verloren

Mit Schlüsselworten dagegen bleibt der fachliche Testfall erhalten – das Framework kapselt die Technik.

> 🛠️ DRY in Reinform: **Was du nicht brauchst, kann auch keinen Fehler verursachen.**

---

## 📌 Fazit

**Abstrakte und elementare Schlüsselwörter sind Partner, keine Gegensätze.**

- Abstrakte Schlüsselwörter: **strukturieren** die fachliche Sicht
- Elementare Schlüsselwörter: **sichern** die technische Umsetzung ab

Zusammen ermöglichen sie:

- Reduzierte Wartung durch zentrale Anpassung
- Wiederverwendbare Tests und Bausteine
- Eliminierung technischer Fehlerquellen
- Trennung von Fachlichkeit und Technik (DRY!)

---

📎 **Zum Vergleich**: [Klassischer Prozess mit zwei Übersetzungen](https://chatgpt.com/g/g-p-68765f9523dc819182113311d4335d65-gitbook-test/uebliche-vorgehensweise/README.md)

📎 **Verwandte Seite**: [Testfallbeschreibung ohne Übersetzungsschritt](https://chatgpt.com/g/g-p-68765f9523dc819182113311d4335d65-gitbook-test/dry-prinzip/keine-uebersetzung-noetig.md)