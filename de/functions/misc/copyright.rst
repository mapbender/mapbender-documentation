.. _copyright:

Copyright
************

Dieses Element zeigt die Nutzungsbedingungen ("Terms of use") in einem Dialog an.

.. image:: ../../../figures/de/copyright.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/copyright_configuration.png
     :scale: 80

* **Automatisches Öffnen (Autoopen):** Schaltet ein/aus, ob das Copyright Fenster beim Start der Anwendung automatisch geöffnet werden soll (Standard: Ausgeschaltet).
* **Title:** Titel des Elements. Der Titel wird neben dem Button angezeigt.
* **Popup width:** Breite des Popup Fensters (Default: 300).
* **Popup height:** Höhe des Popup Fensters (Default: 170).
* **Tooltip:** Text, der als Tooltip angezeigt wird. Dieser wird angezeigt, wenn der Mauszeiger längere Zeit über dem Button verweilt. Er wird außerdem als Kopfzeile im Copyright Fenster verwendet.
* **Content:** Inhalt des Copyright Fensters. Dieser wird angezeigt, wenn das Element per Click aktiviert wird (oder bei Start der Anwendung wenn die "automatisches Öffnen" Option aktiviert wurde).

YAML-Definition:
----------------

.. code-block:: yaml

   class: Mapbender\CoreBundle\Element\Copyright
   title: "Copyright"              # Titel des Elements
   popupWidth: 300
   popupHeight: 170
   tooltip: "Copyright"            # Text des Tooltips
   content: "Lorem ipsum"          # Erstellen Sie ihren Text für das Copyright
   autoOpen: true                  # Automatisches Öffnen beim Start der Anwendung
                

Class, Widget & Style
======================

* **Class:** Mapbender\\CoreBundle\\Element\\Copyright
* **Widget:** mapbender.element.copyright.js
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
