.. _activity_indicator:

Activity Indicator
******************

The Activity Indicator element provides a simple widget showing background activity (Ajax calls and pending map tile requests).
In the default configuration it uses a spinner GIF to work. This can be easily modified by overriding the CSS for the 
widget.

Configuration
=============

.. image:: ../../../../../figures/activity_indicator_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

    activityClass: mb-activity          # CSS class to indicate activity (Ajax or tile)
    ajaxActivityClass: mb-activity-ajax # CSS class to indicate Ajax activity
    tileActivityClass: mb-activity-tile # CSS class to indicate tile loading activity

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\ActivityIndicator
* Widget: mapbender.element.activityindicator.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
