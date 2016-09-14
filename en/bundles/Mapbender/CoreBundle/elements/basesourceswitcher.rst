.. _basesourceswitcher:

BaseSourceSwitcher
******************

BaseSourceSwitcher is a button group to change the map's background sources. The BaseSourceSwitcher allows you to switch over between the predefined source sets. For every sourceset a button will be displayed in the client. Notice that only one button can be active.

You have the possibility to define groups. All sourcesets of the same group will be listed in a dropdown list with the group name as title.


.. image:: ../../../../../figures/basesourceswitcher.png
     :scale: 80

Configuration
=============

The configuration occurs in 2 steps: 

#. Create a BaseSourceSwitcher Element with Title, Tooltip and Target
#. Add Sourceset/s with one or more sources and definition of a group (optional)

.. image:: ../../../../../figures/basesourceswitcher_configuration.png
     :scale: 80

* **Title:** Title of the element.
* **Tooltip:** The text entered as a tooltip will be indicated by hovering over the element with the mouse cursor a longer time.
* **Target:** Id of Map element, activated after the click.
* **Instances:** List of Sourcesets, defined by a title and group: (optional) group name to group of sourcesets by "group name" 


YAML-Definition:
----------------

.. code-block:: yaml

    title: 'BaseSourceSwitcher'                         # title
    tooltip: 'BaseSourceSwitcher'                       # text to use as tooltip
    target: map                                         # Id of Map element
    sourcesets:                                         # List of sourcesets
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}                        # sourceset: title,
                                                        # group: (optional) group name to group of sourcesets by "group name"
                                                        # sources list of sources
        

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\BaseSourceSwitcher
* **Widget:** mapbender.element.basesourceswitcher.js


HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
