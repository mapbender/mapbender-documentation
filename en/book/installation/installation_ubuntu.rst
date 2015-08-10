.. _installation_ubuntu:

Installation auf Ubuntu und Debian
##################################

The following Installation manual describes the neccessary steps on a recent Ubuntu or Debian system. We assume that Apache 2.4 is running on the system. A documentation for Apache 2.2 is added `at the end of the document <installation_ubuntu.html#instructions-for-apache-2-2>`_.

Please take note of the `system requirements <systemrequirements.html>`_. Here is the way to install the neccessary components:

.. code-block:: bash

  sudo apt-get install php5 php5-pgsql php5-gd php5-curl php5-cli php5-sqlite sqlite php-apc php5-intl curl openssl

Load Apache rewrite-module:

.. code-block:: bash

  sudo a2enmod rewrite

Configure the Apache Alias. We assume that Mapbender3 is unzipped into /var/www/mapbender3. Create the file /etc/apache2/sites-available/mapbender3.conf with the content below. 

.. code-block:: apache

 Alias /mapbender3 /var/www/mapbender3/web/
 <Directory /var/www/mapbender3/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender3/
  RewriteCond %{ENV:REDIRECT_STATUS} ^$
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule ^(.*)$ app.php/$1 [PT,L,QSA]
 </Directory>

Activate the site afterwards with

.. code-block:: bash
   a2ensite mapbender3.conf

Reload your Apache server.

.. code-block:: bash

 service apache2 reload


Check
-----

Check that the Alias is working:

* http://localhost/mapbender3/

Open Symfony´s Welcome Script config.php. This script checks whether all necessary components are installed and configurations are done. If there are still problems, you should fix them.
 
* http://localhost/mapbender3/config.php


.. image:: ../../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 


Configuration of Mapbender3 
---------------------------

Set the write permission for user (u), group (g) and others (a) and rights. Assign the files to the Apache user (www-data).

.. code-block:: bash

 sudo chmod -R ugo+r /var/www/mapbender3
 sudo chown -R www-data:www-data /var/www/mapbender3
 sudo chmod -R ug+w /var/www/mapbender3/web/uploads

..  sudo chmod -R ug+w /var/www/mapbender3/web/assets

Adapt the Mapbender3 configuration file parameters.yml (app/config/parameters.yml) and define the database you want to create.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:     ~
    database_user:     postgres
    database_password: secret
 
Run the app/console commands. You find detailed information for this commands in the chapter `Details of the configuration of Mapbender3 <configuration.html>`_.

.. code-block:: bash

 cd /var/www/mapbender3
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console assets:install web
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Installation of Mapbender3 is done. 

Check the config.php again:

* http://localhost/mapbender3/config.php

You have to set write permission to app/cache, app/logs and web/uploads.

.. code-block:: bash

 sudo chmod -R ug+w /var/www/mapbender3/app/cache
 sudo chmod -R ug+w /var/www/mapbender3/app/logs
 sudo chmod -R ug+w /var/www/mapbender3/web/uploads

..  sudo chmod -R ug+w /var/www/mapbender3/web/assets

You can start using Mapbender3 now.

* http://localhost/mapbender3/

**Notice:** Click on the Mapbender3 logo to get to the login page. Log in with the new user you created. 

You can open the developer mode when you run app_dev.php: http://localhost/mapbender3/app_dev.php

To learn more about Mapbender3 have a look at the `Mapbender3 Quickstart <../quickstart.html>`_.


Instructions for Apache 2.2
---------------------------

Unlike Apache 2.4 you have to place the mapbender3.conf file for Apache 2.2 into the directory /etc/apache2/conf.d/

Apache 2.2 configuration:

.. code-block:: apache

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

Please note that Apache 2.2 uses `different Access Control directives than Apache 2.4 <http://httpd.apache.org/docs/2.4/upgrading.html>`_ (Allow from all).
