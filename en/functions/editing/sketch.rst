.. _sketch:

Sketch
******

The Sketch element adds a vector layer in the map and enables geometry objects to draw.

.. image:: ../../../figures/sketch.png
     :scale: 80

Configuration
================

.. image:: ../../../figures/sketch_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Target:** Id of Map element to query.
* **Default:** sketch type from types (s. parameter 'types').
* **Types:** list of supported sketch types.

YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'Sketch'                # text to use as tooltip
   target: ~                        # Id of Map element to query
   types: 'circle'                  # list of supported sketch types     
   defaultType: 'circle'            # sketch type from types (s. parameter 'types')

You need a button to show this element. See :ref:`button` for inherited configuration options.

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\Sketch
* **Widget:** mapbender.element.sketch.js

HTTP Callbacks
==============

None.
