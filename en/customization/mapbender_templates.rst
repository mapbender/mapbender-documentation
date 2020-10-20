.. _mapbender_templates:

Mapbender Templates
###################

Get to know the basic Mapbender templates which are ready to use out of the box.



Fullscreen Template
*******************

.. image:: ../../figures/mapbender_fullscreen.png
     :scale: 50

View a demo of the Mapbender Fullscreen Template https://demo.mapbender.org/application/mapbender_user_yml

Regions of the Fullscreen Template:

  * Toolbar (button region)
  * Sidepane (layertree, legend, search,...)
  * Content (map, navigation toolbar, scalebar,...)
  * Footer (impressum, scaledisplay, ...)

Specials:

  * dark background style of the template
  * fullscreen display with adjustable sidepane:

Configuration of the sidepane
*****************************

It is possible to adjust some properties for the sidepane while working with templates that support it. Elements in the sidepane can be displayed in three different styles:

- "Accordion" shows elements via tabs:

.. image:: ../../figures/sidepane_accordion.png
     :scale: 80

- "Buttons" shows elements via buttons:

.. image:: ../../figures/sidepane_buttons.png
     :scale: 80

- "None" does not contain any styling options at all and displays the elements in the configured backend order:

.. image:: ../../figures/sidepane_nostyle.png
     :scale: 80

Sidepane properties are adjustable in the Sidepane area of the Mapbender backend:

.. image:: ../../figures/sidepane_backend.png
     :scale: 80

Mobile Template
***************

.. image:: ../../figures/mapbender_mobile.png
     :scale: 80

View a demo of the Mapbender Mobile Template https://demo.mapbender.org/application/mapbender_mobile_yml

Regions of the mobile Template

  * footer (button region)
  * Content (map, navigation toolbar)
  * Mobilepane (area that will overlapp the map, when a dialog like Layertree, FeatureInfo is displayed)


Please note that not all elements can be used with the Mobile template at the moment. Here is a list of the elements that can be used:

  * Map
  * GPS-Position
  * Layertree (different design, will only show the root layer title of a service, you can only de-/activate a whole service)
  * BaseSourceSwitcher (different design: list not buttons)
  * FeatureInfo
  * Navigation Toolbar (Zoombar)
  * HTML
  * Button
  * SimpleSearch
