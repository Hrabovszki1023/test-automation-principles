
---

## Aufwand? Kommt drauf an, _wo_ du änderst

Wenn sich an der Software etwas ändert, stellt sich immer die gleiche Frage:  
**Wie viele Stellen in den Tests muss ich jetzt anfassen?**

Im Idealfall lautet die Antwort:

> **Genau eine.** 🎯

Denn je mehr Stellen du anfassen musst, desto größer ist der Aufwand.  
Und desto wahrscheinlicher ist es, dass du irgendwo was vergisst – oder dass etwas kaputtgeht.

---

## Reduktion auf _eine Stelle_ ist möglich!

Auch wenn’s paradox klingt:  
Ja, **jeder Testfall ist ein Einzelfall**.  
Und ja, man muss jeden Test irgendwie spezifizieren.

Aber:  
Wenn du bestimmte Prinzipien und Techniken (wie z. B. **Abstraktion**, **Vererbung**, **Parametrisierung** oder das **DRY-Prinzip**) richtig einsetzt,  
dann ist eine saubere Reduktion auf **eine Änderungsstelle pro Aspekt** möglich.

Konkret heißt das:

- Eine Änderung am UI? → Nur den Lokator ändern – nicht jeden Test.
- Eine neue Berechnung? → Nur die Prüflogik anpassen.
- Ein anderer Testdatenwert? → In der zentralen Testdatenquelle ändern.

Das ist keine Utopie – es ist machbar.  
Man muss es nur **von Anfang an konsequent durchziehen**.

---

## Ohne Struktur wird’s wild

Ein häufiger Aufwandstreiber ist auch das Testumfeld selbst.  
Wenn dort Wildwuchs herrscht – unklare Strukturen, schlecht benannte Objekte, fehlende Synchronisation –  
dann brauchst du für jede kleine Änderung gleich ein Großreinemachen.

Daher lohnt es sich, auch bei „Nebensächlichkeiten“ wie

- guter **Benennung** (von Klassen, Methoden, Schritten), 
- klarer **Skriptstruktur**
- und durchdachter **Synchronisation** der Testumgebung

auf **Lesbarkeit und Nachvollziehbarkeit** zu achten.  
Denn Tests müssen nicht nur laufen – sie müssen **verständlich wartbar** sein.

---

### Fazit

Die Frage ist also nicht _ob_ du Aufwand hast –  
sondern **ob du ihn jedes Mal neu hast oder nur ein einziges Mal**.

Und genau hier liegt der Schlüssel zur effizienten Testautomatisierung.

---

## ✅ Vorschlag zum weiteren Vorgehen

- **Dateiname:** `01_einleitung/Grundsätzliche Überlegungen zur Aufwandsreduzierung.md`
    
- **Titel in GitBook-Menu:** "Aufwand verstehen"
    
- **Interner Link von der Einleitung:**  
    Am Ende der Einleitung ein Satz wie:
    
    > 🔍 _Mehr zur Frage, woher der Aufwand eigentlich kommt: [Aufwand verstehen](https://chatgpt.com/c/Grunds%C3%A4tzliche%20%C3%9Cberlegungen%20zur%20Aufwandsreduzierung.md)_
    

---

Möchtest du den Text so übernehmen und pushbereit machen?  
Oder sollen wir noch etwas ergänzen (z. B. ein kurzes Beispiel oder Schema)?