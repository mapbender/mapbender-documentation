Installation
############

This document describes all neccessary steps in order to get an running
Mapbender3 installation.

Prerequisites
*************

Mapbender3 needs the following components in order to run:

* PHP 5.3.10 or later (php5)
* PHP CLI interpreter (php5-cli)
* PHP SQLite extension (php5-sqlite)
* PHP cURL extension (php5-curl)
* PHP Alternative PHP Cache (php-apc)
* PHP Internationalisierungserweiterung (php5-intl)

Optionally, in order to use a database other than the preconfigured SQLite one,
you need a matching PHP extension supported by `Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_.

If you want to use the developer mode, for using the web installer or to create
profiler data to be used to analyze errors you will still need the SQLite
extension!

Download
********

Installation packages are distributed as compressed packages and are available
for download at the `download <http://mapbender3.org/download>`_ page.

After downloading, extract the package in a directory of your choice. Then make
sure your Webserver points to the web directory inside the mapbender3 directory
you just uncompressed. You will also need to make sure that the default
directory index is *app.php*.

Example for ALIAS configuration for Apache in file /etc/apache2/conf.d/mapbender3

.. code-block:: yaml

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

A :doc:`Git-based <installation_git>` installation - mainly for developers -
is also possible.

Configuration
=============

Using the web installer
-----------------------

Configuration right inside your browser is not yet available. Please use the
command line method below for now.

Using the command line
----------------------

Configuring your Mapbender3 installation is made up of the following steps:

* Creating the database
* Creating the database schema
* Copying the bundles' assets to the public web directory
* Initializing the role system
* Creating the "root" user
* Inserting srs parameters

All can be done using the console utility provided by Symfony2, the awesome
framework Mapbender3 is build upon. There's a mayor caveat though you should
understand, before continuing:

  | The console utility will write files in the app/cache and app/logs
  | directories. These operations are made using the user permissions of
  | whatever user you're logged in with. This is also true for the app/db
  | directory and the SQLite database within. When you open the application
  | from within the browser, the server PHP process will try to access/write
  | all these files with other permissions. So make sure you give the PHP
  | process write access to these files. See last step below.

Adapting the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Database connection parameters are stored together with some more configuration
parameters in the file **app/config/parameters.yml**. This file is using YAML
syntax, so be aware that you can **not** use tabs for indenting. Be careful about this and use whitespaces instead. 

Your database configuration in the parameters.yml could look like this when you use PostgreSQL:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: 1xyz45ab


Creating the database
^^^^^^^^^^^^^^^^^^^^^

Symfony2 can attempt to create your database, this works of course only if the
configured database user is allowed to. Call the console utility like this:

    :command:`app/console doctrine:database:create`

Creating the database schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Symfony2 will create the database schema for you, if you ask nicely:

    :command:`app/console doctrine:schema:create`

We also need to initialize the security system's database tables separately:

    :command:`app/console init:acl`

Copying the bundles' assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each bundle has it's own assets - CSS files, JavaScript files, images and more -
but these need to be copied into the public web folder:

    :command:`app/console assets:install web`


As a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier.

    :command:`app/console assets:install web --symlink --relative`


Creating the administrative user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first user - which has all privileges - must be created using the command:

    :command:`app/console fom:user:resetroot`

This will interactively ask all information needed and create the user in the
database.

There is a silent mode you can use, if you want to use a script to install Mapbender3 and don't want to be asked for all information:

    :command:`app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent`

Now head over to your installation in your browser and enjoy.

Inserting srs parameters
^^^^^^^^^^^^^^^^^^^^^^^^

Inserting from srs parameters into the database occurs using the command:

    :command:`app/console doctrine:fixtures:load  --append`


Check config.php and write permission 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* http://localhost/mapbender3/config.php

You have to set write permission to app/cache and app/logs

.. code-block:: yaml

 chmod -R o+w /var/www/mapbender3/app/cache
 chmod -R o+w /var/www/mapbender3/app/logs


You can start using Mapbender3 now. You can open the developer mode when you run app_dev.php.

* http://localhost/mapbender3/app_dev.php

**Notice:** Klick on the Mapbender3 logo to get to the login page. Login with the new user you created. 



Installation Example for Ubuntu
===============================

Install necessary components:

.. code-block:: yaml

  apt-get install php5 php5-pgsql php5-gd php5-curl php5-cli php5-sqlite sqlite php-apc php5-intl curl


Configure the Apache ALIAS in file /etc/apache2/conf.d/mapbender3 and restart your Apache

.. code-block:: yaml

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

Check the ALIAS is working

* http://localhost/mapbender3/

Open Symfonys Welcome Script config.php. This script checks whether all necessary components are installed and configurations are made. If there are still problems, you should fix them.
 
* http://localhost/mapbender3/config.php


.. image:: figures/mapbender3_symfony_check_configphp.png
     :scale: 80 

Set owner, group and rights

.. code-block:: yaml

 chmod -R uga+r /var/www/mapbender3
 chown -R www-data:www-data /var/www/mapbender3

 
Run the app/console commands

.. code-block:: yaml

 cd /var/www/mapbender3
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console init:acl
 app/console assets:install web
 app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent
 app/console doctrine:fixtures:load  --append

Installation of Mapbender3 is done. 

Check config.php 

* http://localhost/mapbender3/config.php

You have to set write permission to app/cache and app/logs

.. code-block:: yaml

 chmod -R o+w /var/www/mapbender3/app/cache
 chmod -R o+w /var/www/mapbender3/app/logs


You can start using Mapbender3 now. You can open the developer mode when you run app_dev.php.

* http://localhost/mapbender3/app_dev.php

**Notice:** Klick on the Mapbender3 logo to get to the login page. Login with the new user you created. 

To lern more about Mapbender3 have a look at the :doc:`Mapbender3 Quickstart <quickstart>`. 
