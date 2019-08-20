.. _ruler:

Line/Area Ruler
***************

The ruler is used to draw a line or area and display length/area in a dialog. Selecting a type determines whether the element measures lines or areas. Each ruler element can only measure either lines or areas.

.. image:: ../../../figures/ruler.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/ruler_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Tooltip:** Text to use as tooltip.
* **Target:** ID of Map element to query.
* **Type:** Choose type of element: line or area.
* **Immediate:** Select whether the calculated lengths are displayed immediately or only after the click on the map.

YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: "ruler"   # text to use as tooltip
   target: ~          # ID of Map element to query
   type: 'line'       # choose type line or area
   immediate: 'false' # True: Display the calculated lengths immediately. False: The calculated lengths are displayed only after clicking. Default: False.


You need a button to show this element. See :ref:`button` for inherited configuration options.
To use both functions (measuring areas and lines) in an application, you need two buttons that are in a group.

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\Ruler
* **Widget:** mapbender.element.ruler.js, subclasses mapbender.element.button.js
* **Style:** mapbender.elements.css
