Versionshistorie
================

`English Version of this document. <../../en/book/versions.html>`_

Die Übersicht der Meilensteine finden Sie auf Github unter: https://github.com/mapbender/mapbender/milestones


Milestone next
-----------------

Relase Datum: soon

**Bugfixes und Features:**

- Das Messen zeigt die Koordinaten live an, d.h. beim Bewegen der Maus werden schon jeweils die erreichten Segment- und Gesamtlängen angezeigt.
- Die Messergebnisse werden nun von oben hinzugefügt. Damit steht das aktuelle Messergebnis sichtbar an oberster Stelle und muss nicht gescrollt werden.
- Der Login Dialog (Registrierung, Password vergessen) wurde für mobile Geräte optimiert, um den Zugriff auf gesicherte mobile Anwendungen zu erleichtern.
- Neu hinzugefügte Layerset Instances sind nun nicht mehr per Default als Basesource markiert.
  
- Das Löschen von Layersets führte in einigen Fällen zu einem korrupten Map-Element und falschem Layertree

- Anpassungen und Vereinfachung der Styles des FullScreenTemplate
- Einführung der Prüfung der CSS Angaben in der Anwendungskonfiguration

- Delay beim Wechsel von Layern gefixt
- Gefixter GetMap Request bei veränderter Reihenfolge der Layer im TOC
- Fix für WMS support 1.3.0
- Fix für geschützte WMS Dienste bei GetMap, GetFeatureInfo, Print, Export und Legende
- Fix des WMS Parameters Exception Format bei GetMap und GetFeatureInfo Request (Github-Issue 400)
- Fixes bei den Layer-Styles im GetMap und GetFeatureInfo Request

- Ablage von YML-Anwendungen in application/app/config/applications: mapbender_mobile.yml, mapbender_user_basic.yml, mapbender_user.yml und Anpassungen in der WMS Version
- Administrationsoberfläche YAML Editierung und Umformatierungen nach dem Speichern (Github-Issue 350)

- Anpassungen POI-Koordinate: Transformation und SRS, Nachkommastellen
- Fix eines XSS Fehlers im POI Dialog
- Fix in POI Dialog, wenn useMailto = false

- GPS: Fehlermeldungen, wenn kein Signal und Abhängigkeit von Chrome-Browsern und https.
- GPS: Verschieben der Karte nur bei erster Positionsbestimmung.

- Internet Explorer Kompatibilität: Anpassungen Zoombar.
- Internet Explorer Kompatibilität: Anpassungen OverviewMap
- MS Egde Kompatibilität: Import Dialog (https://connect.microsoft.com/IE/feedback/details/1574105/microsoft-edge-file-upload-bug-build-10240-rtm)

- Verbesserung der Performance bei *einigen* Installation unter Windows durch WinCachePHP und PHP Opcache (für Details siehe `Installation unter Windows <installation/installation_windows.html>`_)

- Kopieren von Anwendungen für Benutzer, die nicht root sind (ACL Application: owner, Benutzer: owner, Berechtigungen ACLs: owner, Element: owner, Gruppen: owner, Service Source: owner, spezifische Anwendung: owner)

  
**FOM und Absicherung:**

- Anzeige von Benutzern, die Zugriff auf ein Element in der Anwendung haben
- Überarbeitung des Secure Elements Dialogs


**verschiedenes**

- Anpassung Design FeatureInfo bei Anzeige als Accordion und wenn nicht als Source angezeigt
- Verschieben von Popups innerhalb einer Anwendung
- Anpassungen WMC Edit Dialoggröße und XSS

- Backend: Target-Feld: Leere Auswahl bei Drop-Down Feldern.
- Anpassungen WMS Scale, ScaleHint und Min/Max Werte beim Öffnen einer Layerset-Instance
- Anzeige des WMS-Titels in den Metadaten des TOC bei aktualisiertem WMS
- Anzeige des Applikations-Logos in der Konfiguration
- Anpassungen Simple Search und SearchRouter
- Anpassungen Druck: Farbe bei variablen Texten

- Fehlermeldung bei falsch konfigurierter Layerset-Instance

- Druck: Einführung von setasign/pdf als Alternative zu toooni/fpdf
- Druck: Fix der Fehlermeldung bei fehlendem Drucktemplate
- Messen von Linien und Flächen in WGS84 (EPSG:4326)

- Anpassung Anzeige der Element ACL

- WMS Aktualisierung: Entfernen von User/Passwort Browser Autocomplete
- Anzeige der Nachkommastellen im Coordinates-Display

- Anpassungen, Erweiterungen EPSG import
- Layer Maßstäbe und Fix der Default Visibility eines Layers
- Entfernen des Data Source Monitor Icon (kommt in Version "Next")
- Administration: Bewegung über Tabulator-Taste
- Verbesserung der Konfigurationsoberfläche
- Anzeige der Source-ID in Anwendungen

- Verbesserung Caching Mechanismen
- Verbesserungen Export / Kopieren
- Vereinfachung bei der Erstellung neuer Elemente



**Mobiles Template**

- Generelle Verbesserungen des Mobilen Templates
- Fix für einen Button, wenn dieser nur auf einen Link verweist.
- Fix für das Icon Label und der Schriftdicke normal
- Verbesserungen des Button Handlings allgemein
- Fix des event handlers ""on moveend"

**Digitizer**

- Digitizer: Druck von Multipolygonen
- Objekte erscheinen nicht mehr im Druck, wenn Sie im Digitizer ausgeblendet worden sind.
- Objekte mit einer Linienbreite von 0 werden im Druck nicht mehr sichtbar.
- Close Schaltfläche Anpassung

**Form Genrator:**

- Anpassungen: Hinzufügen des HTMLElement handling  für Services und  DataStore Konfiguration.


**Architektur:**

- PHP 7 Unterstützung
- Anpassungen ElementGenerator
- Ermitteln von Benutzerrollen
- Composer Einträge mit https
- Verschiedene Verbesserungen an Controllern und Bundles.
- Doctrine generate Kommandos als deprecated markiert
- Doctrine assets:dump Kommando als deprecated markiert
- Aktualisierung JOII Bibliothek
- Ablage von Symlinks zu verschiedenen Binaries im bin Verzeichnis

**Dokumentation**

- `FAQ <faq.html>`_ der Dokumentation hinzugefügt.


**config.yml Anpassungen**

DBAL-Parameter:

- default_connection: Bei mehreren Einträgen definiert die default_connection, die Standardverbindung der MB3-Datenbank.
- persistent: Persistente Verbindungen zur Datenbank zwecks Performance (Oracle)
  
.. code-block:: yaml

   doctrine:
     dbal:
       default_connection: default    
         connections:
           default:
             ...
             persistent: true
                

**mapbender-starter/application/app/config/applications/**

Verzeichnis, in das YAML-basierende Anwendungen abgelegt werden können. Als Beispiel sind die drei bekannten Anwendungen Mapbender-User, Mapbeder-User-Basic und Mapbender-Mobile abgelegt.
            
Dieses Release ist Uli gewidmet, der den ersten Pixel in Mapbender programmiert hat `. <https://assets.toggl.com/images/toggl-how-to-save-the-princess-in-8-programming-languages.jpg>`_



Milestone 3.0.5.3
-----------------

Release Datum: 04.02.2016

   
**Bugfixes:**

Besondere Änderungen:

- Performance: Die CSS, JavaScript und Translation Dateien werden nun im `Produktionsmodus <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_ im Symfony Cache gehalten. Dies kann insbesondere bei langsamen Servern zu Performancesteigerungen führen. Die Änderung gilt nicht für den `Entwicklermodus (app_dev.php) <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_.
- Das Paket `eslider/sassc-binaries <https://github.com/eSlider/sassc-binaries>`_ bietet nun auch einen sassc Compiler für 32-bit Linux Systeme an. Dies führte zu Anzeigeproblemen unter 32-bit Linux Systemen (http://lists.osgeo.org/pipermail/mapbender_users/2015-December/004768.html)
- Redlining: Die Inhalte des Redlining Elements sind nun sichtbar und das Element kann sowohl als Dialog als auch Element in der Sidepane verwendet werden. Siehe auch die `Dokumentation zum Redlining Element <../bundles/Mapbender/CoreBundle/elements/redlining.html>`_. Die Scrollbar bei den Geometrie-Types im Konfigurationsdialog wird korrekt angezeigt.

Benutzer und Absicherung:
  
- Benutzer können durch Administratoren, die mindestens das ACL-Benutzerrecht "Operator" besitzen, aktiv oder inaktiv geschaltet werden. Das ist z.B. sinnvoll, wenn Benutzer, die sich selbst registriert sich selbst noch nicht aktiviert haben. Siehe die `Dokumentation zu Benutzern <../bundles/FOM/UserBundle/users.html>`_.
- Texte, Übersetzungen und Styles bei der Registrierung und dem Passwort Reset wurden angepasst, ebenso die `Dokumentation dazu <../bundles/FOM/UserBundle/users.html>`_

Druck und Export Image:
  
- Das `Print-Modul <../bundles/Mapbender/CoreBundle/elements/printclient.html>`_ kann nun auch in die Sidepane eingebaut werden.
- Print Legende: Die Größe der Legende im Ausdruck wurde verkleinert, um die Anzeige zu verbessern.
- Druckvorlagen: Die Standard-Druckvorlagen sind angepasst worden. Der Abstand der dynamischen Texte wurde verringert und die Ausrichtung verbessert.
- Druck: In der Druck-Konfiguration wurden in Kombination von notwendigen (required: true) und optionalen Feldern (required: false) die optionalen Felder teilweise als required angezeigt (Github #380).
- Mapbender druckte unter Umständen die Legende aller Layer eines WMS aus, auch wenn der Layer nicht aktiv war (festgestellt im Mapbender_Users WMS).
- Export Image: Die Transparenz von gekachelten und nicht-gekachelten Diensten wird im Export Image unterstützt.

Kopieren und Import:
  
- Kopieren einer Anwendung unter SQLite und MySQL: Es lag ein Fehler vor, bei dem Anwendungen nicht kopiert werden konnten, wenn das Mapbender3 Repository in einer SQLite oder einer MySQL Datenbank lag.
- Fehler beim Import von Anwendungen als JSON unter MySQL (Elemente verlieren ihr Target) wurde gefixt.

Einzelne Elemente:
  
- **WMC** und Thematische Layer: Wenn ein WMC geladen wird und Keep Sources auf "no" eingestellt ist, werden auch die Thematischen Ebenen aus dem Layerbaum genommen.
- **WMS-URL Parameter** und Legende: Wenn ein Dienst über den wms_url Parameter in die Anwendung geladen wird, wurde die komplette Legende angezeigt und nicht die für die jeweiligen Layer. Dieses Verhalten wurde gefixt.
  
  - *Hinweis*: Es gibt WMS Dienste, die eine Legende im Hauptlayer-Element definieren. Diese wird nach der WMS Spezifikation auf die Layer vererbt, die selbst keine Legende definiert haben (z.B. weil sie nur eine Schrift anzeigen). Der Effekt in MB3 ist ähnlich, die Ursache aber eine andere, so dass in diesem Fall Anpassungen an den Capabilities notwendig sind (für den Layer eine statische Legende definieren).

- **Thematische Layer**: Korrektur im An- und Abschalten von Layern, die in einem eigenen Layerset sind, aber nicht als Thematischer Layer angezeigt werden.
- **Koordinatendisplay**: Das Element zur Koordinatenanzeige zeigte "null" als Text für den Präfix oder Separator, obwohl diese Felder leer sein sollten. Das Element hat weiterhin eine feste Breite bekommen, so dass das Layout im Footer stabiler wird. Der Wert kann verändert werden (Siehe die `CSS-Anpassungen zu dem Element <../bundles/Mapbender/CoreBundle/elements/coordinates_display.html>`_).
- **SearchRouter**: Der Inhalt der Ergebnisse füllt nun das gesamte Dialogfenster aus und passt sich an die Größenänderung an. In der Sidebar wird die gesamte Höhe ausgenutzt. Der SearchRouter ist, wenn er als Dialog eingesetzt wird, `in der Höhe und Breite konfigurierbar <../bundles/Mapbender/CoreBundle/elements/search_router.html>`_.
- **ScaleSelector**: Die Breite des Elements kann mit einem `CSS-Statement verändert werden <../bundles/Mapbender/CoreBundle/elements/scale_selector.html>`_ und ist nicht auf 155 Pixel festgelegt.
- Wenn in einer **Layerset-Instance** alle Layer auf visible=off gestellt sind, waren der Tree und die Legende nicht sichtbar.
- **POI Dialog** Verbesserungen im Styling, wenn  usemailto auf false gesetzt ist.
- **Layertree**: Anzeige der Titel nun mit einer Gesamtlänge von 40. Der Default-Wert wurde verändert. Sie können den `Parameter Titlemaxlength anpassen <../bundles/Mapbender/CoreBundle/elements/layertree.html>`_.
- **GPS**: Verfeinerungen im GPS Tool

Allgemeine Änderungen:
  
- Bei Änderungen an Grunddaten einer Anwendung, dem Layout, den Layersets, dem CSS und der Sicherheit bleibt man nun in dem jeweiligen Reiter und springt nicht zu den Grunddaten zurück.
- Allgemeine Verbesserungen im `Digitizer <https://github.com/mapbender/mapbender-digitizer>`_ Version 1.0. Die Version 1.1 ist kompatibel mit Mapbender 3.0.5.3.
- Github Infodateien: Kleine Aufräumarbeiten im Github Repository, um die automatischen Buildprozesse zu verbessern.
- Transparenz von Diensten: Dienste, die mit einer Transparenz dargestellt werden aktualisierten sich mit einem unschönen Effekt, verursacht durch durch den "transitionEffect" in OpenLayers. Dieser Effekt
  wurde entfernt.
- Gruppenfilter: In dem Konfigurationsdialog zu den Sicherheitseinstellungen wurde die Auswahl von Gruppen verbessert, wenn Gruppen einen gleichem Namen aber unterschiedlichen Suffixe besitzen.
- TileSize Parameter in der Kartenkonfiguration wird unter Umständen nicht gesetzt.
- Anzeige der Symbole unter Internet Explorer 11 und MS Edge 25 (auch ein Fehler in MS Edge 20).
- mapbender.yml: Beim initialen Import der mapbender.yml werden die Angaben von GetFeatureInfo nun auf text/html gesetzt. Die mapbender.yml kann nun mit Redlining erweitert werden.

 
**Umzug der Mapbender Domänen:**

- Wir haben die URL www.mapbender.org auf die Mapbender3 umgeschwenkt. Somit ist die Mapbender3 Seite zukünftig über www.mapbender.org und www.mapbender3.org erreichbar. Mapbender2 ist nun über www.mapbender2.org erreichbar.
  
  - http://www.mapbender.org: Mapbender3,
  - http://www.mapbender3.org: Mapbender3,
  - http://www.mapbender2.org: Mapbender2.

    
**Bekannte Probleme:**

- Das Sketch Tool funktioniert nicht korrekt und wird in Zukunft in das `Redlining Tool <../bundles/Mapbender/CoreBundle/elements/redlining.html>`_ übernommen werden.
- Karte weiterempfehlen funktioniert nicht für Facebook, Twitter und Google+.

    
    
Milestone 3.0.5.2
-----------------

Release Datum: 27.10.2015

**Bugfixes:**

- Kopieren von Anwendungen: Rechte und Gruppen werden mit übernommen. Der Nutzer, der die Anwendung kopiert hat, wird Owner der kopierten Anwendung.
- FOM: Änderungen im Verhalten bei falschen Logins und dem Locking. Es wird nur noch angezeigt, dass der Login fehlgeschlagen ist - unabhängig davon, ob der Benutzer existiert oder nicht.
- Korrigierte Fehlermeldung beim Anlegen eines Benutzers mit zu kurzem Passwort.
- Print: Fix des Replace Patterns.
- Print: Fix, wenn falsch konfigurierter WMS Sonderzeichen (%26) in der Legenden URL hat.
- Image Export in Firefox.
- WMC Loader: Einladen von WMC und das Verhalten der BaseSources.
- BaseSourceSwitcher: Kacheln des nicht sichtbaren Dienstes werden nicht vorgeladen.
- BaseSourceSwitcher: Wenn eine Gruppe definiert ist, ist nur ein Thema beim Start eingeschaltet.
- SearchRouter: Fix der Anführungszeichen für Tabellennamen.
- Anwendungen kopieren: Fix der Suche in der kopierten Anwendung.
- Simple Search: Return Schaltfläche wird abgefangen.
- FeatureInfo: Add WMS Funktionalität und WMS Loader.
- Icon Polygone in der Toolbar von Anwendungen ist sichtbar.
- Icons, die nicht auf FontAwesome basieren, funktionieren auch im Mobilen Template.
- Administration Map Element: Anzeige des Konfigurationdialogs im Backend beginnt oben.
- Administration Datenquelle: Keine Formulardaten Vorbelegung durch den Browser für Benutzername und Passwort.
- Mobile Anwendung: Darstellung unter Firefox für Android.
- Update 3.0.4.x: FeatureInfo autoopen=true bleibt erhalten.
- Doku: FOM `UserBundle Übersetzung <../bundles/FOM/UserBundle/index.html>`_ und `Ergänzung bei falschen Benutzer-Logins <../bundles/FOM/UserBundle/users.html>`_.
- Doku: URL Parameter scale im `Map Element <../bundles/Mapbender/CoreBundle/elements/map.html>`_.
- Doku: `WMC Loader <../bundles/Mapbender/WmcBundle/elements/wmc_loader.html>`_ und KeepSources.


**Änderungen in der config.yml:**

* Die folgenden Änderungen sind optionale Parameter für das Verhalten des Logins (siehe das `entsprechende Kapitel im FOM Bundle <../bundles/FOM/UserBundle/users.html>`_):

    .. code-block:: yaml
                    
                    fom_user:

                      # Allow to create user log table on the fly if the table doesn't exits.
                      # Default: true
                      auto_create_log_table: true

                      # Time between to check login tries
                      login_check_log_time: "-5 minutes" 

                      # Login attemps before delay starts
                      login_attempts_before_delay: 3

                      # Login delay after all attemps are failed
                      login_delay_after_fail: 2 # Seconds




Milestone 3.0.5.1
-----------------

Release Datum: 26.08.2015

**Neue Funktionen**: im `Kartenelement <../bundles/Mapbender/CoreBundle/elements/map.html>`_ und beim `Druck Client <../bundles/Mapbender/CoreBundle/elements/printclient.html>`_:

* Map: OpenLayers TileSize: Es kann die Kachelgröße für die Karte angegeben werden. Default: 256x256.
* Map: Delay before Tiles: Für WMS-T, z.B. bei zeitlichen Parametern (zukünftig)
* Druck: Koordinatenanzeige in der PDF-Druckausgabe
* Druck: Übernahme Druckmaßstab abhängig vom Kartenmaßstab
* Druck: Druck legend_default_behaviour
* Druck: Hinzufügen von Druckvorlagen über das +-Symbol
* Druck: Benutzerabhängiges Logo und Text


**Bugfixes:**

- Layertree: Lade-Symbol und Ausrufezeichen-Symbol.
- Layertree: Zoom Symbol nicht bei Layern ohne BBOX-Information
- WMS Reload: FeatureInfo
- WMS Reload: Einige WMS konnten sich nicht neuladen lassen.
- Export/Import von Anwendungen verschiedene Bugfixes
- WMC-Editor und WMC-Load Fixes.
- WMC aus einer Mapbender 3.0.4.1 Anwendung
- Tile Puffer und BBOX Puffer fixes
- FeatureInfo: Fixes im Design und bei der Anzeige als Accordion Panel
- FeatureInfo: Drucken
- Falscher Link Jquery-UI in layerset instance
- Save Layerset und Save Layout bleibt auf der Seite
- Classic Template: SCSS korrigiert
- Mobile Template: Bootstrap Meldung verdeckt Schließen Schaltfläche
- Mobile Template: SearchRouter Fenster ausblenden
- Mobile Template: Mozilla Firefox Fixes im Layout
- Backend: Layerset Filter und +-Buttons verstecken nicht mehr alles
- composer.json Anpassung Version Digitizer auf 1.0.*
- Dokumentation des JS-UI Generators (Formular-Generator): https://github.com/eSlider/vis-ui.js
- Umstrukturierte `Installations-Dokumentation <installation.html>`_ und einige Anpassungen (php-pear, assets-Verzeichnis, init:acl, openssl).
- Verbesserte Dokumentation der `Mapbender3 Templates <templates.html>`_
- Verbesserte Dokumentation des `Quickstart <quickstart.html>`_

**Known Issues:**

- Kopieren von alten 3.0.4.1 Anwendungen kopiert nicht die anzuzeigenden Layersets der Map. Bitte speichern Sie vorher das Map und Overview-Element.
- Regional Template entfernt



 
Milestone 3.0.5.0
-----------------

Release Datum: 01.07.2015

Übersicht der Änderungen finden Sie unter:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* **WMS neuladen:** WMS Quellen können nun neugeladen werden, wenn sich deren Strutkur geändert hat.

* **Digitalisierung:** Im Rahmen des Releases wurde das neue Element Digitizer eingeführt. Über dieses kann durch eine YAML-Definition eine Erfassungsmaske für Punkte, Linien oder Flächen aufgebaut werden. Dabei wird wie bisher PostgreSQL als Datenquelle unterstützt. Oracle und SpatiaLite sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen wie z.B. OGC WFS erweitert werden kann.

* **Druck mit Legende:** Im Druck ist es nun möglich, die Legende auf einer separaten Seite auszugeben. Die Ausgabe kann über eine Checkbox gesteuert werden.

* **Konfigurierbarer Layerbaum:** Der Layerbaum unterstützt nun mehr als ein layerset. Sie müssen das Kartenelement anpassen, um die Layersets festzulegen, die angezeigt werden sollen sowie den Layerbaum selbt. Die Dokumentation befindet sich unter `auf der Seite zum Layertree <../bundles/Mapbender/CoreBundle/elements/layertree.html>`_.

* **Verbesserte Infoausgabe:** Die Ausgabe der Infoabfrage wurde für die neue Version verbessert. So bleiben nun die Stile der Infoabfrage erhalten. Dienste, die keine Antwort liefern, werden nicht über einen Reiter angezeigt. Es erfolgen Meldungen, wenn keine Antwort geliefert wurde.

* **Mobiles Template:** In mehreren Projektlösungen haben wir uns bereits mit einer mobilen Lösung auf Basis von Mapbender3 auseinandergesetzt. Nun wird diese Lösung als Mapbender Mobile Template in der neuen Version 3.0.5.0 zur Verfügung gestellt.   Sie finden eine neue Demo-Anwendung in der mapbender.yml mit Namen Mapbender Mobile (mapbender_mobile). Diese können Sie als Vorlage für Ihre Lösung verwenden. In der `Release-Demo <http://demo.mapbender3.org/>`_ kann die Anwendung „Mapbender Mobile“ getestet werden.

* **SASS Compiler:** Änderungen an der Architektur bezüglich des SASS Compilers führen zu einer performanteren Oberfläche.

* **Vendor Specific Parameter:** Eine WMS Layer Instanz unterstützt nun die Angabe von Vendor Specific Parametern, die an einen WMS Request angehangen werden. Die Werte können fest vergeben werden oder auf die User- und Gruppeninformation des angemeldeten Benutzers zurückgreifen. Dokumentation ist unter dem Abschnitt `Vendor Specific Parameters <../book/quickstart.html#konfiguration-von-diensten>`_ verfügbar.

* **Formular-Builder:** In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden. Hierbei wurde sich an den Möglichkeiten, die in Mapbender 2.x zur Verfügung stehen, orientiert.

* **Neue Schaltflächen:** Einige Schaltflächen basieren auf einer neuen Schriftart, die alten Schaltflächen sind noch mit dem Namen FontAwesome verfügbar.

* **URL Parameter:** Mapbender3 kann mit Startparametern aufgerufen werden. Eine Liste der Parameter findet sich in der Dokumentation zu den `URL Parametern <../bundles/Mapbender/CoreBundle/elements/map.html#kontrolle-uber-den-aufruf>`_.

* Neue Übersetzungen für Portugiesisch und Russisch.
  
* Symfony Update auf 2.3.30.


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
