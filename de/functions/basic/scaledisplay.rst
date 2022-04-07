.. _scaledisplay_de:

Maßstabsanzeige (ScaleDisplay)
******************************

Die Maßstabsanzeige zeigt den aktuellen Maßstab numerisch an (1:1K or 1:1000).

.. image:: ../../../figures/scaledisplay.png
     :scale: 100

.. image:: ../../../figures/scaledisplay_unit.png
     :scale: 100

Konfiguration
=============

.. image:: ../../../figures/de/scaledisplay_configuration.png
     :scale: 80


* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden.
* **Scale prefix:** Bezeichnung, die vor der Maßstabsangabe steht, z.B. "Maßstab".
* **Unit prefix:** Falls aktiviert, wird die Maßstabszahl nicht ausgeschrieben, sondern mit einem Präfix dargestellt, z.B. 1K für 1000 (Standard: false).


YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

   tooltip: 'ScaleDisplay'          # Text des Tooltips
   target: ~                        # ID des Kartenelements
   anchor: 'inline'/'left-top'/     # Ausrichtung des ScaleDisplay-Elements (Standard: 'right-bottom')
     'left-bottom'/'right-top'/     
     'right-bottom'
   scalePrefix: Scale               # Bezeichnung, die vor der Maßstabsangabe steht, z.B. "Maßstab"
   unitPrefix: true                 # aktiviert Darstellung der Maßstabszahl mit Präfix (Standard: false).

