.. _examples:

Examples
=========

Reset User with ID 1
--------------------

The command ``app/console fom:user:resetroot`` resets the user with ID 1. This user owns generally all rights.

.. code-block:: bash
          $ app/console fom:user:resetroot
                Welcome to the Mapbender root account management command  
                Enter the username to use for the root account.
                Username [root]: root
                Enter the e-mail adress to use for the root account.
                E-Mail [root@root.de]: admin@mycompany.foo
                Enter the password to use for the root account.
                Password: secret
                Do you confirm reset [yes]? yes
                The root is now usable. Have fun!

Create new user
---------------

The root user (ID 1) can create new users. A user itself can create a new user if he owns the Owner role in the ACL "users". We chose this exception of the rules to avoid other users changing their user-name.


Create new applications
-----------------------

A user who would like to create new applications has to have the Create right in the ACL "Applications". Once that right is permitted, the user can also import and export applications.


Configure sources
-----------------

To get permission to the ``Sources`` tab and work with sources in the Mapbender backend, a specified user (or group member) needs the ``Edit`` right in the Global Access Control Lists. 


Copy applications
-----------------

A user can copy applications if he has the ``Edit`` right in ACL "Applications" or within the application itself. The right of the application overwrites the global ACL right.

Thereby, the user automatically becomes the owner of the copied application.


Delete applications
-------------------

A user can delete applications if he has the ``Delete`` right  in the ACL "Applications" or within the application itself. The right of the applications overwriters the global ACL right.
