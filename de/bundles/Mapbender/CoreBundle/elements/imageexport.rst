.. _imageexport:

ImageExport (Bildexport)
***************************

Mit dem  Bildexport kann die aktuelle Kartenansicht exportiert werden. Das Bild kann als png oder jpeg abgespeichert werden.

.. image:: ../../../../../figures/de/image_export.png
     :scale: 80

Konfiguration
=============

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

.. image:: ../../../../../figures/de/image_export_configuration.png
     :scale: 80

* Title: Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* Target: Zielelement (ID des Kartenelements), das bei Anklicken des Buttons ausgelöst wird.

YAML-Definition:

.. code-block:: yaml

   target: ~                        # ID des Kartenelements 

Class, Widget & Style
=========================

* Class: Mapbender\\PrintBundle\\Element\\ImageExport
* Widget: mapbender.element.imageExport.js

HTTP Callbacks
=========================

Keine.

JavaScript API
=========================

Keine.

JavaScript Signals
=============================

Keine.
