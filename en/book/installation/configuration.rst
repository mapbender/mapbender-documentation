.. _configuration:

Details of the configuration of Mapbender3
==========================================

Configuration steps
-------------------

Following we describe the configuration steps of Mapbender3 a bit further. Configuring your Mapbender3 installation is made up of the following six steps:

* Creating the database
* Creating the database schema
* Copying the bundles' assets to the public web directory
* Creating the "root" user
* Inserting srs parameters (EPSG code definition)
* Loading the applications of the mapbender.yml to your database

All can be done using the console utility provided by `Symfony2 <http://symfony.com/>`_, on which Mapbender3 framework is built upon. There's a mayor caveat though you should understand, before continuing:

  | The console utility will write files in the app/cache and app/logs directories. These operations are made using the user permissions of whatever user you're logged in with. This is also true for the app/db directory and the SQLite database within. When you open the application from within the browser, the server PHP process will try to access/write all these files with other permissions. So make sure you give the PHP process write access to these files. See last step below.

**Notice:** The following steps assume that you are in the directory above the app directory (notice that for git installation that means mapbender3/application/ else mapbender3/).

.. code-block:: yaml

   cd mapbender3/
   or for git based installation 
   cd mapbender3/application



Adapting the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Database connection parameters are stored together with some more configuration
parameters in the file **app/config/parameters.yml**. This file is using YAML
syntax, so be aware that you can **not** use tabs for indenting. Be careful about this and use whitespaces instead. 

Your database configuration in the parameters.yml file could look like this when you use PostgreSQL:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: secret


Creating the database
^^^^^^^^^^^^^^^^^^^^^

Symfony2 can attempt to create your database, this works of course only if the
configured database user is allowed to. Call the console utility like this:

.. code-block:: yaml

   app/console doctrine:database:create


Creating the database schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Symfony2 will create the database schema for you:

.. code-block:: yaml

    app/console doctrine:schema:create



Copying the bundles' assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Alternatively, there is a silent mode you can use, if you want to use a script to install Mapbender3 and don't want to be asked for all parameters:

.. code-block:: yaml

    app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent

Inserting srs parameters
^^^^^^^^^^^^^^^^^^^^^^^^

Inserting proj4 srs parameters into a database occurs using the command:

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append

Importing applications from mapbender.yml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Importing applications from mapbender.yml into a database occurs using the command:

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append






Configuration files
-------------------

The basic configuration is done inside the **app/config/parameters.yml** file. A template is
provided in the app/config/parameters.yml.dist file. 

**app/config/config.yml** provides more parameters f.e. to configure portal functionality, owsproxy or provide an additional database. 


parameters.yml
^^^^^^^^^^^^^^

* database: The parameters starting with **database** are the database connection details. 
* mailer: The mailer settings start with **mailer**. Use f.e. smtp or sendmail. 
* locale: You can choose a locale for your application (default is en, de is available). Check http://doc.mapbender3.org/en/book/translation.html to find out how to modify translations or how to add a new language.

**Notice:** You need a mailer for self-registration and reset password functionality.


config.yml
^^^^^^^^^^

* fom_user.selfregistration: To enable or disable self-registration of users, change the fom_user.selfregistration parameter. You have to define self_registration_groups, so that self-registered users are added to these groups automatically, when they register. They will get the rights that are assigned to these groups.
* fom_user.reset_password: In the same way the possibility to reset passwords can be enabled or disabled.
* framework.session.cookie_httponly: For HTTP-only session cookies, make sure the framework.session.cookie_httponly parameter is set to true.

**Notice:** You need a mailer for self-registration and reset password functionality (see parameters.yml).

If you use a proxy you have to add the proxy settings to config.yml at section *ows_proxy3_core*.

This is how the configiration could look like:

.. code-block:: yaml

    ows_proxy3_core:
        logging: true
        obfuscate_client_ip: true
        proxy:
            host: myproxy
            port: 8080
            connecttimeout: 60
            timeout: 90
            noproxy:
                - 192.168.1.123



mapbender.yml
^^^^^^^^^^^^^

You can configure an applications on two ways. In the mapbender.yml file or with the browser in the Mapbender3 backend.

* The Mapbender Team provides an up-to-date mapbender.yml with demo applications. New elements with their parameters are added to this configuration in every new version (You can disable the applications by setting published: false or you can empty the mapbender.yml file)
* applications that are defined in the mapbender.yml are not editable in the backend
* you can import the applications to the database with the following app/console command

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append
