.. _poi:

POI (MeetingPoint)
***********************

Generate POI (aka meeting point) URLs suitable for sending by e-mail


.. image:: ../../../../../figures/poi.png
     :scale: 80


Configuration
=============


.. image:: ../../../../../figures/poi_configuration.png
     :scale: 80
     

YAML-Definition:

.. code-block:: yaml

   target: map # Only target (map element) is needed


Class, Widget & Style
=========================

* Class: Mapbender\CoreBundle\Element\POI
* Widget: mapbender.mbPOI


JavaScript API
==============

defaultAction
-------------

Opens a dialog and listens for next click on map to select POI location.
