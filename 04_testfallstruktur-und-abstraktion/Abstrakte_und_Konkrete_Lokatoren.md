
---

# Abstrakte und konkrete Lokatoren (Web)

**Abstrakter Lokator** = implementationsunabhängiger _Bezeichner_ für ein GUI-Objekt  
→ Beispiel: `Username`, `Password`, `Login Button`, `Terms`.

**Konkreter Lokator** = technische Beschreibung, wie das Objekt gefunden wird  
→ Beispiel: CSS/XPath/`data-test-id`, z. B. `css=[data-test-id="username"]`.

Der Testfall arbeitet **nur** mit abstrakten Namen. Die Auflösung in konkrete Lokatoren passiert zentral in einer Objektliste (z. B. YAML). Das trennt **Was** (Fachlogik) von **Wie** (Technik) und unterstützt direkt das **DRY-Prinzip**: Änderungen an der UI werden **einmalig** in der Objektliste vorgenommen – nicht in allen Testfällen.

---

## Minimalbeispiel (Robot-Style, Web)

```robot
*** Test Cases ***
Login With Valid Credentials
    Select Window    Login
    Set Value        Username           Admin_1
    Set Value        Password           Secret_1
    Click            Login Button
    Verify Text      Welcome Message    Welcome
```

- `Select Window Login` setzt den Kontext (Seite/Dialog).
    
- Aktionen (`Set Value`, `Click`, `Verify Text`) nutzen **abstrakte** Namen.
    
- Der Testfall kennt **keine** CSS/XPath – nur die YAML-Objektliste.
    

---

## Objektliste (YAML) – Abstrakt → Konkret

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
```

**Empfehlung:** Setzt explizit `data-test-id` (oder `data-testid`) in der App. Das ist stabiler und lesbarer als fragile XPath-Ausdrücke.

---

## Checkbox-Konvention (fachlich lesbar)

Checkboxen sind fachlich **2-wertig**. Für Fachtester verwenden wir **„Checked/Unchecked“** statt `true/false`.  
**Schlüsselwort-Schema:** `Select <AbstractName> <Checked|Unchecked>`

**Beispiel**

```robot
*** Test Cases ***
Accept Terms
    Select Window    Registration
    Select           Terms    Checked
    Click            Submit Button
    Verify Text      Toast Message    Registration completed
```

Passender YAML-Eintrag:

```yaml
Registration:
  Terms:
    locator: css=[data-test-id="accept-terms"]
  Submit Button:
    locator: css=[data-test-id="submit"]
  Toast Message:
    locator: css=[data-test-id="toast"]
```

---

## Weitere Web-Beispiele (Robot-Style)

**Dropdown / Select**

```robot
*** Test Cases ***
Select Country In Registration
    Select Window    Registration
    Select Option    Country Dropdown    Germany
    Verify Value     Country Dropdown    Germany
```

YAML (Auszug):

```yaml
Registration:
  Country Dropdown:
    locator: css=[data-test-id="country"]
```

**Fehlermeldung**

```robot
*** Test Cases ***
Login With Empty Password Shows Error
    Select Window    Login
    Set Value        Username           Admin_1
    Click            Login Button
    Verify Text      Error Message      Password is required
```

YAML (Auszug):

```yaml
Login:
  Error Message:
    locator: css=[data-test-id="error-message"]
```

---

## Technischer Kontrast (reine Selenium-Ebene)

Zur Einordnung: Hier würde man die **konkreten** Lokatoren direkt verwenden. In unserem Ansatz macht das die Keyword-Schicht (und liest aus YAML).

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

## Best Practices (kurz & knackig)

- **Bevorzugt:** `data-test-id` / `data-testid` (stabil, semantisch).
    
- **CSS > XPath**, wenn möglich (kürzer, schneller, lesbarer).
    
- **Keine** text-/layout-abhängigen Hacks (brittle).
    
- **Ein Objektkatalog pro Seite/Dialog** (YAML/JSON) – Single Source of Truth.
    
- **Konsistente, sprechende Namen** für abstrakte Lokatoren (z. B. „Login Button“, nicht „btn1“).
    
- **DRY strikt leben:** Testfälle ohne technische Selektoren halten.
    

---

## Glossar (Mini)

- **Abstrakter Lokator:** Fachlicher Name eines UI-Objekts (z. B. `Username`).
    
- **Konkreter Lokator:** Technischer Selektor (z. B. `css=[data-test-id="username"]`).
    
- **Objektliste:** Zentrale Zuordnung Abstrakt → Konkret (z. B. YAML).
    
- **Keyword-Schicht:** Führt Aktionen mit abstrakten Namen aus und löst zur Laufzeit konkret auf.
    

---

