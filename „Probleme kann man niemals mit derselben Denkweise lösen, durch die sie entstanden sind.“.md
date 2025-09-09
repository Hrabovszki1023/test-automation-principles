
---

## 1. Einordnung des Einstein-Zitats

Der Satz

> „Probleme kann man niemals mit derselben Denkweise lösen, durch die sie entstanden sind.“

wird Albert Einstein zugeschrieben (oft ohne Primärquelle). Unabhängig von der Urheberschaft steht er für einen **Paradigmenwechsel im Denken**:

- Probleme sind Produkte eines bestimmten Denkschemas (Ebene A).
- Um sie zu lösen, braucht es ein neues, übergeordnetes Schema (Ebene B).  
    Das ist nichts anderes als ein **Meta-Ebenen-Wechsel** – ein Konzept, das auch in der Erkenntnistheorie und Systemtheorie vorkommt.

---

## 2. Wissenschaftlicher Kontext: Meta-Ebenen in der Problemlösung

### a) Konstruktivismus / Erkenntnistheorie

- Erkenntnis entsteht nicht aus „Dingen an sich“, sondern aus **Modellen, die wir uns bilden**.
- Wenn ein Modell nicht mehr ausreicht, brauchen wir eine **Meta-Reflexion** und ein neues Modell.  
    Beispiel: Newtons Mechanik erklärt die klassische Physik → aber nicht die Relativität → Einsteins Theorie ist eine neue Meta-Ebene.
   

### b) Systemtheorie (Luhmann, Bateson)

- Probleme in einem System lassen sich selten im System selbst lösen (Batesons „second-order learning“).
- Notwendig ist ein Wechsel in ein **höheres Ordnungssystem**, das die Regeln des darunterliegenden Systems neu bestimmt.

### c) Abstraktion in der Informatik

- Informatik lebt von **Abstraktionsebenen** (Maschinencode → Assemblersprache → Hochsprache → Framework → Domain-Specific Language).
- Jede neue Ebene abstrahiert vom „Rauschen“ der darunterliegenden Ebene und löst die dort unlösbaren Probleme.

---

## 3. Übertragung auf Testautomatisierung

### a) Konkrete Ebene (symptomorientiert)

- Testskripte enthalten direkt **konkrete Implementierungsdetails** (XPath, IDs, CSS-Selektoren).
- Fehler entstehen, wenn die GUI sich ändert.
- Lösungsversuche innerhalb dieser Ebene: Auto-Healing, reguläre Expressions, Retry-Mechanismen.  
    👉 Sie bekämpfen Symptome, nicht Ursachen.

### b) Abstrakte Ebene (Meta-Ebene)

- Einführung einer **Abstraktionsschicht**: Fachliche Namen („LoginButton“), Schlüsselwörter, YAML-Objektlisten.
- Diese Ebene formuliert **Testlogik unabhängig von der Implementierung**.
- Änderungen in der GUI schlagen nicht mehr direkt durch → DRY bleibt gewahrt, Wartbarkeit steigt.

### c) Wissenschaftlicher Schluss

Das DRY-Prinzip wird auf der abstrakten Ebene **konsistent erzwingbar**, auf der konkreten Ebene bleibt es ein Flickwerk.  
→ Genau das entspricht Einsteins Forderung nach einem **Wechsel des Denkrahmens**.

---

## 4. Verknüpfung von Einstein zu „Konkret vs. Abstrakt“

|Dimension|Ebene 1 – Konkret|Ebene 2 – Abstrakt (Meta)|
|---|---|---|
|**Einstein**|Denken, das Problem erzeugt|Neues Denkmodell|
|**Systemtheorie**|1. Ordnung (Regeln befolgen)|2. Ordnung (Regeln ändern)|
|**Informatik**|Locator: `//div[3]/button[2]`|Objektname: `LoginButton`|
|**Testdesign**|Skript mit Klicks und Eingaben|Schlüsselworttest „Log in as Customer“|
|**DRY-Prinzip**|Wiederholte Fragmente|Einmalige Definition, mehrfacher Gebrauch|

---

## 5. Fazit (wissenschaftlich formuliert)

- Ein Problem (hier: **instabile, redundante Testautomatisierung**) entsteht durch das Arbeiten auf einer bestimmten **konkreten Ebene** (z. B. direkte Nutzung technischer Lokatoren).
- Nach Einstein und den Theorien der Systemwissenschaften ist eine **nachhaltige Lösung nur durch einen Meta-Ebenen-Wechsel möglich**.
- Dieser Wechsel entspricht in der Testautomatisierung der **Einführung von Abstraktionsschichten** (Keywords, funktionale Objektlisten, treiberunabhängige Adapter).
- Damit wird das DRY-Prinzip systematisch durchgesetzt und nicht länger von den Zufälligkeiten der GUI-Technik bedroht.

---
