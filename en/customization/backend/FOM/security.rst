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

Assign roles to a user by ``Users → Edit your User → Security``.

  .. image:: ../../../../figures/mapbender_roles.png
     :width: 100%


Assign an Application to a User/Group
*************************************

#. Edit your application by ``Application → Edit-Button``.

#. Choose ``Security``.

#. Publish your application for everyone by clicking ``Security → public access`` or in the application overview by clicking the ``Publish`` button.

#. Alternatively and for an individual configuration, click the ``Add users and groups`` button and configure your selection. Then, set permissions like view, edit, delete, operator, master or owner via the rights table.

#. Logout from Mapbender by ``Logout`` and log in again with a configured account to test the configuration.

#. Another method would be to choose ``Security → Global Access Control Lists → Applications`` to quickly set permissions for several users/groups to all applications.

  .. image:: ../../../../figures/mapbender_security.png
     :width: 100%


Assign single elements to a User/Group
**************************************

Per default, all elements are available to all users/groups that have permission to an application. It is possible to hide single elements from individual users/groups like this: 

#. Edit your application by clicking ``Application → Edit``.

#. Choose ``Layouts``.

#. Every element has a ``ACL element`` button (key). Choose the ``ACL element`` button from the element that should be only availale for selected users/groups.

#. Now, add the users/groups via the ``Add users and groups`` button. Then, set permissions like view, edit, delete, operator, master or owner via the rights table.

#. Test your configuration. For example, open the application with a user account that has (no) rights to a previously configured element. 

  .. image:: ../../../../figures/fom/element_security_key_popup.png
     :width: 100%


Assign a user to another User/Group
***********************************

#. Edit a user by clicking ``Security → Users``.

#. In the user administration, choose ``Security``.

#. Give users/groups individual rights on the selected user: Add users/groups via the ``Add users and groups`` button. Thereafter, set permissions within the rights table.

#. You have now assigned a user/group controlling options over another user account. Test your configuration with the entitled user accounts.
