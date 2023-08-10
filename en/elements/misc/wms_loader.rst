.. _wms_loader:

WMS Loader
**********

Opens a dialog in which a WMS can be loaded via the getCapabilities request. It is possible to load WMS 1.1.1 and WMS 1.3.0.


.. image:: ../../../figures/wms_loader.png
     :scale: 80


Configuration
=============

.. image:: ../../../figures/wms_loader_configuration.png
     :scale: 80

* **Auto open:** Opens the element when application is started (default: false).
* **Split layers:** Splits layer on load of the service (default: false).
* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Default format:** image/png, image/gif, image/jpeg (default: image/png).
* **Default info format:** text/html, text/xml, text/plain (default: text/html).

You need a :ref:`button` to show this element.


YAML-Definition:
----------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

   target: ~                            # Id of Map element to query
   tooltip: 'WMS Loader'                # text to use as tooltip
   autoOpen: false                      # true/false open when application is started (default: false)
   defaultFormat: 'image/png'           # image/png, image/gif, image/jpeg (default: image/png)
   defaultInfoFormat: 'text/html'       # text/html, text/xml, text/plain (default: text/html)
   splitLayers: false                   # split layer on load of the service (default: false)

How to add a WMS by defining a link
====================================

You can add a WMS to Mapbender by defining a link, e. g. in your :ref:`feature_info` or your search results. The link has to look like this:

.. code-block:: html

  <a href="#"
  mb-action="source.add.wms" mb-layer-merge="1" mb-wms-merge="1"
  mb-wms-layers="Gewaesser,Fluesse"
  mb-add-vendor-specific="bplan=123" 
  mb-url="http://wms.wheregroup.com/cgi-bin/germany.xml?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS">load service</a>


.. code-block:: yaml

    mb-action="source.add.wms"         # defines action to add a  WMS
    mb-wms-merge="1"                   # adds the WMS only once, if WMS is already part of the application it will use the WMS which is there (default: 1)
    mb-layer-merge="1"                 # activate the layers passed mb-wms-layers and do not disable the layers which are already active (default: 1)
    mb-wms-layers="Gewaesser,Fluesse"  # defines the layers to be activated, _all activates all layers, default all layers are deactivated
    href oder mb-url                   # refer to the WMS getcapabilities URL
    mb-add-vendor-specific="bplan=123" # define a vendor specific that will be added to the requests (version 3.2.9 and up)

