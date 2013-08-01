.. _layertree:

Layertree - Table of Content
****************************

The layertree diplays the layers and Service folders. The layertree allows you to de/activate layer in the map. 

.. image:: ../../../../../figures/layertree.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/layertree_configuration.png
     :scale: 80

You can optionally use a button to show this element. See :doc:`button` for inherited configuration options.

YAML-Definition:

.. code-block:: yaml

   title: layertree
   target: ~                    # Id of the Map element to query   
   type: element                # dialog/element
   displaytype: tree            # only tree in 3.0, future will offer list
   useAccordion: false          # default is false
   autoOpen: false              # true/false open when application is started, default is false
   titleMaxLength: 20           # max length of layer title, default is 20  
   showBaseSource: true         # show base layer, default is true
   showHeader: true             # shows a headline which counts the number of services  
   layerMenu: false             # show contextmenu for the layer (like legend, transparency, zoom to layer, metadata u.o.), default is false, not implemented in 3.0
   layerRemove: false		# default is false

Class, Widget & Style
======================

* Class: Mapbender\\CoreBundle\\Element\\Layertree
* Widget: mapbender.element.layertree.js
* Style: mapbender.elements.css

HTTP Callbacks
==============

None.

JavaScript API
==============

open
----------

Opens the layertree

reload
----------


JavaScript Signals
==================

None.

