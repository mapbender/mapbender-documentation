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

* **Show label:** Displays label of the Scale Selector (Default: false).
* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Tooltip:** Text to use as tooltip.

YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: "Scale selector"  # text to use as tooltip
   target: ~         # Id of Map element to query
   label: false      # false/true to label the scale selector, default is false


CSS-Styling
===========

You can overwrite the style of the element, for example you can adjust the width with the following statement:

.. code-block:: css

                .mb-element-scaleselector.dropdown {
                    width: 200px;
                 }


Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\ScaleSelector
* **Widget:** mapbender.element.scaleselector.js
* **Style:** mapbender.elements.css
