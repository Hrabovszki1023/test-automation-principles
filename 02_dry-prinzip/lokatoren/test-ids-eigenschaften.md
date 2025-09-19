---
title: Eigenschaften guter Test-IDs
description: Ausführliche Richtlinien für stabile, sprechende und DRY-konforme Test-IDs.
tags: ["dry", "lokatoren", "test-id", "richtlinien"]
status: Entwurf
type: artikel
---

# Eigenschaften guter Test-IDs

**Heilige Dreifaltigkeit (Orientierung):**  
👤 Abstrakter Bezeichner · ✨ **Konkreter Lokator (Fleischwerdung)** · 🛠️ Widget/Adapter (Interaktion)

Test-IDs (z. B. `data-testid`, `automation-id`, Swing-`setName`) sind das **Rückgrat der Automatisierung**.  
Hier sammeln wir die ausführlichen Kriterien, die eine gute Test-ID erfüllen sollte.

---

## 1. Eindeutigkeit & Stabilität
- **Global eindeutig**: jede ID existiert applikationsweit nur einmal.  
- **Stabil über Releases**: einmal vergeben ⇒ bleibt erhalten.  
- **Deterministisch**: ableitbar aus Domäne/Kontext, nicht aus Layout.  
- **Nicht Layout-basiert**: keine CSS-Klassen, keine Indexe, keine Reihenfolgen.

---

## 2. Sprechend & domänennah
- **Fachlich** statt technisch: `customer.search.submit` statt `btn123`.  
- **Sinnvolle Granularität**: nicht zu generisch (`button1`), nicht zu detailreich (`searchButtonGreenRightTop`).  
- **Keine UI-Technik im Namen**: „Button“, „Div“, „Xpath“ bleiben in den Adaptern.

---

## 3. Namensschema & Konventionen
- **Namespaces**: `<domäne>.<kontext>.<funktion>[.<variante>]`.  
  - Beispiel: `customer.search.submit`, `invoice.row.{invoiceId}.amount`.  
- **Zeichenmenge**: `[a-z0-9_.-]`.  
- **Kleinschreibung** und **Punkt-Notation** für Lesbarkeit.  
- **Keine Umlaute**, keine Leerzeichen, keine Sonderzeichen.  
- **Länge**: kurz genug zum Tippen, lang genug zur Eindeutigkeit (≈ 20–60 Zeichen).  
- **Mehrfachinstanzen**: mit stabilem Schlüssel statt Index (`{invoiceId}` statt `row[3]`).

---

## 4. Lebenszyklus & Governance
- **Zentrale Registry**: alle IDs in einer Datei (`locator-ids.yaml`).  
- **Review-Prozess**: Änderungen nur via Pull-Request + Review (Dev + QA).  
- **Deprecation-Policy**: alte IDs min. 1 Release als Alias belassen, dann entfernen.  
- **Versionierung**: Registry im Git, Änderungen sind nachvollziehbar.

---

## 5. Technische Anforderungen
- **Maschinenlesbar**: simpler String, keine Logik.  
- **Performant**: Zugriff in O(1), kein DOM-Wildwuchs.  
- **Unsichtbar für Endnutzer**: IDs tauchen nicht in der UI auf.  
- **a11y-neutral**: darf Accessibility nicht stören; nicht verwechseln mit `aria-*`.

---

## 6. Sicherheit & Datenschutz
- **Keine PII**: keine Namen, IBANs, Vorgangsnummern etc.  
- **IDs ≠ Geschäftslogik**: dürfen keine Autorisierungs- oder Geschäftsentscheidungen triggern.  
- **Logging**: IDs sollen unkritisch geloggt werden können.

---

## 7. Internationalisierung
- **Sprachneutral**: IDs bleiben gleich, egal ob die UI deutsch, englisch oder japanisch ist.  
- **Keine Übersetzungen** in IDs.  
- **Einheitlich englisch/neutral** als Standard.

---

## 8. Plattform-Übertragbarkeit
- **Eine Quelle, viele Targets**: abstrakte ID (`customer.search.submit`) wird in Web, Swing oder Mobile konkretisiert.  
- **Generator** baut pro Plattform die passenden Locator-Ausdrücke.  

Beispiel:
```yaml
# locator-ids.yaml
- id: customer.search.submit
  intent: "Suche auslösen"
````

Web:

```css
[data-testid="customer.search.submit"]
```

Swing:

```java
component.setName("customer.search.submit");
```

---

## 9. Kompatibilität & Migration

- **Aliases** für Umbenennungen:
    
    ```yaml
    current: customer.search.submit
    aliases: [ customer.search.searchSubmit ]
    ```
    
- **CI-Check** warnt bei Alias-Nutzung → sanfte Migration.
    

---

## 10. Tooling & Qualitätssicherung

- **Linting**: prüft Namensschema, verbietet Duplikate, scannt nach PII.
    
- **Doc-Gen**: Registry automatisch als HTML/MD-Doku exportieren.
    
- **Coverage-Report**: ungenutzte IDs finden.
    
- **„Red Button“-Check**: jeder interaktionsrelevante Control muss eine ID haben.  
    → Build bricht, wenn IDs fehlen.
    

---

## 11. Anti-Patterns (bitte vermeiden)

❌ IDs aus Layout ableiten:

```xpath
page > div:nth-child(3) .btn.blue
```

❌ Indexbasierte IDs:

```xpath
list.item[0].title
```

❌ Fachdaten als ID:

```
customer.anna.mueller.submit
```

❌ Technik-Bezeichner:

```
btnSubmit, div-123
```

❌ Sprachabhängige IDs:

```
kunde.suche.absenden
```

---

## Zusammenfassung

Eine gute Test-ID ist **eindeutig, stabil, sprechend, neutral, zentral gepflegt und generierbar**.  
Sie ist das **Verbindungsstück** zwischen abstraktem Bezeichner (Vater) und Interaktion (Heiliger Geist) – die **Fleischwerdung** der Automatisierung. ✨
