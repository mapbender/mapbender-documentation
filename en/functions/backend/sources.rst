.. _sources:

Sources
=======

With Sources, you can register OGC WMS and OGC WMTS/TMS services in version 1.1.1 and 1.3.0 in Mapbender.

Further information about the registration process of services and their usage in Mapbender applications is available in the `Quickstart document <../../quickstart.html#loading-web-map-services>`_.


Load sources
------------

.. tip:: It is important to check the service before it is registered in Mapbender. To do that, open the getCapabilities-Request (see example in Service URL) in your browser.

To register a service, click on ``Add source``:

* **Type**: Mandatory service type selection (OGC WMS or OGC WMTS / TMS).

* **Service URL**: URL to the Capabilities document of the service (e.g. OGC WMS (1.3.0): ``http://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities``)

* **Username / Password**: Input of the username and the password for secured services.

Click on ``Load`` to register the service to the repository.

  .. image:: ../../../figures/mapbender_add_source.png
     :scale: 80


After a successful registration, Mapbender will provide an overview of the service.


Sources Overview
----------------

The sources and shared instances sections list and provide additional information about the services registered in Mapbender:

* **Filter**: Search for services names, URLs, types and descriptions.
* **Show metadata**: Shows metadata about a specific service. Opens a new field that lists specific metadata, Mapbender applications that use the source, contact information, details (e.g. service version) and layers.
* **Update source**: Updates service information by reloading the getCapabilities document.
* **Delete source**: Removes the registered service from Mapbender.


  .. image:: ../../../figures/mapbender_sources.png
     :scale: 80


Sources menu button
-------------------

In the metadata dialog of a specific service, it is also possible to click on the menu button (top right) that allows:

* **Update source**: Updates service information by reloading the getCapabilities document.
* **Create shared instance**: Creates a new shared instance from the specific service. The instance is listed in the Shared instances tab.
* **Delete**: Removes the registered shared instance from Mapbender.

  .. image:: ../../../figures/source_overview.png
     :scale: 80
