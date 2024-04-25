.. _map:

Map
***
The map is the central element of a Mapbender application. It is based on OpenLayers and has be integrated into the Map area of the :ref:`backend`.

.. image:: ../../../figures/map.png
     :width: 75%

Configuration
=============

.. image:: ../../../figures/map_dialog.png
     :width: 50%

* **Title:** Title of the element. It will be listed in the :ref:`layouts` section.
* **Layersets:** Select which :ref:`layerset` will be displayed on the map. Their order is changeable via drag & drop.
* **Tile size:** Size of the tiles of tiled WMS services.
* **SRS:** Spatial reference system. Two ways of SRS definitions are supported: EPSG:CODE or EPSG:CODE|MY SRS TITLE. If you do not enable a custom SRS title, the default title for each SRS from the *mb_core_srs* table is used.
* **Max. Extent:** Maximal map extent, defined by BBOX parameters. This rectangle defines the possible map extent. In response to clicking the globe icon in the :ref:`navigation_toolbar`, the map view will zoom out to this extent.
* **Start Extent:** Map extent that is visible at application launch, defined by BBOX parameters. This rectangle defines the start map extent. In response to clicking the home icon in the :ref:`navigation_toolbar`, the map view will zoom to this extent.
* **Default resolution [dpi]**: The default resolution adapts to the screen resolution based on the configured value in dpi. Default: 96 dpi.
* **Fixed zoom steps:** This option activates a zoom behaviour with fixed scales. This is useful to increase visual quality of services that are cached on very particular resolution steps only. When set true, scale denominator snaps to one of the values given in the *scales* option as defined below (default: false).
* **Scales (csv):** A csv scale list. These scales will be supported in your application if you zoom (e.g. via mouse wheel)
* **Other SRS:** Other spatial reference systems. Two SRS definitions are supported: EPSG:CODE or EPSG:CODE|MY SRS TITLE.


Configuration example
=====================

The map element has to be included into the Map area:

.. image:: ../../../figures/add_map_area.png
     :scale: 80

The map can entail all instances that are defined in the layerset. The following example distinguishes between a *main* (1) and *overview* (2) layerset.

.. image:: ../../../figures/map_example_layersets.png
     :width: 100%

In order to display all *Layersets* on the map, they have to be activated. Multiple selections are possible as well. De-selected layersets can function as an :ref:`overview`. In the example, *main* is displayed on the main map and *overview* as an overview map.

The field *SRS* defines the coordinate reference system that is used at application start. In this example, the coordinate reference system EPSG:25832 or ETRS89/UTM Zone 32N was chosen. If the application should support other coordinate systems, simply add those in the *Other SRS* field. In this example, the following codes are used: EPSG:25833 (ETRS89/UTM Zone 33N), EPSG:31466 (DHDN/3-degree Gauss-Kruger Zone 2), EPSG:31467 (DHDN/3-degree Gauss-Kruger Zone 3), EPSG:3857 (WGS 84/Pseudo-Mercator) and EPSG:4326 (WGS 84).

The field *max. Extent* states the maximum zoomable extent of the map application. If there is data outside of the extent, it will not appear in the map. The field *start Extent* refers to the extent of the map that is visible when the application is started in the browser (in this example: the city of Bonn).

The *Default resolution* in dpi defines the resolution of the device being used; the corresponding default value of 96 dpi can be adjusted through this field. If the displayed resolution of the map does not match that of the WMS service, changing this value can help to align the map accordingly.

.. note:: The scale-dependent resolution currently only works reliably on desktops with regular resolution.

Furthermore, the field *scales (csv)* defines the scales that are usable in the application. It is possible to switch between the defined scales with :ref:`scale_selector` or :ref:`navigation_toolbar`. *Fixed zoom steps* were deactivated in the example. That means it is possible to display undefined zoom levels via mouse scrolling.
     

YAML-Definition
---------------

This template can be used to include the map into a YAML application.

.. code-block:: yaml

   layerset: null             # refer to a layerset, define the layerset first and refer to it
   srs: "EPSG:4326"           # coordinate reference system. Two ways of srs definitions are supported:
                                - "EPSG:CODE" or
                                - "EPSG:CODE|MY SRS TITLE"
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



Controlling URL parameters
==========================

.. _layer_activation:

Activating Layers
-----------------

Mapbender enables the option of activating layers when an application is started via ``visiblelayers``. Activation is possible either via `ID` or `Name`.

* **ID**: <InstanceID>/<InstanceLayerID>
* **Name**: <RootLayerName>/<LayerName>

**InstanceID/InstanceLayerID**: This allows a transmission of the application-specific values of InstanceID and InstanceLayerID:

.. code-block:: php

  ?visiblelayers=<InstanceID>/<InstanceLayerID>

**RootLayerName/LayerName**: This allows layers along the combination of RootLayerNamename and LayerName to be transferred as parameters:

.. code-block:: php

  ?visiblelayers=<RootLayerName>/<LayerName>

.. hint:: Please note that the IDs change after every refresh of the service. Passing the name may therefore be the more constant solution.

To display the attribute values, there is an icon with three dots next to each layer in the layerset tab of an application.
Click on the icon to open a info window:

.. image:: ../../../figures/layerset/layerset_instance_dotmenu.png
     :scale: 80

* **ID**: The first value in the upper text field is the internal `SourceID` and the `SourceLayerID` (3-15). The second value in the upper text field is the `InstanceID` and the `InstanceLayerID` (4-79).
* **Layer's Name**: The second text field contains the `LayerName`. The output of the first line will instead pass the `RootLayerName`.
* **Style**: Styling alternatives can be selected in the third drop-down field (if available).

For an Instance(Layer)ID transfer, use the *second* value combination after the slash for the ``visiblelayers`` parameter in the URL.
Separate the two associated values with a slash (instead of a hyphen):

For example: ``https://localhost/mapbender/application/myapp?visiblelayers=4/79``

Separate two or more non-visible layers by commas. To do this, insert the respective attribute values according to the same scheme:

For example: ``https://localhost/mapbender/application/myapp?visiblelayers=4/79,1/42``

Combinations of names and ID values are also possible:

``https://localhost/mapbender/application/myapp?visiblelayers=Mapbender/Mapbender_Names,Mapbender/Mapbender_User,39/149``


Passing POIs
------------

You can pass a POI in the URL. A POI has the following parameters:

- point: coordinate pair as comma-separated values (mandatory),
- label: Label to display (optional),
- scale: Scale to show POI in (optional).

To pass a POI, use the following URL format:

.. code-block:: php
   
   ?poi[point]=368777,5619411&poi[label]=Rheinaue&poi[scale]=10000


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


Passing a centered Coordinate
-----------------------------

You can pass a coordinate. The application will open and display the coordinate in the center.

.. code-block:: php

   ?center=364286,5622263


More Start Parameters
---------------------

The elements WMS Loader and WMC Loader also provide parameters you can use on start. Have a look at the element descriptions for further information.

