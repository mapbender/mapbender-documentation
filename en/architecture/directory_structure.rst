.. _directory_structure:

Directory structure in Mapbender
################################

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


app/config
----------

Basic configuration files of Mapbender are placed in the app/config directory. Two files are of particular importance:

* parameters.yml

* config.yml

More Information: :ref:`yaml_en`.

  
app/config/applications
-----------------------

The directory app/config/applications contains all applications that are defined in a YAML file. 

More Information: :ref:`yaml_en`.


bin
***

Here are symlinks to the following binaries placed:

* apigen
* composer
* coveralls
* doctrine
* doctrine.php
* phantomjs
* phing
* phpunit


documentation
*************

Folder for this documentation.


fom
***

Directory of the `FOM submodule <https://github.com/mapbender/fom>`_.


mapbender
*********

Directory of the `Mapbender submodule <https://github.com/mapbender/mapbender>`_. Provides the mapbender-specific bundles and the Mapbender code.


mapbender/...../translations
----------------------------

Directory: mapbender/src/Mapbender/CoreBundle/Resources/translations/

The translations are stored in `XLIFF textfiles <https://en.wikipedia.org/wiki/XLIFF>`_. Every language needs an xliff-file like messages.en.xlf for the English translation.



owsproxy
********

Directory of the `OWSProxy submodule <https://github.com/mapbender/owsproxy3>`_.



vendor
******

Directory for external libraries (loaded by composer) and further Mapbender modules (a.o. Digitizer, Mapbender-Icons).



web
***

This directory has to be published by the webserver. The ALIAS has to refer to this directory. 

It controls: 

* the FrontendController (PHP-Script, which can be called). These are **app.php** for the productive-system and **app_dev.php** for the development version. The development version contains the profiler for perfomance tests and more.
* this directory contains the static resoures like css, js, favicon etc.


web/bundles
-----------

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
