.. _installation_ubuntu:

Installation on Ubuntu/Debian
#############################

Mapbender is shipped with a preconfigured SQLite database which includes preconfigured applications (the database is located under `<mapbender>/var/db/demo.sqlite`).
You can find instructions for a test installation based on the Symfony web server at :ref:`installation_symfony`.

.. hint:: PostgreSQL is strongly recommended for productive use. Look up the neccessary configurational steps in the chapter `Optional > Mapbender Deployment on PostgreSQL <#optional>`_.


Requirements
------------

* PHP >= 8.1
* Apache installation with the following modules activated:
    * mod_rewrite
    * libapache2-mod-php
* PostgreSQL Installation
    * It is recommended to use a PostgreSQL database for Mapbender.
    * It is recommended to create a database user to access the Mapbender database.

Nginx can also be used as web server (this will not be discussed in detail here).


Preparation
-----------

Installation of mandatory PHP extensions:

.. code-block:: bash

    sudo apt install php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-apcu php-intl openssl php-zip php-mbstring php-bz2

* Please check the :ref:`faq` for further PHP settings. 


Unpack and register to web server
---------------------------------

Download the current Mapbender version and unzip it into `/var/www/mapbender` or a different location:

.. code-block:: bash

    wget https://mapbender.org/builds/mapbender-starter-current.tar.gz -O /var/www/mapbender-starter-current.tar.gz
    tar -zxf /var/www/mapbender-starter-current.tar.gz -C /var/www
    mv $(ls -d /var/www/*/ | grep mapbender) /var/www/mapbender/


Configuration Apache 2.4
------------------------

Create the file `/etc/apache2/sites-available/mapbender.conf` with the following content:

.. code-block:: apache

 Alias /mapbender /var/www/mapbender/public/
 <Directory /var/www/mapbender/public/>
  Options MultiViews FollowSymLinks
  Require all granted

  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ index.php [QSA,L]
 </Directory>

Activate the site and reload Apache:

.. code-block:: bash

 a2ensite mapbender.conf
 service apache2 reload


Directory rights
----------------

.. code-block:: bash

 sudo chown -R :www-data /var/www/mapbender

 sudo chmod -R ug+w /var/www/mapbender/var/log
 sudo chmod -R ug+w /var/www/mapbender/var/cache
 sudo chmod -R ug+w /var/www/mapbender/public/uploads

 sudo chmod -R ug+w /var/www/mapbender/var/db/demo.sqlite


First steps
-----------

The Mapbender installation can now be accessed under ``http://[hostname]/mapbender/``.
User data by default:

* username: root
* password: root


Troubleshooting is available via the following command (must be executed in the application directory):

.. code-block:: yaml

	bin/console mapbender:config:check

.. hint:: Please note that ``config:check`` will use the php-cli version. The settings may be different from your webserver PHP settings. Please use ``php -r 'phpinfo();'`` to show your PHP webserver settings.

Congratulations! Mapbender is now set up correctly and ready for further configuration.
Find Information about the first steps with Mapbender in the :ref:`Mapbender Quickstart <quickstart>`.


Optional
--------

LDAP
++++

To use the optional LDAP-connection, following PHP-LDAP-extension is required:

.. code-block:: bash

   sudo apt install php-ldap

.. note:: To use LDAP, the `LDAP-Bundle <https://github.com/mapbender/ldapBundle>`_ must be integrated into Mapbender. Further setup instructions can be found in the `Bundle's README.md <https://github.com/mapbender/ldapBundle/blob/master/README.md>`_ on GitHub.


Mapbender installation with PostgreSQL
++++++++++++++++++++++++++++++++++++++

Configuration of PostgreSQL database for productive use:

Requirements:
- configured PostgreSQL database
- database for Mapbender configuration
- PostgreSQl database user to access the database with *create database* right

Installation PHP-PostgreSQL driver

.. code-block:: bash

   sudo apt install php-pgsql

Configuration of database connection is done by a variable that contains the entire connection string. Configure it by adding it in your *.env.local* file.

.. code-block:: yaml

    MAPBENDER_DATABASE_URL="postgresql://dbuser:dbpassword@localhost:5432/dbname?serverVersion=14&charset=utf8"

For further information: :ref:`yaml`.

Initialisation of the database connection:

.. code-block:: bash

 cd /var/www/mapbender
 bin/console doctrine:database:create
 bin/console doctrine:schema:create
 bin/console mapbender:database:init -v
 bin/composer run reimport-example-apps

Create root user for access:

.. code-block:: bash

    bin/console fom:user:resetroot

Find further information in :ref:`installation_configuration`.


Mapbender installation with MySQL
++++++++++++++++++++++++++++++++++

Similar to configuration with PostgreSQL.

Install the MySQL driver:

.. code-block:: bash

   sudo apt install php-mysql

Adapt these parameters (in *parameters.yaml*) accordingly:

.. code-block:: yaml

                    database_driver:   pdo_mysql
                    database_port:     3306

To initialize your database connection, see :ref:`en/installation/installation_ubuntu:Mapbender installation with PostgreSQL`.
