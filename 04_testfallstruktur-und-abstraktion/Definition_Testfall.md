## Definition Testfall nach ISTQB:
![[Testfall#^dca4ed]]
 
## Testfall etwas anders beleuchtet

 $E_{Erwartet} = F( O_{Test}, D_{Umgebung}, D_{Eingabe} )$

D.h, das erwartete Ergebnis ist abhängig vom

- Testobjekt,
- von (der Funktionalität) der Testumgebung
- vom Datenbestand der Testumgebung 
- und von den Eingabewerten.

__Wichtig:__ Wenn ein Testfall reproduzierbar und wiederholbar sein soll, dann darf die einzige veränderliche Größe das Testobjekt selbst sein. Diesen tauschen wir von Version zu Version aus. 

Wenn Aspekte des Objektes über mehrere Versionen gleich bleiben, dann sollten die Testfälle zu diesen Aspekten auch gleich bleiben, d.h. wiederum, dass zwei Testfälle gleich sind, wenn

* die Umgebung, 
* die Eingabewerte und
* das erwartete Ergebnis gleich, d.h. konstant bleiben.

Diese _müssen_ konstant bleiben, damit auf ein konstantes und bekanntes Ergebnis geprüft werden kann.

Tests müssen reproduzierbar sein. Es darf immer nur ein Parameter variieren. Sind dies mehrere, so kann im Fall einer Abweichung nicht sicher gesagt werden, welcher Parameter für die Abweichung ursächlich ist.

Wird der Parameter, bzw. werden die Parameter, verändert und bei einem wiederholten Testlauf ergibt sich eine Abweichung, besteht _nicht_ die Möglichkeit einer sicheren Aussage über die Ursachen dieser Abweichung.

Diese kann ihre Ursache in der neuen Version der [[)d Software under Test (SUT)|Software under Test]] oder in der Variation der Daten unter Einbeziehung einer falschen Vorhersage des Oracles haben.

Eine schnelle Aussage über die Versionsänderung, wie in einem Test erwünscht, kann so nicht getroffen werden. 

Neue Testfälle sind durchaus erwünscht, aber für einen verlässlichen Vergleich zwischen einer alten und einer neuen Version des Testlings, müssen bereits durchgeführte Testfälle wiederholt werden.

Bei neuen Testfällen ist es wichtig, dass diese auch neue Aspekte des Testlings abprüfen. Sie müssen systematisch abgeleitet werden.

- [Was auch immer](Aequivalenzklassentest.md)
- [[Pairwise Methode]] - Erläuterung unter http://de.wikipedia.org/wiki/Pairwise-Methode
- [[White-Box Test]] - Erläuterung unter http://de.wikipedia.org/wiki/White-Box-Test
- etc.

## Organisation von Testfällen
[[../05_test-denkmodelle/01_Keine_Verkettung_von_Testfaellen]]
  
### Testfall Zuständigkeit
Jeder Testfall sollte nur für eine bestimmte Testling Eigenschaft zuständig sein. Das hat den Vorteil, wenn so ein Testfall fehlschlägt, dann ist sofort erkennbar welche Eigenschaft betroffen ist. 

- [[Clean Code]] - Erläuterung unter \url http://de.wikipedia.org/wiki/Clean_Code
 
## Funktional/fachlicher Testfall.
\todo 

## Ablauf

*/