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
==============

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
----------
<>


insert
----------
<>


rebuildStacking
----------
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
----------
<>

zoomToScale
----------
<>

panMode
----------
<>

addPopup
----------
<>

removePopup
----------
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
----------
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
