.. _scalebar:

ScaleBar (Maßstabsbalken)
**************************

Der Maßstabsbalken ist eine schmale Linie, die den aktuellen Maßstab anzeigt.

.. image:: ../../../../../figures/scalebar.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../../../figures/scalebar_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Scale Bar'             # Text des Tooltips
   target: ~                        # ID des Kartenelements
   anchor: 'inline'/'left-top'/     # Ausrichtung des Maßstabsbalkens, der Standardwert ist 'right-bottom' (rechts unten)
     'left-bottom'/'right-top'/     # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'     
   position: array('0px','0px')     # Position des Maßstabsbalkens, der Standardwert ist: x=20px, y=20px
   maxWidth: 200                    # Maximale Breite des Maßstabsbalkens, der Standardwert ist 200
   units: array('km')               # Einheiten des Maßstabsbalkens, 'kilometer' und/oder 'miles' (ml), Standard ist ['km']

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\ScaleBar
* Widget: mapbender.element.scalebar.js
* Style: mapbender.element.scalebar.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
