.. _scale_selector:

Scale Selector
***************

Displays a selctbox with scales. The map scale changes when an value from the selectbox is choosen. 

Notice: The Selectbox offers the scales that are defined for the map-Element.

.. image:: ../../../../../figures/scale_selector.png
     :scale: 100

Configuration
=============

.. image:: ../../../../../figures/scale_selector_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: "Scale"  # text to use as tooltip
   target: ~         # Id of Map element to query
   label: false      # false/true to label the scale selector, default is false

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\ScaleSelector
* Widget: mapbender.element.scaleselector.js
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
