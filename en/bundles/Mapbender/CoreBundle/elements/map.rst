.. _map:

Map
***********************

MapQuery/OpenLayers based map

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Map
* Widget: , mapquery//lib//openlayers//OpenLayers.js, mapquery//lib//jquery//jquery.tmpl.js, mapquery//src//jquery.mapquery.core.js, proj4js//proj4js-compressed.js, mapbender.element.map.js
* Style: mapbender.elements.css, mapquery//lib//openlayers//theme//default//style.css

Configuration
=============

.. code-block:: yaml

   layerset: null      # main
   dpi: 72             #
   srs: "EPSG:4326"    #
   otherSrs: "EPSG:31466,EPSG:31467,EPSG:25832" #
   units: "degrees"    # units to use deegrees/meters
   extents: array(
       max: array(0, 40, 20, 60) 
       start: array(5, 45, 15, 55)) #
   maxResolution: "auto" #
   scales: "25000000,10000000,5000000,1000000,500000" # 
   imgPath: "bundles/mapbendercore/mapquery/lib/openlayers/img" #

HTTP Callbacks
==============

None.

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
Moves a layer up (direction == true) or down (direction == false) on the same level in the layer hierarchy.

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
Searches for a MapQuery layer by it's Mapbender id. Returns the layer or null if not found.

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

None.
