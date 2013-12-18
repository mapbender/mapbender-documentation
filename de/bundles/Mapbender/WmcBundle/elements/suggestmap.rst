.. _suggestmap:

Suggest Map
***********************


**Beachten Sie:** Diese Funktion kann nur verwendet werden, wenn ein WMC-Editor vorhanden ist.

**Beachten Sie:** Alle Konfigurationen sind im Moment öffentlich. In Zukunft soll ACL (Access Control) zu diesem Element hinzugefügt werden.



.. image:: ../../../../../figures/suggestmap.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/suggestmap_configuration.png
     :scale: 80

Für das Element wird ein Button benötigt. Siehe unter :doc:`button` für die Konfiguration.


YAML-Definition:

.. code-block:: yaml

    title: Suggest Map   
    tooltip: Suggest Map      # Text des Tooltips
    icon: iconSuggestMap      # Icon wählen
    label: true               # Titel als Beschriftung
    target: wmceditor         # wählen Sie wmceditor als target
    action: open              # öffnen
    deactivate: close         # schließen


Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\SuggestMap
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


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


