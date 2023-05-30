.. _applicationsecurity:

Security (Application tab)
##########################
Each application has its own security tab. Here, you can set individual permissions for a single application or its elements.


Assign an Application to a User/Group
*************************************

Per default, all applications are available to all users/groups that have specific permissions to the backend. Nethertheless, it is possible to hide applications from individual users/groups: 

#. Edit your application by clicking **Application**.

#. Choose **Security**.

#. Publish your application for everyone by clicking **Security** → **public access** or in the application overview by clicking the **Publish** button.

#. Alternatively and for an individual configuration, click the **Add users and groups** button and configure your selection. Then, set permissions like view, edit, delete, operator, master or owner via the rights table.

#. Logout from Mapbender by **Logout** and log in again with a configured account to test the configuration.

#. Another method would be to choose **Security** → **Global Access Control Lists** → **Applications** to quickly set permissions for several users/groups to all applications.

  .. image:: ../../../figures/mapbender_security.png
     :width: 100%


Assign single elements to a User/Group
**************************************

Per default, all elements are available to all users/groups that have permission to an application. It is possible to hide single elements from individual users/groups: 

#. Edit your application by clicking **Application**.

#. Choose **Layouts**.

#. Every element has a ``ACL element`` button (key). Choose the **ACL element** button from the element that should be only availale for selected users/groups.

#. Now, add the users/groups via the **Add users and groups** button. Then, set permissions like view, edit, delete, operator, master or owner via the rights table.

#. Test your configuration. For example, open the application with a user account that has (no) rights to a previously configured element. 

  .. image:: ../../../figures/fom/element_security_key_popup.png
     :width: 100%
