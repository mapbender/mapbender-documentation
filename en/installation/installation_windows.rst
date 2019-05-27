.. _installation_windows:

Installation on Windows
#######################

We show you two different options to install Mapbender on Windows. The `first one uses the MS4W Package <#install-via-ms3w-package>`_ and the included Mapbender version. The `second one presents the manual installation <#manual-installation>`_, where you unpack Mapbender and adjust Apache and PHP by yourself.

We don't offer EXE-installers, yet because it might unpack Mapbender to a specific directory but the adjustments have to be made on PHP and Webserver side (Apache/Nginx).


Notes on the Windows installation
---------------------------------

Depending on the PHP-version the PHP variables for the Temp-directory are not set in Windows.

Please check if the two variables

* ``sys_temp_dir`` and
* ``upload_tmp_dir`` are set.

Please set them in the ``php.ini`` file. If you use seperate ``php.ini`` files for the command client (CLI) and the web, you can change both.

The value for the web can be checked with a ``phpinfo.php`` page (remember to set that file not to the public).



Install via MS3W package
------------------------

Mapbender is part of `MS4W (Mapserver for Windows) <http://www.ms4w.com/>`_ and can be installed via this package including Mapserver, Apache, GDAL, PHP among others. It's more or less a release version of Mapbender configuried for the MS4W Apache/PHP environment.

If you choose the EXE-Installer, you can select Mapbender from the list of apps:

.. image:: ../../figures/installation/ms4w_installer.png
     :scale: 80

If you choose the ZIP from MS4W, you have to download and unpack Mapbender by hand from `the MS4W download page <http://www.ms4w.com/>`_ and unpack it into the MS4W directory.

.. image:: ../../figures/installation/ms4w_packages.png
     :scale: 80

Please refer to `the MS4W homepage <http://ms4w.com>`_ for further details.



Manual installation
-------------------

Please take note of the `system requirements <systemrequirements.html>`_ where you can also find the Download links to Mapbender. Install the neccessary components:

 * add the path to your PHP-bin directory to the PATH variable 
 * activate the PHP extensions in your php.ini configuration file
 * load the Apache module rewrite

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


For development:

.. code-block:: ini

 # php.ini
 extension=php_bz2.dll

 

Additional for PHP 7:

.. code-block:: ini

 # php.ini
 extension=php_zip.dll
 extension=php_bz2.dll
  

.. code-block:: apache

    # Windows: edit file httpd.conf (remove the comment-sign #) and restart apache
    LoadModule rewrite_module modules/mod_rewrite.so

Create the Apache alias. In Windows there are several ways. A clear way is to create a file mapbender.conf and to refer to that file in Apaches httpd.conf

* Create a subfolder "alias" in the directory "<apache>/conf". Create the mapbender.conf file there. (You can use this directory to place additional Alias definition-files for other sites there.)
* In the httpd.conf (in directory <apache>/conf/)refer to this file mapbender.conf

In httpd.conf:

.. code-block:: apache

                # Refer to Mapbender alias
                Include "conf/alias/mapbender.conf"

In mapbender.conf:

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

We assume in this example, that Mapbender is unzipped directy under **C:/** (see the `System Requirements and Download <systemrequirements.html#download-of-mapbender>`_ chapter for details). You can easily choose a different directory and have to adjust the Apache mapbender.conf file above to the right location.

Restart the Apache webserver.



Optional features
=================

The following steps may lead to a better performance under some Windows installations.


SASS Compiler
-------------

The SASS compiler is part of Mapbender since version 3.0.5 and contains und contains a filter since version 3.0.6.0 which makes sure that the generated CSS statements are stored in a temporary file instead of delivering it out in a pipe.


mod_fcgid
---------

"mod_fcgid" is an Apache handler that is recommended for Windows Installations with Apache, because server requests can be executed parallel. These instructions are an offer for your deployment, although many other varaiants exist, which we cannot cover in this documentation.

The common way to register PHP in Apache is as a module:

.. code-block:: apache

                # LoadModule php5_module "c:/bin/php/5.6.30/php5apache2_4.dll"
                # AddHandler application/x-httpd-php .php

                # configure the path to php.ini
                # PHPIniDir "c:/bin/php/5.6.30"

This way is substituded with the FCGID method. It needs some preparation since them module is not shipped with Apache installations out of the box.

* Website: https://httpd.apache.org/mod_fcgid/
* Download for Windows (VC 11, please mind your dependencies): https://www.apachelounge.com/download/VC11/ and there the **modules-...zip** file.
* Unzip the mod_fcgid.so file from the archive into the module-directory of Apache.

Adjust the httpd.conf:

.. code-block:: apache

                # FCGI
                LoadModule fcgid_module "modules/mod_fcgid.so"
                FcgidInitialEnv PHPRC "c:/bin/php/5.6.30"
                AddHandler fcgid-script .php
                FcgidWrapper "c:/bin/php/5.6.30/php-cgi.exe" .php


In the Mapbender-Apache-Site file (mapbender.conf), add the "ExecCGI" parameter, for example:

.. code-block:: apache

                <Directory c:/srv/mapbender3-starter-3.0.6.0/web/>
                    [...]
                    Options MultiViews FollowSymLinks ExecCGI
                    [...]
                </Directory>



WinCache PHP (optional)
-----------------------

The Windows Cache Extension for PHP is a PHP accelerator that is used to increase the speed of PHP applications running on Windows and Windows Server. The extension included PHP opcode cache, user data cache, session cache, file system cache and relative path cache.

Further information under:

- https://www.iis.net/downloads/microsoft/wincache-extension
- https://sourceforge.net/projects/wincache/

**WinCache Installation**

- Download: https://sourceforge.net/projects/wincache/
- The download is shipped as a self-extracting archive (.exe).

.. code-block:: txt
                
                To install and enable the extension, use the following steps:
                Unpack the package that is appropriate for the PHP version you are using.
                Copy the php_wincache.dll file into the PHP extensions folder. Typically this folder is called "ext" and it is located in the same folder with all PHP binary files. For example:
                "C:\Program Files\PHP\ext".
                Using a text editor, open the php.ini file, which is usually located in the same folder where all PHP binary files are. For example:
                "C:\Program Files\PHP\php.ini".
                Add the following line at the end of the php.ini file:
                extension = php_wincache.dll
                Save and close the php.ini file.


**set session.handler to WinCache:**

.. code-block:: txt
                
                To change the location of the session file use session.save_path directive.
                sesion.save_handler = wincache
                session.save_path = C:\inetpub\tmp\session\


**activate wincache.reroute_enabled**

.. code-block:: txt
                
                The reroutes are not enabled by default. To enable them, set the reroute_enabled directive in either the php.ini or the .user.ini.
                wincache.reroute_enabled = 1


OpCache (optional)
------------------

OPCache is a PHP-extension which is delievered with PHP since version 5.5.5. but is not activated by default.

More info: https://www.sitepoint.com/understanding-opcache/


**OPCache installation**

- http://php.net/manual/de/book.opcache.php

In php.ini:

.. code-block:: ini
                
                [opcache]
                ; Pfad zur php_opcache.dll
                zend_extension=C:/bin/php/5.6.30/ext/php_opcache.dll

                ; Determines if Zend OPCache is enabled
                opcache.enable=1
 
                ; Determines if Zend OPCache is enabled for the CLI version of PHP
                ;opcache.enable_cli=0
 
                ; The OPcache shared memory storage size.
                opcache.memory_consumption=64
                ; The amount of memory for interned strings in Mbytes.
                opcache.interned_strings_buffer=4
                ; The maximum number of keys (scripts) in the OPcache hash table.
                ; Only numbers between 200 and 100000 are allowed.
                opcache.max_accelerated_files=2000
                ; The maximum percentage of "wasted" memory until a restart is scheduled.
                opcache.max_wasted_percentage=5

Symfony recommends, to increase the **opcache.max_accelerated_files** value: http://symfony.com/doc/3.1/performance.html#optimizing-all-the-files-used-by-symfony

                

Check
=====

Check that the Alias is accessible:

* http://localhost/mapbender/

Open Symfony´s Welcome Script config.php. This script checks whether all necessary components are installed and configurations are done. If there are still problems, you should fix them.
 
* http://localhost/mapbender/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 

Adapt the Mapbender configuration file parameters.yml (app/config/parameters.yml) and define the database you want to create. Further information is available in the chapter `Configuring the database <../database.html>`_.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: secret

Run the app/console commands with php. First you have to open a terminal (cmd).

.. code-block:: text
 
 c:
 cd mapbender
 php.exe app/console doctrine:database:create
 php.exe app/console doctrine:schema:create
 php.exe app/console assets:install web
 php.exe app/console fom:user:resetroot
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append


Installation of Mapbender is done. 

Check the config.php again:

* http://localhost/mapbender/config.php


You can start using Mapbender now. You can open the developer mode when you run app_dev.php.

* http://localhost/mapbender/app_dev.php

**Notice:** Go to the login link at the right-top and log in with the new user you created. 

To learn more about Mapbender have a look at the `Mapbender Quickstart <../quickstart.html>`_.

