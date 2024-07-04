.. _fom:

 .. |mapbender-button-add| image:: ../../../figures/mapbender_button_add.png
 .. |mapbender-button-edit| image:: ../../../figures/mapbender_button_edit.png

Security (FOMUserBundle)
========================

The security for domain objects is implemented in Mapbender using a permission system.
It allows global authorizations for areas and individual authorizations for objects.
Therefore, it provides flexible permissions and security for the following entities:

.. toctree::
   :maxdepth: 1

   Applications<../applications/applicationsecurity>
   ../sources
   users
   roles_groups


.. important:: Assign rights to an entity via ``Security`` → ``Global Permissions``.


Permission management
*********************

An authorized user can manage global or individual permissions to secure the domain objects. Mapbender provides the following permission rights:

- **Create**: Create a new object
- **View**: View an existing object
- **Edit**: Edit an existing object
- **Delete**: Delete an existing object
- **Manage Permissions**: Allow permission editing  
- **Refresh**: Allow source refreshing  

Add users and groups to this area via ``Security`` → ``Global permissions`` → ``Permission management`` so that they have access to manage permissions.

