.. _scalebar:

ScaleBar
***********************

The ScaleBar displays a small line indicator representing the current map scale.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\ScaleBar
* Widget: mapbender.element.scalebar.js
* Style: mapbender.element.scalebar.css

Configuration
=============

<Put YAML configuration here, include defaults and explain>

.. code-block:: yaml

   tooltip: 'Scale Bar'             # text to use as tooltip
   target: ~                        # Id of Map element to query
   layerset: ~                      # layer collection
   maxWidth: 200                    # the max width of the scale bar, default 200
   anchor: array('inline',
     'left-top','left-bottom',
     'right-top','right-bottom')    # scale bar alignment
   position: array('0px','0px')     # scale bar  position, default: x=0px, y=0px
   units: array('kilometer','mile') # scale bar units, default 'kilometer'

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
