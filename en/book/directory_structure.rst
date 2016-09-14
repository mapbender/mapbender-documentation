.. _directory_structure:

Directory structure in Mapbender3
#################################

app
***
This directory contains:

* the php-Cache (app/cache)
* the logs (app/logs)
* the configurations (app/config)
* the applicationkernel (app/AppKernel.php) (this is called by the FrontendControllers and controlls the whole application)
* the Autoloading (autoload.php) 
* the application specific resource directory (Resources)
* the command line application for maintaining and management tasks (app/console)


bin
***

* is not in use at the moment. Here you can deposit e.g. installation scripts.


mapbender
*********

* provides the mapbender-specific bundles and the Mapbender3 code.


web
***

This directory has to be published by the webserver. The ALIAS has to refer to this directory. 

It controlls: 

* the FrontendController (PHP-Script, which can be called). These are **app.php** for the productive-system and **app_dev.php** for the development version. The development version contains the profiler for perfomance tests and more.
* this directory contains the static resoures like css, js, favicon etc.


web/bundles
***********

* here the static resources of the single bundles are stored.
* the following command copies the resources from the bundles to the folder. 

.. code-block:: yaml

     app/console assets:install --symlink web

* **Notice**: if you use Windows you can't create symbolic links and therefore you have to run the command (**app/console assets:install web**) after every change in the code to copy the files to the directory.


src
***

* directory for applications specific bundles (similar to the former x-directories in Mapbender 2.x)


vendor
******
* directory where all the Bundles which are used from Symfony are found. Resources are used by Symfony using the Autoloading.


translations
*************
The translation is stored in xliff-textfiles. Every language needs an xliff-file like messages.de.xliff for the german translation.

* mapbender/src/Mapbender/CoreBundle/Resources/translations/
