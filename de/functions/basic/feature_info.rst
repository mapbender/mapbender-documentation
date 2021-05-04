.. _feature_info_de:

FeatureInfo (Information)
*************************

Mit diesem Element können Sie Informationen eines WMS abfragen. In der folgenden Abbildung sehen Sie ein Beispiel für eine solche Informationsabfrage. Es wurde hierfür der WMS "Krankenhäuser NRW" (http://www.wms.nrw.de/wms/krankenhaus?) vom Ministerium für Gesundheit, Emanzipation, Pflege und Alter NRW verwendet.

.. image:: ../../../figures/de/feature_info.png
     :scale: 80
     
Konfiguration
=============

Das Element FeatureInfo wird im Content eingebunden:


.. image:: ../../../figures/de/feature_info_content.png
     :scale: 80

.. image:: ../../../figures/de/feature_info_configuration.png
     :scale: 80



* **Automatisches Öffnen (Autoopen):** Schaltet ein/aus, ob das Informationsfenster beim Start der Anwendung automatisch geöffnet werden soll (Default: false).
* **Beim Schließen deaktivieren:** Steuert, ob das FeatureInfo beim Schließen des Ergebnisfensters deaktiviert wird oder nicht.
* **Print Result:** Anzeige eines Links, über den die abgefragten Daten ausgedruckt werden können (Default:false). 
* **Nur valide zeigen** Anzeige von validen WMS
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Target:** ID des Kartenelements, auf das sich das Element bezieht.
* **Display type:** Anzeige der Information als Tabs oder in Accordionform (Default: tabs).
* **Max count:** Maximale Anzahl an Treffern/Ergebnissen, die angezeigt werden soll.
* **Width/Height:** Größe des Dialogfeldes (Breite und Höhe in Pixel).
* **Highlighting aktiv** Aktivierung des FeatureInfo Highlightings 
* **Grundfarbe** Farbe mit der ausgewählte Geometrien hervogehoben werden
* **Hover-Farbe** Farbe mit der ausgewählte Geometrien hervogehoben werden, wenn man darüber hovert

Für das Element wird zudem ein Button benötigt. Zu der Konfiguration des Buttons besuchen sie die Dokumentationsseite unter `Button <../misc/button.html>`_.

Einstellungen im Layertree
---------------------------

Layer "Krankenhäuser NRW" ist sichtbar und FeatureInfo-Abfrage für den Layer aktiviert:

.. image:: ../../../figures/de/feature_info_on.png
     :scale: 80

Layer "Krankenhäuser NRW" ist sichtbar und FeatureInfo-Abfrage für den Layer deaktiviert:

.. image:: ../../../figures/de/feature_info_off.png
     :scale: 80

Layer "Krankenhäuser NRW" ist nicht sichtbar, es erfolgt zusätzlich keine FeatureInfo-Abfrage, auch wenn diese aktiviert ist:

.. image:: ../../../figures/de/feature_info_on_layer_invisible.png
     :scale: 80
     

Anzeige als Tabs und Accordion
------------------------------

Mit dem Schalter "Type" können die Responses mehrerer Dienste in unterschiedlichen Tabs oder als Accordion angezeigt werden.

Beispiel Tabs:

.. image:: ../../../figures/de/feature_info_tabs.png
     :scale: 80

Beispiel Accordion:

.. image:: ../../../figures/de/feature_info_accordion.png
     :scale: 80



Ausdruck der Resultate
----------------------

Mit dem Schalter "Print result" kann die Information des FeatureInfo ausgedruckt werden. Eine Druckschaltfläche ist dann in dem FeatureInfo-Dialog sichtbar. Das Drucken geschieht über den Druckdialog des Webbrowsers.

Um alle Bilder und Hintergrundfarben im Ausdruck zu erhalten, sollten Sie die Druckeinstellungen des Webbrowsers beachten: In Firefox kann man die Option "Hintergrund drucken" im Druckoptionendialog anschalten, in Chrome-basierten Browsern nennt sich die Option "Hintergrundgrafiken". Die übermittelten Schriften können bei einem Ausdruck in PDF je nach Viewer unterschiedlich gut funktionieren. Des Weiteren modifizieren die meisten Browser Webseiten etwas vor dem Druck, damit nicht so viel Tinte/Toner verbraucht wird.


FeatureInfo Highlighting
------------------------

Ab Mapbender 3.2.3 können einzelne Geometrien eines WMS über die Infoabfrage farblich in der Karte hervorgehoben werden. Dies ist besonders bei der Arbeit mit umfangreichen WMS hilfreich, da somit einzelne Geometrien leichter zugeordnet werden können.

Eine Infoabfrage mit aktiviertem FeatureInfo Highlighting könnte beispielsweise folgendermaßen aussehen:

.. image:: ../../../figures/de/feature_info_highlighting.png
     :scale: 80

In der vorherigen Abbildung wurden mehrere Geometrien in der Karte ausgewählt (PLZ: 53111, 53113 und 53115). Der FeatureInfo Dialog zeigt nur die Informationen dieser Geometrien an. Die Fläche mit der PLZ 53115 wird durch Hovering rot in der Karte markiert.  

Zur Aktivierung von FeatureInfo Highlighting, navigieren Sie zu Ihrem FeatureInfo-Element im Content-Bereich. Hier können Sie das Highlighting aktivieren, sowie Grund- und Hoverfarbe setzen.

Weiterhin muss die HTML-Ausgabe der Infoabfrage angepasst werden. Hierfür ist es notwendig, dass die Geometrieabfrage versteckt als WKT in ein HTML-div erfolgt. Diese wird nicht angezeigt. Zusätzlich muss der EPSG-Code übergeben und eine eindeutige ID in dem HTML-div vorliegen.
Mapbender wertet diese Informationen aus und stellt die Geometrien in der Karte dar. Beim Mouse-Over auf den Treffern des Infofensters wird die dazugehörige Geometrie entsprechend hervorgehoben. Je nachdem welche WMS-Server-Software Sie nutzen, sieht die Anpassung unterschiedlich aus. Anpassungen können für MapServer, QGIS Server, GeoServer problemlos erfolgen.

Die notwendige Anpassung wird hier am Beispiel von MapServer gezeigt. In der DATA-Angabe wird zusätzlich die Geometrie als WKT ausgegeben. Außerdem wird das FeatureInfo-Template angepasst.Wird nun ein WMS über GetFeatureInfo abgefragt, werden die entsprechenden Flächen in der Karte hervorgehoben. 

.. code-block:: console

DATA "geom from (Select *, ST_AsText(geom) as geom_wkt from plz) as foo USING UNIQUE gid USING SRID 4326"

<div class="geometryElement" id="[gid]" data-geometry="[geom_wkt]" data-srid="EPSG:4326">
  <table>
	...
  <table>
</div>



YAML-Definition:
----------------

.. code-block:: yaml

   title: FeatureInfo      # Titel des Elements
   tooltip: Feature Info   # Text des Tooltips
   type: dialog            # Default und mandatory: dialog.
   target: map             # ID des Kartenelements
   autoActivate: false     # true, wenn die Infoabfrage beim Start der Anwendung geöffnet wird, der Standardwert ist false.
   deactivateOnClose: true # true/false um die Funktion nach dem Schließen des Ergebnisfensters zu deaktivieren, der Standardwert ist true
   onlyValid: false        # Korrekte HTML Ausgabe erfordern. Standardwert ist false.
   printResult: false      # Anzeige eines Links, über den die Infoabfrage ausgedruckt werden kann. Standardwert ist false.
   showOriginal: false     # Der Original css-Stil des Ergebnisses wird angezeigt. Standardwert ist false.
   displayType: tabs       # tabs/accordion Default: tabs
   width: 700              # Breite des Dialogs in Pixel, Standardwert: 700
   height: 500             # Höhe des Dialog in Pixel, Standardwert: 500



Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\FeatureInfo
* **Widget:** mapbender.element.featureInfo.js
* **Style:** mapbender.elements.css
