.. _legend:

Legend
************

The legend object shows the legend of the layers that are displayed in the map.

.. image:: ../../../../../figures/legend.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/legend_configuration.png
     :scale: 80

You need a button to show this element. See :doc:`button` for inherited configuration options.

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Legend'                    # text to use as tooltip
   elementType: dialog                  # dialog/blockelement, default is dialog
   autoOpen: true                       # true/false open when application is started, default is true
   displayType: list                    # accordion/list type of display, default is list
   target: ~                            # Id of Map element to query
   hideEmptyLayer: true                 # true/false hide when no legend is available, default is true
   generateGetLegendGraphicUrl: false   # true/false generate GetLegendGraphic-Url if the operation GetLegendGraphic is supported, default is false
   showWmsTitle: true                   # true/false show WMS title, default is true
   showLayerTitle: true                 # true/false show layer title, default is true
   showGroupedLayerTitle: true          # true/false show group title for grouped layers, default is true

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\Legend
* Widget: mapbender.element.legend.js
* Style: mapbender.element.legend.css

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
