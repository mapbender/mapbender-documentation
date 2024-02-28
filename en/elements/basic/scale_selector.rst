.. _scale_selector:

Scale Selector
**************

This element displays a selectbox with scales. The map scale changes when a different value from the selectbox is chosen. The selectbox only offers scales that have been defined in the map element.

.. image:: ../../../figures/scale_selector.png
     :scale: 100

Configuration
=============

.. image:: ../../../figures/scale_selector_configuration.png
     :scale: 80

* **Show label:** Displays label of the Scale Selector (default: false).
* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Tooltip:** Text to use as tooltip.

YAML-Definition
---------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

   tooltip: "Scale selector"  # text to use as tooltip
   target: ~         # Id of Map element to query
   label: false      # false/true to label the scale selector (default: false)

