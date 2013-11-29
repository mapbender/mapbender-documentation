.. _coordinates_display:

Coordinates Display (Koordinatenanzeige)
****************************************

Das Koordinatenanzeige-Element zeigt die aktuelle Mausposition in den Kartenkoordinaten.

.. image:: ../../../../../figures/coordinates_display.png
     :scale: 90

Konfiguration
=============

.. image:: ../../../../../figures/coordinates_display_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'coordinates display' # Text des Tooltips
   numDigits: 2                   # die Anzahl der Nachkommastellen, die jede Koordinate haben soll
   target: ~                      # ID des Kartenelements
   label: true                    # false/true, um den Button zu beschriften. Der Standardwert ist true.
   empty: 'x= - y= -'             # zeigt diesen Text, wenn die Maus sich nicht in der Karte befindet.
   prefix: 'x= '                  # zeigt ein Präfix vor der X-Koordinate
   separator: ' y= '              # zeigt einen Separator vor der Y-Koordinate

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\CoordinatesDisplay
* Widget: mapbender.element.coordinatesdisplay.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

reset
-----

<>

showHidde
----------

<>

JavaScript Signals
==================

Keine.
