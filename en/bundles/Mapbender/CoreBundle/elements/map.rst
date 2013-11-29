.. _map:

Map
***********************

MapQuery/OpenLayers based map. You have to define the units, the start and max extent, scales and supported projections.

.. image:: ../../../../../figures/map.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/map_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   layerset: null             # refer to a layerset, define the layerset first and refer to it
   dpi: 72                    # resolution, default is 72
   srs: "EPSG:4326"           # coordinate reference system. Two ways of srs definitions are supported:
                                - "EPSG:CODE" or
                                - "EPSG:CODE|MY SRS TITLE"
   units: "degrees"           # units to use degrees/meters, default is deegrees
   extents: array(
       max: array(0, 40, 20, 60)
       start: array(5, 45, 15, 55)) # map extents
   scales: "25000000,10000000,5000000,1000000,500000" # a csv scale list
   maxResolution: "auto"      # at the moment only auto is supported, so please do not change
   otherSrs: array(
      "EPSG:31466",
      "EPSG:31467",
      "EPSG:25832")           # other coordinate reference systems. Two srs definitions are supported:
                                - ["EPSG:CODE","EPSG:CODE"] or
                                - ["EPSG:CODE|MY SRS TITLE","EPSG:CODE|MY SRS TITLE"]
   imgPath: "bundles/mapbendercore/mapquery/lib/openlayers/img"   # path of images

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Map
* Widget: , mapquery//lib//openlayers//OpenLayers.js, mapquery//lib//jquery//jquery.tmpl.js, mapquery//src//jquery.mapquery.core.js, proj4js//proj4js-compressed.js, mapbender.element.map.js
* Style: mapbender.elements.css, mapquery//lib//openlayers//theme//default//style.css

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
Searches for a MapQuery layer by its Mapbender id. Returns the layer or null if not found.

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

Controlling by URL
==================

Make Layer visible
------------------

If you have a Layer with the id <layerid> in a service with the id <serviceid> you may pass the URL parameter
visiblelayers to turn the layer visible:


.. codeblock
  ?visiblelayers=<serviceid>/<layerid>

You may pass multiple such layers, seperated by comma.

Passing POIs
------------

You can pass one or more POIs in the URL. Each POI has the following parameters:

- point: coordinate pair with values separated by comma (mandatory)
- label: Label to display (optional)
- scale: Scale to show POI in (optional, makes only sense with one POI)

If you pass more than one POI, the map will zoom to 150% of the POIs bounding.

To pass a single POI, use the following URL format:

   ?poi[point]=363374,5621936&po[label]=Label&poi[scale]=5000

To pass multiple POIs, use the following format:

   ?poi[0][point]=363374,5621936&poi[0][label]=Label%201&poi[1][point]=366761,5623022&poi[1][label]=Label%202

Passing BBOX
------------

You can pass a BBOX to zoom to by using the following URL query parameter:

   ?bbox=364286,5622263,365979,5622806
