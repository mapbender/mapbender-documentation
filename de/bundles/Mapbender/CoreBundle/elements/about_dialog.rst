.. _about_dialog:

About Dialog
************

Dieses Element rendert einen Button, der einen Dialog über Mapbender anzeigt.
Bisher wird die Mapbender Version angezeigt. In Zukunft kann auch die Lizenz 
oder kundenspezifische Daten angezeigt werden.

.. image:: ../../../../../figures/about_dialog.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/about_dialog_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'Über Mapbender3'   # Text des Tooltips
   label: true                  # false/true-Einstellung, um den BUtton zu beschriften. Voreingestellt ist true.
   icon: 'abouticon'            # Symbol für den Button

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\AboutDialog
* Widget: mapbender.mbAboutDialog
* Style: mapbender.elements.css

HTTP Callbacks
==============

about
-----

Ruft Inhalte des Dialogs auf.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.

