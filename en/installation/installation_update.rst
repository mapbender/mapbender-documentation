.. _installation_update:

Update Mapbender to a newer Version
===================================

To update Mapbender you have to do the following steps:

* Get the new version from https://mapbender.org/builds/.
* Save your configuration files (``parameters.yml`` for versions < 4.0.0 respectively ``.env.local`` for >= 4.0.0, and the files from the folder *config/packages*) and your old Mapbender version (files and database).
* Replace the old with the new Mapbender files.
* Merge your configuration files (check for new parameters and changes).
* Update your :ref:`Mapbender database <en/customization/commands:bin/console doctrine:schema:update>`.
* Copy the screenshots from your old Mapbender version from */public/uploads/* (web/uploads for < 4.0.0) to the folder */public/uploads* of your new installation.
* Templates: If you are using your own template, you have to compare your scripts with the new scripts (are there any changes?).
* Print templates: If you use your own print templates, copy them back to *config/MapbenderPrintBundle/templates/*.
* Import the demo applications; either via ``bin/composer run reimport-example-apps`` or via the web administration.
* At :ref:`en/installation/installation_ubuntu:Unpack and register to web server`, you can see how the config file for the Apache Alias should look like.

And that's all! Have a look at your new Mapbender version.

.. hint::
    
    Please follow the migration instructions on specific Mapbender versions, see the :ref:`migration`.


Update Example for Linux
--------------------------
Have a look at the steps as commands

.. code-block:: bash

 # Download the new version
 wget http://mapbender.org/builds/mapbender-starter-current.tar.gz /tmp/build_mapbender/
 tar xfz /tmp/build_mapbender/mapbender-starter-current.tar.gz
 
 # save the old version
 mv /var/www/mapbender /var/www/mapbender_save
 
 # get the code of the new version
 cp -R /tmp/build_mapbender/mapbender-starter-v4.0.0 /var/www/
 mv /var/www/mapbender-starter-v4.0.0 /var/www/mapbender
 
 # transfer your old configuration information to the new version
 # transfer the information from config/parameters.yml to .env.local resp. /config/parameters.yaml
 # transfer the information from old config.yml to  /var/www/mapbender/config/packages/doctrine.yaml

 
 # manual step
 # merge parameters.yaml, doctrine.yaml and other YAML files you use
 # if you use screenshots: copy the screenshots from the old version back to mapbender/public/uploads
 # if you have individual templates: merge the templates with the new Mapbender version
 # if you use your own print templates: copy them back to config/MapbenderPrintBundle/templates/
 
 # change the accessrights and owner of the files
 sudo chmod -R ugo+r /var/www/mapbender
 sudo chown -R :www-data /var/www/mapbender
 
 # Update your Mapbender database
 cd /var/www/mapbender/
 bin/console doctrine:schema:update --complete --dump-sql
 bin/console doctrine:schema:update --complete --force
  
 # Import the mapbender demo applications
 bin/composer run reimport-example-apps

 # Update the symbolic links
 bin/console assets:install public --symlink --relative
 
 # change the access rights and group of the files
 sudo chmod -R ug+r /var/www/mapbender
 sudo chown -R :www-data /var/www/mapbender

 # You have to set write permission to var/cache and var/log.
 sudo chmod -R ug+w /var/www/mapbender/var/cache
 sudo chmod -R ug+w /var/www/mapbender/var/log
 sudo chmod -R ug+w /var/www/mapbender/public/uploads

Update Example for Windows
------------------------------------
 
.. code-block:: bash

 # Download the new version http://mapbender.org/builds/
   
 # Save the old version (files and database)
   
 # Copy the configuration files (parameters.yaml and files from folder config/packages) to your new Mapbender version. 
 # You have to check the configuration files for changes (new parameter, other changes)

 # Call the bin/console commands with php.exe
 # You have to open a windows console to send the commands
 c:
 cd mapbender
 
 # Update your Mapbender database
 php.exe bin/console doctrine:schema:update --complete --dump-sql
 php.exe bin/console doctrine:schema:update --complete --force

 # Import the mapbender demo applications
 php.exe bin/composer run reimport-example-apps

 # Export files to the web-directory
 php.exe bin/console assets:install public

 # Delete your cache and the logdateien at mapbender/var/cache und mapbender/var/log

 # if you use screenshots: copy the screenshots from the old version back to mapbender/public/uploads
 # if you have individual templates: merge the templates with the new Mapbender version
 # if you use your own print templates: copy them back to config/MapbenderPrintBundle/templates/
 

