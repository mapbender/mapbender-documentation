.. _wmc_editor:

WMC Editor
***********************

Im Mapbender können mit dem WMC Editor Konfigurationen gespeichert und bearbeitet werden. 
Diese Konfigurations können mit dem WMC-Lader geladen werden (siehe WMC-Lader).

Sie können den WMC-Editor ihrer Applikation hinzufügen. Beachten Sie, dass der WMC-Editor einen Button benötigt.

Mit dem Editor können Konfigurationen erzeugt und bearbeitet werden. Es können Konfigurationen mit einem Titel, einer Beschreibung und einem Screenshot gespeichert werden.

**Beachten Sie:** Alle Konfigurationen sind im Moment öffentlich. In Zukunft soll ACL (Access Control) zu diesem Element hinzugefügt werden.



.. image:: ../../../../../figures/wmc_editor.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/wmc_editor_configuration.png
     :scale: 80

Für das Element wird ein Button benötigt. Siehe unter :doc:`button` für die Konfiguration.


YAML-Definition:

.. code-block:: yaml

    title: WMC Editor
    tooltip: WMC Editor   # Text des Tooltips
    target: map           # Name des Kartenelements 
    accessGroups: [0,1]   # definiert Gruppen, die den WMC Editor verwenden können

Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\WmcEditor
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


HTTP Callbacks
==============


<action>
--------------------------------

Öffnet einen Dialog mit einem Editor, in dem Konfigurationen gespeichert und bearbeitet werden können.


JavaScript API
==============


<function>
----------


JavaScript Signals
==================

<signal>
--------


