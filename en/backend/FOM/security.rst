.. _security:

Security Concepts
#################

Security as provided by the FOMUserBundle is anchored on these base concepts:

- :doc:`Users <users>`
- :doc:`Roles and Groups <roles_groups>`
- :doc:`ACL <acl>`


Rights management
*****************

Mapbender provides different rights. They refer to the :doc:`Access Control Lists (ACL) <acl>`.

* view - Whether someone is allowed to view the object.
* edit - Whether someone is allowed to make changes to the object.
* delete - Whether someone is allowed to delete the object.
* operator - Whether someone is allowed to perform all of the above actions.
* master - Whether someone is allowed to perform all of the above actions and in addition is allowed to grant any of the above mentioned permissions to others.
* owner - Whether someone owns the object. An owner can perform any of the above actions and grant master and owner permissions.

Assign roles to a user by **Users** → **Edit your User** → **Security**.

  .. image:: ../../../figures/mapbender_roles.png
     :width: 100%


Assign a user to another User/Group
***********************************

#. Edit a user by clicking **Security** → **Users**.

#. In the user administration, choose **Security**.

#. Give users/groups individual rights on the selected user: Add users/groups via the **Add users and groups** button. Thereafter, set permissions within the rights table.

#. You have now assigned a user/group controlling options over another user account. Test your configuration with the entitled user accounts.
