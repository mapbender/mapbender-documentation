.. _zoom_bar:

Overview (Übersicht)
***********************

Mit diesem Element kann eine Übersichtskarte erstellt werden, ähnlich wie in OpenLayers.
Es kann die Größe des Übersichtsfensters und die Position bestimmt werden. In der Übersicht wird ein vorher definiertes Layerset angezeigt.
Die Übersichtskarte kann fixiert sein, oder sie ist zoomfähig, d.h. wenn in der Hauptkarte gezoomt wird, wird dies auch in der Übersicht angezeigt.
Es kann auch definiert werden, ob die Übersichtskarte nach dem Öffnen der Applikation minimiert oder maximiert ist.


.. image:: ../../../../../figures/overview.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/overview_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Overview'              # Text des Tooltips
   target: ~                        # ID des Kartenelements
   layerset: ~                      # vorher definiertes Layerset, das angezeigt werden soll.
   width: 200                       # Breite der Übersicht
   height: 100                      # Höhe der Übersicht
   anchor: 'inline'/'left-top'/     # Ausrichtung der Übersicht, Standard ist 'right-top' (rechts oben)
     'left-bottom'/'right-top'/     # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'   
   position: array('0px','0px')     # Position der Übersicht in Relation zum Anker, Standard: x=0px, y=0px
   maximized: true                  # true/false ob die Applikation beim Start maximiert ist, der Standardwert ist true
   fixed: true                      # true/false um den Übersichtsbereich zu fixieren, der Standardwert ist true

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Overview
* Widget: mapbender.element.overview.js
* Style: mapbender.element.overview.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
