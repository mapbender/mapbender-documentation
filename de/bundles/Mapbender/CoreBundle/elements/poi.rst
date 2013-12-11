.. _poi:

POI
***

Generiert POI-URLs (Treffpunkt-URLS), verwendbar für das Verschicken per eMail.

.. image:: ../../../../../figures/nameoftheelement.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/nameoftheelement_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   target: map # Nur das Map-Element wird benötigt.


Class, Widget & Style
============================

* Class: Mapbender\CoreBundle\Element\POI
* Widget: mapbender.mbPOI


JavaScript API
==============

defaultAction
-------------

Ein Dialog wird geöffnet und wartet auf den nächsten Klick in der Karte, um einen POI Standort zu selektieren.
