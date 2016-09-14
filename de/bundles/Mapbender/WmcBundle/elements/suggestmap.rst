.. _suggestmap:

Suggest Map
***********************


**Beachten Sie:** Diese Funktion kann nur verwendet werden, wenn ein `WMC Editor <../elements/wmc_editor.html>`_ vorhanden ist.

**Beachten Sie:** Alle Konfigurationen sind im Moment öffentlich. In Zukunft soll ACL (Access Control) zu diesem Element hinzugefügt werden.

.. image:: ../../../../../figures/suggestmap.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/suggestmap_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Target:** ID des Kartenelements, auf das sich das Element bezieht.
* **Receiver:** Medium, das genutzt wird (E-Mail, Facebook, Twitter, Google+)

YAML-Definition:
----------------

.. code-block:: yaml

    title: Suggest Map   
    tooltip: Suggest Map      # Text des Tooltips
    icon: iconSuggestMap      # Icon wählen
    label: true               # Titel als Beschriftung
    target: wmceditor         # wählen Sie wmceditor als target
    action: open              # öffnen
    deactivate: close         # schließen

Für das Element wird ein Button benötigt. Siehe unter :ref:`button_de` für die Konfiguration.

Class, Widget & Style
=====================

* **Class:** Mapbender\\WmcBundle\\Element\\SuggestMap
* **Widget:** <Put Widget name here>
* **Style:** <Put name of css file here>


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


