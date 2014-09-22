.. _map:

Map (Karte)
***********************

MapQuery/OpenLayers basierte Karte.
Es müssen die Einheiten, der Start und der Max Bereich (extent), die Maßstäbe und die unterstützten Projektionen angegeben werden.

.. image:: ../../../../../figures/map.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/map_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   layerset: null             # verweist auf ein Layerset, definiert zuerst das layerset und verweist darauf
   dpi: 72                    # Auflösung, Standard ist 72
   srs: "EPSG:4326"           # Koordinatenbezugssystem. Zwei Arten der SRS Definition werden unterstützt:
                                - "EPSG:CODE" oder
                                - "EPSG:CODE|MEIN SRS TITEL"
   units: "degrees"           # Einheiten in Grad oder Meter, Standard ist "degrees" (Grad)
   extents: array(
       max: array(0, 40, 20, 60) 
       start: array(5, 45, 15, 55)) # Kartenbereich (extent)
   scales: "25000000,10000000,5000000,1000000,500000" # eine CSV-Liste für den Maßstab
   maxResolution: "auto"      # Auflösung, im Moment wird nur auto unterstützt, bitte ändern Sie es nicht.
   otherSrs: array(
      "EPSG:31466",
      "EPSG:31467",
      "EPSG:25832")           # andere Koordinatenbezugssystem. Zwei Arten der SRS Definition werden unterstützt:
                                - ["EPSG:CODE","EPSG:CODE"] or
                                - ["EPSG:CODE|MEIN SRS TITEL","EPSG:CODE|MEIN SRS TITEL"]
   imgPath: "bundles/mapbendercore/mapquery/lib/openlayers/img"   # Pfad der Bilder (images)

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\Map
* Widget: , mapquery//lib//openlayers//OpenLayers.js, mapquery//lib//jquery//jquery.tmpl.js, mapquery//src//jquery.mapquery.core.js, proj4js//proj4js-compressed.js, mapbender.element.map.js
* Style: mapbender.elements.css, mapquery//lib//openlayers//theme//default//style.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

center
----------
<>

highlight
----------
<>

layer
----------
<>


appendLayer
--------------------
<>


insert
----------
<>


rebuildStacking
--------------------
<>

move
----------
Bewegt den Layer nach oben (direction == true) oder nach unten (direction == false) im gleichen Level in der Layerhirarchie.

zoomIn
----------
<>

zoomOut
----------
<>

zoomToFullExtent
--------------------
<>

zoomToScale
--------------------
<>

panMode
----------
<>

addPopup
----------
<>

removePopup
--------------------
<>

removeById
----------
<>

layerById
----------
Sucht nach einem MapQuery Layer mit der Mapbender ID. Gibt einen Layer zurück oder Null, wenn kein Layer gefunden wird.

scales
----------
<>

setMapProjection
--------------------
<>

getAllSrs
----------
<>

ready
----------
<>


JavaScript Signals
==================

Keine.


Kontrolle über den Aufruf
=====================================

Ebenen sichtbar machen
------------------------

Sie können die ID der Ebene mit der ID <layerid> und des Dienstes <serviceid> in der URL als parameter übergeben, um einen Layer in der Startansicht zu aktivieren.

.. codeblock
  ?visiblelayers=<serviceid>/<layerid>

Es können mehrere Layer Komma separiert übergeben werden.

Punkte übergeben
------------------------

Sie können einen oder mehrere Punkte in der URL übergeben. Jeder Punkt verfügt dabei über die folgenden Parameter:

- Punkt (point): Koordinatenpaar, die Werte werden mit Komma getrennt (zwingend)
- Beschriftung (label): Beschriftung, die angezeigt werden soll (optional)
- Maßstab (scale): Maßstab, in dem der Punkt angezeigt werden soll (optional. Die Angabe ist nur bei der Anzeige eines Punktes sinnvoll)

Wenn Sie mehr als einen Punkt im Aufruf übergeben, zoomt die Karte auf 150% der Gesamt-Boundingbox.

Format für die Übergabe eines Punktes:

   ?poi[point]=363374,5621936&po[label]=Label&poi[scale]=5000

Für die Übergabe vieler Punkte wird das folgende Format verwendet:

   ?poi[0][point]=363374,5621936&poi[0][label]=Label%201&poi[1][point]=366761,5623022&poi[1][label]=Label%202

Rechteck (BBOX) übergeben
------------------------------------------------

Es kann ein Rechteck (BBOX) beim Start übergeben werden. Es wird dann auf dieses Rechteck gezoomt. Der Aufruf sieht wie folgt aus:

   ?bbox=364286,5622263,365979,5622806
