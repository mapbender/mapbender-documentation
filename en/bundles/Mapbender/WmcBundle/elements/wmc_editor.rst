.. _wmc_editor:

WMC Editor
***********************

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

    title: WMC Editor
    tooltip: WMC Editor   # text to use as tooltip
    target: map           # name of map element
    accessGroups: [0,1]   # define groups that can use the WMC Editor

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


