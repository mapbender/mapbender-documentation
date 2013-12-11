.. _zoom_bar:

Navigation Toolbar (Zoombar) (Navigationswerkzeug)
*********************************************************************

Das Navigationswerkzeug bietet Zoomen und Verschieben an, ähnlich wie bei OpenLayers.

.. image:: ../../../../../figures/zoom_bar.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../../../figures/zoom_bar_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Navigation Toolbar' # Text des Tooltips
   components: array("pan",      # Komponenten des Navigationswerkzeugs, Standardmäßig wird alles selektiert.
     "history","zoom_box",
     "zoom_max","zoom_slider")
   target: ~                     # ID des Kartenelements
   stepSize: 50                  # Schrittweite für das Verschieben
   stepByPixel: false            # Schritttyp: Pixel oder Prozent, false = Prozent, Standard ist false
   anchor: 'inline'/'left-top'/  # Ausrichtung des Navigationswerkzeugs, Standard ist 'left-top' (oben-links) 
     'left-bottom'/'right-top'/  # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'
   draggable: true               # das Navigationswerkzeug ist verschiebbar oder nicht, Standard ist true

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\ZoomBar
* Widget: mapbender.element.zoombar.js
* Style: mapbender.element.zoombar.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
