.. _ruler:

Line/Area Ruler (Längen und Flächen berechnen)
***************
 
 Mit dem Lineal wird eine Linie oder eine Fläche gezeichnet, deren Länge oder Flächeninhalt berechnet wird.

.. image:: ../../../../../figures/ruler.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/ruler_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

YAML-Definition:

.. code-block:: yaml

   tooltip: "ruler"   # Text des Tooltips
   target: ~          # ID des Kartenelements
   type: 'line'       # Wählen Sie Typ 'line' oder 'area'

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\Ruler
* Widget: mapbender.element.ruler.js, subclasses mapbender.element.button.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

activate
--------

Aktiviert das Modul, welches auf Mausklicks in der Karte wartet und dann die Messung startet.

deactivate
----------
Deaktiviert das Modul.

JavaScript Signals
==================

Keine.
