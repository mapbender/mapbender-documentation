.. _directory_structure:

Directory structure in Mapbender
################################

app
***
This directory contains:

* the php-Cache (var/cache)
* the logs (var/logs)
* the configuration directory (config)
* the applicationkernel (app/AppKernel.php) (this is called by the FrontendControllers and controlls the whole application)
* the Autoloading (autoload.php) 
* the application specific resource directory (Resources)
* the command line application for maintaining and management tasks (bin/console)


config
------

Basic configuration files of Mapbender are placed in the config directory. Two files are of particular importance:

* parameters.yml

* config.yml

More Information: :ref:`yaml`.

  
config/applications
-------------------

The directory config/applications contains all applications that are defined in a YAML file. 

More Information: :ref:`yaml` .


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

* storage for the static resources of the single bundles.
* the following command copies the resources from the bundles to the folder: 

.. code-block:: yaml

     bin/console assets:install --symlink public

* **Notice**: If you use Windows, you cannot create symbolic links and therefore have to run the command (**bin/console assets:install public**) to copy the files to the directory after every change in the code.


src
***

* directory for applications specific bundles (similar to the former x-directories in Mapbender 2.x)


vendor
******
* directory where all the Bundles which are used from Symfony are found. Resources are used by Symfony using the Autoloading.
