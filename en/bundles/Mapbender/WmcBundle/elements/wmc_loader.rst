.. _wmc_loader:

WMC Loader
***********************

**Notice:** this functionality will come in Mapbender3 Version 3.0.1.

Mapbender can save configurations (see WMC Editor). This configurations can be loaded with the element WMC loader.

You can add WMC Loader to your application as a selectbox or a button which opens a dialog.

When you choose a configuration, the services in the configuration will be merged in your existing application.

.. image:: ../../../../../figures/wmc_loader.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/wmc_loader_configuration.png
     :scale: 80

You can configure this module as a selectbox or dialog. When you use dialog then you need a button to show this element. See :doc:`button`_ for inherited configuration options.


YAML-Definition:

.. code-block:: yaml

   foo: bar # Example, delete me!


Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\WmcLoader
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


HTTP Callbacks
==============


<action>
--------------------------------



JavaScript API
==============


<function>
----------


JavaScript Signals
==================

<signal>
--------


