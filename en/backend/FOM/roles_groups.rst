.. _roles_groups:

Groups and Roles
================

Groups
******
Groups are individually created database entities that can be assigned to one or more users.
Their primary use case is to distribute a set of permissions which are assigned to every user of that group.
Assuming that an account has the permission, groups will be created and configured via ``Security`` → ``Groups`` → ``Add new group``.
Mapbender offers an overview over every group at the same place:

  .. image:: /figures/mapbender_security_group_overview.png
   :scale: 70

Roles
*****
Roles are used for global permission checks, even if no other permission structure (e.g., a group membership) is involved. They can be used as security identities for domain objects.
In Mapbender, there are currently two roles for permission allocation available:

* **Public Access**: Sets global permissions for users which are browsing Mapbender without an individual account.
* **All authenticated users**: Gives global permissions for one or more entities to all users that are logged in while working with Mapbender.

Depending on the context, roles can be assigned authorizations in the ``Security`` tab of an application or under ``Global permissions``.
An individual application could be secured as follows:

  .. image:: /figures/mapbender_roles_application_overview.png
   :scale: 70
