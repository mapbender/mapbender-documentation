.. _concepts_de:

Konzept
#######

Dieses Kapitel gibt eine Einführung in das Konzept von Mapbender. Nach dem Lesen sollten Sie den Aufbau von Mapbender und die Interaktion zwischen den verschiedenen Komponenten der Software verstehen.

Anwendung
===========

Eine Anwendung (Applikation) ist eine einzelne Mapbender-Konfiguration, die normalerweise als interaktive Webkarte verwendet wird.

Jede Anwendung besteht aus verschiedenen Komponenten:

* Elemente 
* Layersets 
* Anwendungsvorlagen

Elemente
========

Elemente sind die Bausteine der Anwendung. Jedes Element liefert Funktionalität und kann ggf. mit anderen Elementen interagieren. Das Kartenelement ist vermutlich das Element, das Sie am meisten benutzen werden.

Jedes Element besteht aus vier Bereichen: 

* PHP-Klasse: Sie beschreibt das Element mit seinen Möglichkeiten. Die Klasse kann auch ein Ajax callback point bereitstellen, so dass das clientseitige Widget (siehe unten) Datenbankabfragen ausführen kann und die Ergebnisse beispielsweise anzeigen kann.
* JavaScript-Widget: Dies ist der clientseitige Teil des Elements. Dieser Teil beinhaltet alles, was Sie am Bildschirm ausführen und mit dem Sie interagieren. Über Ajax kann dieser Teil den serverseitigen Gegenpart aufrufen und beispielsweise Datenbankabfragen ausführen.
* Template: HTML, welche das Element verwendet. In der einfachsten Version würde dies nur ein DIV-Tag sein. Aber es kann auch komplexer sein.
* CSS: Dient dem Styling der Elemente.

Anwendungsvorlage
==================

Jede Anwendung ist eine HTML-Seite. Die Anwendungsvorlage definiert das Basislayout der Seite. Die Anwendungen können unterschiedliche Vorlagen verwenden, beispielsweise spezielle Vorlagen für die mobile Anwendung.

Frontend
========

Das Frontend ist die Anwendungssicht der Mapbender-Installation. Es beinhaltet die Anwendungsliste und jede Sicht auf die Anwendung. Der Anwender interagiert mit dem Frontend.

Backend
=======

Über das :ref:`backend_de` wird die Mapbender-Installation konfiguriert. Es wird auch der Manager genannt. Mit ihm lassen sich Benutzer, Gruppen und Rollen, Dienste, Anwendungen und Elemente verwalten.

