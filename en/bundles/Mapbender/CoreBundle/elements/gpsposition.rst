.. _gpspostion:

GPS-Position
***********************

Provides a button to navigate to your current position.


Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\GpsPosition
* Widget: mapbender.element.gpsPostion.js
* Style: mapbender.element.gpsPosition.css


Configuration
=============

.. code-block:: yaml

   tooltip: GPS-Position # text to use as tooltip
   target: map           # Id of Map element to query
   label: true           # true/false to label button
   icon: gpspostion      # icon to display on button
   autoStart: false	 # true/false (default is false)
   refreshinterval: 5000 # refresh interval in ms


HTTP Callbacks
==============

None.


JavaScript API
==============

None.

JavaScript Signals
==================

None.
