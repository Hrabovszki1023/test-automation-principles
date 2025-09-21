---
title: Warum DRY für Testautomatisierung so entscheidend ist
sidebar_position: 2
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
editors:
  - zoltan
created: 2025-09-09
updated: 2025-09-09
---

## Warum DRY für Testautomatisierung so entscheidend ist

Das DRY-Prinzip („Don't Repeat Yourself“) ist einer der **zentralen Hebel**, um den **Wartungsaufwand** in der Testautomatisierung dauerhaft zu reduzieren.

Denn jedes redundante Element – egal ob Testcode, Testdaten, Konfiguration oder Lokatoren – ist eine **potenzielle Fehlerquelle**, die gepflegt werden muss.  
Und jede unnötige Wiederholung erhöht den Aufwand **exponentiell mit jedem neuen Testfall**.

---

## Was bedeutet DRY konkret in der Testautomatisierung?

> [!TIP] Weckruf  
> In den aktuellen ISTQB-Lehrplänen zur Testautomatisierung (Stand September 2025) taucht das **DRY-Prinzip kein einziges Mal** auf.  
> Dabei ist gerade „Don’t Repeat Yourself“ eine der entscheidenden Grundlagen für wartbare Testautomatisierung.  
> 👉 Hier setzen wir an: DRY gehört ins Pflichtprogramm.

Das DRY-Prinzip („Don’t Repeat Yourself“) besagt, dass **jede Information nur einmal im System vorkommen sollte**.  
In der Testautomatisierung zeigen sich dafür vier **Grundmethoden**, die je nach **Ebene** (Testfall-übergreifend, Testfall, Testtreiber) eingesetzt werden.
Wenn dir dabei etwas fehlt oder du eine weitere Methode siehst – nur her damit!


---

### Grundmethoden von DRY

|DRY-Methode|Umsetzung / Beispiele|Ebene|
|---|---|---|
|**1) Abstrakt ↔ Konkret (Mapping)**|Abstrakte Lokatoren → Test-IDs/XPath, Abstrakte Keywords → Elementare Keywords, Abstrakte Daten → konkrete Werte|**Testtreiber** (Lokatoren/Widgets) · **Testfall** (Keywords/Daten)|
|**2) Funktionen / Kapselung**|Zentrale Keywords/Helper, parametrische Assertions, gemeinsames Setup/Teardown|**Testfall** (Keywords/Helper) · **Testfall-übergreifend** (Libraries)|
|**3) Vererbung / Templates & Defaults**|Testdaten-Templates mit Override, Konfigurationsvererbung, Widget-Vererbung|**Testfall** (Testdaten/Config) · **Testtreiber** (Widgets)|
|**4) Modelle**|Zustandsmodelle, MBT-Übergangsgraphen, Entscheidungsbäume|**Testfall-übergreifend** (Szenarien/Generierung)|

> **Hinweis:** Die Methode **„Modelle“** wird hier nur genannt. Die ausführliche Erklärung inkl. Zustandsdiagramm und Generierung landet auf der Seite: `02_dry-prinzip/modelle-mbt.md`.

---
> [!NOTE] Kombination der Methoden  
> In der Praxis treten die DRY-Methoden **selten isoliert** auf – sie ergänzen sich gegenseitig.  
> 
> **Beispiele:**  
> - **Heilige Dreifaltigkeit (Lokator ↔ Widget ↔ Aktion):**  
>   - Die **Objektliste** setzt *Abstrakt/Konkret* um (funktionaler Name → technischer Locator).  
>   - Die **Widget-Klasse** kapselt Aktionen in *Funktionen*.  
>   - Die Widget-Klasse kann durch *Vererbung* erweitert werden (`BaseWidget` → `Button` → `CustomButton`).  
> - **Templates & Mapping:**  
>   - Testdaten-Templates (*Vererbung*) enthalten abstrakte Werte (`<defaultRole>`).  
>   - Diese werden beim Ausführen durch konkrete Daten ersetzt (*Abstrakt/Konkret*).  
> - **Modelle & Funktionen:**  
>   - Ein Zustandsmodell (*Modell*) erzeugt abstrakte Übergänge.  
>   - Jeder Übergang ruft wiederum *zentrale Keywords* (Funktionen) auf.  
> 
> 👉 Das ist auch der Grund, warum die Grundmethoden nicht immer sofort erkennbar sind:  
> Sie bilden **Bausteine**, die sich in der Architektur ineinander verschränken.  

---
#### 1) Abstrakt ↔ Konkret (Mapping)

Trenne fachliche Begriffe von technischen Details.  
Abstrakte Namen (z. B. `UserNameField`, `Log In`) werden zur Laufzeit in **konkrete Lokatoren** und **elementare Aktionen** aufgelöst. Deine Tests bleiben stabil, auch wenn sich die Oberfläche ändert.

**Robot-Beispiel (OKW-Notation):**

```robot
*** Test Cases ***
Login With Valid User
    Log In    Alice    Secret123

*** Keywords ***
Log In
    [Arguments]    ${User}    ${Password}
    SetValue    UserNameField    ${User}
    SetValue    PasswordField    ${Password}
    Click       LoginButton
```

---

#### 2) Funktionen / Kapselung

Kapsle wiederkehrende Abläufe in **ein zentrales Keyword** oder eine Helper-Funktion.  
Einmal definiert, überall genutzt – statt Copy&Paste in zig Testfällen.

**Robot-Beispiel (OKW-Notation):**

```robot
*** Test Cases ***
Reset System And Login
    Reset Database
    Log In    Alice    Secret123

*** Keywords ***
Reset Database
    Call API           /reset-database
    VerifyValue        ApiStatus    OK
```

---

#### 3) Vererbung / Templates & Defaults

Halte **gemeinsame Defaults** in Templates und überschreibe im Testfall nur die Unterschiede.  
So bleiben Testdaten kurz, konsistent und zentral wartbar.

**Robot-Beispiel (OKW-Notation):**

```robot
*** Variables ***
&{DefaultUser}     role=customer    active=true    password=Secret123
&{AdminUser}       &{DefaultUser}   role=admin
&{InactiveUser}    &{DefaultUser}   active=false

*** Test Cases ***
Login As Admin
    Log In    Alice    ${AdminUser}[password]

Login As Inactive
    Log In    Bob      ${InactiveUser}[password]
```

> Für die tiefergehende Variante (YAML-Templates mit Merging/Overrides) siehe die Detailseite: `02_dry-prinzip/templates-defaults.md`.

---

#### 4) Modelle (Referenz)

Mit **Zustandsmodellen / MBT** beschreibst du Zustände und Übergänge einmal zentral und **generierst** daraus systematische Testpfade (inkl. Positiv/Negativ-Varianten).  
Details, inkl. PlantUML-Diagramm und Beispiel-Generierung: `02_dry-prinzip/modelle-mbt.md`.

---

### Beispiele für DRY in der Praxis

|Bereich|DRY-Anwendung|
|---|---|
|**Testskripte**|Gemeinsame Schritte in zentrale Schlüsselwörter oder Bibliotheken auslagern|
|**Testdaten**|Zentrale Definition in YAML/CSV/JSON statt hartcodiert im Test|
|**Element-Lokatoren**|Zentrale Objektlisten statt XPath in jedem Skript|
|**Konfiguration**|Eine zentrale Stelle für Timeouts, URLs, Benutzerkonten etc.|
|**Protokollierung**|Gemeinsames Logging-Framework für alle Tests|
|**Testframework**|GUI-Adapter, Assertions, Fehlerbehandlung als wiederverwendbare Module|
|**Testumgebungsaufbau**|SetUp-/TearDown-Logik zentralisiert statt in jedem Testfall dupliziert|
|**Templates & Änderungswerte**|Standard-Defaults definieren, nur Unterschiede testfallspezifisch überschreiben|

---
> [!NOTE] Augenzwinkern zum Schluss  
> Falls du im nächsten ISTQB-Lehrplan nach **DRY** suchst – spar dir die Mühe, du findest es dort nicht.  
> Einige der Methoden (z. B. Wiederverwendung, Parametrisierung) tauchen zwar auf,  
> aber das Prinzip selbst wird mit keinem Wort genannt.  
> Vielleicht schaffen wir’s ja, dass es in der nächsten Version endlich drinsteht 😉

---

## Was passiert, wenn DRY ignoriert wird?

Wenn jede Automatisierung „für sich“ gebaut wird:

- entstehen hunderte Kopien derselben Logik,
- müssen Anpassungen mehrfach erfolgen – oft **nicht überall vollständig**,
- schleichen sich Inkonsistenzen, Inkapselungsfehler und „vergessene Stellen“ ein,
- wird die Wartung zur täglichen Qual.

---

## DRY als Erfolgsfaktor für nachhaltige Automatisierung

Ein gutes DRY-konformes Design sorgt dafür, dass du Änderungen **nur an einer Stelle** machen musst:

> **Ein geänderter Button-Name?**  
> → Nur den zentralen Lokator ändern – alle Tests profitieren.

> **Ein neues Format für Testdaten?**  
> → Parser anpassen – alle Tests nutzen die Änderung automatisch.

> **Ein neuer Login-Prozess?**  
> → `Login`-Schlüsselwort anpassen – keine einzige Testfallzeile muss geändert werden.

---

## DRY geht über Code hinaus

Das DRY-Prinzip lässt sich auf **alle Ebenen der Automatisierung** anwenden:

- **Technik:** Wiederverwendbare Schlüsselwörter, Adapter, Logging, Fehlerbehandlung
- **Fachlichkeit:** Abstrakte Schlüsselwörter, zentral gepflegte Testbeschreibungen
- **Testdaten:** Parametrisierte Testdatenquellen, generische Konfigurationen
- **Umgebung:** Zentraler Aufbau von Testsystemen, zentrale Konfigurationsprofile
- **Wartung:** Gemeinsame Standards, Skriptstrukturen, Synchronisationsstrategien

---

## 📎 Siehe auch

- 🔗 [Die Dreifaltigkeit der Lokatoren](./07_die_Dreifaltigkeit_der_Lokatoren.md)
- 🔗 [Abstrakte und elementare Schlüsselwörter](02_Abstrakte_und_elementare_Schluesselwoerter.md)

---

## Fazit

Das DRY-Prinzip ist **keine theoretische Schönwetterregel** –  
sondern die **praktische Voraussetzung**, um Testautomatisierung **überhaupt wartbar** zu halten.

Je komplexer das System, desto mehr zahlt sich DRY aus:  
**Jede eingesparte Redundanz ist ein Stück Skalierbarkeit.**

