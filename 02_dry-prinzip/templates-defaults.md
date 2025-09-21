---
title: Templates & Defaults
description: DRY mit Vorlagen und Standardwerten – Unterschiede überschreiben statt duplizieren.
tags: ["dry", "templates", "testdaten"]
status: Entwurf
type: technik
---

# Templates & Defaults

Eine elegante DRY-Methode ist die Arbeit mit **Vorlagen (Templates)**.  
Anstatt komplette Testdatenstrukturen mehrfach zu kopieren, werden **Defaultwerte** zentral definiert.  
Im Testfall werden nur die abweichenden Werte überschrieben – das hält Daten **kurz, konsistent und wartbar**.

---

## Beispiel: YAML-Testdaten mit Overrides

```yaml
# Defaultwerte für einen Standardnutzer
DefaultUser: &DefaultUser
  role: "customer"
  active: true
  country: "DE"
  password: "Secret123"

# Abgeleitete Varianten überschreiben nur Unterschiede
AdminUser:
  <<: *DefaultUser
  role: "admin"

InactiveUser:
  <<: *DefaultUser
  active: false
````

---

## Umsetzung in Robot Framework (OKW-Notation)

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

---

## Best Practices

- **Flach halten** – zu viele Ebenen von Overrides machen Daten intransparent.
- **Sichtbare Unterschiede** – im Testfall sollten nur die relevanten Änderungen stehen.
- **Namen sprechend wählen** – `AdminUser`, `InactiveUser` statt kryptischer Kürzel.
- **Zentraler Ablageort** – Templates gehören ins Repository, nicht in einzelne Tests gestreut.

---

## Fallstricke

- **Versteckte Abhängigkeiten**: Änderungen im Template wirken auf alle abgeleiteten Daten.   
- **Komplexität**: Bei zu starker Vererbung wird Debugging schwierig („woher kommt dieser Wert?“).

---
