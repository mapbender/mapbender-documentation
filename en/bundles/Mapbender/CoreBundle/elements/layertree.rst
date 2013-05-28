.. _layertree:

Layertree - Table of Content
****************************

The layertree diplays the layer. The Table of Content allows you to de/activate layer in the map. 

Class, Widget & Style
======================

* Class: Mapbender\\CoreBundle\\Element\\layertree
* Widget: mapbender.element.layertree.js
* Style: mapbender.elements.css

Configuration
=============

.. code-block:: yaml

   title: layertree
   target: ~                    # Id of Map element to query   type: element # dialog/element
   displaytype: tree            # only tree in 3.0, future will offer list
   useAccordion: false          # default is false
   autoOpen: false              # true/false open when application is started, default is false
   titleMaxLength: 20           # max length of layer title, default is 20  
   showBaseSource: true         # show base layer, default is true
   showHeader: true             # shows a headline which counts the number of services  
   layerMenu: false             # show contextmenue for layer (like legend, transparency, zoom to layer, metadata u.o.), default is false, not implemented in 3.0


HTTP Callbacks
==============

None.

JavaScript API
==============

open
----------

Shows the legend.

reload
----------


JavaScript Signals
==================

None.

