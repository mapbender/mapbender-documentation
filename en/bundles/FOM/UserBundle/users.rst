Users
=====

User are implemented as FOM\\UserBundle\\Entity\\User and stored in the database.
The entity has only some basic information about the user itself, more complex
user data will have to be implemented by user profiles (yet to be done).

The bundles provides all means to administrate users by admin as well as self-
registration and password recovery.

The user with the id 1 is special, as this user is created during installation
and will always be given full access. If all is lost, you can use this user
to manage everything. And in the event that the credentials for this user are
also lost, a console command (fom:user:resetroot) is available for resetting.

Login Failures
--------------

Login failures will not lock the account indefinately after four attempts.
Rather the account will be locked for a given period of time where the time
depends on the number of unsuccessful attempts. The time grows exponentially
with the attempts and starts with one second for the first failure:

    1. 1s
    2. 2s
    3. 4s
    4. 8s
    5. 16s
    6. 32s
    7. 64s
    8. 128s
    9. 256s
    10. ...


After that time, the user may try to login again.

