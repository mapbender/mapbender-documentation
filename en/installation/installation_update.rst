.. _installation_update:

Update Mapbender to a newer Version
===================================

To update Mapbender you have to do the following steps:

* get the new version from http://mapbender.org/builds/
* save your configuration files (parameters.yml and config.yml) and your old Mapbender (files and database)
* replace the new files 
* merge your configuration files (check for new parameters and changes)
* update your Mapbender database
* copy the screenshots from your old Mapbender version from /web/uploads/ to the folder /web/uploads of your new installation
* Templates: If you are using your own template, you have to compare your scripts with the new scripts (are there any changes?)
* print templates: if you use your own print templates: copy them back to app/Resources/MapbenderPrintBundle/templates/.
* Import the demo applications either via bin/composer run reimport-example-apps or via the web administration
* At https://doc.mapbender.org/en/installation/installation_ubuntu.html under the section **Unpack and register in your Web-Server** you can see how the config file for the Apache Alias should look like
* That's all! Have a look at your new Mapbender version


Update Example for Linux
--------------------------
Have a look at the steps as commands

.. code-block:: bash

 # Download the new version
 wget -O http://mapbender.org/builds/mapbender-starter-current.tar.gz /tmp/build_mapbender/
 tar xfz /tmp/build_mapbender/mapbender-starter-current.tar.gz
 
 # save the old version
 mv /var/www/mapbender /var/www/mapbender_save
 
 # get the code of the new version
 cp -R /tmp/build_mapbender/mapbender-starter-v3.2.5 /var/www/
 mv /var/www/mapbender-starter-v3.2.5 /var/www/mapbender
 
 # copy your old configuration files to the new version
 cp /var/www/mapbender_save/app/config/parameters.yml /var/www/mapbender/app/config/parameters.yml
 cp /var/www/mapbender_save/app/config/config.yml /var/www/mapbender/app/config/config.yml 
 
 # manual step
 # merge parameters.yml, config.yml and if used mapbender.yml 
 # if you use screenshots: copy the screenshots from the old version back to mapbender/web/uploads
 # if you have individual templates: merge the templates with the new Mapbender version
 # if you use your own print templates: copy them back to mapbender/app/Resources/MapbenderPrintBundle/templates/
 
 # change the accessrights and owner of the files
 sudo chmod -R ugo+r /var/www/mapbender
 sudo chown -R www-data:www-data /var/www/mapbender
 
 # Update your Mapbender database
 cd /var/www/mapbender/
 app/console doctrine:schema:update --dump-sql
 app/console doctrine:schema:update --force
  
 # Import the mapbender demo applications
 bin/composer run reimport-example-apps

 # Update the symbolic links
 app/console assets:install web --symlink --relative
 
 # change the access rights and owner of the files
 sudo chmod -R ugo+r /var/www/mapbender
 sudo chown -R www-data:www-data /var/www/mapbender

 # You have to set write permission to app/cache and app/logs.
 sudo chmod -R ug+w /var/www/mapbender/app/cache
 sudo chmod -R ug+w /var/www/mapbender/app/logs
 sudo chmod -R ug+w /var/www/mapbender/web/uploads

Update Example for Windows
------------------------------------
 
.. code-block:: bash

 # Download the new version http://mapbender.org/builds/
   
 # Save the old version (files and database)
   
 # Copy the configuration files (parameters.yml and config.yml) to your new Mapbender version. 
 # You have to check the configuration files for changes (new parameter, other changes)

 # Call the app/console commands with php.exe
 # You have to open a windows console to send the commands
 c:
 cd mapbender
 
 # Update your Mapbender database
 php.exe app/console doctrine:schema:update --dump-sql
 php.exe app/console doctrine:schema:update --force
 
 # Notes for MS4W users:
 #     - be sure to first execute setenv.bat to properly set the required paths for PHP
 #     - you may have to also pass the extension you need, at the commandline, for example:
 #            php -d extension=C:\ms4w\Apache\php\ext\php_pdo_pgsql.dll app/console doctrine:schema:update --dump-sql
 
 # Import the applications from mapbender.yml to your database to get to know about the latest developments
 php.exe bin/composer run reimport-example-apps

 # Export files to the web-directory
 php.exe app/console assets:install web

 # Delete your cache and the logdateien at mapbender/app/cache und mapbender/app/logs

 # if you use screenshots: copy the screenshots from the old version back to mapbender/web/uploads
 # if you have individual templates: merge the templates with the new Mapbender version
 # if you use your own print templates: copy them back to mapbender/app/Resources/MapbenderPrintBundle/templates/
 

