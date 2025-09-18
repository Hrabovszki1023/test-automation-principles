---
title: Die Dreifaltigkeit der Lokatoren
description: "Kurz gesagt: Abstrakter Lokator (Was), Konkreter Lokator (Wie), Interaktion/Keyword-Schicht (Tut). Drei Rollen – eine Einheit."
tags: [dry, prinzipien, wartbarkeit, testautomatisierung, technikensammlung, lokatoren, abstraktion, robot-framework, objektliste]
status: Fertig
type: artikel
editors: [zoltan]
created: 2025-07-13
updated: 2025-09-18
rolle: Anwendungsbeispiel
---

## Worum es geht

Testautomatisierungswerkzeuge kennen viele Namen für dasselbe Prinzip: _Objekt-Repository_, _GUI-Map_, _Test-Frame_ … Am Ende ist es immer eine **zentrale Objektliste**, in der wir **abstrakte** und **konkrete** Lokatoren pflegen und die **Interaktionen** darauf aufsetzen.

**Ziel:** Eine Stelle der Wahrheit (Single Source of Truth) für Lokatoren → **DRY**.

{% hint style="info" %}
Details zur Web-Umsetzung inkl. Robot-Beispielen & YAML:
{% content-ref url="../abstrakte-und-konkrete-lokatoren/README.md" %}
[Abstrakte und konkrete Lokatoren (Web)](../abstrakte-und-konkrete-lokatoren/README.md)
{% endcontent-ref %}
{% endhint %}



---

## Die drei Rollen

### 1) Abstrakter Lokator – der funktionale Name

Der Ursprung und die Idee: ein sprechender Bezeichner wie `Username`, `Password`, `Login Button`.

- **Bedeutung** im Testfall, keine Technik
    
- Stabil bei UI-Änderungen
    
- Wird zur Laufzeit in „konkret“ aufgelöst
    

### 2) Konkreter Lokator – die technische Adresse

Das Abstrakte wird „greifbar“: CSS/XPath/`data-test-id` etc.

- Beispiel (Web, bevorzugt CSS & Test-IDs):
    
    - `css=[data-test-id="username"]`
    - `css=[data-test-id="password"]`
    - `css=[data-test-id="login-btn"]`
    
- Liegt **zentral** in der Objektliste (z. B. YAML)
    

### 3) Interaktion/Keyword-Schicht – die Aktion

Unsichtbar, aber spürbar: Keywords wie `Set Value`, `Click`, `Verify Text` machen den Testfall lebendig. Sie **verwenden abstrakte Namen** und fragen die konkreten Selektoren aus der Objektliste ab.

---

## „Drei – und doch eins“ (Analogie)

- **Abstrakt** weiß _was_ etwas bedeutet, aber nicht _wo_ es ist.
    
- **Konkret** kennt _wo_, aber ohne _Bedeutung_.
    
- **Interaktion** kann _handeln_, braucht aber _was_ und _wo_.
    

👉 Erst zusammen ist es eine **lebendige Einheit**.

---

## Robot-Style (englische Keywords) – Web-fokussiert

### Login – Minimalbeispiel

```robot
*** Test Cases ***
Login With Valid Credentials
    Select Window    Login
    Set Value        Username           Admin_1
    Set Value        Password           Secret_1
    Click            Login Button
    Verify Text      Welcome Message    Welcome
```

Weiterführende Beispiele & komplette YAML-Struktur:  [Abstrakte und konkrete Lokatoren (Web)](../04_testfallstruktur-und-abstraktion/Abstrakte_und_Konkrete_Lokatoren.md)

### Checkbox – als 2-Wert-Element (fachlich lesbar)

```robot
*** Test Cases ***
Accept Terms
    Select Window    Registration
    Select           Terms    Checked
    Click            Submit Button
    Verify Text      Toast Message    Registration completed
```

> Konvention: Für Checkboxes verwenden wir **`Select <Name> <Checked|Unchecked>`** (statt true/false).

### Dropdown / Select

```robot
*** Test Cases ***
Select Country In Registration
    Select Window    Registration
    Select Option    Country Dropdown    Germany
    Verify Value     Country Dropdown    Germany
```

---

## Objektliste (YAML) – Abstrakt → Konkret (Web)

```yaml
Login:
  Window:
    locator: css=[data-test-id="login-dialog"]

  Username:
    locator: css=[data-test-id="username"]

  Password:
    locator: css=[data-test-id="password"]

  Login Button:
    locator: css=[data-test-id="login-btn"]

  Welcome Message:
    locator: css=[data-test-id="welcome-message"]

Registration:
  Terms:
    locator: css=[data-test-id="accept-terms"]
  Submit Button:
    locator: css=[data-test-id="submit"]
  Toast Message:
    locator: css=[data-test-id="toast"]

  Country Dropdown:
    locator: css=[data-test-id="country"]
```

**Best Practices:**

- **Bevorzugt**: `data-test-id`/`data-testid` (stabil, semantisch)
    
- Möglichst **CSS statt XPath** (kürzer, schneller, lesbarer)
- Keine text-/layout-abhängigen Hacks
- Einheitliche, sprechende Namen in der ganzen Kette (Test, Doku, Objektliste)

**Siehe auch:**  [Abstrakte und konkrete Lokatoren (Web)](../04_testfallstruktur-und-abstraktion/Abstrakte_und_Konkrete_Lokatoren.md)

---

## Technischer Kontrast (nur zur Einordnung)

Auf der reinen Selenium-Ebene würden die konkreten Lokatoren direkt verwendet. In unserem Ansatz macht das die Keyword-Schicht (und liest aus YAML).

```java
WebElement username = driver.findElement(By.cssSelector("[data-test-id='username']"));
WebElement password = driver.findElement(By.cssSelector("[data-test-id='password']"));
WebElement loginBtn = driver.findElement(By.cssSelector("[data-test-id='login-btn']"));
WebElement welcome  = driver.findElement(By.cssSelector("[data-test-id='welcome-message']"));

username.sendKeys("Admin_1");
password.sendKeys("Secret_1");
loginBtn.click();
assertTrue(welcome.getText().contains("Welcome"));
```

---

## Diagramm (Trinitäts-Dreieck)

Zur besseren Veranschaulichung nutzen wir das klassische „Trinitätsdreieck“ – angepasst an unsere Objektlisten:

![Trinitäts-Dreieck der Objektlisten](../assets/diagrams/dry-prinzip/trinitaet_objektlisten.svg)

- **Objektliste** = das Zentrum, das alle Rollen vereint.  
- Von der Mitte zu den Ecken: **ist**  
- Zwischen den Ecken: **ist nicht**  

So wird klar: jede Rolle ist **eigenständig und darf nicht verwechselt werden**, aber sie gehören **unumstößlich zusammen**.

---

## Exkurs: Zombie-Automatisierung

Wenn nur „irgendwas klickt“, aber Abstrakt und Konkret fehlen, wirkt die Suite lebendig, **stirbt** aber innerlich: hohe Wartung, fragile Tests, Intransparenz. **Lebendig** wird es erst im Dreiklang: Abstrakt + Konkret + Interaktion.

---

## Seitenhieb: POM – das scheinheilige Modell

POM sammelt oft alles in einer Klasse: Lokatoren, Interaktionen **und** (häufig) Logik. Ergebnis: **Vermischung**, **Kopplung**, **Anti‑DRY**.

**Unser Gegenentwurf:**

- **Abstrakt** (fachliche Namen) getrennt von **Konkret** (Selektoren)
    
- **Interaktionen** als eigenständige Keyword-Schicht
    
- Zentrale Objektliste statt verteilter Seitenschnipsel
    

➡️ Ziel: _Wartbar_, _wiederverwendbar_, _transparent_.

---

## Verweise

- **Testfallstruktur und Abstarktion**: → [Abstrakte und konkrete Lokatoren (Web)](../04_testfallstruktur-und-abstraktion/Abstrakte_und_Konkrete_Lokatoren.md)
    
- **Keyword-Referenz (engl.)**: `Select Window`, `Set Value`, `Click`, `Verify Text`, `Verify Value`, `Select Option`, `Select <Checked|Unchecked>` (eigene Seite)
    

---

## Merksatz

**Abstrakt, konkret, interaktiv** – drei verschiedene Rollen. **Zusammen** bilden sie die lebendige Einheit unserer Testautomatisierung.


