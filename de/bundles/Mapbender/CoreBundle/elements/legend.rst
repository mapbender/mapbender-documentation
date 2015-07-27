.. _legend:

Legende
************

Dieses Element zeigt eine Legende der Layer an, die in der Karte dargestellt werden.

.. image:: ../../../../../figures/legend.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/de/legend_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

* Automatisches Öffnen: true, wenn die Legende beim Start der Anwendung geöffnet werden soll, der Standardwert ist false.
* Ebenen ohne Objekte ausblenden: Layer wird versteckt, wenn keine Legende verfügbar ist, der Standardwert ist true
* Title: Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* Tooltip: Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* Element type: Anzeige als Dialog- oder Blockelement, Standard ist Dialog.
* Display type: akkordeonartige Anzeige oder Liste. Standard ist Liste.
* Target: Zielelement (Titel(ID)) des Buttons, das bei Anklicken des Buttons ausgelöst wird. 

* Legenden-URL generieren: generiert eine GetLegendGraphic-Url, wenn die Operation GetLegendGraphic unterstützt wird, der Standardwert ist false.
* Titel der Datenquelle anzeigen: zeigt den WMS Titel, der Standardwert ist true.
* Titel der Ebene anzeigen: zeigt den Layertitel, der Standardwert ist true.
* Titel der gruppierten Ebenen anzeigen: zeigt den Gruppenlayertitel für gruppierte Layer, der Standardwert ist true.


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
============================

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
