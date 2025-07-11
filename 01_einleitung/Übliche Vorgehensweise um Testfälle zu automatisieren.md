# Übliche Vorgehensweise um Testfälle zu automatisieren
Bei der üblichen Vorgehensweise von Testfällen fallen folgende Arbeiten an:

1. Ein Fachtester erstellt zunächst einen Testfall. Dieser wird in Prosa aufgeschrieben.
2. Ein technischer Tester übersetzt die Prosa-Testfallbeschreibung in die Skriptsprache des Automatisierungswerkzeuges. 
  
Hieraus folgt, dass zur Umsetzung einer fachlichen Anforderung in ein Testfall üblicherweise zwei _Übersetzungen_ erfolgen:

1. Anforderung zu Prosa-Testfallbeschreibung, und
2. Prosa-Testfallbeschreibung zu Skriptsprache des Automatisierungswerkzeuges.

Prosa-Testfallbeschreibung ist in der Regel ein abstrakter Testfall, d.h. es gibt keine konkreten Daten.
 
Folgende Mängel im Übersetzungsprozess können die Erstellung der Automatisierungsskripte erschweren oder verhindern:
 
* Die Beschreibung des Prosa-Testfalls ist zu ungenau. ( "Man wähle eine geeignete Person aus." )
* Der Prosa-Testfall enthält keine Testdaten, d.h. es handelt sich um einen abstrakten Testfall.
* Die Start-Bedingung für den Testfall ist nicht definiert. Es ist unklar welche Umgebungsdaten die SUT benötigt. 

## Aufwandsreduzierung
Durch eine exakte Beschreibung der Testfälle inkl. der notwendigen Eingabedaten
können die genannten Aufwände verringert werden. - Der Arbeitsaufwand wird minimiert,
weil Rückfragen der technischen Tester an die fachlichen Tester reduziert werden.
 
_Aber:_ Eine Fehlinterpretation der Testfälle kann in der Prosa-Notation nicht ausgeschlossen werden.
Es sind weiterhin zwei Übersetzungen notwendig:
* Anforderung nach Prosa-Testfall und
* Prosa-Testfall in die Skriptsprache des Testwerkzeuges.