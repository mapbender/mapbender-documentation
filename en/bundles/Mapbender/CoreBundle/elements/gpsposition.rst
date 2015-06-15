.. _gpspostion:

GPS-Position
***********************

Provides a button to navigate to your current position and display a symbol at that position. The scale will not be changed.

.. image:: ../../../../../figures/gps_position.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/gps_position_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

    tooltip: GPS-Position  # text to use as tooltip
    label: true            # true/false to label button, default is true
    icon: gpsposition      # icon to display on button
    target: map            # Id of Map element to query
    autoStart: false	  # true/false, default is false
    refreshinterval: 5000  # refresh interval in ms, default is 5000 ms
    follow: true           # default false, true refreshs the map for every received GPS position received, only use with WMS in tiled mode
    average: 1             # calculates the average of the last at parameter average defined amount of received GPS coordinates, default 1
    centerOnFirstPosition: true # center map only on first received gps position
    zoomToAccuracy: false  # zoom map according to received gps position accuracy
    zoomToAccuracyOnFirstPosition: true # zoom map according to first received gps position accuracy

Class, Widget & Style
======================

* Class: Mapbender\\CoreBundle\\Element\\GpsPosition
* Widget: mapbender.element.gpsPostion.js
* Style: mapbender.element.gpsPosition.css

HTTP Callbacks
==============

None.


JavaScript API
==============

None.

JavaScript Signals
==================

None.
