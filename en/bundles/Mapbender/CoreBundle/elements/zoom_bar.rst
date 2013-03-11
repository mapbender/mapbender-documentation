.. _zoom_bar:

Navigation Toolbar (Zoombar)
***********************

The Navigation Toolbar element provides a control to pan and zoom, similar to the OpenLayers PanZoomBar control. This element though is easier to use when custom styling is needed.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\ZoomBar
* Widget: mapbender.element.zoombar.js
* Style: mapbender.element.zoombar.css

Configuration
=============

<Put YAML configuration here, include defaults and explain>

.. code-block:: yaml

   tooltip: 'Navigation Toolbar' # text to use as tooltip
   components: array("pan",
     "history","zoom_box",
     "zoom_max","zoom_slieder")  # components of the navigation toolbar, default all
   target: ~                     # Id of Map element to query
   stepSize: 50                  # step value for pan 
   stepByPixel: false            # step type "by pixel"/"percent" (false = percent)
   anchor: array('inline',
     'left-top','left-bottom',
     'right-top','right-bottom') # navigation toolbar alignment
   position: array('0px','0px')  # navigation toolbar position, default: x=0px, y=0px
   draggable: true               # element is draggable or not

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
