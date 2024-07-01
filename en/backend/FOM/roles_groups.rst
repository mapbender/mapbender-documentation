.. _roles_groups:

Groups and Roles
================

Groups are individually created database entities that can be assigned to one or more users. Their primary use case is to distribute a set of permissions which are assigned to every user of that group.

Roles are used for global permission checks when no other permission structure (e.g., a group membership) is involved. They can be used as security identities for domain objects.

In Mapbender, there are currently two roles for rights allocation available:

* Public Access: Sets global permissions for users which are browsing Mapbender without an individual account.
* All authenticated users: Gives global permissions for one or more entities to all users that are logged in while working with Mapbender.

