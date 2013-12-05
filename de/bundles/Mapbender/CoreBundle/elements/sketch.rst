.. _sketch:

Sketch
***********************

Das Sketch Element fügt einen Vektorlayer zu der Karte hinzu, wodurchein Geometrieobjekt gezeichnet wird.

.. image:: ../../../../../figures/sketch.png
     :scale: 80

Konfiguration
================

.. image:: ../../../../../figures/sketch_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Sketch'                # Text des Tooltips
   target: ~                        # ID des Kartenelements
   types: 'circle'                  # Liste der unterstützten Sketch Typen
   defaultType: 'circle'            # Sketch Typ der Typen (s. parameter 'types')

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\Sketch
* Widget: mapbender.element.sketch.js

HTTP Callbacks
=====================

Keine.

JavaScript API
==============

activate
--------

Aktiviert das Element. Dieses wartet auf einen Mausklick in die Karte, um das Zeichnen zu starten

deactivate
----------

Deaktiviert das Element.

JavaScript Signals
==================

Keine.
