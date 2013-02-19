.. _legend:

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

   target: ~                            # Id of Map element to query
   tooltip: 'Legend'                    # text to use as tooltip
   noLegend: 'No legend available'      # text to display if no legend is available
   elementType: dialog                  # dialog/blockelement, default is dialog
   autoOpen: true                       # true/false open when application is started
   displayType: list                    # accordion/list type of display, default is list
   hideEmptyLayer: true                 # true/false hide when no legend is available, default is true
   generateGetLegendGraphicUrl: false   # true/false generate GetLegendGraphic-Url if the operation GetLegendGraphic is supported, default is false
   showWmsTitle: true                   # true/false show WMS title, default is true
   showLayerTitle: true                 # true/false show layer title, default is true
   showGroupedLayerTitle: true          # true/false show group title for grouped layers, default is true

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
