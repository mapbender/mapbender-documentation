.. _installation_windows:

Installation on Windows
#######################

.. For a quick installation (e.g. on a test system), use the MS4W-Installer (https://ms4w.com/download.html).

.. Read on for a detailed description on a productive system.

Mapbender needs a database to store information. The Mapbender download package contains a SQLite databse that is ready to use. For production we recommend the use of a PostgreSQL database.


Requirements
------------

* PHP NTS >= 8.1 (https://windows.php.net/download/)
* Apache installation (https://www.apachelounge.com/download/, run as service with these modules):
    * mod_rewrite
    * mod_fcgid
* PostgreSQL Installation (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
    * It is recommended to use a PostgreSQL database for Mapbender. 
    * It is recommended to create a database user to access the Mapbender database.


Nginx can also be used as web server, but it will not be discussed in this manual.   


Configuration PHP
-----------------

* Unzip the Zip archive, for example under `c:\\php`.
* Depending on the PHP version, PHP variables for a temp directory are not set correctly under Windows.
* Therefore, it has to be checked if the following variables (*php.ini*) are set correctly:

.. code-block:: ini

    sys_temp_dir
    upload_tmp_dir
    date.timezone

* The path from `PHP-bin` directory to the ``PATH`` variable (Windows environment variable) needs to be set.
* Activate the required PHP extensions in the *php.ini* configuration file:

.. code-block:: ini

    # php.ini
    extension=php_curl
    extension=php_fileinfo
    extension=php_gd
    extension=php_intl
    extension=php_pdo_pgsql
    extension=php_pdo_sqlite
    extension=php_pgsql
    extension=php_openssl
    extension=php_mbstring
    extension=php_zip
    extension=php_bz2

* Please check the :ref:`faq` for further PHP settings. 


Extract Mapbender and register to web server
--------------------------------------------

Download the `current Mapbender version <https://mapbender.org/builds/mapbender-starter-current.zip>`_ and unzip it into `c:\\mapbender\\`


Configuration Apache
--------------------

A subfolder `conf.d` must be prepared in the directory `<apache>/conf`.

Add the following code at the end of file *httpd.conf*:

.. code-block:: apache

                # Include directory conf.d
                Include "conf/conf.d/*.conf"

Create file `<apache>\\conf\\conf.d\\mapbender.conf` with:

.. code-block:: apache

 Alias /mapbender c:/mapbender/public/
 <Directory c:/mapbender/public/>
  Options MultiViews FollowSymLinks
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ index.php [QSA,L]
 </Directory>


Restart Apache.


mod_fcgid
---------

Create file `<apache>\\conf\\conf.d\\fcgi.conf` with:

.. code-block:: apacheconf

    LoadModule fcgid_module modules/mod_fcgid.so
    
    FcgidInitialEnv PHPRC "c:/php/"
    FcgidInitialEnv PATH "c:/php;C:/WINDOWS/system32;C:/WINDOWS;C:/WINDOWS/System32/Wbem"
    FcgidInitialEnv SystemRoot "C:/Windows"
    FcgidInitialEnv TEMP "C:/WINDOWS/TEMP"
    FcgidInitialEnv TMP "C:/WINDOWS/TEMP"
    FcgidInitialEnv windir "C:/WINDOWS"

    FcgidPassHeader Authorization
    FcgidIOTimeout 1200
    FcgidConnectTimeout 1200
    FcgidBusyScanInterval 1200
    FcgidBusyTimeout 1200
    FcgidErrorScanInterval 1200
    FcgidIdleScanInterval 1200
    FcgidIdleTimeout 1200
    FcgidZombieScanInterval 1200
    FcgidMaxProcesses 1000
    FcgidOutputBufferSize 64
    FcgidProcessLifeTime 3600
    FcgidMaxRequestsPerProcess 10000
    FcgidMinProcessesPerClass 0
    FcgidFixPathinfo 0
    MaxRequestLen 200000

    <Files ~ "\.php$">
        Options Indexes FollowSymLinks ExecCGI
        AddHandler fcgid-script .php
        FcgidWrapper "c:/php/php-cgi.exe" .php
    </Files>


Configuration PostgreSQL
------------------------

Configuration of PostgreSQL database for productive use:

Requirements:

* Installation of PostgreSQL
* database for the Mapbender configuration
* PostgreSQl database user to access the database (optional) 

Activate the PHP-PostgreSQL driver

.. code-block:: ini

    # php.ini
    extension=php_pgsql
    extension=php_pdo_pgsql

Configuration of database connection is done by a variable that contains the entire connection string. Configure it by adding it in your *.env.local* file.

.. code-block:: yaml

    MAPBENDER_DATABASE_URL="postgresql://dbuser:dbpassword@localhost:5432/dbname?serverVersion=17&charset=utf8"

For more information on the database configuration, see :ref:`yaml`.

Open the windows shell.

Create the Mapbender database if it does not exist already:

.. code-block:: bash
 
    cd c:\mapbender
    php.exe bin/console doctrine:database:create


Create the Mapbender table structure and the load example applications:

.. code-block:: bash
 
    cd c:\mapbender
    php.exe bin/console doctrine:schema:create
    php.exe bin/console mapbender:database:init -v
    php.exe bin/composer run reimport-example-apps

To administrate Mapbender you need a user. Create root user for access:

.. code-block:: text

    php.exe bin/console fom:user:resetroot


Find further information in :ref:`installation_configuration`


First steps
-----------

The Mapbender installation can now be accessed under **http://[hostname]/mapbender/**.


**Check if the alias is working**

* ``http://localhost/mapbender/``

* username: root
* password: root

Troubleshooting is available via the following command (must be executed above the `bin/` directory):

.. code-block:: yaml

	php.exe bin/console mapbender:config:check

.. hint:: Please note that ``config:check`` will use the php-cli version. The settings may be different from your webserver PHP settings. Please use ``php -r 'phpinfo();'`` to show your PHP webserver settings.

Further information can be found at :ref:`en/customization/commands:bin/console mapbender:config:check`.

Congratulations! Mapbender is now set up correctly and ready for further configuration.
Find information about the first steps with Mapbender in the :ref:`Mapbender Quickstart <quickstart>`.

