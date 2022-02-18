.. _versions_de:

Versionshistorie
================

`English version of this document. <../en/versions.html>`_

Die Übersicht der Meilensteine finden Sie auf `Github <https://github.com/mapbender/mapbender/milestones>`_.



Version 3.2.9
-------------

Release Datum: 28.01.2022

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v329


Version 3.2.8
-------------

Release Datum: 02.11.2021

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v328


Version 3.2.7
-------------

Release Datum: 07.09.2021

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v327


Version 3.2.6
-------------

Release Datum: 09.08.2021

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v326


Version 3.2.5
-------------

Release Datum: 08.06.2021

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v325


Version 3.2.4
-------------

Release Datum: 04.03.2021

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v324


Version 3.2.3
-------------

Release Datum: 21.12.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v323


Version 3.2.2
-------------

Release Datum: 02.11.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v322


Version 3.2.1
-------------

Release Datum: 06.08.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v321


Version 3.2.0
-------------

Release Datum: 29.07.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v320


Version 3.0.8.6
---------------

Release Datum: 15.09.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3086


Version 3.0.8.5
---------------

Release Datum: 05.02.2020

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3085


Version 3.0.8.4
---------------

Release Datum: 04.09.2019

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3084


Version 3.0.8.3
---------------

Release Datum: 05.07.2019

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3083


Version 3.0.8.2.1
-----------------

Release Datum: 05.07.2019

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v30821


Version 3.0.8.2
---------------

Release Datum: 03.07.2019

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3082


Version 3.0.8.1
---------------

Release Datum: 14.05.2019

**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3081


Version 3.0.8.0
---------------

Release Datum: 12.04.2019


**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v308

**Hinweise zur Aktualisierung**

https://github.com/mapbender/mapbender/blob/master/UPGRADING.md#308


Version 3.0.7.7
---------------

Release Datum: 07.11.2018


**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3077


Version 3.0.7.6
---------------

Release Datum: 18.10.2018


**Verbesserungen und Bugfixes:**

* https://github.com/mapbender/mapbender-starter/blob/master/CHANGELOG.md#v3076


Version 3.0.7.5
---------------

Release Datum: 26.09.2018


**Verbesserungen und Bugfixes:**

* Die Beschreibung zu den Fixes ist in den Repository-Links zu finden
* Aktualisierung `Mapbender-Starter v3.0.7.5 <https://github.com/mapbender/mapbender-starter/releases/tag/v3.0.7.5>`_
* Aktualisierung Mapbender Repository auf `v3.0.7.5 <https://github.com/mapbender/mapbender/releases/tag/v3.0.7.5>`_
* Aktualisierung Owsproxy Repository auf `v3.0.6.4 <https://github.com/mapbender/owsproxy3/releases/tag/v3.0.6.4>`_, includes Owsproxy dependencies
* Aktualisierung mapbender/vis-ui.js Repository auf `0.0.72 <https://github.com/mapbender/vis-ui.js/releases/tag/0.0.72>`_
* Aktualisierung mapbender/data-source Repository auf `0.1.8 <https://github.com/mapbender/data-source/releases/tag/0.1.8>`_
* Aktualisierung mapbender/digitizer Repository auf `1.1.66 <https://github.com/mapbender/mapbender-digitizer/releases/tag/1.1.66>`_
* Aktualisierung bundled Composer Repository auf `1.6.5 <https://github.com/composer/composer/releases/tag/1.6.5>`_ 
* ComposerBootstrap Bereinigungen


Version 3.0.7.4
---------------

Release Datum: 29.08.2018


**Verbesserungen und Bugfixes:**

* [Sicherheit] In Entwicklungsumgebungen kann es bei den Assets zu einem XSS Fehler kommen. Dieser Fehler tritt nur in einigen Umgebungen mit spezifischen PHP Einstellungen (error_reporting z.B. E_ALL) auf.
* Zurücknahme der Keyword Spalte zum Datentyp "varchar", um Inkompatibilitäten mit Oracle zu vermeiden. Zu lange Keywords werden auf 255 Zeichen abgeschnitten. (#1000)
* Einige JavaScript Fixes, die beim stillgelegten Internet Explorer 11 zu Problemen führten. (#990)
* Leere Layernamen werden beim FeatureInfo nicht mehr angefragt (PR #1010).
* Doctrine Optimierungen um die Layerreihenfolge Einstellungen in PostgreSQL zu setzen.
* Regressions-Fix beim WmsLoader und image format / info format Einstellungen.
* Fix beim Delete Cascade SQL Statement in PostgreSQL, wenn eine Wms Quelle gelöscht wird.
* Fix bei Übersetzungen, wenn nur ein Platzhalter ausgegeben worden ist. Diese nehmen nun die Fallback Übersetzung (per default: Englisch)
* OSGeo Logo aktualisiert (PR #861)


**Anmerkungen zum Update:**

Bitte führen sie wieder ein **app/console doctrine:schema:update** durch, um die Keyword-Tabelle wieder zu varchar zu ändern.

.. code-block:: bash

                $ app/console doctrine:schema:update

Falls der Update Befehl fehlschlägt, z.B. mit der PostgreSQL Meldung ``SQLSTATE[22001]: String data, right truncated:`` und ``7 FEHLER:  Wert zu lang für Typ character varying(255)``, dann haben Sie einen Schlüsselwort-Eintrag in der Tabelle ``mb_core_keyword``, der 255 Zeichen überschreitet. Diesen können Sie mit folgendem SQL-Statement herausfinden:

.. code-block:: postgres

                SELECT x, id, length(x) FROM (
                  select value, id from  mb_core_keyword
                ) AS t(x) order by length desc;



Version 3.0.7.3
---------------

Release Datum: 13.07.2018

**Allgemein:**

* Ändern des Mapbender Logos und des Namens: Mapbender3 wurde der Einfachheit halber in Mapbender umbenannt und wir haben sowohl die Texte in der Dokumentation als auch die Logos augetauscht. Unsere URLs hatten wir schon auf http://mapbender.org umgestellt.
* Mapbender erwartet mindestens PHP > 5.6 zum laufenden Betrieb. PHP 7 wird empfohlen.

**Neue Funktionen:**

* QGIS Server Layerreihenfolgende, dokumentiert unter der Rubrik :ref:`layerset_de`
* Neues Element: :ref:`coordinate_utility_de`
* Mouse-Over im SearchRouter
* GPS Button im POI
* Dynamisches Laden von Legendenbildern im Legenden-Element (PR #605, PR #606)
* Anzeige eines Cookie Banners in Anwendungen. Siehe :ref:`cookieconsent_de`.

**Änderungen:**

* Die Standard-Anwendungen befinden sich nun im Verzeichnis `(application)/app/config/applications`, jede in ihrer eigenen Datei. Dazu gehören:

  * Die Mapbender Demo Map Anwendung
  * Die Mapbender Demo Map basic Anwendung
  * Die Mapbender mobile Anwendung

Weitere YAML-Anwendungen können dort hinterlegt werden.


**Verbesserungen:**

WMS Dienste und WMS Loader:

* Verbesserungen im WMS Loader und der Service Kompatibilität, dessen Logik nun dem Backend folgt
* Fix im GetLegendGraphic Request auf geschützten Diensten über den Tunnel
* Fix und Verbesserungen im URL-Signen (#590)
* Viele Verbesserungen im WMS Backend
* Fix im Instance-Tunnel zum Zugriff auf geschützte Dienste
* Fix beim Zugriff auf WMS Dienste mit undefinierten Kontaktinformationen
* Verschiedene Fixes bei Min / Max Scale Definitionen in Sublayern gegenüber dem Root-Layer
* Fix der Layerreihenfolge in PostgreSQL
* Über WMS Loader zugefügte WMS Dienste und Metadaten Anzeige. Wir können die Metadaten nicht anzeigen, werfen aber keinen Fehler mehr

Design und CSS:

* Transparenz in der Zoombar und der Toolbar angepasst für eine gleichbleibende Farbe der Schaltflächen
* Fix im Erstellen von Anwendungen und dem Hinzufügen eines Bildes

Druck:
* Fix im Druck von PNG8 Karten, wenn das Image Format "image/png; mode=8bit" ist
* Fix im Druck bei speziellen Schriftgrößen (insbesondere unter Windows bei PHP 7.1)
* Fix im Druck, wenn PHP-Notices angeschaltet sind und die yStartPosition fehlte (#555)


FOM:

* Verbesserung im FOM: Wrong Type Definition in ACL Provider Constructor #641
* Verbesserung im FOM beim SSPI


Übersetzungen:

* Verbesserung in den Übersetzungen. Danke an den Code-Sprint der FOSS4G!
* Änderung der Übersetzungen von XLIF nach YAML in den Modulen FOM und OWSProxy


Verschiedenes:

* Standardmäßig ist nun der "maximum feature count" Parameter für GetFeatureInfo Anfragen auf 1000 gesetzt
* Fix im Scale-Selector, der sich in einigen Fällen nicht aktualisieren wollte
* Fix im Aufruf von Mapbender mit POI-Parameter (#642)
* Fix im Legendenelement bei überlangen Legendenbildern (#640)
* Fix im Backend beim Hinzufügen von Elementen
* Fix eines Foreign Key Violation Fehlers in PostgreSQL, wenn einen Datenquelle gelöscht wird (PR#840)
* Einbau von Cookieconsent für Mapbender
* Dateiname Präfix für Druckausgaben geändert.



**Code-Verbesserungen:**

* Update auf Symfony 2.8 (siehe PHP Voraussetzungen)
* Einbau des Doctrine Migrations Frameworks
* Fix eines möglichen URL Signing Spoofings bei fehlenden URL Query Parametern
* Doctrine Param Coverter Definitionen (PR #645)
* WMSLayerSource: getAuthority (PR #542)
* DimensionsHandler (#610). Dieser kann in den kommenden Versionen veröffentlicht werden.
* Das Hinzufügen von Elementen im Backend konnte zu einem Fehler "Warning: usort(): Array was modified ..." führen (#586)
* Element Template und AdminType Verbesserungen (#743)
* Serialisierung der MetadataURL (#747)
* UnitTest und deren Pre-Conditions (#760)
* USort und array_multisort durch einen PHP-Bug (#586)
* Strikte SCSS Warnungen beim Kompilieren mit ruby-sass
* Fix des Wachsens in "autority" bei wiederholtem Export / Reimport / Kopieren von Anwendungen
* Bypass bei (womöglich sehr langen) WMS Loader DTD/XSD Validationen von GetCapabilities Dokumenten
* PHP 5.6 Kompatibilität bei Migrations


**Dokumentation:**

* Neues Design der Dokumentation. Wir haben diese auf das Sphinx RTD Thema umgestellt, so dass die Dokumentation auch unter mobilen Geräten leichter lesbar ist. Ein Ausdruck der einzelnen Seiten ist möglich.

* Umstrukturierung der Dokumentation: Die einzelnen :ref:`functions_de` sind unterteilt in:
  
  * :ref:`basic_de`
  * :ref:`search_de`
  * :ref:`export_de`
  * :ref:`editing_de`
  * :ref:`wmc_de`
  * :ref:`backend_de`
  * :ref:`fom_de`
  * :ref:`misc_de`

* Verbesserte Dokumentation zu den Elementen:
  
  * :ref:`basesourceswitcher_de`
  * :ref:`button_de`
  * :ref:`coordinates_display_de`
  * :ref:`html_de`
  * :ref:`legend_de`
  * :ref:`map_de`
  * :ref:`overview_de`
  * :ref:`search_router_de`
  * :ref:`srs_selector_de`
  * :ref:`zoom_bar_de`

* Dokumentation: Erweiterung zu dem :ref:`printclient` und den neuen dynamischen Features bei den Drucktemplates.

* Dokumentation: Aufnahme des MS4W Pakets zur Installation unter :ref:`installation_windows_de`. Vielen Dank an Jeff McKenna.


**Anmerkungen zum Update:**

Bitte führen sie ein **app/console doctrine:schema:update** durch, wenn Sie auf diese Version aktualisieren. Die QGIS-Layerreihenfolge benötigt eine Änderung in der Mapbender-Datenbank. Auch die 255 Zeichen für WMS-Dienste erforderten eine Änderung der Datenbank.

.. code-block:: bash

                $ app/console doctrine:schema:update


Version 3.0.7.2, 3.0.7.1 und 3.0.7.0
------------------------------------

Aufgrund von Tagging-Fehlern im Code auf Github wurden diese Versionen nie offiziell veröffentlicht. Da es nicht korrekt ist, Code zu re-taggen, führen wir die Entwicklungslinie mit Version 3.0.7.3 fort.


Version 3.0.6.3
---------------

Release Datum: 27.07.2017

**Bugfixes:**

* Regression: Koordinaten-Reihenfolge bei Anfragen an WMS 1.3.0 gefixt. Koordinatensysteme mit getauschter Axis-Orientation werden von der Karte, Druck und Export unterstützt. (#529)
* Regression: ScaleHint bei WMS Diensten korrigiert. Einige WMS Dienste mit einem Scale in den Capabilities konnten nicht in die Anwendung eingeladen werden. (#584)



Version 3.0.6.2
---------------

Release Datum: 20.07.2017

**Bugfixes:**

* Search Router: Fehler mit OpenLayers gefixt (#543)
* Search Router: Auto Close nach dem Klick in der mobilen Anwendung (#548)
* Koordinaten-Reihenfolge bei Anfragen an WMS 1.3.0 gefixt (#529)
* Druck: Darstellung von Punkten und Labels bei hochauflösendem Druck (#573, #574, #492)
* Abspeichern von WMC im WMC Editor Dialog (#577)
* ScaleHint bei Sublayern von 1:1 korrigiert (#565)
* Verbreiterung der Titel-Spalte bei Layerset-Instanzen (#559)
* Kommando, um den Imagepfad in bestehenden Map-Elementen zu aktualisieren (#530) 
* Übersetzung Drucken Schaltfläche im FeatureInfo Dialog (#552)
* Anpassungen Default-Wert "immediate" bei Messtool (#538)
* SRS: Definitionen aktualisiert (#550, #562) und YAML-Standard-Anwendungen angepasst (#561)
* Anpassungen an der Doku bei den Translations.

**Zusätzliche Update Schritte:**

**(1) Aktualisierung der EPSG-Codes**

Führen Sie nochmals den Befehl ``app/console doctrine:fixtures:load --fixtures=mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append`` aus. Es werden zwei neue Koordinatensysteme (EPSG:4839|ETRS89 / LCC Germany (N-E) und EPSG:5243|ETRS89 / LCC Germany (E-N)) der Mapbender Tabelle ``mb_core_srs`` hinzugefügt.

**(2) Aktualisierung der Parameter im Map-Control**

Führen Sie den Befehl ``app/console mapbender:upgrade:database`` aus, um den OL-ImagePath Parameter des Map-Controls anzupassen: Von ``bundles/mapbendercore/mapquery/lib/openlayers/img`` nach ``components/mapquery/lib/openlayers/img``. Das ist notwendig, falls Sie das POI-Element nutzen bzw. Mapbender mit dem poi-Parameter aufrufen und keine Sprechblase für den POI sehen. Beispiel: https://demo.mapbender.org/application/mapbender_user?poi[point]=366164%2C5623183&poi[scale]=25000&poi[label]=Please+take+a+look+at+this+POI%3A



Version 3.0.6.1
---------------

Release Datum: 24.05.2017

**Bugfixes:**

- Druck zeigte falsche Maßstäbe im Kartendisplay.
- Spezifische WMS konnten nicht gedruckt werden, wenn sie als HTTP Antwort image/pntg; charset-iso... übertragen haben.
- Backend: FOM Dialoge mit vielen Einträgen machten die Checkboxen unbenutzbar.
- config.php wieder zurück im mapbender-starter.
- Aktualisierung des bin/composer Kommandos zum Bauen von Mapbender.
- Style-Fix bei Administrations-Dialog des Basesource-Switcher.
- WmcEditor Standard Parameter für Breite und Höhe eingetragen.
- Aktualisierung Startseite Dokumentation.
- Kleine Styling Verbesserungen im Backend.
- Kleine Säuberungen des Code.



Version 3.0.6.0
---------------

Release Datum: 05.05.2017

**Architektur:**

- Systemvoraussetzung PHP: 5.5.4 oder höher
- Unterstützung von PHP 7.
- Mapbender, FOM and OWSProxy als Module ausgelagert. Sie sind nun in der composer.json eingebunden.
- Die Dokumentation ist Teil des Composers.
- Anpassungen ElementGenerator
- Ermitteln von Benutzerrollen
- Composer Einträge mit https
- Verschiedene Verbesserungen an Controllern und Bundles.
- Doctrine generate Kommandos als deprecated markiert
- Doctrine assets:dump Kommando als deprecated markiert
- Aktualisierung JOII Bibliothek
- Ablage von Symlinks zu verschiedenen Binaries im bin Verzeichnis
- Composer abgelegt im application/bin Verzeichnis
- Check in der Composer-Installation, ob die SASS Compiler Binaries ausführbar sind. Falls nicht, werden sie ausführbar gesetzt.
- Neue Composer-Kommandos zum Generieren der Dokumentation: Nur API Dokumentation generieren: bin/composer gen-api-docs
- Neue Composer-Kommandos zum Generieren der Dokumentation: Nur Benutzerdokumentation generieren: bin/composer gen-user-docs
- Verweis auf eigene Forks von open-sans, joii, compass-mixins und codemirror Bibliotheken.


**Bugfixes und Features:**

- Das Messen zeigt die Koordinaten live an, d.h. beim Bewegen der Maus werden schon jeweils die erreichten Segment- und Gesamtlängen angezeigt.
- Die Messergebnisse werden nun von oben hinzugefügt. Damit steht das aktuelle Messergebnis sichtbar an oberster Stelle und muss nicht gescrollt werden.
- Der Login Dialog (Registrierung, Password vergessen) wurde für mobile Geräte optimiert, um den Zugriff auf gesicherte mobile Anwendungen zu erleichtern.
- Neu hinzugefügte Layerset Instances sind nun nicht mehr per Default als Basesource markiert.

- Das `Copyright Element Popup <functions/misc/copyright.html>`_ kann mit einer Höhe und Breite definiert werden.

- Das Löschen von Layersets führte in einigen Fällen zu einem korrupten Map-Element und falschem Layertree

- Anpassungen und Vereinfachung der Styles des FullScreenTemplate
- Einführung der Prüfung der CSS Angaben in der Anwendungskonfiguration

- Delay beim Wechsel von Layern gefixt
- Gefixter GetMap Request bei veränderter Reihenfolge der Layer im TOC
- Fix für WMS support 1.3.0
- Fix für geschützte WMS Dienste bei GetMap, GetFeatureInfo, Print, Export und Legende
- Fix für geschützte WMS Dienste, bei denen im Username oder Passwort ein Hashzeichen vorkommt.
- Fix des WMS Parameters Exception Format bei GetMap und GetFeatureInfo Request (Github-Issue 400)
- Fixes bei den Layer-Styles im GetMap und GetFeatureInfo Request
- Default Tile Size bei der Kartenkomponente auf 512 gesetzt (war 256)
- WMS Keyword Begrenzung (war: 255 Zeichen) ist geändert. Der Spaltentyp wurde auf "text" geändert. Das Kommando app/console doctrine:schema:update ist notwendig, um die MB3-Datenbank einer Vorversion zu aktualisieren,
- Fix beim Import von YAML Anwendungen und der Erstellung von Duplikaten bei WMS Datenquellen.
- Fix bei Minimal und Maximal Scale Hint Angaben eines WMS Dienstes.

- Druck: Farbe kann bei variablen Texten eingefügt werden.
- Druck: Druck der Legende, wenn der Dienst über einen Proxy eingebaut wird.
- Druck: Dienste, die mit PNG8 registriert wurden, konnten in einigen Fällen nicht exportiert oder gedruckt werden. Die Typen image/png8 und image/png mode=24bit werden nun unterstützt.
- Druck: In einigen Fällen wurde die Legende nicht ausgegeben, wenn OWSProxy aktiviert war

- BaseSourceSwitcher: Mehrere Requests an einen WMS der auf nicht sichtbar gesetzt war, wenn der BaseSourceSwitcher als Menü angezeigt wurde.
- Überflüssige WMS Anfragen an bestimmte WMS, abhängig vom Maßstab.

- Ablage von YML-Anwendungen in application/app/config/applications: mapbender_mobile.yml, mapbender_user_basic.yml, mapbender_user.yml und Anpassungen in der WMS Version
- Administrationsoberfläche YAML Editierung und Umformatierungen nach dem Speichern (Github-Issue 350)

- Anpassungen POI-Koordinate: Transformation und SRS, Nachkommastellen
- Fix eines XSS Fehlers im POI Dialog
- Fix in POI Dialog, wenn useMailto = false

- GPS: Fehlermeldungen, wenn kein Signal und Abhängigkeit von Chrome-Browsern und https.
- GPS: Verschieben der Karte nur bei erster Positionsbestimmung.

- User-Interface: Scrollen der Dropdownliste im Backend, z.B. bei den Icons für Buttons, scrollte auch den Hintergrund.

- "Only valid" Checkbox beim `Einladen eines WMS <functions/backend/source.html>`_ ist nun standardmäßig nicht mehr aktiviert.

- Umformatierte Meldungen, wenn die Schemata eines WMS beim Hinzufügen nicht zugreifbar sind.

- Der `SearchRouter <functions/search/search_router.html>`_ zeigt, wenn er in der Sidepane eingebettet ist, die Schaltflächen Suche und Reset.

- Internet Explorer Kompatibilität: Anpassungen `Zoombar <functions/basic/zoom_bar.html>`_.
- Internet Explorer Kompatibilität: Anpassungen `OverviewMap <functions/basic/overview.html>`_.
- MS Egde Kompatibilität: Import Dialog (https://connect.microsoft.com/IE/feedback/details/1574105/microsoft-edge-file-upload-bug-build-10240-rtm)

- Verbesserung der Performance bei *einigen* Installation unter Windows durch WinCachePHP und PHP Opcache (für Details siehe `Installation unter Windows <installation/installation_windows.html>`_)

- Änderung der Systemvoraussetzungen: Für Windows ist die "Non-Thread-Safe" Variante von PHP notwendig!

- Kopieren von Anwendungen für Benutzer, die nicht root sind (ACL Application: owner, Benutzer: owner, Berechtigungen ACLs: owner, Element: owner, Gruppen: owner, Service Source: owner, spezifische Anwendung: owner)

  
**FOM und Absicherung:**

- `Anzeige von Benutzern <functions/backend/FOM/users.html>`_, die Zugriff auf ein Element in der Anwendung haben.
- Überarbeitung des Secure Elements Dialogs
- Benutzer mit der Rolle View bei Diensten dürfen Metadaten sehen und Dienste in eine Anwendung einladen.


**verschiedenes**

- Anpassung Design FeatureInfo bei Anzeige als Accordion und wenn nicht als Source angezeigt
- Verschieben von Popups innerhalb einer Anwendung
- Anpassungen WMC Edit Dialoggröße und XSS
- Fix in den Übersetzungen

- YAML basierende Anwendungen können die Sidebar anpassen: align (left/right), closed (true/false), width (px/em/%)

- Backend: Target-Feld: Leere Auswahl bei Drop-Down Feldern.
- Anpassungen WMS Scale, ScaleHint und Min/Max Werte beim Öffnen einer Layerset-Instance
- Anzeige des WMS-Titels in den Metadaten des TOC bei aktualisiertem WMS
- Anzeige des Applikations-Logos in der Konfiguration
- Anpassungen Simple Search und SearchRouter

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

- Entfernen des provide ext-ldap Statements in Composer. Die Komponenten wurden ausgelagert. Wir werden die LDAP Module in Version 3.0.7 einbauen.

- Restrukturierung von DataManager und DataSource seit der `Version 1.0.2 des data-manager <https://github.com/mapbender/data-manager/releases/tag/1.0.2>`_.


**Mobiles Template**

- Generelle Verbesserungen des Mobilen Templates
- Fix für einen Button, wenn dieser nur auf einen Link verweist.
- Fix für das Icon Label und der Schriftdicke normal
- Verbesserungen des Button Handlings allgemein
- Fix des event handlers ""on moveend"


**Digitizer**

- Update `Digitizer <functions/editing/digitizer.html>`_ auf Version 1.1.
- Druck von Multipolygonen.
- Objekte erscheinen nicht mehr im Druck, wenn Sie im Digitizer ausgeblendet worden sind.
- MinScale Einschränkung hinzugefügt
- Objekte mit einer Linienbreite von 0 werden im Druck nicht mehr sichtbar.
- Anpassungen der Close Schaltfläche: "allowCancelButton" und "allowDeleteByCancelNewGeometry".

**Form Generator:**

- Anpassungen: Hinzufügen des HTMLElement handling  für Services und  DataStore Konfiguration.

**Dokumentation**

- `FAQ <faq.html>`_ der Dokumentation hinzugefügt.
- Einführung der Contributing Guide für `Mapbender-Starter <https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md>`_ und `OWSProxy <https://github.com/mapbender/owsproxy3/blob/release/3.0.6/CONTRIBUTING.md>`_. Mapbender selbst und FOM werden folgen. Dies sind die Einstiegsdokumentationen für Entwickler und Mitwirkenden von Mapbender.
- Die Developer Dokumentation wird dort aktualisiert und aus dieser Benutzerdokumentation schrittweise überführt. Somit wird in der Zukunft diese Dokumentation hier sich mehr an die Anwender richten, während die Entwickler ihre Dokumentation direkt im Source-Code der einzelnen Module finden.
- Ausführlichere `Layertree <functions/basic/layertree.html>`_ Dokumentation

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

**app/console doctrine:schema:update**

.. code-block:: bash

                $ app/console doctrine:schema:update --dump-sql
                ALTER TABLE mb_core_keyword ALTER value TYPE TEXT;
                ALTER TABLE mb_core_keyword ALTER value DROP DEFAULT;




Version 3.0.5.3
-----------------

Release Datum: 04.02.2016

   
**Bugfixes:**

Besondere Änderungen:

- Performance: Die CSS, JavaScript und Translation Dateien werden nun im `Produktionsmodus <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_ im Symfony Cache gehalten. Dies kann insbesondere bei langsamen Servern zu Performancesteigerungen führen. Die Änderung gilt nicht für den `Entwicklermodus (app_dev.php) <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_.
- Das Paket `eslider/sassc-binaries <https://github.com/eSlider/sassc-binaries>`_ bietet nun auch einen sassc Compiler für 32-bit Linux Systeme an. Dies führte zu Anzeigeproblemen unter 32-bit Linux Systemen (http://lists.osgeo.org/pipermail/mapbender_users/2015-December/004768.html)
- Redlining: Die Inhalte des Redlining Elements sind nun sichtbar und das Element kann sowohl als Dialog als auch Element in der Sidepane verwendet werden. Siehe auch die `Dokumentation zum Redlining Element <functions/editing/redlining.html>`_. Die Scrollbar bei den Geometrie-Types im Konfigurationsdialog wird korrekt angezeigt.

Benutzer und Absicherung:
  
- Benutzer können durch Administratoren, die mindestens das ACL-Benutzerrecht "Operator" besitzen, aktiv oder inaktiv geschaltet werden. Das ist z.B. sinnvoll, wenn Benutzer, die sich selbst registriert sich selbst noch nicht aktiviert haben. Siehe die `Dokumentation zu Benutzern <functions/backend/FOM/users.html>`_.
- Texte, Übersetzungen und Styles bei der Registrierung und dem Passwort Reset wurden angepasst, ebenso die `Dokumentation dazu <functions/backend/FOM/users.html>`_

Druck und Export Image:
  
- Das `Print-Modul <functions/export/printclient.html>`_ kann nun auch in die Sidepane eingebaut werden.
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
- **Koordinatendisplay**: Das Element zur Koordinatenanzeige zeigte "null" als Text für den Präfix oder Separator, obwohl diese Felder leer sein sollten. Das Element hat weiterhin eine feste Breite bekommen, so dass das Layout im Footer stabiler wird. Der Wert kann verändert werden (Siehe die `CSS-Anpassungen zu dem Element <functions/basic/coordinates_display.html>`_).
- **SearchRouter**: Der Inhalt der Ergebnisse füllt nun das gesamte Dialogfenster aus und passt sich an die Größenänderung an. In der Sidebar wird die gesamte Höhe ausgenutzt. Der SearchRouter ist, wenn er als Dialog eingesetzt wird, `in der Höhe und Breite konfigurierbar <functions/search/search_router.html>`_.
- **ScaleSelector**: Die Breite des Elements kann mit einem `CSS-Statement verändert werden <functions/basic/scale_selector.html>`_ und ist nicht auf 155 Pixel festgelegt.
- Wenn in einer **Layerset-Instance** alle Layer auf visible=off gestellt sind, waren der Tree und die Legende nicht sichtbar.
- **POI Dialog** Verbesserungen im Styling, wenn  usemailto auf false gesetzt ist.
- **Layertree**: Anzeige der Titel nun mit einer Gesamtlänge von 40. Der Default-Wert wurde verändert. Sie können den `Parameter Titlemaxlength anpassen <functions/basic/layertree.html>`_.
- **GPS**: Verfeinerungen im GPS Tool

Allgemeine Änderungen:
  
- Bei Änderungen an Grunddaten einer Anwendung, dem Layout, den Layersets, dem CSS und der Sicherheit bleibt man nun in dem jeweiligen Reiter und springt nicht zu den Grunddaten zurück.
- Allgemeine Verbesserungen im `Digitizer Code <https://github.com/mapbender/mapbender-digitizer>`_ Version 1.0. Die Version 1.1 ist kompatibel mit Mapbender 3.0.5.3.
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

- Das Sketch Tool funktioniert nicht korrekt und wird in Zukunft in das `Redlining Tool <functions/editing/redlining.html>`_ übernommen werden.
- Karte weiterempfehlen funktioniert nicht für Facebook, Twitter und Google+.

    
    
Version 3.0.5.2
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
- Doku: FOM `UserBundle Übersetzung <functions/backend/FOM/index.html>`_ und `Ergänzung bei falschen Benutzer-Logins <functions/backend/FOM/users.html>`_.
- Doku: URL Parameter scale im `Map Element <functions/basic/map.html>`_.
- Doku: `WMC Loader <functions/wmc/wmc_loader.html>`_ und KeepSources.


**Änderungen in der config.yml:**

* Die folgenden Änderungen sind optionale Parameter für das Verhalten des Logins (siehe das `entsprechende Kapitel im FOM Bundle <functions/backend/FOM/users.html>`_):

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




Version 3.0.5.1
-----------------

Release Datum: 26.08.2015

**Neue Funktionen**: im `Kartenelement <functions/basic/map.html>`_ und beim `Druck Client <functions/export/printclient.html>`_:

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
- Verbesserte Dokumentation der `Mapbender3 Templates <customization/templates.html>`_
- Verbesserte Dokumentation des `Quickstart <quickstart.html>`_

**Known Issues:**

- Kopieren von alten 3.0.4.1 Anwendungen kopiert nicht die anzuzeigenden Layersets der Map. Bitte speichern Sie vorher das Map und Overview-Element.
- Regional Template entfernt



 
Version 3.0.5.0
-----------------

Release Datum: 01.07.2015

Übersicht der Änderungen finden Sie unter:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* **WMS neuladen:** WMS Quellen können nun neugeladen werden, wenn sich deren Strutkur geändert hat.

* **Digitalisierung:** Im Rahmen des Releases wurde das neue Element Digitizer eingeführt. Über dieses kann durch eine YAML-Definition eine Erfassungsmaske für Punkte, Linien oder Flächen aufgebaut werden. Dabei wird wie bisher PostgreSQL als Datenquelle unterstützt. Oracle und SpatiaLite sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen wie z.B. OGC WFS erweitert werden kann.

* **Druck mit Legende:** Im Druck ist es nun möglich, die Legende auf einer separaten Seite auszugeben. Die Ausgabe kann über eine Checkbox gesteuert werden.

* **Konfigurierbarer Layerbaum:** Der Layerbaum unterstützt nun mehr als ein layerset. Sie müssen das Kartenelement anpassen, um die Layersets festzulegen, die angezeigt werden sollen sowie den Layerbaum selbt. Die Dokumentation befindet sich unter `auf der Seite zum Layertree <functions/basic/layertree.html>`_.

* **Verbesserte Infoausgabe:** Die Ausgabe der Infoabfrage wurde für die neue Version verbessert. So bleiben nun die Stile der Infoabfrage erhalten. Dienste, die keine Antwort liefern, werden nicht über einen Reiter angezeigt. Es erfolgen Meldungen, wenn keine Antwort geliefert wurde.

* **Mobiles Template:** In mehreren Projektlösungen haben wir uns bereits mit einer mobilen Lösung auf Basis von Mapbender3 auseinandergesetzt. Nun wird diese Lösung als Mapbender Mobile Template in der neuen Version 3.0.5.0 zur Verfügung gestellt.   Sie finden eine neue Demo-Anwendung in der mapbender.yml mit Namen Mapbender Mobile (mapbender_mobile). Diese können Sie als Vorlage für Ihre Lösung verwenden. In der `Release-Demo <http://demo.mapbender3.org/>`_ kann die Anwendung „Mapbender Mobile“ getestet werden.

* **SASS Compiler:** Änderungen an der Architektur bezüglich des SASS Compilers führen zu einer performanteren Oberfläche.

* **Vendor Specific Parameter:** Eine WMS Layer Instanz unterstützt nun die Angabe von Vendor Specific Parametern, die an einen WMS Request angehangen werden. Die Werte können fest vergeben werden oder auf die User- und Gruppeninformation des angemeldeten Benutzers zurückgreifen. Dokumentation ist unter dem Abschnitt `Vendor Specific Parameters <quickstart.html#konfiguration-von-diensten>`_ verfügbar.

* **Formular-Builder:** In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden. Hierbei wurde sich an den Möglichkeiten, die in Mapbender 2.x zur Verfügung stehen, orientiert.

* **Neue Schaltflächen:** Einige Schaltflächen basieren auf einer neuen Schriftart, die alten Schaltflächen sind noch mit dem Namen FontAwesome verfügbar.

* **URL Parameter:** Mapbender3 kann mit Startparametern aufgerufen werden. Eine Liste der Parameter findet sich in der Dokumentation zu den `URL Parametern <functions/basic/map.html#kontrolle-uber-den-aufruf>`_.

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
                    

Version 3.0.4.1
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
 

Version 3.0.4.0
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
 

Version 3.0.3
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
 

Version 3.0.2
---------------

Release Datum: 27-11-2013
Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=6

* Such-Router für SQL-Suchen
* WMC Editor und Loader
* WMSLoader Erweiterung WMS über Link hinzufügen
 

Version 3.0.1
---------------

Release Datum: 06-09-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=5

* Kopieren einer Anwendung mit Diensten
* Popup - draggable
* PrintClient Erweiterung Druck EPSG 4326, neue Drucklayouts, Druck A4-A0
* Abfangen von fehlerhaften Anmeldungen zum Abwenden von brute force login Versuchen
* Bug fixes
 

Version 3.0.0.2
-----------------

Bugfix-Release Datum: 19-07-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=4

 

Version 3.0.0.1
-----------------

Bugfix-Release Datum: 07-06-2013

Übersicht der Tickets finden Sie unter: https://github.com/mapbender/mapbender/issues?milestone=3

 

Version 3.0.0.0
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
* Dokumentation unter http://doc.mapbender.org
