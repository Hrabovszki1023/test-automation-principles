---
title: Modelle & MBT
description: DRY durch Zustandsmodelle – Szenarien systematisch ableiten statt Testfälle duplizieren.
tags: ["dry", "modelle", "mbt"]
status: Entwurf
type: technik
---

# Modelle & MBT

Eine weitere DRY-Methode ist der Einsatz von **Modellen** (Model-Based Testing).  
Statt jeden Testfall einzeln zu schreiben, wird das **Systemverhalten abstrakt beschrieben** – z. B. durch ein Zustandsmodell.  
Aus dem Modell lassen sich **Testfälle automatisch generieren**.

---

## Beispiel: Checkout-Zustandsmodell

> Ablage: `inhalt/assets/diagrams/dry-modelle/checkout-flow.puml`

```plantuml
@startuml
skinparam shadowing false
skinparam defaultTextAlignment left
title Checkout – Zustandsmodell (Abstrakt → Konkret via OKW)

[*] --> LoggedOut
LoggedOut --> LoggedIn : Log In(user, pass) [valid]
LoggedOut --> LoginError : Log In(user, pass) [invalid]
LoginError --> LoggedOut : Dismiss Error

state LoggedIn {
  [*] --> Browsing
  Browsing --> Cart : Add Item(itemId)
  Cart --> Browsing : Remove Item(itemId)
  Cart --> Checkout : Proceed To Checkout
}

Checkout --> Paid : Pay Order(method) [payment ok]
Checkout --> PaymentError : Pay Order(method) [payment failed]
PaymentError --> Checkout : Retry Payment
Paid --> [*]
@enduml
````

---

## Abgeleiteter Testfall (Beispiel)

```robot
*** Test Cases ***
Checkout_Success_Path
    Log In                Alice    Secret123
    Add Item To Cart      BOOK-1
    Proceed To Checkout
    Pay Order             CreditCard
    VerifyValue           OrderStatus    SUCCESS
```

---

## Vorteile

- **Redundanzarm** – Szenarien sind nicht mehrfach niedergeschrieben.
- **Systematisch** – auch „unpopuläre“ Pfade (Fehlerfälle) werden generiert.
- **Erweiterbar** – neue Zustände/Übergänge werden einmalig im Modell ergänzt.

---

## Fallstricke

- **Over-Engineering** – für einfache Systeme lohnt MBT nicht immer.
- **Generierungskomplexität** – zu viele Zustände/Übergänge → Testexplosion.
- **Pfad-Auswahl** – man muss bewusst entscheiden, welche Pfade getestet werden sollen.