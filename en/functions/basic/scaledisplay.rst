.. _scaledisplay:

ScaleDisplay
************

The ScaleDisplay displays the current map scale (1:1K or 1:1000).

.. image:: ../../../figures/scaledisplay.png
     :scale: 100

.. image:: ../../../figures/scaledisplay_unit.png
     :scale: 100

Configuration
=============

.. image:: ../../../figures/scaledisplay_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons.
* **Scale prefix:** Prefix shown with scale.
* **Unit prefix:** Prefix shown with unit, e.g. 1K as 1000.
* **Position:** ScaleDisplay alignment (Default: 'bottom right').


YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'ScaleDisplay'          # text to use as tooltip
   target: ~                        # ID of Map element to query
   anchor: 'inline'/'left-top'/     # ScaleDisplay alignment, default is 'right-bottom'
     'left-bottom'/'right-top'/     # use inline, e.g. in sidebar
     'right-bottom'
   scalePrefix: Scale               # prefix, shown with scale
   unitPrefix: false                # prefix, shown with unit, e.g. 1K as 1000

