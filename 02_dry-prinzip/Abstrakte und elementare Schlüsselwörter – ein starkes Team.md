---
title: Abstrakte und elementare Schlüsselwörter – ein starkes Team
beschreibung: Wie sich abstrakte und elementare Schlüsselwörter in der Testautomatisierung ergänzen – und warum sie gemeinsam DRY ermöglichen.
tags:
  - schlüsselwörter
  - abstraction
  - dry
  - wiederverwendung
status: in Bearbeitung
type: artikel
sidebar_position: 3
editors:
  - zoltan
created: 2025-08-12
updated: 2025-08-12
rolle: Technik-Erläuterung
kapitel: DRY-Prinzip
---

# Abstrakte und elementare Schlüsselwörter – ein starkes Team

In der Theorie vieler Keyword-basierter Frameworks unterscheidet man zwei Typen von Schlüsselwörtern:

- **Abstrakte Schlüsselwörter**, z. B. `LogIn`, `Benutzer anlegen`, `Rechnung stornieren`
- **Elementare Schlüsselwörter**, z. B. `SetValue`, `Click`, `VerifyValue`

In der Praxis sind abstrakte Schlüsselwörter weit verbreitet – während **elementare Schlüsselwörter deutlich seltener zu finden sind**. Denn deren Einsatz erfordert ein **robustes und gut durchdachtes Framework**, das **technisch aufwendig** umzusetzen ist – und das viele Projekte nicht leisten können oder wollen.

Dabei gilt: Diese beiden Typen sind **keine Konkurrenz**, sondern **Ergänzungen** – sie erfüllen unterschiedliche Aufgaben:

- Abstrakte Schlüsselwörter beschreiben *was* auf fachlicher Ebene passiert.
- Elementare Schlüsselwörter beschreiben *wie* es konkret an der GUI passiert.

Abstrakte Schlüsselwörter helfen, die Testfallbeschreibung grob zu strukturieren (z. B. auf Basis von User Stories oder Akzeptanzkriterien).  
Elementare Schlüsselwörter werden in der **Konkretisierung** verwendet – also in der detaillierten Umsetzung.

---

## Testfälle direkt in Skriptcode? Lieber nicht …

Natürlich kann man auch direkt in Selenium, Cypress oder Playwright einen Testfall implementieren – ganz ohne abstrahierte Schlüsselwörter.  
Aber das hat einige Nachteile:

1. Die Testfälle sind **nicht mehr für Fachtester lesbar** – was die Zusammenarbeit erschwert.  
2. Die Testfälle sind **technisch abhängig vom Automatisierungswerkzeug**.  
   Wenn das Tool gewechselt wird, müssen **alle Testfälle neu geschrieben** werden.  
3. **Die eigentliche Investition** steckt in der Testfallbeschreibung. Diese soll möglichst unabhängig von der technischen Umsetzung sein.

Ein gutes Schlüsselwortframework kapselt die Technik –  
und schützt damit die fachliche Testbeschreibung vor technischen Veränderungen.

> 🔄 In der Praxis wurden bereits Frameworks umgebaut, bei denen:  
> – Selenium durch Cypress ersetzt wurde  
> – eine komplette GUI von Swing auf Web migriert wurde  
>
> In beiden Fällen konnten die bestehenden Testfälle **weiterverwendet** werden – weil nur das Framework angepasst wurde.

---

## Warum elementare Schlüsselwörter so wertvoll sind

### 1. **Stabilität durch Wiederverwendung**

Elementare Schlüsselwörter werden **einmalig** implementiert und dann **immer wieder verwendet**.  
Dadurch entsteht über die Zeit ein **stabiles, erprobtes Framework**.

> 👷‍♂️ Je mehr du wiederverwendest, desto weniger neue Fehler entstehen.

Bei handgeschriebenem Testcode dagegen wird jede neue Testfallzeile zur potenziellen Fehlerquelle.

---

### 2. **Zentrale Behandlung von GUI-Eigenheiten**

Jedes Projekt hat eigene UI-Spezialitäten – kreative Dropdowns, merkwürdige Modal-Dialoge oder nicht standardkonformes Verhalten.

Ein zentral implementiertes `Select()`-Schlüsselwort für eine Combobox, kann diese Eigenheiten **projektweit kapseln**.  
Ändert sich das Verhalten einer Komponente, wird **nur eine Stelle angepasst**.

Das spart Zeit – und verhindert Fehler, die sonst überall korrigiert werden müssten.

---

### 3. **Testfälle bleiben clean**

Durch die Kapselung technischer Details bleiben die Testfälle **kurz, lesbar und wartbar**.  
Sie beschreiben nur noch die fachliche Logik – der Rest liegt im Framework.

> 🧼 Weniger technischer Lärm – mehr fachliche Klarheit.

---
## 🛠️ Tipps für abstrakte Schlüsselwörter

Abstrakte Schlüsselwörter haben große Vorteile – aber nur, **wenn sie klar benannt und sinnvoll strukturiert sind**.

### 💡 1. Wähle sprechende und eindeutige Bezeichner

Ein abstraktes Schlüsselwort wie `Benutzer anlegen` oder `Artikel stornieren` muss auf den ersten Blick verständlich machen, **was genau geschieht**.

- **Kurz:** keine Romane – aber auch nicht kryptisch.
    
- **Eindeutig:** es darf kein Ratespiel sein, was „ausführen“ oder „weiterverarbeiten“ bedeutet.
    
- **Fachlich klar:** am besten im Vokabular des Anwenders oder der Domäne bleiben.
    

> ❗ Unklare oder zu generische Namen führen schnell zu Verwirrung – und machen das Debuggen zur Hölle.

---

### 🧱 2. Keine Verschachtelung abstrakter Schlüsselwörter

Was verlockend klingt („Ich rufe im Schlüsselwort A das Schlüsselwort B auf…“)  
führt schnell zu unlesbaren Monstern mit schwer nachvollziehbarem Ablauf.

**Ein guter Testfall ist wie ein Drehbuch:**

- Eine Anweisung nach der anderen
    
- Klarer Ablauf
    
- Ohne versteckte Unterkapitel
    

> 👉 Verschachtelung ist Aufgabe des Frameworks – **nicht des Testfalls**.

Wenn komplexe Abläufe nötig sind, lieber mehrere klar benannte Schritte verwenden als alles in ein Mega-Konstrukt zu packen.

---

### 📌 Fazit

Abstrakte Schlüsselwörter sind ein mächtiges Werkzeug – **aber nur so gut wie ihre Benennung**.  
Klare, eindeutige Begriffe machen den Test lesbar, wartbar – und vertrauenswürdig.

---
## Fazit

Abstrakte und elementare Schlüsselwörter sind zwei Seiten derselben Medaille:

- Die **einen strukturieren die fachliche Sicht**,  
- die **anderen sichern die technische Umsetzung ab**.

Gemeinsam ermöglichen sie ein **robustes, wartbares und wiederverwendbares** Testdesign – ganz im Sinne des DRY-Prinzips.

Und das Beste: Wenn sich etwas ändert, musst du es **nur an einer Stelle** anpassen.


---
## 🔗 Vermeidung technischer Fehlerquellen

Ein großer Vorteil der Schlüsselwort-Notation ist, dass **kein technischer Übersetzungsschritt** nötig ist.  
Damit entfällt eine häufige Fehlerquelle in klassischen Automatisierungsprozessen.

📎 Siehe auch: [[Wie Schlüsselwörter die Brücke zwischen Fachtest und Automatisierung schlagen]]

> 🛠️ DRY in Reinform:  
> Was du **nicht brauchst**, kann auch **keinen Fehler verursachen**.

---
### 🧭 Zum Vergleich: Der klassische Prozess mit zwei Übersetzungen

Zur Erinnerung – so sieht die herkömmliche Vorgehensweise aus:

📎 [[Übliche Vorgehensweise um Testfälle zu automatisieren#Zwei Übersetzungen = doppelte Fehlerquelle]]
