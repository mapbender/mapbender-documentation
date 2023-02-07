.. _coordinate_utility:

Coordinates Utility
*******************

The element *Coordinates Utility* allows two different things:

1. Zoom to a given point coordinate
2. Show the clicked point of the map

Both functions can be accessed with one user interface:

.. image:: ../../../figures/coordinate_utility.png
     :scale: 80

Both cases allow a dynamic coordinate transformation so that also points in a different coordinate system can be used.
Additionally, you have the possibility to copy the coordinates into the clipboard.
The element can be configured in the Mapbender backend as a dialog with a button or as an element directly into the Sidepane.

Configuration
=============

.. image:: ../../../figures/coordinate_utility_configuration.png
     :scale: 80

* **Title:** Title of the element.
* **Srs List:** You can define additional SRS to which the tool has to transform the coordinates. This list can be left empty.
* **Zoom-Level:** Zoom level of the map (default: 6)
* **Add map's srs list:** The supported coordinate systems defined in the `Map element  <../basic/map>`_ are automatically used. These coordinate systems, defined in the map, are also used by the `SRS Selector  <../basic/srs_selector>`_ (default: true).

If you define Coordinates Utility as a dialog, you need a `Button  <../misc/button>`_ that you place in the Toolbar. 


Using the tool
===============

.. image:: ../../../figures/coordinate_utility.png
     :scale: 80

**Get Coordinate:**

* If Coordinates Utility is opened as a dialog, the map reacts on a click. Click into the map and the click-coordinate is displayed in the dialog.
* Change the coordinate system with the dropdown-list. The click-coordinate is displayed in the given coordinate system.
* The last line therefore shows the click-coordinate in the original coordinate system of the map.
* The button at the end of each text-field allows to copy the coordinate directly into the clipboard.
* If Coordinates Utility is opened via the Sidepane, the button `Coordinate search` will appear that allows switching between a pan-cursor and a coordinate-cursor.

**Zoom to coordinate:**

* The text field can be used to edit your own coordinates. They must be given in the coordinate system that is chosen in the upper dropdown-list.
* With a click on the **Center map** button, the map zooms to the given coordinate and shows the position with an orange symbol.


YAML-Definition
===============

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

    coordinatesutility:
        title: 'Koordinaten Utility'
        class: Mapbender\CoordinatesUtilityBundle\Element\CoordinatesUtility
        type: element
        target: map
        srsList:
            -
                name: 'EPSG:31466'
                title: '31466'
            -
                name: 'EPSG:31468'
                title: '31468'
            -
                name: 'EPSG:25833'
                title: '25832'
            -
                name: 'EPSG:4326'
                title: '4326'
                addMapSrsList: true
