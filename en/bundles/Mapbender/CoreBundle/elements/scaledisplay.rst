.. _scaledisplay:

ScaleDisplay
***********************

The ScaleDisplay displays a representing the current map scale (1:1K or 1: 1000).

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\ScaleDisplay
* Widget: mapbender.element.scaledisplay.js
* Style: mapbender.element.scaledisplay.css

Configuration
=============

.. code-block:: yaml

   tooltip: 'Scale Bar'             # text to use as tooltip
   target: ~                        # Id of Map element to query
   unitPrefix: true/false           # use true for unit prefix
   anchor: 'inline'/'left-top'/     # scale bar alignment, default is 'right-bottom'
     'left-bottom'/'right-top'/     # use inline f.e. in sidebar
     'right-bottom'

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
