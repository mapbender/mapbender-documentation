.. _feature_info:

Feature Info
************

This element provides feature info capabilties to Mapbender 3. It works for WMS services.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\FeatureInfo
* Widget: mapbender.element.featureInfo.js
* Style: mapbender.elements.css

Configuration
=============

.. code-block:: yaml

   tooltip: Feature Info # text to use as tooltip
   target: ~             # Id of Map element to query
   autoOpen: false       # true/false open when application is started, default: false

HTTP Callbacks
==============

None.

JavaScript API
==============

activate
--------

Activates the widget which then waits for mouse click on the map and starts the feature info queries.

deactivate
----------
Deactivates the widget.

JavaScript Signals
==================

None.
