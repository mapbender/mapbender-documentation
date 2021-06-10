.. _scalebar:

ScaleBar
***********************

The ScaleBar displays a small line indicator representing the current map scale.

.. image:: ../../../figures/scalebar.png
     :scale: 100

Configuration
=============

.. image:: ../../../figures/scalebar_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts".
* **Tooltip:** Text to use as tooltip.
* **Target:** ID of the Map element to query.
* **MaxWidth:** The maximum width of the scale bar, default 200px.
* **Anchor:** Scale bar alignment, default is 'right-bottom' (use inline e.g. in sidebar).
* **Units:** Scale bar units 'kilometer' and/or 'miles' (ml), default ['km'].

YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'Scale Bar'             # text to use as tooltip
   target: ~                        # ID of the Map element to query
   anchor: 'inline'/'left-top'/     # scale bar alignment, default is 'right-bottom'
     'left-bottom'/'right-top'/     # use inline, e.g. in sidebar
     'right-bottom'
   position: ['10px', '10px']       # scale bar position, default: x=20px, y=20px
   maxWidth: 200                    # the maximum width of the scale bar, default 200px
   units: ['km']                    # scale bar units 'kilometer' and/or 'miles' (ml), default ['km']

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\ScaleBar
* **Widget:** mapbender.element.scalebar.js
* **Style:** mapbender.element.scalebar.css
