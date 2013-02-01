Legend
************

The legend object shows the legend of the map's layers.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Legend
* Widget: mapbender.element.legend.js
* Style: mapbender.element.legend.css

Configuration
=============

Also see :doc:`button` for inherited configuration options.

.. code-block:: yaml

   target: ~                       # Id of Map element to query
   tooltip: 'Legend'               # text to use as tooltip
   nolegend: 'No legend available' # text to display if no legend is available
   elementType:                    # dialig/blockelement 
   autoOpen: true                  # true/false open when application is started
   displayType: accordion          # accordion/list type of display
   hiddeemptylayer: false          # true/false hidde when no legend is available

HTTP Callbacks
==============

None.

JavaScript API
==============

open
----------

Shows the legend.


JavaScript Signals
==================

None.
