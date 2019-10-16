.. _installation_windows:

Installation on Windows
#######################

For fast installation (test system) MS4W-Installer (https://ms4w.com/download.html) can be used.

Below the installation for a productive system is descriped. 


Requirements
------------

* PHP NTS (version 5.6 - 7.1, https://windows.php.net/download/)
* Apache installation run as service (https://www.apachelounge.com/download/)   
  with the following modules:
 
  * mod_rewrite
  * mod_fcgid
 
* eingerichtete PostgreSQL Datenbank (Version < 10, https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 
  
  * established database for Mapbender configuration 
  * if necessary  own user for access


Nginx can also be used as web server, but it will not be discussed in this manual.   


Configuration PHP
-----------------

Unzip the Zip archive, for example under c:\php .

Based on the PHP-version, PHP-variables won't be set correctly in the temp-directory.

* It needs to be checked, if both variables (php.ini) are set correctly:

.. code-block:: ini

    sys_temp_dir
    upload_tmp_dir
    date.timezone

* the path from PHP-bin directory to the PATH-variable (Windows environment variable) needs to be set
* activate the requiered PHP extensions in the php.ini configuration file

.. code-block:: ini

    # php.ini
    extension=php_curl.dll
    extension=php_fileinfo.dll
    extension=php_gd2.dll
    extension=php_intl.dll
    extension=php_pdo_pgsql.dll
    extension=php_pdo_sqlite.dll
    extension=php_pgsql.dll
    extension=php_openssl.dll
    extension=php_mbstring.dll
    extension=php_zip.dll
    extension=php_bz2.dll


Unpack and register to web server
---------------------------------

Download the current Mapbender version (https://mapbender.org/builds/mapbender-starter-current.zip) and unzip into c:\mapbender\


Configuration Apache
--------------------

A subfolder "conf.d" must be prepared in the directory <apache>/conf.

Add following code at the end of file httpd.conf :

.. code-block:: apache

                # Include directory conf.d
                Include "conf/conf.d/*.conf"

Create file **<apache>\conf\conf.d\mapbender.conf** with:

.. code-block:: apache

 Alias /mapbender c:/mapbender/web/
 <Directory c:/mapbender/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>

Reload Apache.


mod_fcgid
---------

Create file **<apache>\conf\conf.d\fcgi.conf** with:

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

Database configuration (app/config/parameters.yml).
Following information :ref:`yaml_en`.


.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: secret
    

Open the windows shell and initialisation the database connection with the following commands:

.. code-block:: text
 
    cd c:\mapbender
    php.exe app/console doctrine:database:create
    php.exe app/console doctrine:schema:create
    php.exe app/console assets:install web
    php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
    php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixture/ORM/Application/ --append


First steps
-----------


The Mapbender installation can now be accessed under **http://hostname/mapbender/**.
User data by default: username: "root", passwort: "root"

Following information: `Mapbender Quickstart Document <../en/quickstart.html>`_. 



**Check it the alias is working**

* http://localhost/mapbender/

Open the Symfony Welcome Script config.php. The script will check if all required components are installed.

* http://localhost/mapbender/config.php
