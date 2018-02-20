.. _scaledisplay_de:

ScaleDisplay (Maßstabsanzeige)
********************************

Die Maßstabsanzeige zeigt den aktuellen Maßstab an (1:1K or 1: 1000).

.. image:: ../../../figures/de/scaledisplay.png
     :scale: 100


Konfiguration
=============

.. image:: ../../../figures/de/scaledisplay_configuration.png
     :scale: 80


* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Target:** ID des Kartenelements, auf das sich das Element bezieht.
* **Scale prefix:** Bezeichnung, die vor dem Maßstab als Einheit steht.
* **Unit prefix:** Bezeichnung, die vor dem Maßstab als Einheit steht.
* **Anchor:** Ausrichtung des Maßstabs, der Standardwert ist 'right-bottom' (rechts unten)


YAML-Definition:
----------------

.. code-block:: yaml

   tooltip: 'Scale Bar'             # Text des Tooltips
   target: ~                        # ID des Kartenelements
   anchor: 'inline'/'left-top'/     # Ausrichtung des Maßstabs, der Standardwert ist 'right-bottom' (rechts unten)
     'left-bottom'/'right-top'/     # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\ScaleDisplay
* **Widget:** mapbender.element.scaledisplay.js
* **Style:** mapbender.element.scaledisplay.css

HTTP Callbacks
==============

Keine.
