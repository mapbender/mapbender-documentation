.. _components:

Components
#####################

Mapbender3 is made up of different components. On the server side we use Symfony2 as a framework which comes along with powerfull components like Doctrine, Twig, Monolog and more.

On the client side we use OpenLayers, MapQuery and jQuery & jQuery UI.

We have a Mapbender core bundle with the Mapbender basic functionalities. And more Mapbender bundles which are optional.

We offer a Mapbender Starter package. With the Mapbender Starter package you can set up a Mapbender3 installation easily.

  .. image:: ../../figures/mapbender3_components.png
     :scale: 60




Symfony2
********

.. image:: http://symfony.com/images/common/logo/logo_symfony_header.png
  :scale: 60 %
  :alt: Symfony Project page
  :align: center
  :target: http://symfony.com/

Symfony2 is a full object oriented PHP Web Development Framework. It builds blocks for all modern web application needs. It is a collection of software and a development methodology. It relies on the philosophy of building blocks. It is optimized for speed. It uses Byte Code Cache.

Here comes just a list of some components Symfony offers:

* Symfony config.php to check the prerequisites
* Symfony Profiler 
* Database abstraction via Doctrine
* User authentication, authorization
* Templating via Twig
* Translation using xliff-files
* Logging via Monolog
* Security

The project has a very good documentation 

* http://symfony.com/symfony-in-five-minutes 
* TheBook http://symfony.com/doc/current/book/index.html


OpenLayers
**********
.. image:: http://www.openlayers.org/images/OpenLayers.trac.png
  :scale: 80 %
  :alt: OpenLayers Project page
  :align: center
  :target: http://openlayers.org/

OpenLayers is a powerfull software for web maps. It supports lot of data sources and functionality.

Read more about OpenLayers at http://openlayers.org/

You find example applications with OpenLayers at http://openlayers.org/dev/examples/


MapQuery
********
.. image:: http://mapquery.org/img/logo.png
  :scale: 80 %
  :alt: MapQuery Project page
  :align: center
  :target: http://mapquery.org/

MapQuery implements a jQuery interface to OpenLayers. It provides a set of mapping related widgets. In Mapbender3 MapQuery is used to interact with OpenLayers.

Read more about MapQuery at http://mapquery.org/

jQuery and jQuery UI
********************
.. TODO find a nice logo
  .. image:: http://upload.wikimedia.org/wikipedia/de/d/d3/Logo_jQuery.svg
  :scale: 60 %
  :alt: jQuery Project page
  :align: center
  :target: http://jquery.com/


jQuery is a feature-rich JavaScript library. jQuery UI is a set of user interface interactions, effects, widgets, and themes built on top of the jQuery JavaScript Library.  

 http://jquery.com

 http://jqueryui.com/


Mapbender3
**********
Mapbender3 is a collection of bundles. Only the MapbenderCoreBundle and the FOMBundles are mandatory.

There are optional bundles like:

* WMSBundle
* WMTSBundle
* WMCBundle
* MonitoringBundle


CoreBundle
~~~~~~~~~~
The Mapbender CoreBundle is the base bundle for Mapbender. It offers base classes for applications, elements, layers and more.

It provides jQuery, jQuery UI, OpenLayers and MapQuery for all other Mapbender bundles.

.. ToDo
  FOM Bundle

Mapbender Starter
*****************
Mapbender Starter is Symfony2 demo project which uses the Mapbender bundles to showcase a Mapbender3 application.

It contains demo applications which are defined in the mapbender.yml with WMS, WMTS. It provides a web interface with authentication which provides the possibility to create applications, create users/groups and build up a service repository.

Mapbender Starter can be used as a boiler template to start Mapbender3 projects.


External Repositories
*********************
You find more code connected to Mapbender3 at GitHub, which is not part of the main project. Other providers can offer Bundles for Mapbender3 like the DesktopIntegrationBundle which is provided by `WhereGroup <http://wheregroup.com>`__ and sponsored by customers.

WhereGroup offers Bundles for Mapbender3 at:
 https://github.com/WhereGroup


