.. _roles_groups:

Roles and Groups
================

Roles are used for global permission checks when no domain object is involved and can be used as security identities of Access Control Entries in Access Control Lists of domain objects.

In Mapbender, there are currently two roles for rights allocation in the backend available:

* All authenticated users: Gives global set permissions for one or more domain object to all users that are logged in while working with Mapbender.
* Anonymous users: Sets global permissions for users which are browsing Mapbender without an individual account.

Groups are individually created database entities which can be assigned to one or more users. Therefore their primary use is to collect rights which are assigned to every user of that group.
