.. _share:

Share
*****

Application Switcher
====================

This element allows the user to switch from one application to another. When selecting to jump to another application, the current map view parameters (center, scale, srs, rotation) will be retained.

The Application Switcher can be implemented into the toolbar or footer of an application. Frontend users define themselves to which of the predefined applications they want to be able to switch to. 

The backend element dialogue offers the currently available applications a user can potentially switch to. Select one or more applications in the list to add them to the Application Switcher. Moreover, switched-to applications can be configurated to automatically open in a new browser tab with the checkbox "Open in new tab".

.. image:: ../../../figures/application_switcher.png
     :scale: 80


YAML-Definition:
----------------

.. code-block:: yaml

  applications: ['mapbender_user', 'mapbender_mobile', 'mapbender_user_basic']   # Definition of the switchable applications
  open_in_new_tab: false                                                         # Open application in a new tab (Default: false). 

