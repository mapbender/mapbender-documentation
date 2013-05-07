.. _wms_loader:

WMS-Loader
***********************

Opens a dialog in  wich a WMS can be loaded via the getCapabilities-Request.
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
   autoOpen: false			 # true/false open when application is started, default false 
   defaulformat: 'png'		         # default format is image/png
   defaultinfoformat: 'html'	         # default infoformat is text/html

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