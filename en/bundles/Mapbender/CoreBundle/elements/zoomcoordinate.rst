.. _zoomcoordinate:

Zoomcoordinate
**********************************

This element provides a template where you can type in coordinates of different projections types. The zoomcoordinate element will transform the coordinates to the actual projection of the map and will zoom to the position of these coordinates.

.. image:: ../../../../../figures/zoomcoordinate.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/zoomcoordinate_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Zoomcoordinate'  		# text to use as title
   prefix_projection: 'projection'      # prefix for the projections
   prefix_x: 'x'			# prefix for input column x-coordinate
   prefix_y: 'y'			# prefix for input column y-coordinate
   type: 'element'                      # choose position of the element
   target: ~				# Id of Map element to query


Repository
=============

* https://github.com/mapbender/mapbender-zoomcoordinate.git

Class, Widget & Style
===========================

* Class: Mapbender\\ZoomcoordinateBundle\\Element\\Zoomcoordinate
* Widget: mapbender.mbZoomcoordinate
* Style: mapbender.elements.zoomcoordinate.scss


HTTP Callbacks
==============

<action>
--------------------------------

JavaScript API
==============

<function>
----------

JavaScript Signals
==================

<signal>
--------

