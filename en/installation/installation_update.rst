.. _installation_update:

Update Mapbender to a newer Version
===================================

To update Mapbender you have to do the following steps:

* get the new version from http://mapbender.org/builds/
* save your configuration files (parameters.yaml and files from folder config/packages) and your old Mapbender (files and database)
* replace the new files 
* merge your configuration files (check for new parameters and changes)
* update your Mapbender database
* copy the screenshots from your old Mapbender version from /public/uploads/ to the folder /public/uploads of your new installation
* Templates: If you are using your own template, you have to compare your scripts with the new scripts (are there any changes?)
* print templates: if you use your own print templates: copy them back to config/MapbenderPrintBundle/templates/.
* Import the demo applications either via bin/composer run reimport-example-apps or via the web administration
* At :ref:`installation_ubuntu` under the section **Unpack and register in your Web-Server** you can see how the config file for the Apache Alias should look like
* That's all! Have a look at your new Mapbender version

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
 
 # copy your old configuration files to the new version
 cp /var/www/mapbender_save/application/config/parameters.yaml /var/www/mapbender/application/config/parameters.yaml
 cp /var/www/mapbender_save/application/config/packages/doctrine.yaml /var/www/mapbender/application/config/packages/doctrine.yaml
 
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
 bin/console doctrine:schema:update --dump-sql
 bin/console doctrine:schema:update --force
  
 # Import the mapbender demo applications
 bin/composer run reimport-example-apps

 # Update the symbolic links
 bin/console assets:install public --symlink --relative
 
 # change the access rights and group of the files
 sudo chmod -R ug+r /var/www/mapbender
 sudo chown -R :www-data /var/www/mapbender

 # You have to set write permission to var/cache and var/log.
 sudo chmod -R ug+w /var/www/mapbender/application/var/cache
 sudo chmod -R ug+w /var/www/mapbender/application/var/log
 sudo chmod -R ug+w /var/www/mapbender/application/public/uploads

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
 php.exe bin/console doctrine:schema:update --dump-sql
 php.exe bin/console doctrine:schema:update --force
 
 # Import the applications from mapbender.yaml to your database to get to know about the latest developments
 php.exe bin/composer run reimport-example-apps

 # Export files to the web-directory
 php.exe bin/console assets:install public

 # Delete your cache and the logdateien at mapbender/var/cache und mapbender/var/log

 # if you use screenshots: copy the screenshots from the old version back to mapbender/public/uploads
 # if you have individual templates: merge the templates with the new Mapbender version
 # if you use your own print templates: copy them back to config/MapbenderPrintBundle/templates/
 

