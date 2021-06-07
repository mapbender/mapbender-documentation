.. _share:

Share
*****

Applikation Switcher
====================

The element allows the user to switch from a current application to another one. When selecting an application, the current view parameters (center, scale, srs, rotation) will be retained.

The Application Switcher can be implemented in toolbar or footer. Users define themselves, to which applications they want to be able to switch to. (Note: Definitions are only possible according to access rights.)

Applications can be configurated to open up in a new tab.

.. image:: ../../../figures/application_switcher.png
     :scale: 80


YAML-Definition:
----------------

.. code-block:: yaml

  applications: ['mapbender_user', 'mapbender_mobile', 'mapbender_user_basic']   #Definition of the switchable applications
  open_in_new_tab: false                                                         #Opens application in a new tab (Default=false). 

