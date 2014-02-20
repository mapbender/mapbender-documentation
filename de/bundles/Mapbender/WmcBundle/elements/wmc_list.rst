.. _wmc_list:

WMC List (WMC Liste)
***********************

Im Mapbender können mit dem WMC Editor Konfigurationen gespeichert und bearbeitet werden. 
Diese Konfigurations können mit WMC-Lader geladen werden (siehe WMC-Lader).

Ihrer Applikation können Konfigurationen von einer Selektbox hinzugefügt werden.


**Beachten Sie:** Alle Konfigurationen sind im Moment öffentlich. In Zukunft soll ACL (Access Control) zu diesem Element hinzugefügt werden.

**Beachten Sie:** Diese Funktion kann nur verwendet werden, wenn ein WMC-Lader vorhanden ist.


.. image:: ../../../../../figures/wmc_list.png
     :scale: 80


Konfiguration
=============

.. image:: ../../../../../figures/wmc_list_configuration.png
     :scale: 80


YAML-Definition:

.. code-block:: yaml

    title: WMC List         
    tooltip: WMC List           # Text des Tooltips
    target: wmcloader           # Target mit dem interagiert wird, sollte wmcloader sein
    label: true                 # Titel als Beschriftung der Selektbox. Standard ist false
    


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


