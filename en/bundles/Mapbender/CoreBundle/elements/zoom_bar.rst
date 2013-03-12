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

.. code-block:: yaml

   tooltip: 'Navigation Toolbar' # text to use as tooltip
   components: array("pan",      # components of the navigation toolbar, default all selected
     "history","zoom_box",
     "zoom_max","zoom_slider")
   target: ~                     # Id of Map element to query
   stepSize: 50                  # step value for pan 
   stepByPixel: false            # step type "by pixel"/"percent" (false = percent)
   anchor: 'inline'/'left-top'/  # navigation toolbar alignment, default is 'left-top' 
     'left-bottom'/'right-top'/  # use inline f.e. in sidebar
     'right-bottom'
   position: array('0px','0px')  # navigation toolbar position, default: x=20px, y=20px
   draggable: true               # element is draggable or not, default true

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
