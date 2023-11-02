.. _directory_structure:

Directory structure in Mapbender
################################

app
***
This directory contains:

* the php-Cache (var/cache)
* the logs (var/log)
* the configuration directory (config)
* the applicationkernel (src/Kernel.php) (this is called by the FrontendControllers and controlls the whole application)
* the Autoloading (autoload.php) 
* the application specific resource directory (Resources)
* the command line application for maintaining and management tasks (bin/console)


config
------

Basic configuration files of Mapbender are placed in the config directory and the config/packages directory. Two files are of particular importance:

* parameters.yaml

* packages/doctrine.yaml

More Information: :ref:`yaml`.

  
config/applications
-------------------

The directory config/applications contains all applications that are defined in a YAML file. 

More Information: :ref:`yaml` .


bin
***

Here you find some libraries.



mapbender
*********

Directory of the `Mapbender submodule <https://github.com/mapbender/mapbender>`_. Provides the mapbender-specific bundles and the Mapbender code.


mapbender/...../translations
----------------------------

Directory: mapbender/src/Mapbender/CoreBundle/Resources/translations/

The translations are stored in `YAML-Dateien <https://en.wikipedia.org/wiki/YAML>`_. Every language needs an YAML-file like messages.en.yaml for the English translation.



public
******

This directory has to be published by the webserver. The ALIAS has to refer to this directory. 

It controls: 

* the FrontendController (PHP-Script, which can be called). These are **app.php** for the productive-system and **app_dev.php** for the development version. The development version contains the profiler for perfomance tests and more.
* this directory contains the static resoures like css, js, favicon etc.


public/bundles
--------------

* storage for the static resources of the single bundles.
* the following command copies the resources from the bundles to the folder: 

.. code-block:: yaml

     bin/console assets:install --symlink --relative public

* **Notice**: If you use Windows, you cannot create symbolic links and therefore have to run the command (**bin/console assets:install public**) to copy the files to the directory after every change in the code.



src
***

* directory for applications specific bundles


vendor
******
* Directory for external libraries (loaded by composer) are placed. Resources are used by Symfony using the Autoloading.
