.. _installation_ubuntu:

Installation on Ubuntu and Debian
#################################

The fast way and the preconfigured database
-------------------------------------------

The following Installation manual describes the neccessary steps on a recent Ubuntu or Debian system. We assume that Apache 2.4 is running on the system. Notes on `PHP 7 <installation_ubuntu.html#php-7>`_  and `Apache 2.2  <installation_ubuntu.html#instructions-for-apache-2-2>`_ are added below.

If you prefer a quick test without any configuration of a web-server, please take a look into the chapter `Installation in the Symfony built-in webserver <installation_symfony.html>`_.

Since version 3.0.6.0 Mapbender is shipped with a pre-configured database on base of SQLite which includes pre-configured applications (the database resides unter **<mapbender>/app/db/demo.sqlite**). The database includes the Mapbender-configuration like applications, users and registered services but no Geodata.

If you have another database like PostgreSQL and want to use that, you'll find the neccessary configuration steps in chapter `Mapbender Deployment on PostgreSQL <#mapbender-deployment-on-postgresql>`_.



Preparation
-----------

Please take note of the `system requirements <systemrequirements.html>`_, where you can also find the Download links to Mapbender.

There are also the neccessary components listed that you can install like this:

.. code-block:: bash

  sudo apt install php5 php5-gd php5-curl php5-cli php5-sqlite sqlite php5-intl php5-mbstring curl openssl

Please note that this components require the use of PHP5 but many of the latest systems (e.g Ubuntu 16.04 and newer) are using PHP7. See below at the section **PHP7** which packages need to be installed for the use of Mapbender with PHP7.


Additionally for development:
 
.. code-block:: bash

 apt install php5-bz2


Load the Apache rewrite-module:

.. code-block:: bash

  sudo a2enmod rewrite



Unpack and register in your Web-Server
--------------------------------------

Unpack the Mapbender archive (tar.gz or zip) for example into the directory **/var/www/mapbender** (see the `System Requirements and Download <systemrequirements.html#download-of-mapbender>`_ chapter for details).

Configure now the Apache Alias. You can easily unpack Mapbender to a different directory and only adjust the following file to refer to the right directory.

Create the file **/etc/apache2/sites-available/mapbender.conf** with the content below. 

.. code-block:: apache

 Alias /mapbender /var/www/mapbender/web/
 <Directory /var/www/mapbender/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
   
  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>

Activate the site afterwards with:

.. code-block:: bash
                
   a2ensite mapbender.conf

Reload your Apache server.

.. code-block:: bash

 service apache2 reload


Directory rights
----------------

Set the write permission for user (u), group (g) and others (a) and rights. Assign the files to the Apache user (www-data).

.. code-block:: bash

 sudo chown -R www-data:www-data /var/www/mapbender/app/logs
 sudo chown -R www-data:www-data /var/www/mapbender/app/cache
 sudo chown -R www-data:www-data /var/www/mapbender/web/uploads

 # if you want to use the preconfigured file-database
 sudo chmod -R ug+w /var/www/mapbender/app/db/demo.sqlite


The Apache user needs especially write-access to app/cache, app/logs, web/uploads and app/db/demo.sqlite (if you want to use the preconfigured file-based database). The user needs also read-access to the web-directory.


Start and login into Mapbender
------------------------------

You can now access your Mapbender installation with **http://hostname/mapbender/**.

Click on the Login-link at top-right to get to the login page. Log in with the new user you created. Per default the login-data is root/root.

You can open the developer mode when you run app_dev.php: http://localhost/mapbender/app_dev.php

To learn more about Mapbender have a look at the `Mapbender Quickstart <../quickstart.html>`_.



Mapbender deployment on PostgreSQL
----------------------------------

If you want to store the Mapbender configuration in another database than the SQLite one (and there is nothing wrong with that), please follow the next steps. We assume here PostgreSQL as database system.


You need the PHP-PostgreSQL driver

.. code-block:: bash

   apt install php5-pgsql


Adapt the Mapbender configuration file parameters.yml (app/config/parameters.yml) and define the database you want to create and use. Further information is available in the chapter :ref:`database`.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: secret
 
Run the app/console commands. You find detailed information for this commands in the chapter :ref:`installation_configuration`.

.. code-block:: bash

 cd /var/www/mapbender
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console assets:install web --symlink --relative
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Now the configuration of Mapbender for PostgreSQL is done and it contains now also the three default applications as well as the supported EPSG codes.



Mapbender deployment on MySQL
-----------------------------

Deployment of Mapbender for MySQL is similar to the one for PostgreSQL. You only need another PHP-driver and another parameter in the parameters.yml. So, if you want to store the Mapbender configuration in another database than the SQLite one (and there is nothing wrong with that), please follow the next steps.


You need the PHP-MySQL driver

.. code-block:: bash

   apt install php-mysql


Adapt the Mapbender configuration file parameters.yml (app/config/parameters.yml) and define the database you want to create and use. Further information is available in the chapter :ref:`database`.

.. code-block:: yaml

                    database_driver:   pdo_mysql
                    database_host:     localhost
                    database_port:     3306
                    database_name:     mapbender
                    database_path:     null
                    database_user:     root
                    database_password: secret

Run the app/console commands. You find detailed information for this commands in the chapter :ref:`installation_configuration`.

.. code-block:: bash

 cd /var/www/mapbender
 app/console doctrine:database:create
 app/console doctrine:schema:create
 # app/console assets:install web # nicht notwendig
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append



PHP 7
-----
 
PHP 7 needs additional packages. The list of packages for PHP 7:

.. code-block:: bash

   sudo apt install apache2 libapache2-mod-php php php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-intl openssl php-zip php-mbstring php-bz2
  

Under Ubuntu 16.04 you need to install the appropriate module for the Apache web server manually:

.. code-block:: bash

   sudo apt install libapache2-mod-php7.0


To use PostgreSQL:

.. code-block:: bash

   sudo apt install php-pgsql


For MySQL:

.. code-block:: bash

   sudo apt install php-mysql


Enable PHP 7 in Apache

.. code-block:: bash

   a2enmod php7.0



Instructions for Apache 2.2
---------------------------

Some versions of Debian support for Apache 2.2 to drop the mapbender.conf file into the directory ``/etc/apache2/sites-available`` and the activation with the command ``a2ensite``. Depending on the operating-system the file has to be placed into the directory ``/etc/apache2/conf.d/``.

Activate the Rewrite-Modul of Apache.

.. code-block:: bash

 sudo a2enmod rewrite

Unlike version 2.4, Apache 2.2 uses other directives and other default values (``Order`` and ``Allow``, ``AllowOverride``) that has to be written into the mapbender.conf file. These differences are explained in the `Upgrade-Guide from Apache 2.2 to Apache 2.4 <http://httpd.apache.org/docs/2.4/upgrading.html>`_.

Apache 2.2 configuration ``mapbender.conf``:

.. code-block:: apache

  ALIAS /mapbender /var/www/mapbender/web/
  <Directory /var/www/mapbender/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    AllowOverride none
    Order allow,deny
    Allow from all
    
    RewriteEngine On
    RewriteBase /mapbender/
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>

 
Check
-----

Check that the Alias is working:

* http://localhost/mapbender/

Open Symfony´s Welcome Script config.php. This script checks whether all necessary components are installed and configurations are done. If there are still problems, you should fix them.
 
* http://localhost/mapbender/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 
