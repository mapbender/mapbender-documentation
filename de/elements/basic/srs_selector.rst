.. _srs_selector_de:

SRS Auswahl (SRS Selector)
**************************

Mit der SRS Auswahl kann das räumliche Referenzsystem (SRS) der Karte geändert werden.
Nach der Konfiguration stehen die Koordinatensysteme der Karte in einer Selectbox zur Auswahl, die vorher im :ref:`Kartenelement <map_de>` definiert wurden.

.. image:: ../../../figures/srs_selector.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../figures/de/srs_selector_configuration.png
     :scale: 70

* **Beschriftung anzeigen:** Beschriftet die SRS Auswahl (Standard: false).
* **Titel:** Titel des Elements. Dieser wird in der Layouts-Liste angezeigt und ermöglicht die Unterscheidung mehrerer Button-Elemente voneinander. Der Titel wird außerdem neben dem SRS Selector angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.


YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

   tooltip: 'SRS Selector'  # Text des Tooltips
   label: false             # false/true, um den SRS Selector zu beschriften (Standard: false).
   target: ~                # ID des Kartenelements

