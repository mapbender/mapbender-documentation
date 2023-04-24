.. _sources:

  .. |mapbender-button-update| image:: ../../../figures/mapbender_button_update.png

Sources
=======

With the sources backend tab, it is possible to register OGC sources into your applications. Further information about the registration process of services and their usage in Mapbender is available in the `Quickstart document <../../quickstart.html#loading-web-map-services>`_.

.. image:: ../../../figures/source_wms.png
     :width: 100%

* **Type**: Predefined service type selection (OGC WMS or OGC WMTS / TMS).

* **Service URL**: URL to the Capabilities document of the WMS service (e.g.: ``http://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities``)

* **Username / Password**: Input of the username and the password for secured services.


In general, OGC WMS Capabilities refer to ``xsi:schemaLocation="http://www.opengis.net/wms http://schemas.opengis.net/wms/1.3.0/capabilities_1_3_0.xsd``. The supported namespaces in that schema are:
  
  * http://www.w3.org/1999/xlink,
  * http://www.opengis.net/wms,
  * http://www.w3.org/2001/XMLSchema


Updating sources
----------------
To update a source in the backend, you first need to navigate to the ``Sources`` backend list.
On this page, look for the layer you wish to update via scrolling or use the search box.
After you've found it, click on its |mapbender-button-update| ``Refresh`` button.
You can then update the WMS: If you wish, modify the URL or other settings, such as user name and/or password.

.. hint:: Of course, it is possible to update a source without changing any parameters.

Moreover, there are two checkboxes handling layer updates:

* **Activate newly added layers**: If active, the newly added layers will automatically set active in embedded applications.
* **Select newly added layers**: If active, the newly added layers will automatically be visible in embedded applications. Note: They must also be activated to be displayed in the map area.

If you don't want to update your source, click the ``Cancel`` button at the bottom to discard any changes.
If you want to save the changes or simply update the source, click the ``Load`` button to refresh the WMS.