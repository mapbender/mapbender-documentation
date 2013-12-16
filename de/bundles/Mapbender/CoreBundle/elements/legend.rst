.. _legend:

Legende
************

Dieses Element zeigt eine Legende der Layer an, die in der Karte dargestellt werden.

.. image:: ../../../../../figures/legend.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/legend_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.


YAML-Definition:

.. code-block:: yaml

   tooltip: 'Legend'                    # Text des Tooltips
   elementType: dialog                  # Anzeige als Dialog- oder Blockelement, Standard ist Dialog.
   autoOpen: true                       # true, wenn die Legende beim Start der Anwendung geöffnet werden soll, der Standardwert ist false.
   displayType: list                    # akkordeonartige Anzeige oder Liste. Standard ist Liste.
   target: ~                            # ID des Kartenelements
   hideEmptyLayer: true                 # true/false Layer wird versteckt, wenn keine Legende verfügbar ist, der Standardwert ist true
   generateGetLegendGraphicUrl: false   # true/false generiert eine GetLegendGraphic-Url, wenn die Operation GetLegendGraphic unterstützt wird, der Standardwert ist false
   showWmsTitle: true                   # true/false zeigt den WMS Titel, der Standardwert ist true
   showLayerTitle: true                 # true/false zeigt den Layertitel, der Standardwert ist true
   showGroupedLayerTitle: true          # true/false zeigt den Gruppentitel für gruppierte Layer, der Standardwert ist true

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Legend
* Widget: mapbender.element.legend.js
* Style: mapbender.element.legend.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

open
----------

Zeigt die Legend.


JavaScript Signals
==================

Keine.
