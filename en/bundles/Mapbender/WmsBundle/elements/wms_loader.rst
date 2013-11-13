.. _wms_loader:

WMS Loader
***********************

Opens a dialog in  which a WMS can be loaded via the getCapabilities-Request.
You can load WMS 1.1.1 and  WMS 1.3.0.

Configuration
=============

.. image:: ../../../../../figures/wms_loader_configuration.png
     :scale: 80

You need a button to show this element. See :ref:`button` for inherited configuration options.

YAML-Definition:

.. code-block:: yaml

   target: ~                            # Id of Map element to query
   tooltip: 'WMS Loader'                # text to use as tooltip
   autoOpen: false                      # true/false open when application is started, default false 
   defaultformat: 'image/png'                 # default format is image/png, further possibilities: image/gif, image/jpeg
   defaultinfoformat: 'text/html'            # default infoformat is text/html, further possibilities: text/xml, text/plain


How to add a WMS by defining a link
====================================

You can add a WMS to Mapbender by defining a link f.e. in your WMS featureinfo or your search results.

The link has to look like this:

.. code-block:: yaml

<a id="abc" mb-action="source.add.wms" mb-wms-merge="1" 
mb-wms-layers="Gewaesser,Fluesse" 
href="http://wms.wheregroup.com/cgi-bin/germany.xml?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS">Laden</a>


.. code-block:: yaml

mb-action="source.add.wms"    # defines action to add a  WMS
mb-wms-merge="1"              # adds the WMS only once, if WMS is already part of the application it will use the WMS which is there (default is 1)
mb-wms-layers="Gewaesser,Fluesse" # defines the layers to be activated, _all activates all layers, default all layers are deactivated
href oder mb-url              # refer to the WMS getcapabilities URL

   

Class, Widget & Style
=======================

* Class: Mapbender\\WmsBundle\\Element\\WmsLoader
* Widget: 
* Style: 

HTTP Callbacks
==============

None.


JavaScript API
==============

activate
----------

Opens a dialog in wich a WMS can be loaded via the getCapabilities-Request.
You can load WMS 1.1.1 and WMS 1.3.0.


JavaScript Signals
==================

None.
