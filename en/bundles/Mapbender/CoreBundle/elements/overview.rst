.. _zoom_bar:

Map's Overview (Overview)
***********************

The Map's Overview element provides a control to overview, similar to the OpenLayers Overview control. This element though is easier to use when custom styling is needed.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Overview
* Widget: mapbender.element.overview.js
* Style: mapbender.element.overview.css

Configuration
=============

<Put YAML configuration here, include defaults and explain>

.. code-block:: yaml

   tooltip: 'Overview'              # text to use as tooltip
   target: ~                        # Id of Map element to query
   layerset: ~                      # layer collection
   width: 200                       # overview width
   height: 100                      # overview height
   position: array('inline',
     'left-top','left-bottom',
     'right-top','right-bottom')    # the overview position
   maximized: true                  # false/true to open/close on start
   fixed: true                      # false/true to fix the overview

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
