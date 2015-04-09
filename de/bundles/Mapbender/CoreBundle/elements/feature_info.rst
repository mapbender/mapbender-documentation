.. _feature_info:

Feature Info (Infoabfrage)
**************************

Dieses Element stellt die Infoabfrage bereit, die mit WMS Services funktioniert.

.. image:: ../../../../../figures/feature_info.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/feature_info_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

YAML-Definition:

.. code-block:: yaml

   tooltip: Feature Info   # Text des Tooltips
   target: ~               # ID des Kartenelements
   autoOpen: false         # true, wenn die Infoabfrage beim Start der Anwendung geöffnet wird, der Standardwert ist false.
   deactivateOnClose: true # true/false um die Funktion nach dem Schließen des Ergebnisfensters zu deaktivieren, der Standardwert ist true
   width: 700              # Breite des Dialogs, Standardwert: 700 px
   height: 700             # Höhe des Dialog, Standardwert: 500 px

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\FeatureInfo
* Widget: mapbender.element.featureInfo.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

activate
--------

Aktiviert das Modul, welches dann auf einen Mausklick wartet, um die Infoabfrage zu öffnen.

deactivate
----------
Deaktiviert das Modul.

JavaScript Signals
==================

Keine.
