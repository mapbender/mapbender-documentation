.. _view_manager:

View Manager
************

View Manager stores and reapplies custom map states. These contain the following map parameters:

* Center
* Layers of :ref:`sources`
* Selected :ref:`layerset`
* Rotation
* Scale
* Source opacities
* SRS

Saved states are always reapplied on top of the current configuration. This means that changed application configurations will remain in effect even after reloading the page.

.. image:: ../../../figures/view_manager_overview.png
     :scale: 80


.. note:: Thus far, View Manager can only be implemented in the Sidepane.

Basic operations
----------------

Each state must be given a title for reidentification. For saving the current map view as a new state, enter a title and click on the adjoined save button.

.. image:: ../../../figures/view_manager_create_map_state.png
     :scale: 80

The most basic interaction (always available) is re-applying the map state stored in the entry. This option is always on: The saved map state will be reapplied as soon as "Apply" is hit on the selected map state in list view. Moreover, entries may offer a "Replace" interaction. This will overwrite the map state stored in the entry, and will also update the title, using the global title input field. Also, entries may offer a "Delete" interaction (with an extra confirmation step).

The View Manager does **not** store or reapply the following configurations:

* any interactively added sources (via :ref:`wms_loader`)
* any interactively removed layers (via :ref:`layertree` context menu)
* any values for WMS dimensions
* any dynamically rendered geometries (:ref:`digitizer` etc.)


Access rights
-------------

Each map state is attributed to an application and further separated into a public and user-private list. The rights to save, reapply or delete map states are defined in the element configuration. Furthermore, rights to show private lists and dates as well as the permission for anonymous users to save map states can be set here.

In general, access checks on public entries are suspended for the root user. The administrator can create, update and delete public entries at will.

Anonymous users are excluded from working with private entries and they can never delete public entries. Their ability to create and update public entries is gated through the "Allow saving to anonymous users" option. If this checkbox is deactivated, their access to public entries is downgraded to read-only. If the goal is to exclude anonymous visitors completely, a ROLE_USER access restriction has to be set on the entire element.


Configuration
=============

.. image:: ../../../figures/view_manager_configuration.png
     :scale: 70

Controlling URL parameters
--------------------------

.. image:: ../../../figures/view_manager_viewid.png
     :scale: 70

Mapbender provides the ability to call different saved views using the ``viewid`` parameter in the URL. This feature allows users to quickly switch between predefined views of the map application, as demonstrated in the screenshot.

Each saved view is assigned a unique ID, which can be used to load the corresponding view directly. For example, the view titled "Poppelsdorfer Schloss" can be accessed using the following URL parameter:

.. code-block:: php

     ?viewid=1

By appending this parameter to the application's URL, Mapbender will automatically load the saved view associated with the specified ID.

YAML-Definition
---------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

  viewmanager:
    title: View Manager                              # Title of the element
    class: Mapbender\CoreBundle\Element\ViewManager  # Path to element class
    publicEntries: rw                                # String or empty (falsy value disables public entries entirely); other allowed values are ro (read only), rw (allow read and write), rwd (allow read and write and deletion) (default: ro).
    privateEntries: true                             # Turns user-private states on, with full usage (save, reapply, delete) (default: true).
    allowAnonymousSave: true                         # Extend right to save public entries also to anonymous users (default: false).
    showDate: true                                   # Show date of creation or last update in entry listing (default: true).