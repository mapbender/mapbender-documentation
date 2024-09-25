.. _applicationsecurity:

 .. |mapbender-button-add| image:: ../../../figures/mapbender_button_add.png
 .. |mapbender-button-edit| image:: ../../../figures/mapbender_button_edit.png
 .. |mapbender-button-key| image:: ../../../figures/mapbender_button_key.png
 .. |mapbender-button-publish| image:: ../../../figures/mapbender_button_publish.png

Security (Application tab)
##########################

Each application has its own security tab. There, you can set individual permissions for a single application or its elements.

.. note:: A set global permission overwrites an individual permission set on this page.

Assign an Application to a User/Group
*************************************

Per default, all applications are available to all :ref:`users` and :ref:`roles_groups` that have specific permissions to the :ref:`backend`. Nethertheless, it is possible to hide applications from individual accounts: 

#. Edit your application by clicking |mapbender-button-edit|.

#. Choose the **Security** tab.

#. Publish your application for everyone by clicking **Security** → **public access** or in the application overview by clicking **Toggle public access** |mapbender-button-publish|.

#. For an individual configuration, click the **Add users and groups** button and configure your selection. Then, set permissions like view, edit or delete the permission table.

#. Logout from Mapbender and log in again with a configured account to test the configuration.

#. Another method would be to choose **Security** → **Global Permissions** → **Applications** to quickly set global application rights for several users or groups.

  .. image:: ../../../figures/mapbender_security.png
     :width: 100%


Assign single elements to a User/Group
**************************************

Per default, all elements of an application are available to all :ref:`users` and :ref:`roles_groups` that have permission to it. It is possible to hide single elements from individual accounts: 

#. Edit your application by clicking |mapbender-button-edit|.

#. Choose the **Layouts** tab.

#. Every element has a |mapbender-button-key| *Restrict element access* button. Use it for the element that should be only availale for selected users/groups.

#. Now, add the users/groups via the **Add users and groups** button. Then, set permissions like view, edit or delete via the rights table.

#. Test your configuration. For example, open the application with a user account that has (no) rights to a previously configured element. 

  .. image:: ../../../figures/fom/element_security_key_popup.png
     :width: 100%
