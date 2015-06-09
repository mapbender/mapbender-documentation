Versionshistorie
================

`English Version of this document. <../../en/book/versions.html>`_

Die Übersicht der Milestones finden Sie auf Github unter: https://github.com/mapbender/mapbender/milestones

Future Milestones: Details finden sich unter https://github.com/mapbender/mapbender/issues

 
Milestone 3.0.5.0
-----------------

Release Datum: xx-05-2015

Übersicht der Änderungen finden Sie unter:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* WMS Aktualisierung
* Digitalisierung
* Druck mit Legende
* konfigurierbarer Layerbaum
* Mobiles Template
* SASS Compiler
* addvendorspecific
* erweiterte Funktion des HTML Elements durch den Formularbuilder
* Neue Button Kollektion
* verbessertes Verhalten des featureInfo-Dialoges (Stilvorgaben erhalten, Reiter nur bei Treffern öffnen, Angabe Breite/Höhe des Dialogs)
* Startparameter (Wechsel srs, poi, bbox, center)
* Symfony Update 2.3.27

**Änderungen in der config.yml:**

* Änderung bei einer dbal connection:

  * **logging: false**: Die Option sorgt dafür, das *alle* SQL's nicht mehr geloggt werden. Mehr dazu hier: http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste/

  * **profiling: false**: Profiling von SQL Anfragen. Diese Option kann in der Produktion ausgeschaltet werden.

    Wo möglich sollen die Optionen so umgestellt werden, dass die erst in Debug modus aktiv werden:

    .. code-block:: yaml

                    logging:               "%kernel.debug%"
                    profiling:             "%kernel.debug%" 


**Bekannte Probleme**

* Beim Kopieren einer Anwendung von Mapbender 3.0.4.x muss in der Map/Overview der jeweilige Layerset neu gesetzt werden.
                    

Milestone 3.0.4.1
-----------------

Release Datum: 23-01-2015

Übersicht der Änderungen finden Sie unter:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* parameter 'layerRemove' removed from layertree configuration
* option 'removelayer' added into layertree menu
* container accordion structure changed
* import / export from applications added (without acls)
* display layer metadata
* Frontend: Sidepane Accordeon Legend is displayed without horizontal Scrollbar
* Backend: WMS Instanz configuration - contextmenu for layers shows wrong ID (only instance ID)
* Frontend: Legend - displays WMS Information although the checkbox Show
* Frontend: Layertree - contextmenu zoomlayer does not use the layer extent
* Backend: Add Source with user/password - informations is added to field originUrl not to fields user and password
* app/console mapbender:generate:element fixed errors
* bug visiblelayers fixed
* WMS with authentication saves in table mb_wms_wmssource username and password
* no metadata for applications coming from mapbender.yml definition (no entry in context menu)
* copy an application via button on application fixed
* print template resize northarrow, overview added
* improved screenshot for application handling
* https://github.com/mapbender/mapbender/milestones/3.0.4.1
 

Milestone 3.0.4.0
-----------------

Release Datum: 12-09-2014
Übersicht der Änderungen finden Sie unter:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* Wechsel zur MIT Lizenz
* Symfony Update 2.3 LTS
* OpenLayers 2.13 mit zusätzlichen Patches
* Dienste Aktivieren über Button oder Menü (BaseSourceSwitcher)
* HTML-Element
* CSS-Editor für Anwendungen
* Reiterstruktur in der Seitenleiste
* Laden von Vorschaubildern für Anwendungen
* Import/Export von Anwendungen und Diensten
* spanische Übersetzung
 

Milestone 3.0.3
----------------

Release Datum: 17-03-2014
Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=8

* Erweiterungen Such-Router für SQL-Suchen (Selectboxen, Distinct)
* WMC Editor und Loader
* WMSLoader Erweiterung WMS über Link hinzufügen
* i18n - Internationalisation (english / german)
* Sketch zum Zeichnen von Skizzen
* POI - Treffpunktfunktion
* Bildexport zur Ausgabe von png und jpg
* WMS Anzeige über Button wechseln
* Druckausgabe mit Übersichtskarte, Replace-Pattern, optionalen Feldern
* Zusammenstellung von mehreren Elementen in der Seitenleiste (Wechsel über Button)
* Layerbaum mit Kontextmenü zur Transparenzeinstellung und zum Zoom auf das Thema
* Übergabe von Parametern beim Öffnen der Anwendung (Position)
* ACL für Elemente
* Funktion zur Validierung von WMS GetCapabilities Dokumenten
 

Milestone 3.0.2
---------------

Release Datum: 27-11-2013
Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=6

* Such-Router für SQL-Suchen
* WMC Editor und Loader
* WMSLoader Erweiterung WMS über Link hinzufügen
 

Milestone 3.0.1
---------------

Release Datum: 06-09-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=5

* Kopieren einer Anwendung mit Diensten
* Popup - draggable
* PrintClient Erweiterung Druck EPSG 4326, neue Drucklayouts, Druck A4-A0
* Abfangen von fehlerhaften Anmeldungen zum Abwenden von brute force login Versuchen
* Bug fixes
 

Milestone 3.0.0.2
-----------------

Bugfix-Release Datum: 19-07-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=4

 

Milestone 3.0.0.1
-----------------

Bugfix-Release Datum: 07-06-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=3

 

Milestone 3.0.0.0
-----------------

Release Datum: 29-05-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=1

* Administrations Backend für Services, Applikationen, Benutzer/Gruppen und Zugriffsverwaltung
* Backend-/Frontend Design  
* Zugriffsverwaltung
* Benutzer-/Gruppen-Administration
* WMS Administration
* Kartenelement
* Layerbaum
* Legende
* Übersichtskarte
* Navigations-Werkzeugkasten
* Infoabfrage
* Koordinatenanzeige
* Copyright
* Linien/Flächen-Messung
* Maßstabsauswahl
* Maßstabsleiste
* Spatial Reference System-Auswahl
* GPS-Position
* Druck
* WMS zur Anwendung hinzufügen
* Dokumentation unter http://doc.mapbender3.org
