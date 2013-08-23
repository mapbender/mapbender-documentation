.. _wmc_editor:

WMC Editor
***********************

**Notice:** this functionality will come in Mapbender3 Version 3.0.1.

Mapbender can save and edit configurations with the WMC Editor. This configurations can be loaded with the element WMC loader (see WMC Loader).

You can add WMC Editor to your application. Notice that the editor needs a button to open.

The Editor offers the possibility to create and update configurations. You can save configurations with a title, desciption and upload a screenshot.

**Notice:** that all configurations are pubic at the moment. Later in development we want to add access control to this module too.



.. image:: ../../../../../figures/wmc_editor.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/wmc_editor_configuration.png
     :scale: 80

You need a button to show this element. See :doc:`button` for inherited configuration options.


YAML-Definition:

.. code-block:: yaml

   foo: bar # Example, delete me!


Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\WmcEditor
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


HTTP Callbacks
==============


<action>
--------------------------------

Opens a dialog with an editor in which configurations can be saved and edited.


JavaScript API
==============


<function>
----------


JavaScript Signals
==================

<signal>
--------


