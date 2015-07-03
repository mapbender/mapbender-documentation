.. _zoomcoordinate:

Zoom to Coordinate (Koordinate anzeigen)
****************************************

Dieses Elemenet ermöglicht eine vom Koordinatensystem unabhängige Suche nach Koordinaten. Nach Angabe des Koordinatensystems und des Koordinatenpaares werden die Werte auf das aktuelle Koordinatensystem umgerechnet und die entsprechende Stelle auf der Karte zentriert. 

.. image:: ../../../../../figures/zoomcoordinate.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/zoomcoordinate_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Zoomcoordinate'            # Titel
   prefix_projection: 'projection'      # Präfix für die Angabe des Projektionssystem
   prefix_x: 'x'                        # Präfix vor dem Textfeld zur Angabe der x-Koordinate
   prefix_y: 'y'                        # Präfix vor dem Textfeld Angabe der y-Koordinate
   type: 'element'                      # Auswahl Positionierung des Elements ( Sidepane(element) oder Popup(dialog))
   target: ~                            # ID/Name des Elements Karte (map)


Repository
=============

* https://github.com/mapbender/mapbender-zoomcoordinate.git

Class, Widget & Style
===========================

* Class: Mapbender\\ZoomcoordinateBundle\\Element\\Zoomcoordinate
* Widget: mapbender.mbZoomcoordinate
* Style: mapbender.elements.zoomcoordinate.scss


HTTP Callbacks
==============

<action>
--------------------------------

JavaScript API
==============

<function>
----------

JavaScript Signals
==================

<signal>
--------

