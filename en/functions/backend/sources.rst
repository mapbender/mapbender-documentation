.. _sources:

Sources
=======

With the sources backend tab, it is possible to register OGC sources into your applications. 

Further information about the registration process of services and their usage in Mapbender is available in the `Quickstart document <../../quickstart.html#loading-web-map-services>`_.

.. image:: ../../../figures/source_wms.png
     :scale: 80

* **Type**: Predefined service type selection (OGC WMS or OGC WMTS / TMS).

* **Service URL**: URL to the Capabilities document of the WMS service (e.g.: ``http://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities``)

* **Username / Password**: Input of the username and the password for secured services.

  In general, OGC WMS Capabilities refer to ``xsi:schemaLocation="http://www.opengis.net/wms http://schemas.opengis.net/wms/1.3.0/capabilities_1_3_0.xsd``. The supported namespaces in that schema are:
  
  * http://www.w3.org/1999/xlink,
  * http://www.opengis.net/wms,
  * http://www.w3.org/2001/XMLSchema


Update source
-------------
To update a source in the backend, you first need to navigate to the sources backend list. Find the layer you wish to update and click on the Refresh button to open its configuration settings.
You can then update the WMS: Modify the URL (or other settings, such as user name and/or password). If you don't want to update your source, click the Cancel button at the bottom to discard any changes.
If you want to save the changes, click the Load button to refresh the WMS.