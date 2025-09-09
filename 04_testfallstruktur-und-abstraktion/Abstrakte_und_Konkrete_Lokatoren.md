# Abstrakter Lokator

Ein abstrakter Lokator ist ein implantationsunabhängiger *Bezeichner* für ein GUI-Objekt. Dies bedeutet, dass er nicht an die spezifische Implementierung oder den Code des Benutzeroberflächen-Elements gebunden ist, sondern vielmehr eine allgemeine und flexible Methode darstellt, um auf das Objekt zu verweisen. Ein solcher Lokator ist besonders nützlich in der Softwareentwicklung und beim Testen von Anwendungen, da er es ermöglicht, Änderungen an der Benutzeroberfläche vorzunehmen, ohne dass die Testfälle angepasst werden müssen. 

Ein praktisches Beispiel hierfür wäre ein abstrakter Lokator, der ein Eingabefeld in einer Webanwendung beschreibt. Anstatt sich auf den genauen HTML-Code oder die CSS-Klassen zu beziehen, könnte der Lokator eine Beschreibung wie "Eingabefeld für Benutzername auf der Anmeldeseite" verwenden. Diese Beschreibung bleibt auch dann gültig, wenn sich der zugrunde liegende Code ändert, solange das Eingabefeld weiterhin dieselbe Funktion erfüllt.

Der abstrakte Lokator hilft dem Fachtester, ein GUI-Objekt eindeutig in den Testfällen zu bezeichnen. Fachtester, die oft nicht tief in die technischen Details der Implementierung involviert sind, profitieren von dieser Abstraktionsebene, da sie sich auf die Funktionalität und das Verhalten der Anwendung konzentrieren können, ohne sich um die technischen Details kümmern zu müssen. Dies erleichtert die Kommunikation zwischen Entwicklern und Testern und trägt dazu bei, dass die Testfälle robuster und weniger anfällig für Fehler durch Änderungen in der Benutzeroberfläche sind. 

Zusammenfassend lässt sich sagen, dass abstrakte Lokatoren eine wesentliche Rolle im modernen Softwaretestprozess spielen, indem sie die Wartbarkeit und Flexibilität von Testfällen erhöhen und gleichzeitig die Zusammenarbeit zwischen verschiedenen Teams verbessern.

Am Beispiel eines Login-Dialogs, bestehend aus  
- "Dialog-Fenster" - "Login" 
- "Eingabefeld" - "Benutzer"
- "Eingabefeld" - "Passwort"
- "Schaltfläche" - "Login"
- "Schaltfläche" - "Abbruch"

Beispiel implementationsunabhängige Beschreibung eines Testfalls:

``` 
SetWindow( "Login" );
SetValue( "Benutzer", "Admin_1" );
SetValue( "Passwort", "Geheim_1");
Select("Login");
```

In diesem Beispiel wird ein Testfall beschrieben, der unabhängig von der spezifischen Implementierung der Benutzeroberfläche ist. Der erste Schritt, `SetWindow("Login")`, setzt den Kontext auf das Fenster oder den Bildschirm, auf dem der Benutzer sich anmelden soll. Dies ist ein entscheidender Schritt, da es sicherstellt, dass alle nachfolgenden Aktionen im richtigen Kontext ausgeführt werden. 

Der nächste Schritt, `SetValue("Benutzer", "Admin_1")`, setzt den Wert des Benutzernamensfeldes auf "Admin_1". Hierbei ist es wichtig zu beachten, dass "Admin_1" ein Platzhalter für einen tatsächlichen Benutzernamen ist, der in einem realen Szenario verwendet werden könnte. Dies ermöglicht es, den Testfall flexibel zu gestalten und ihn leicht an verschiedene Testumgebungen anzupassen.

Ebenso wird mit `SetValue("Passwort", "Geheim_1")` das Passwortfeld auf "Geheim_1" gesetzt. Auch hier handelt es sich um einen Platzhalter, der in der Praxis durch ein echtes Passwort ersetzt werden würde. Diese Platzhalterstrategie ist besonders nützlich, um die Sicherheit zu gewährleisten und sensible Daten nicht direkt im Testfall zu hinterlegen.

Der letzte Schritt, `Select("Login")`, simuliert das Drücken des Login-Buttons. Dies ist der entscheidende Moment, in dem die Anmeldedaten an das System übermittelt werden, um den Anmeldevorgang zu initiieren.

Der erste Parameter in jedem dieser Schritte ist der abstrakte Lokator des jeweiligen Objekts. Diese abstrakten Lokatoren sind von der spezifischen Implementierung der Benutzeroberfläche unabhängig und werden typischerweise zur Laufzeit durch konkrete Lokatoren ersetzt. Diese konkreten Lokatoren sind spezifische Identifikatoren, die das System benötigt, um die richtigen Elemente auf der Benutzeroberfläche zu finden und zu manipulieren.

Ein zentraler Aspekt dieser Methode ist das Prinzip des DRY (Don't Repeat Yourself). Die konkreten Lokatoren werden zentral an genau einer Stelle verwaltet, was bedeutet, dass Änderungen an der Benutzeroberfläche nur an einer Stelle im Code vorgenommen werden müssen. Dies reduziert die Wartungsarbeit erheblich und minimiert das Risiko von Fehlern, die durch inkonsistente Lokatoren entstehen könnten. Dieses Prinzip trägt dazu bei, die Testfälle robust und leicht wartbar zu gestalten, was besonders in großen Projekten von Vorteil ist.

# Konkreter Lokator