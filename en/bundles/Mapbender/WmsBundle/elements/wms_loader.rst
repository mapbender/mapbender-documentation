.. _wms_loader:

WMS Loader
***********************

Opens a dialog in  which a WMS can be loaded via the getCapabilities-Request.
You can load WMS 1.1.1 and  WMS 1.3.0

Class, Widget & Style
==============

* Class: Mapbender\\WmsBundle\\Element\\WmsLoader
* Widget: 
* Style: 

Configuration
=============

.. code-block:: yaml

   target: ~                            # Id of Map element to query
   tooltip: 'WMS Loader'                # text to use as tooltip
   autoOpen: false                      # true/false open when application is started, default false 
   defaultformat: 'png'                 # default format is image/png, further possibilities: image/gif, image/jpeg
   defaultinfoformat: 'html'            # default infoformat is text/html, further possibilities: text/xml, text/plain

HTTP Callbacks
==============

None.


JavaScript API
==============

activate
----------

Opens a dialog in  wich a WMS can be loaded via the getCapabilities-Request.
You can load WMS 1.1.1 and  WMS 1.3.0


JavaScript Signals
==================

None.
