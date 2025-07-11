## Einleitung
Bestehende Software zu testen _muss_ schnell vorgenommen werden können. Der Einfluss von Erweiterungen und Änderungen an den Objekten des Projektes muss idealerweise _sofort_ und ohne größere Umstände zu testen sein. 
Ein Testlauf darf keinen hohen Arbeitsaufwand fordern, sonst wird gänzlich auf einen Test verzichtet.
[[Unittest]]s müssen durch den Entwickler _sofort_ durchführbar sein. Der Unittest muss innerhalb von Sekunden ablaufen können. Es muss unmittelbar geprüft werden können welche Auswirkungen die Änderungen haben.
Wenn das nicht möglich ist steht zu vermuten, dass die Regeln des Clean Code nicht beachtet worden sind.

![[)c Robert C. Martin Clean Code#^dd9eb9]]

Effizientes automatisiertes Testen erfordert die Reduzierung auf eine einzige Stelle, damit erfolgt die Reduzierung des Erstellungs- und Pflegeaufwands auf _DAS MINIMUM_.

Klonen, bzw. Kopieren von Testfällen oder von Skriptabschnitten erzeugt bei kleinen Änderungen viel Arbeit im Bereich Anpassung. Wenn kleine Änderungen im [[)d Software under Test (SUT)]] vorgenommen werden, dann kann das einen großen Aufwand für die Testautomatisierung bedeuten.

\begin{Beispiel}
Beispiel .
\end{Beispiel}

Die nun folgenden Absätze verfolgen alle das Ziel das Testen _effizient_ zu machen und 
befassen sich mit der Aufwandsreduzierung bei der Erstellung von
funktionalen, fachlichen GUI Tests. 

![[Grundsätzliche Überlegungen zur Aufwandsreduzierung bei der Testautomatisierung]]

![[Übliche Vorgehensweise um Testfälle zu automatisieren]]

![[Strategien zur Vermeidung von Aufwänden in der Testautomatisierung]]
 
![[DRY-Prinzip Objekt-Erkennungseigenschaft]]

