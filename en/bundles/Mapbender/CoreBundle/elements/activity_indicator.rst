.. _activity_indicator:

Activity Indicator
******************

The activity indicator element provides a simple widget showing background activity (Ajax calls and pending map tile requests).
In the default configuration it uses a Font symbol. This can be easily modified by changing the CSS for the 
widget in the css-file fom//src//FOM//CoreBundle//Resources//public//css/frontend//mapbender3_theme.css.

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
