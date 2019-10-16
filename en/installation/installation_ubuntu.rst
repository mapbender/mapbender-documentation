.. _installation_ubuntu:

Installation on Ubuntu/Debian
#############################

Mapbender is shipped with a pre-configured database on base of SQLite which includes pre-configured applications (the database is located under **<mapbender>/app/db/demo.sqlite**).

For productive use PostgreSQL is recommended, you'll find the neccessary configuration steps in chapter `Mapbender Deployment on PostgreSQL <#mapbender-deployment-on-postgresql>`_.

Requirements
------------

- PHP (from version 5.6 to 7.1)
- Apache installation with the following modules activated:
 
  * mod_rewrite
  * libapache2-mod-php
  
Nginx can also be used as web server, but it will not be discussed in this manual.   
  
  
Preparation
-----------

Installation of needed PHP extensions:

.. code-block:: bash

    sudo apt install php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-apcu php-intl openssl php-zip php-mbstring php-bz2
    
    
Unpack and register to web server
---------------------------------

Download the current Mapbender version and unzip into /var/www/mapbender:

.. code-block:: bash

    wget https://mapbender.org/builds/mapbender-starter-current.tar.gz -O /var/www/mapbender-starter-current.tar.gz  
    tar -zxf /var/www/mapbender-starter-current.tar.gz -C /var/www
    mv $(ls -d /var/www/*/ | grep mapbender) /var/www/mapbender/
    

Configuration Apache 2.4
------------------------

A file **/etc/apache2/sites-available/mapbender.conf** must be prepared, with the following content:

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

Activate site and reload Apache:

.. code-block:: bash

 a2ensite mapbender.conf
 service apache2 reload


Directory rights
----------------

.. code-block:: bash

 sudo chown -R www-data:www-data /var/www/mapbender/app/logs
 sudo chown -R www-data:www-data /var/www/mapbender/app/cache
 sudo chown -R www-data:www-data /var/www/mapbender/web/uploads

 sudo chmod -R ug+w /var/www/mapbender/app/logs
 sudo chmod -R ug+w /var/www/mapbender/app/cache
 sudo chmod -R ug+w /var/www/mapbender/web/uploads

 sudo chmod -R ug+w /var/www/mapbender/app/db/demo.sqlite
 
 
First steps
-----------

The Mapbender installation can now be accessed under **http://hostname/mapbender/**.
User data by default: username: "root", passwort: "root"

Following information: `Mapbender Quickstart Document <../en/quickstart.html>`_. 


Optional
--------

**LDAP**

To use the optional LDAP-connection, following PHP-LDAP-extension is required:

.. code-block:: bash

   sudo apt install php-ldap
   
   
**Mapbender installation with PostgreSQL**

Configuration of PostgreSQL database for productive use:

Requirements:
- configured PostgreSQL database (version < 10)
- database for Mapbender configuration
- possibly user for access

Installation PHP-PostgreSQL driver

.. code-block:: bash

   sudo apt install php-pgsql
   
Configuration of database connection (app/config/parameters.yml):

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: secret
    
Following information: :ref:`yaml_en`.    
    
Initialisation of the database connection:

 .. code-block:: bash

    cd /var/www/mapbender
    app/console doctrine:database:create
    app/console doctrine:schema:create
    app/console assets:install web --symlink --relative
    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append
    
Following information: :ref:`installation_configuration_en`    
    
   

**Mapbender installation with MySQL:**

Analog to configuration with PostgreSQL.

Installation MySQL driver:

.. code-block:: bash

   apt install php-mysql

Following parameter (parameters.yml) needs to be adapted:

.. code-block:: yaml

                    database_driver:   pdo_mysql
                    database_port:     3306
                    
To initialize database connection, see PostgreSQL.                    


