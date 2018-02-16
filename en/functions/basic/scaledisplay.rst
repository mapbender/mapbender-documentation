.. _scaledisplay:

ScaleDisplay
***********************

The ScaleDisplay displays the current map scale (1:1K or 1: 1000).

.. image:: ../../../figures/de/scaledisplay.png
     :scale: 100

Configuration
=============

.. image:: ../../../figures/scaledisplay_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Tooltip:** text to use as tooltip.
* **Target:** Id of Map element to query.
* **Scale prefix:** prefix, shown with scale.
* **Unit prefix:** prefix, shown with unit.
* **Anchor:** scale bar alignment, default is 'right-bottom' (use inline f.e. in sidebar).


YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'Scale Bar'             # text to use as tooltip
   target: ~                        # Id of Map element to query
   anchor: 'inline'/'left-top'/     # scale bar alignment, default is 'right-bottom'
     'left-bottom'/'right-top'/     # use inline f.e. in sidebar
     'right-bottom'

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\ScaleDisplay
* **Widget:** mapbender.element.scaledisplay.js
* **Style:** mapbender.element.scaledisplay.css

HTTP Callbacks
==============

None.
