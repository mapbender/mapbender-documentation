.. _installation_configuration:

Details of the configuration of Mapbender
=========================================

Configuration steps
-------------------

In the following, we will describe the configurational steps of Mapbender a bit further. Configuring your Mapbender installation consists of the following six steps:

* Creating the database
* Creating the database schema
* Copying the bundles' assets to the public web directory
* Creating the "root" user
* Initializing the database
* Loading the applications of the mapbender.yml to your database

All that can be done using the console utility provided by `Symfony <http://symfony.com/>`_, on which the Mapbender framework is built upon. There's a mayor caveat though you should understand before continuing:

.. note:: The console utility will write files in the var/cache and var/logs directories. These operations are made using the user permissions of whatever user you're logged in with. This is also true for the var/db directory and the SQLite database within. When you open the application from within the browser, the server PHP process will try to access/write all these files with other permissions. So make sure you give the PHP process write access to these files. See last step below.

.. note:: **Important:** The following steps assume that you are in the directory above the app directory (notice that for git installation that means mapbender/application/, else mapbender/).

.. code-block:: yaml

   cd mapbender/
   or for git based installation 
   cd mapbender/application



Adapting the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Database connection parameters are stored together with some more configuration parameters in the file ``app/config/parameters.yml``. 

More Information: :ref:`yaml`.

Creating the database
^^^^^^^^^^^^^^^^^^^^^

Symfony can attempt to create your database, this works of course only if the
configured database user is allowed to do so. Call the console utility like this:

.. code-block:: yaml

   bin/console doctrine:database:create


Creating the database schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Symfony will create the database schema for you:

.. code-block:: yaml

    bin/console doctrine:schema:create



Copying the assets bundles
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each bundle has its own assets - CSS files, JavaScript files, images and more -
but these need to be copied into the public web folder:

.. code-block:: yaml

    bin/console assets:install web


Alternatively, as a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier.

.. code-block:: yaml

   bin/console assets:install web --symlink --relative


Creating the administrative user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first user - which has all privileges - must be created using the command:

.. code-block:: yaml

    bin/console fom:user:resetroot

This will interactively ask all information needed and create the user in the
database.

Alternatively, there is a silent mode you can use, if you want to use a script to install Mapbender and don't want to be asked for all parameters:

.. code-block:: yaml

    bin/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent

Initialize the database
^^^^^^^^^^^^^^^^^^^^^^^

Initializing the database can be done using the command:

.. code-block:: yaml

    bin/console mapbender:database:init

Importing applications from application/app/config/applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to (re-)import applications from the applications folder into the database with the command:

.. code-block:: yaml

    bin/composer run reimport-example-apps


Configuration files
-------------------

The configuration files are located under **app/config**.

Find more information in: :ref:`yaml`.

.. _app_cache:

Production and Development environment and Caching: app.php and app_dev.php
---------------------------------------------------------------------------

Mapbender provides two environments: a production environment for the
general operation and a development environment in which the application can
be tested. This concept follows the `"environments" in the Symfony framework
<http://symfony.com/doc/current/book/configuration.html>`_.

The production environment is called with the URL
http://localhost/app.php, the development environment with the
URL http://localhost/app_dev.php. The call with app_dev.php is
and should only be available from localhost.

There are differences in the behaviour of app.php and app_dev.php:

* The cache mechanism of the development environment behaves differently: Not
  all files are cached, thus code changes are directly
  visible. Therefore, the usage of app_dev.php is always slower than the
  production environment.

  In detail, the development environment of Mapbender does not cache the
  CSS, JavaScript and Translation files, among others.

  The production environment caches all these files and puts them into the
  var/cache folder.

* The development environment gives out error messages and stack traces
  to the user interface. The production environment logs them into the file
  app/log/prod.log.

* The development environment shows the Symfony Profiler. This tool logs
  things that are important for developers but are not supposed to be visible for
  common users.

The directory var/cache contains the cache files. It contains directories
for each environment (prod and dev). But the mechanism of the dev-cache, as
described before, behaves differently.

If changes of the Mapbender interface or the code are made, the
cache directory (var/cache) has to be cleared to see the changes in the
application.
