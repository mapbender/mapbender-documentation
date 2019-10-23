.. _installation_configuration:

Details of the configuration of Mapbender
=========================================

Configuration steps
-------------------

Following we describe the configuration steps of Mapbender a bit further. Configuring your Mapbender installation is made up of the following six steps:

* Creating the database
* Creating the database schema
* Copying the bundles' assets to the public web directory
* Creating the "root" user
* Inserting srs parameters (EPSG code definition)
* Loading the applications of the mapbender.yml to your database

All can be done using the console utility provided by `Symfony <http://symfony.com/>`_, on which Mapbender framework is built upon. There's a mayor caveat though you should understand, before continuing:

.. note:: The console utility will write files in the app/cache and app/logs directories. These operations are made using the user permissions of whatever user you're logged in with. This is also true for the app/db directory and the SQLite database within. When you open the application from within the browser, the server PHP process will try to access/write all these files with other permissions. So make sure you give the PHP process write access to these files. See last step below.

.. note:: **Notice:** The following steps assume that you are in the directory above the app directory (notice that for git installation that means mapbender/application/ else mapbender/).

.. code-block:: yaml

   cd mapbender/
   or for git based installation 
   cd mapbender/application



Adapting the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Database connection parameters are stored together with some more configuration parameters in the file ``app/config/parameters.yml``. 

More Information: :ref:`yaml_en`.

Creating the database
^^^^^^^^^^^^^^^^^^^^^

Symfony can attempt to create your database, this works of course only if the
configured database user is allowed to. Call the console utility like this:

.. code-block:: yaml

   app/console doctrine:database:create


Creating the database schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Symfony will create the database schema for you:

.. code-block:: yaml

    app/console doctrine:schema:create



Copying the assets bundles
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each bundle has it's own assets - CSS files, JavaScript files, images and more -
but these need to be copied into the public web folder:

.. code-block:: yaml

    app/console assets:install web


Alternatively, as a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Creating the administrative user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first user - which has all privileges - must be created using the command:

.. code-block:: yaml

    app/console fom:user:resetroot

This will interactively ask all information needed and create the user in the
database.

Alternatively, there is a silent mode you can use, if you want to use a script to install Mapbender and don't want to be asked for all parameters:

.. code-block:: yaml

    app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent

Inserting SRS parameters
^^^^^^^^^^^^^^^^^^^^^^^^

Inserting Proj4 SRS parameters into a database can be done using the command:

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append

Importing applications from application/app/config/applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See chapter: :ref:`yaml_en`.


Configuration files
-------------------

The basic configuration is done inside the **app/config/parameters.yml** file. 

More Information: :ref:`yaml_en`.


Production- and Development environment and Caching: app.php and app_dev.php
-----------------------------------------------------------------------------

Mapbender provides two environments: a production-environment for the
general operation and a development-environment in which the application can
be testet. This concept follows the `"environments" in the Symfony framework
<http://symfony.com/doc/current/book/configuration.html>`_.

The production-environment is called with the URL
http://localhost/mapbender/app.php, the development-environment with the
URL http://localhost/mapbender/app_dev.php. The call with app_dev.php is
and should only be available from localhost.

There are differences in the behaviour of app.php and app_dev.php:

* The cache-mechanism of the development-environment behaves different: Not
  all files are cached, so that the code-changes are directly
  visible. Therefore is the usage of the app_dev.php always slower that the
  production-environment.

  In detail, the development-environment of Mapbender does not cache the
  CSS, JavaScript and Translation files, among others.

  The production-environment caches all theses files and puts them into the
  app/cache folder.

* The development-environment gives out error-messages and stack-traces out
  to the user-interface. The production-environment logs them into the file
  app/log/prod.log.

* The development-environment shows the Symfony Profiler. This tool logs
  things, that are important for developers but should not be visible for
  common users.

  .. image:: ../../figures/symfony_profiler.png
             :scale: 80
  

The directory app/cache contains the cache-files. It contains directories
for each environment (prod and dev) but the mechanism of the dev-cache, as
described, behaves different.

If changes of the Mapbender interface or the code are made, the
cache-directory (app/cache) has to be cleared to see the changes in the
application.

The following screenshots shows the location of the cache-directory in
Mapbender:

.. image:: ../../figures/mapbender_cache_directories.png 
           :scale: 80



Deleting the cache
------------------

Especially in development or testing environments it may be required to delete the internal symfony cache. You can do this using the following console command:

.. code-block:: bash

                app/console cache:clear

Alternatively, you can remove all data within the Mapbender cache directory by using the following command. Be careful!

.. code-block:: bash

                rm -rf app/cache/*


More detailed information regarding the cache can be found under the appropriate symfony documentation page: https://symfony.com/doc/current/console/usage.html



Logging in Mapbender
--------------------

The Log-Level is defined in the files ``config_dev.yml`` and ``config_prod.yml``. These files are placed in the folder ``application/app/config/``. The config-files are for the different environments (see `production- and development environment <configuration.html#production-and-development-environment-and-caching-app-php-and-app-dev-php>`_).

For the development-environment (at the development on local systems) Mapbender is called with ``app_dev.php`` and therefore the file ``config_dev.yml`` is responsible. In the production-environment, where the ``app.php`` file is used, the configuration from ``config_prod.yml`` is applied.


Loglevel
^^^^^^^^

Overall, 6 log-levels are used:

* DEBUG (100): Detailed debug information.
* INFO (200): Interesting events. Examples: User logs in, SQL logs.
* NOTICE (250): Normal but significant events.
* WARNING (300): Exceptional occurrences that are not errors. Examples: Use of deprecated APIs, poor use of an API, undesirable things that are not necessarily wrong.
* ERROR (400): Runtime errors that do not require immediate action but should typically be logged and monitored.
* CRITICAL (500): Critical conditions. Example: Application component unavailable, unexpected exception.
* ALERT (550): Action must be taken immediately. Example: Entire website down, database unavailable, etc. This should trigger the SMS alerts and wake you up.
* EMERGENCY (600): Emergency: system is unusable.

This description of the log-level is analog to the `IETF Syslog Protocol <http://tools.ietf.org/html/rfc5424>`_.


config_dev.yml
^^^^^^^^^^^^^^

You find the responsible part of the ``config_dev.yml`` in the section "monolog":

.. code-block:: yaml
                
    monolog:
        handlers:
            main:
                type:  stream
                path:  %kernel.logs_dir%/%kernel.environment%.log
                level: debug
            firephp:
                type:  firephp
                level: info

Two "handler" are described: ``main`` und ``firephp``.

* **main:** The handler ``main`` is set to the log-level ``debug`` and streams all entries in a file which is defined unter ``path``. This file is defined with variables which means that the file ``dev.log`` is placed under the folder ``application/app/logs/``.

* **firephp:** The handler ``firephp`` can communicate with an appropriate  Extension of the web browser. The developer can therefore see the debug-messaged directly in the web browser without opening the log files.

These are the preferred settings for development tasks.



config_prod.yml
^^^^^^^^^^^^^^^

.. code-block:: yaml

    monolog:
        handlers:
            main:
                type:         fingers_crossed
                action_level: error
                handler:      nested
            nested:
                type:  stream
                path:  "%kernel.logs_dir%/%kernel.environment%.log"
                level: debug


This settings lead to a two-step logging. Here we have also two handlers: ``main`` and ``nested``.

* **main:** The ``main`` handler ist a type ``fingers-crossed`` and set to the ``error`` level. This means, the error is only active when an error occurs.

* **nested:** The ``main``-Handler calls the ``nested`` handler, which writes the entries into the ``prod.log`` file.

  Per default the handler is set to ``debug`` so that on an error also the debug-messages are written into the ``prod.log`` file.

  If you want to disable the debug-messages you can set here also the log-level ``error``.


**Further links:**

* In the package "monolog":
  
  * `Using Monolog <https://github.com/Seldaek/monolog/blob/master/doc/01-usage.md>`_
  * `Handlers, Formatters and Processors <https://github.com/Seldaek/monolog/blob/master/doc/02-handlers-formatters-processors.md>`_
  
* `Symfony, Monolog and different log types <http://www.whitewashing.de/2012/08/26/symfony__monolog_and_different_log_types.html>`_. Blog-entry by Benjamin Eberlei.
