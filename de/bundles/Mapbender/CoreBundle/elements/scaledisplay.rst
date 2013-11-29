.. _scaledisplay:

ScaleDisplay (Maßstabsanzeige)
********************************

Die Maßstabsanzeige zeigt den aktuellen Maßstab an (1:1K or 1: 1000).


Konfiguration
=============

.. image:: ../../../../../figures/scaledisplay_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Scale Bar'             # Text des Tooltips
   target: ~                        # ID des Kartenelements
   anchor: 'inline'/'left-top'/     # Ausrichtung des Maßstabs, der Standardwert ist 'right-bottom' (rechts unten)
     'left-bottom'/'right-top'/     # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\ScaleDisplay
* Widget: mapbender.element.scaledisplay.js
* Style: mapbender.element.scaledisplay.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
