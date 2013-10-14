.. _layertree:

Layertree - Table of Content (Layerbaum)
********************************************************

Der Layerbaum zeigt die Layer und Service-Ordner an. Im Layerbaum können einzelne Layer in der Karte aktiviert und deaktiviert werden. 
Hier kann auch die Infoabfrage für einzelne Layer aktiviert oder deaktiviert werden.

Die Reihenfolge der Service können geändert und Layer via drag & drop verschoben werden.

.. image:: ../../../../../figures/layertree.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/layertree_configuration.png
     :scale: 80

Optional kann ein Button für dieses Element verwendet werden. Siehe unter :doc:`button` für die Konfiguration. 
Der Layerbaum kann auch als Element definiert werden. Dann wird der Layerbaum in einem frame wie der Sidebar angezeigt.

YAML-Definition:

.. code-block:: yaml

   title: layertree             # Titel des Layerbaums
   target: ~                    # ID des Kartenelements  
   type: ~                      # Typ des Layerbaums
   displaytype: tree            # In 3.0 gibt es nur den Baum (Tree), in Zukunft wird auch eine Liste angeboten.
   useAccordion: false          # akkordeonartige Anzeige. Standard ist false
   autoOpen: false              # true, wenn die Infoabfrage beim Start der Anwendung geöffnet wird, der Standardwert ist false.
   titleMaxLength: 20           # Maximale Länge des Layertitels, Standard ist 20  
   showBaseSource: true         # Anzeige des Basislayers, der Standardwert ist true
   showHeader: true             # zeigt eine Überschrift, die die Anzahl der Services zählt, der Standardwert ist true
   layerMenu: false             # zeigt ein Kontextmenü für den Layer an (wie Legende, Transparenz, Zoom, Metadaten u.a.), der Standardwert ist false. Das Element ist in 3.0 noch nicht implementiert.
   layerRemove: false		 # Entfernen von Layern. der Standardwert ist false

Class, Widget & Style
======================

* Class: Mapbender\\CoreBundle\\Element\\Layertree
* Widget: mapbender.element.layertree.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

open
----------

Öffnet den Layerbaum (layertree)

reload
----------


JavaScript Signals
==================

Keine.

