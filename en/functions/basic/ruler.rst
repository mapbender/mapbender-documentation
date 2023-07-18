.. _ruler:

Line/Area Ruler
***************

The ruler is used to draw a line or area and display length/area in a dialog. You need a button to show this element. See :ref:`button` for inherited configuration options.
To use both functions (measuring areas and lines) in an application, you need two buttons that are in the same pre-defined group. Selecting a type determines whether the element measures lines or areas. Each ruler element can only measure either lines or areas.

.. image:: ../../../figures/ruler.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/ruler_configuration.png
     :scale: 80

* **Title:** Title of the element. It will be displayed in the measuring window in the application itself.
* **Geometry:** Choose type of element: line or area. Mandatory field.
* **Helptext:** Displays a help text. The default value `mb.core.ruler.help` translates to "Double-click to end drawing" (depending on the browser's display language).
* **Line width while drawing:** Pixel value that defines the stroke width during drawing.
* **Stroke color:** RGBA value that defines the stroke color. Can be changed using a color picker after clicking on the input field.
* **Stroke width (pixels):** Pixel value that defines the stroke width of the measured geometry.
* **Fill color:** RGBA value that defines the fill color of a measured area. Can be changed using a color picker after clicking on the input field. When *Line* geometry is selected, this option has no effect.
* **Font color:** RGBA value that defines the font color of the calculated result displayed within the geometry. Can be changed using a color picker after clicking on the input field. When *Line* geometry is selected, this option has no effect.
* **Font size:** Numeric value that defines the font size of the area displayed within the geometry. When *Line* geometry is selected, this option has no effect.


YAML-Definition:
----------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

   title: mb.core.ruler.tag.line             # Choose 'line', 'area' or another title
   class: Mapbender\CoreBundle\Element\Ruler # Class of element
   target: map                               # ID of Map element to query, e.g. 'map'
   type: line                                # Choose type 'line' or 'area'
   strokeColor: 'rgba(16, 101, 93, 0.8)'     # Choose rgba value (line and area)
   fillColor: rgba(100, 100, 100, 0.5)       # Choose rgba value (area only)
   fontColor: 'rgba(0,0,0,1)'                # Choose rgba value (area only)
   fontSize: 14                              # Choose numeric value (area only)
   strokeWidth: 4                            # Choose pixel value (line and area)
   strokeWidthWhileDrawing: 3                # Choose pixel value (line and area)
