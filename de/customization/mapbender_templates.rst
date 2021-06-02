.. _mapbender_templates_de:

Mapbender Templates
#####################

Ein Mapbender Template bestimmt die grundlegende Darstellung (Farbe, Schrift etc.) einer Anwendung. Es definiert außerdem die Bereiche (z.B. Toolbar oder Sidepane), in welche neue Elemente eingefügt werden können.

Es werden insgesamt drei Mapbender Templates bei der Installation mitgeliefert:

* Fullscreen Template
* Basis Template (Fullscreen ohne Sidepane)
* Mobiles Template

Fullscreen Template
*******************

.. image:: ../../figures/mapbender_fullscreen.png
     :scale: 50

Schauen Sie sich die Demo zum Mapbender Fullscreen an: https://demo.mapbender.org/application/mapbender_user_yml

Regionen des Fullscreen Templates:

  * Toolbar (Bereich für die Platzierung von Buttons)
  * Sidepane (Seitenleiste für den Ebenenbaum, Legende, Suche,...)
  * Content (Karte, Maßstabsleiste,...)
  * Footer (Fußleiste mit Impressum, Aktivitätsanzeige...)

Besonderheiten:

  * Template mit dunklem Hintergrund
  * Großansicht mit konfigurierbarer Sidepane:
  
Sidepane-Konfigurationsmöglichkeiten
************************************

Das Fullscreen Template bietet eine vielseitig konfigurierbare Sidepane an.
Die Ansichtsoptionen für die Sidepane können im Sidepane-Bereich im Mapbender-Backend ausgewählt werden. Dazu genügt ein Klick auf das Einstellungszahnrad.
Im Anschluss können folgende Optionen konfiguriert werden:

 * Typ
 * Bildschirmtyp
 * Breite (in Pixeln)
 * Position
 * Checkbox "Geschlossen starten"


.. image:: ../../figures/de/sidepane_backend.png
     :scale: 80


Die Option "Typ" zeigt die Sidepane-Elemente in unterschiedlichen Ansichten an:

- "Akkordeon" zeigt alle hinzugefügten Elemente in Reitern:

.. image:: ../../figures/de/sidepane_accordion.png
     :scale: 80

- "Buttons" zeigt alle hinzugefügten Elemente über Buttons:

.. image:: ../../figures/de/sidepane_buttons.png
     :scale: 80

- "Unformatiert" verzichtet auf Styling-Optionen und zeigt die Elemente direkt und in der im Backend gewählten Reihenfolge untereinander an:

.. image:: ../../figures/de/sidepane_nostyle.png
     :scale: 80

Die Option "Bildschirmtyp" legt fest, für welche Geräteart (Alle, Mobil oder Desktop) die Sidepane angezeigt werden soll.

Über die Option "Breite" kann ein Pixelwert definiert werden, der die Breite der Sidepane in der Anwendung verändert.

Die Position gibt an, ob die Sidepane am linken oder rechten Bildschirmrand angezeigt wird.

Die Checkbox "Geschlossen starten" hält nach Aktivierung die Sidepane bei Anwendungsstart eingeklappt. Sie ist über den einen Button in der Anwendung nachträglich aus- & erneut einklappbar.

Mobiles Template
****************

.. image:: ../../figures/mapbender_mobile.png
     :scale: 80

Schauen Sie sich die Demo zum Mapbender Mobile Template an: https://demo.mapbender.org/application/mapbender_mobile_yml


Regionen des Mobile Templates

  * footer (Bereich für die Platzierung von Buttons)
  * Content (map, navigation toolbar)
  * Mobilepane (Bereich, der über der Karte eingeblendet wird, wenn sich Dialoge wie Themenauswahl, Hintergrundwechsel oder Infoabfrage öffnen)


Bitte beachten Sie, dass derzeit nicht alle Elemente im Mobilen Template verwendet werden können. Die folgende Liste führt die Element auf, die verwendet werden können:

  * Map
  * GPS-Position
  * Layertree (anderes Design, nur der root-Layer-Titel eines Services wird angezeigt, Dienst können nur komplett de-/aktiviert werden)
  * BaseSourceSwitcher (anderes Design: Anzeige als Liste nicht als Buttons)
  * FeatureInfo
  * Navigation Toolbar (Zoombar)
  * HTML
  * Button
  * SimpleSearch
