---
title: Kontext & Scoping
description: Fenster, Dialoge und Bereiche als Kontext nutzen – statt globale Wild-XPaths.
tags: ["dry", "lokatoren", "scoping", "fenster"]
status: Entwurf
type: artikel
---

# Kontext & Scoping

**Heilige Dreifaltigkeit (Orientierung):**  
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

---

## Motivation

Ein häufiger Fehler in Tests ist die Suche „im ganzen DOM“ – mit globalen XPaths wie:

```xpath
//*[@data-testid="customer.search.field"]
````

Das ist fragil und widerspricht DRY:

- **Wiederholung**: In jedem Child-Locator steckt wieder die Fenster-/Bereichs-ID.
    
- **Fehleranfällig**: Schon kleine Layout-Änderungen können globale Suchen brechen.
    
- **Unlesbar**: lange Ketten wie `//*[@id='root']/div[2]/div[3]/button[2]`.
    

---

## Prinzip: Kontext wählen

Stattdessen wird die Anwendung in **Fenster, Dialoge oder Container** gegliedert:

1. **Kontext setzen**:
    
    ```robot
    Select Window    customer.search
    ```
    
2. **Kindobjekte relativ suchen**:
    
    ```xpath
    .//*[@data-testid="customer.search.field"]
    .//*[@data-testid="customer.search.submit"]
    ```
    

Relativ zum Fenster-Kontext werden nur noch die Kinder angesprochen – **ohne den Fensterteil in jedem Locator zu wiederholen**.

---

## DRY im Generator

Die Fenster-ID wird **einmal** gepflegt.  
Der Generator baut daraus automatisch die Kind-Lokatoren:

```yaml
# locator-ids.yaml (abstrakt)
- id: customer.search.window
- id: customer.search.field
- id: customer.search.submit
```

Ergebnis:

```yaml
# locators/web/generated.yaml
customer.search.field:  '[data-testid="customer.search.window"] [data-testid="customer.search.field"]'
customer.search.submit: '[data-testid="customer.search.window"] [data-testid="customer.search.submit"]'
```

---

## Vorteile

- **Single Source of Truth**: Fenster-ID steht nur einmal in der Registry.
    
- **Kein Copy-Paste**: Kind-Lokatoren müssen nicht den ganzen Fensterpfad wiederholen.
    
- **Robustheit**: Fenster/Kind-Beziehungen bleiben stabil, auch wenn das Layout sich ändert.
    
- **Lesbarkeit**: Tests zeigen nur noch die abstrakten Bezeichner.
    

---

## Mini-Checkliste fürs Scoping

-  Hat jedes Fenster/Dialog eine eigene Test-ID?
    
-  Werden Kindobjekte **relativ** gesucht (nicht global)?
    
-  Fenster-IDs stehen nur **einmal** in der Registry?
    
-  Mehrfachinstanzen (z. B. Tabellenzeilen) haben stabile Schlüssel (`{invoiceId}`)?
    
-  iFrames/Browser-Tabs werden explizit gescoped?
    

---

## Anti-Patterns (bitte vermeiden)

❌ Global suchen:

```xpath
//*[@data-testid="window"]//*[@data-testid="child"]
```

❌ Layout-abhängig suchen:

```xpath
//div[3]//button[2]
```

❌ Fenster-IDs in jedem Kind duplizieren:

```yaml
search.field: '//*[@data-testid="customer.search.window"]//*[@data-testid="customer.search.field"]'
```

---

## Zusammenfassung

Kontext-Scoping bedeutet:  
👉 **Fenster einmal selektieren, Kinder nur noch relativ suchen.**

Damit wird das **Fenster zur Klammer**, die alles zusammenhält –  
und das DRY-Prinzip bleibt gewahrt.
