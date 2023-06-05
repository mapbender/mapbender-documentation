.. _components_de:

Komponenten
###########

Mapbender besteht aus unterschiedlichen Software-Komponenten. Serverseitig wird Symfony als Framework mit seinen integrierten Bestandteilen (Doctrine, Twig, Monolog) genutzt.

Clientseitig nutzt Mapbender OpenLayers, MapQuery, jQuery und jQuery UI.

Wir stellen das Mapbender Core Bundle mit den Mapbender-Funktionalitäten bereit. Darüber hinaus gibt es weitere optionale Bundles.

Außerdem bieten wir das Mapbender Starter Paket an. Mit diesem ist Mapbender leicht installierbar.

  .. image:: ../../figures/mapbender_components.png
     :scale: 60


Symfony
********
Symfony ist ein objektorientiertes PHP Web Development Framework. Es gilt als Standard für den Bau von Webseiten und Web-Applikationen.

Diese Komponenten bietet Symfony an:

* Symfony config.php zum Prüfen von Voraussetzungen
* Symfony Profiler 
* Datenbankabstraktion mit Doctrine
* Benutzerauthentifizierung & -autorisierung
* Templating mit Twig
* Übersetzungen über xliff-files
* Logging mit Monolog
* Sicherheitskomponenten

Mehr über Symfony und dessen Funktionsweisen findet sich in der offiziellen Dokumentation: 

* https://symfony.com/doc/current/book/index.html


OpenLayers
**********
OpenLayers ist eine JavaScript-Bibliothek, die das Anzeigen von Geodaten im Webbrowser ermöglicht.

Mehr über OpenLayers findet sich auf der offiziellen Website unter: https://openlayers.org/


jQuery and jQuery UI
********************
jQuery ist eine Standard-JavaScript-Bibliothek. jQuery UI bietet eine Sammlung von Benutzeroberflächenelementen auf Grundlage der jQuery JavaScript Bibliothek an.  

Mehr über jquery: https://jquery.com

Mehr über jquery UI: https://jqueryui.com/


Mapbender
**********
Mapbender ist aus Komponentensicht eine Bundle-Sammlung. Als Voraussetzung muss das MapbenderCoreBundle und die FOMBundles genutzt werden.

Andere (optionale) Bundles, die die Funktionalität grundlegend erweitern, sind:

* WMSBundle
* WMTSBundle
* WMCBundle
* MonitoringBundle


CoreBundle
~~~~~~~~~~
Das Mapbender CoreBundle ist das Mapbender Standard-Bundle. Es beinhaltet grundlegende Klassen für Anwendungen, Elemente, Layer und mehr.

Es stellt jQuery, jQuery UI, OpenLayers und MapQuery für alle anderen Mapbender Bundles bereit.

.. ToDo
  FOM Bundle

Mapbender Starter
*****************
Mapbender Starter ist ein Symfony Demo-Projekt welches Mapbender Bundles nutzt, um eine grundlegende Mapbender-Anwendung zu präsentieren.

Es enthält die Standard-Demo-Anwendungen, welche in der mapbender.yml definiert werden. Diese sind über ein Web-Interface mit Authentifizierungsmöglichkeiten (Backend) eingebunden. Das Backend kann darüber hinaus genutzt werden, um Anwendungen, Benutzer und Gruppen zur Rechteverwaltung zu erstellen und verschiedene Dienste einzubinden.

Mapbender Starter kann als einfache Startmöglichkeit in das eigene Mapbender-Projekt genutzt werden.

Link zum GitHub-Repository: https://github.com/mapbender/mapbender-starter


Externe Repositories
*********************
Noch mehr mit Mapbender zusammenhängende Repositories finden sich auf GitHub. Verschiedene Anbieter können auf dieser Plattform Mapbender-spezifische Bundles anbieten; bspw. das DesktopIntegrationBundle, welches von der `WhereGroup <https://wheregroup.com>`__ bereitgestellt und von Kunden gesponsert wird.

Die WhereGroup bietet Mapbender-Bundles in GitHub an: https://github.com/WhereGroup

