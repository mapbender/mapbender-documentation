.. _coordinates_display:

Coordinates Display
********************

The coordinates display shows your mouse position in map coordinates.

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\CoordinatesDisplay
* Widget: mapbender.element.coordinatesdisplay.js
* Style: mapbender.elements.css

Configuration
=============

.. code-block:: yaml

   tooltip: 'coordinates display' # text to use as tooltip
   numDigits: 2                   # the number of digits each coordinate shall have when being rendered, default 2
   target: ~                      # Id of Map element to query 
   label: true                    # true/false to label  the coordinates display
   empty: 'x= - y= -'             # 
   prefix: 'x= '                  #
   separator: ' y= '              #

HTTP Callbacks
==============

None.

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

None.
