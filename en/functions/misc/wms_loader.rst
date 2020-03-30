.. _wms_loader:

WMS Loader
***********************

Opens a dialog in  which a WMS can be loaded via the getCapabilities-Request.
You can load WMS 1.1.1 and  WMS 1.3.0.


.. image:: ../../../figures/wms_loader.png
     :scale: 80


Configuration
=============

.. image:: ../../../figures/wms_loader_configuration.png
     :scale: 80

* **Auto open:** true/false open when application is started, default false.
* **Split layers:** split layer on load of the service, default false.
* **Use declarative:** allow to load service from a link (for example from featureInfo or search) and define the layers to activated, default false. 
* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Tooltip:** text to use as tooltip.
* **Target:** Id of Map element to query.
* **Defaultformat:** default format is image/png, further possibilities: image/gif, image/jpeg.
* **Default infoformat:** default infoformat is text/html, further possibilities: text/xml, text/plain.

You need a button to show this element. See `button <button.html>`_ for inherited configuration options.

How to add a WMS by defining a link
====================================

You can add a WMS to Mapbender by defining a link f.e. in your :ref:`WMS featureinfo<feature_info>` or your search results.

Activate the option **use Declarative** in the WMS Loader element (in a YAML application set the option ``useDeclarative`` to true).

The link has to look like this:

.. code-block:: html

  <a href="#"
  mb-action="source.add.wms" mb-layer-merge="1" mb-wms-merge="1"
  mb-wms-layers="Gewaesser,Fluesse" 
  mb-url="http://wms.wheregroup.com/cgi-bin/germany.xml?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS">load service</a>