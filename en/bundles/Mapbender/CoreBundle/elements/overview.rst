.. _zoom_bar:

Overview
***********************

The Overview element provides a control of an overview map, similar to the OpenLayers Overview control. This element though is easier to use when custom styling is needed.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Overview
* Widget: mapbender.element.overview.js
* Style: mapbender.element.overview.css

Configuration
=============

.. code-block:: yaml

   tooltip: 'Overview'              # text to use as tooltip
   target: ~                        # Id of Map element to query
   layerset: ~                      # layer collection
   width: 200                       # overview width
   height: 100                      # overview height
   anchor: 'inline'/'left-top'/     # overview alignment, default is 'left-top'
     'left-bottom'/'right-top'/     # use inline f.e. in sidebar
     'right-bottom'   
   position: array('0px','0px')     # overview position in relation to anchor, default: x=0px, y=0px
   maximized: true                  # false/true to open/close on start, default is true
   fixed: true                      # false/true to fix the overview, default is true

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
