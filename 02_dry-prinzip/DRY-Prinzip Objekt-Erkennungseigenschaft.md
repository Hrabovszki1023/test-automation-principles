#status/entwurf

# Vermeidung von Aufwänden bei den Objekt-Erkennungseigenschaft

Testautomatisierungswerkzeuge bieten unter verschiedenen Bezeichnungen wie 
* Objekt-Repository, 
* GUI-Frame
* GUI-Map, 
* Test-Frame
jeweils eine eigenen Lösung für das gleiche Problem: Eine Struktur für zentrale Verwaltung der Objekterkennungseigenschaften. Dieses ist im Grunde eine Liste, in der [[Abstrakte Lokatoren und konkrete Lokatoren]] verwaltet werden. 

Fachlicher Bezeichner,  Lokator, GUI verwenden einheitlich das gleiche Attribut.
Vorteil:
* Lokatoren können vorab erstellt werden
* Lokatoren sind mit einem Attribute leicht erstellbar
* Lokatoren sind in der Ausführung schneller
* im Fehlerfall ist die Identifizierung der Objekte einfach, da alle Komponenten einheitlich benannt sind.
* Kommunikation zwischen Tester und Entwickler und Anforderungsanalytiker wird vereinfacht.