Users
=====

User are implemented as FOS\UserBundle\Entity\User and stored in the database.
The entity has only some basic information about the user itself, more complex
user data will have to be implemented by user profiles (yet to be done).

The bundles provides all means to administrate users by admin as well as self-
registration and password recovery.

The user with the id 1 is special, as this user is created during installation
and will always be given full access. If all is lost, you can use this user
to manage everything. And in the event that the credentials for this user are
also lost, an console command (fom:user:resetroot) is available for resetting.