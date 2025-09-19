---
title: Kontext-Scoping – Umsetzung im Detail
description: Wie Fenster/Container als Kontext gesetzt werden und wie Kindobjekte relativ gesucht werden.
tags: ["dry", "lokatoren", "scoping", "umsetzung"]
status: Entwurf
type: technik
---

# Kontext-Scoping – Umsetzung im Detail

**Heilige Dreifaltigkeit (Orientierung):**  
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

---

## Idee

Kontext-Scoping bedeutet:  
👉 **Ein Fenster/Dialog/Container wird als Suchkontext gesetzt** – und alle Kindobjekte werden **relativ** gesucht.

Dadurch muss die Fenster-ID **nicht in jedem Kind-Locator** wiederholt werden.  
Das spart Redundanz und macht die Tests stabiler (DRY).

---

## Schritt 1 – Fenster wählen

Robot Framework Beispiel:

```robot
Select Window    customer.search
````

- Sucht das Fenster mit `data-testid="customer.search.window"`.
- Speichert dieses Element als **aktuellen Kontext**.

---

## Schritt 2 – Relativ suchen

Alle Kindobjekte werden **im Kontext des Fensters** gefunden:

```xpath
.//*[@data-testid="customer.search.field"]
.//*[@data-testid="customer.search.submit"]
```

Das führende `.` bedeutet:  
„suche **relativ** zum aktuellen Kontext“ (Fenster)  
statt im **gesamten DOM**.

---

## Schritt 3 – Umsetzung im Adapter

Python-Beispiel (Selenium-Style):

```python
ctx = None

def select_window(window_id):
    global ctx
    ctx = driver.find_element(By.CSS_SELECTOR, f'[data-testid="{window_id}"]')

def in_window_click(child_id):
    element = ctx.find_element(By.CSS_SELECTOR, f'[data-testid="{child_id}"]')
    element.click()
```

Robot-Keywords könnten dann heißen:

```robot
Select Window        customer.search
Click In Window      submit
Set Value In Window  field    Anna
```

---

## Warum ist das DRY?

- Fenster-Locator (`customer.search.window`) steht nur **einmal**.
- Kind-Lokatoren (`field`, `submit`) enthalten **keinen duplizierten Fensterteil**.
- Änderungen am Fenster → nur **eine Stelle** in der Registry anpassen.

---

## Anti-Patterns

❌ Fenster-Locator in jedem Kind duplizieren:

```xpath
//*[@data-testid="customer.search.window"]//*[@data-testid="customer.search.field"]
```

❌ Ohne Kontext global suchen:

```xpath
//*[@data-testid="customer.search.field"]
```

→ Kann bei mehreren Fenstern zum falschen Element führen.

---

## Zusammenfassung

- `Select Window` setzt den Suchkontext.
    
- `.//`-Notation sorgt für relative Suche.
    
- Adapter implementiert das Kontext-Handling.
    
- Ergebnis: **einmal Fenster, viele Kinder** → DRY bleibt gewahrt.
    
