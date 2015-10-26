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

Login failures are responded with the Message "Bad credentials". For
security reasons it is not shown if the error is is based on a wrong
username or a wrong password. Login failures will not lock the account
indefinately after four attempts.  Rather the account will be locked for a
given period of time.

The config.yml allows to adjust the behaviour:

.. code-block:: yaml

   fom_user:

       # Allow to create user log table on the fly if the table doesn't exits.
       # Default: true
       auto_create_log_table: true
       
       # Time between to check login tries
       login_check_log_time: "-5 minutes" 
       
       # Login attemps before delay starts
       login_attempts_before_delay: 3
       
       # Login delay after all attemps are failed
       login_delay_after_fail: 2 # Seconds
   

* **auto_create_log_table:** Backwards compatibility parameter (default: true).
* **login_check_log_time:** Cleaning of the login-failure table (default: -5 minutes)
* **login_attempts_before_delay:** Number of login failures before the login delay starts (default: 3)
* **login_delay_after_fail:** Number of seconds of the login-delay (default: 2).
