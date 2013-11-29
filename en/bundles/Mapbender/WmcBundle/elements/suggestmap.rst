.. _suggestmap:

Suggest Map
***********************


**Notice:** that you need the element WMC Editor to use this functionality.

**Notice:** that all configurations are pubic at the moment. Later in development we want to add access control to this module too.



.. image:: ../../../../../figures/suggestmap.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/suggestmap_configuration.png
     :scale: 80

You need a button to show this element. See :doc:`button` for inherited configuration options.


YAML-Definition:

.. code-block:: yaml

    title: Suggest Map   
    tooltip: Suggest Map      # text to use as tooltip
    icon: iconSuggestMap      # choose an icon
    label: true               # add title as label
    target: wmceditor         # choose wmceditor as target
    action: open              #
    deactivate: close         #


Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\SuggestMap
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


