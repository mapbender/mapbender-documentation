.. _scalebar:

ScaleBar
***********************

The ScaleBar displays the current map scale graphically.

.. image:: ../../../figures/scalebar.png
     :scale: 100

Configuration
=============

.. image:: ../../../figures/scalebar_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts".
* **MaxWidth:** The maximum width of the scale bar (Default: 200px).
* **Units:** Scale bar units 'kilometer' and/or 'miles' (Default: 'kilometer').
* **Position:** Scale bar alignment (Default: 'bottom right').

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
