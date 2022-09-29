.. _scalebar_de:

Maßstabsleiste (Scale bar)
**************************

Die Maßstabsleiste stellt den aktuellen Maßstab graphisch als Linie dar:

.. image:: ../../../figures/scalebar.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../figures/de/scalebar_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird unter dem Reiter Layouts angezeigt.
* **Max width:** Maximale Breite der Maßstabsleiste (Standard: 200px).
* **Units:** Die wählbaren Einheiten der Maßstabsleiste:'kilometer' oder 'miles' (Standard: kilometer)
* **Position:** Ausrichtung der Maßstabsleiste (Standard: Unten rechts).

YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

   tooltip: 'Scale Bar'             # Text des Tooltips
   target: ~                        # ID des Kartenelements
   anchor: 'inline'/'left-top'/     # Ausrichtung des Maßstabsbalkens (Standard: 'right-bottom')
     'left-bottom'/'right-top'/     # Benutzen Sie inline z.B. für die Sidebar
     'right-bottom'
   position: ['10px', '10px']       # Position des Maßstabsbalkens (Standard: x=20px, y=20px)
   maxWidth: 200                    # Maximale Breite des Maßstabsbalkens (Standard: 200)
   units: ['km']                    # Einheiten des Maßstabsbalkens, 'kilometer' und/oder 'miles' (ml), (Standard: ['km'])

