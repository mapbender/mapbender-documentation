.. _map:

Map
***

MapQuery/OpenLayers based map.
You have to define units, start and max. extent, scales and supported projections.

.. image:: ../../../figures/map.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/map_dialog.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Layersets:** Refers to a layerset. Define the layerset first and refer to it.
* **DPI:** Resolution, default is 72.
* **SRS:** Spatial reference system. Two ways of SRS definitions are supported: EPSG: CODE or EPSG:CODE|MY SRS TITLE.
* **Tile size:** Size of the tiles of tiled WMS services.
* **Max. Extent:** Maximal map extent, defined by BBOX parameters.
* **Start Extent:** Map extent that is visible at application launch. Defined by BBOX parameters.
* **Scales (csv):** a csv scale list. These scales will be supported in your application if you zoom (e.g. via mouse wheel)
* **Other SRS:** Other spatial reference systems. Two SRS definitions are supported: EPSG: CODE or EPSG:CODE|MY SRS TITLE.


Configuration example
=====================

The main map element is included in the content section of the application menu. A map element can be added with the ``+`` -button.

.. image:: ../../../figures/add_content.png
     :scale: 80

All layersets can be included in the main map element if they are set in the layersets tab in the application backend beforehand. For this example, those are the following:

.. image:: ../../../figures/map_example_layersets.png
     :scale: 80

The layersets are visible in the configuration dialog in the *Layersets* (1) section. It is possible to multi-select the desired layers. Unchecked layersets can be used in the overview element (as a overview map) later on.

.. image:: ../../../figures/map_example_dialog.png
     :scale: 80

The field *SRS* (2) defines the coordinate reference system that is used at application launch. In this example, the coordinate reference system ETRS89 / UTM Zone 32N was chosen. The affiliated ESPG-code is 25832. If the application should support other coordinate systems, simply add those in the *Other SRS* (6) field (enter the EPSG code). It is possible to enter several comma-separated codes. In this example, the following codes are used: 25833 (ETRS89 / UTM Zone 33N), 31466 (DHDN / 3-degree Gauss-Krüger Zone 2), 31467 (DHDN / 3-degree Gauss-Krüger Zone 3), 3857 (WGS 84 / Pseudo-Mercator) and 4326 (WGS 84). Switching between the registered coordinate systems works with the element "SRS Selector". To get more details on the SRS selector, visit :ref:`scale_selector`.

The field *max. Extent* (3) states the max. zoomable extent of the map application. If there is data outside of the extent, it cannot be seen by the frontend user. The field *start Extent* (4) refers to the extent of the map that is visible when the application is launched in the browser (in the example the city of Bonn).

The field *scales (csv)* (5) defines the scales that are usable in the application. This element can come handy if the user should e.g. see the map, but not too many details of it (just define no possibility to zoom closer than 1:10000). Moreover, it is possible to switch between the defined SRS's with the element scale selector. For further details, view :ref:`scale_selector`. Alternatively, this can be realized with the navigation toolbar element.
For further integrational details see :ref:`zoom_bar`.


YAML-Definition:
----------------

.. code-block:: yaml

   layerset: null             # refer to a layerset, define the layerset first and refer to it
   dpi: 72                    # resolution, default is 72
   srs: "EPSG:4326"           # coordinate reference system. Two ways of srs definitions are supported:
                                - "EPSG:CODE" or
                                - "EPSG:CODE|MY SRS TITLE"
   units: "degrees"           # units to use degrees/meters, default is degrees
   extents:
       max: [0, 40, 20, 60]    # maximal map extents
       start: [5, 45, 15, 55]  # map extents for the start of the application
   scales: "25000000,10000000,5000000,1000000,500000" # a csv scale list
   otherSrs:
       - EPSG:31466
       - EPSG:31467
       - EPSG:25832          # other coordinate reference systems. Two srs definitions are supported:
                                - ["EPSG:CODE","EPSG:CODE"] or
                                - ["EPSG:CODE|MY SRS TITLE","EPSG:CODE|MY SRS TITLE"]
   tileSize: 256             # size of tiles



Controlling by URL-parameters
=============================

Make Layer visible
------------------

If you have a layer with the id <layerid> in a service with the id <serviceid>, you may pass the URL parameter
visiblelayers to turn the layer visible:


.. code-block:: php

  ?visiblelayers=<serviceid>/<layerid>


You may also pass multiple layers separated by comma.

The layerid and serviceid values are specific to an application. You can get
the layerid and serviceid in the specific application, namely in the
layerset and there in a layer. Each layer has an icon with three small dots
on the right side. Click on the icon and a popup window will appear.

.. image:: ../../../figures/wms_instance_layer_id.png
     :scale: 80

The first value lists the internal SourceID and SourceLayerId (31-591). The
seconds value lists the InstanceID and InstanceLayerId that we want to use
now (73-836).

Use this values for the "visibleLayers" parameter in your URL, and seperate them by a slash.

For example: http://localhost/mapbender/application/myapp?visiblelayers=73/836

If you have two layers that are not visible by default, put the two values
of layerid and serviceid into the URL and seperate them by a comma.

For example: http://localhost/mapbender/application/myapp?visiblelayers=73/836,73/840




Passing POIs
------------

You can pass one or more POIs in the URL. Each POI has the following parameters:

- point: coordinate pair with values separated by comma (mandatory)
- label: Label to display (optional)
- scale: Scale to show POI in (optional, makes only sense with one POI)

If you pass more than one POI, the map will zoom to 150% of the POIs bounding.

To pass a single POI, use the following URL format:

.. code-block:: php

   ?poi[point]=363374,5621936&poi[label]=Label&poi[scale]=5000


To pass multiple POIs, use the following format:

.. code-block:: php

   ?poi[0][point]=363374,5621936&poi[0][label]=Label%201&poi[1][point]=366761,5623022&poi[1][label]=Label%202


Passing BBOX
------------

You can pass a BBOX to zoom to by using the following URL query parameter:

.. code-block:: php

   ?bbox=364286,5622263,365979,5622806


Passing the scale
-----------------

You can set the scale from the list of available scales.

.. code-block:: php

   ?scale=1000


Passing SRS
-----------

You can pass a favorite EPSG code you want to use on start of the application by URL query parameter:

.. code-block:: php

   ?srs=EPSG:4326


Passing Center
--------------

You can pass a coordinate. The application will open and display the coordinate in the center. In this case, you also have to set the SRS.

.. code-block:: php

   ?center=364286,5622263


More Start Parameters
---------------------

The elements WMS Loader and WMC Loader also provide parameters you can use on start. Have a look at the element descriptions for further information.



Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\Map
* **Widget:** mapbender.element.map.js
