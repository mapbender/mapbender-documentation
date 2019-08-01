.. _srs_selector_de:

Spatial Reference System Selector (SRS Selector) (Auswahl des räumlichen Referenzsystems)
************************************************************************************************

Mit dem SRS Selector kann das räumliche Referenzsystems (SRS) der Karte geändert werden.
In der Karte stehen die Koordinatensysteme in der Selectbox zur Auswahl, die vorher im `Kartenelement <map.html>`_ definiert wurden.

.. image:: ../../../figures/srs_selector.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../figures/de/srs_selector_configuration.png
     :scale: 80

* **Beschriftung anzeigen:** True, um den SRS Selector zu beschriften. Der Standardwert ist false.
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem SRS Selector angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Target:** ID des Kartenelements, auf das sich der SRS Selector bezieht.

YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'SRS Selector'  # Text des Tooltips
   label: false             # false/true, um den SRS Selector zu beschriften. Der Standardwert ist false.
   target: ~                # ID des Kartenelements

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\SrsSelector
* **Widget:** mapbender.element.srsselector.js
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

Keine.
