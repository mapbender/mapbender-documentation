.. _directory_structure:

Directory structure in Mapbender
################################

bin
***

Mapbender-related libraries are stored here, e.g.:

* The command line application for maintaining and managing tasks (`bin/console`)

config
******

Basic configuration files of Mapbender are placed in the `config/` directory and the `config/packages` directory. These files are of particular importance:

* :ref:`doctrine.yaml<en/customization/yaml:doctrine.yaml>`
* :ref:`parameters.yaml<en/customization/yaml:parameters.yaml>`
* *services.yaml*: Serves as entry point to configure services.

config/applications
-------------------

The directory `config/applications` contains all applications that are defined in a YAML file. 

Find more information in :ref:`yaml` .

mapbender
*********

* Directory of the `Mapbender submodule <https://github.com/mapbender/mapbender>`_. Provides the Mapbender-specific bundles and the Mapbender code.
* Directory for application resources (`Resources/`)

mapbender/...../translations
----------------------------

Directory: `../mapbender/src/Mapbender/CoreBundle/Resources/translations/`

The translations are stored in `YAML files <https://en.wikipedia.org/wiki/YAML>`_. Every language needs a YAML-file, like *messages.fr.yaml* for the French translation of Mapbender.

public
******

This directory has to be published by the webserver. The ALIAS has to refer to this directory. 
It contains the static resoures like css, js, favicon etc.

It controls: 

* *index.php* - the FrontendController (PHP script which can be called).
* *index_dev.php* - FrontendController for easy access to the development environment. By default, it can only be accessed from local IP addresses.

public/bundles
--------------

* Is the storage for the static resources of the single bundles.
* The following command copies the resources from the bundles to the folder: 

.. code-block:: yaml

     bin/console assets:install --symlink --relative public

.. note:: If you use Windows, you cannot create symbolic links and therefore have to run the command ``bin/console assets:install public`` to copy the files to the directory after every change in the code.


src
***

* Directory for applications specific bundles
* The application kernel (`src/Kernel.php`) (is called by the FrontendControllers and controls the whole application)

var
***

This directory contains:

* the caches (`var/cache/dev` and `var/cache/prod`)
* the logs (`var/log`)
* Sqlite-databases (`var/db`)

vendor
******

Directory for external libraries (loaded by composer) are placed here. Resources are used by Symfony using the Autoloading:

* Autoloading: *autoload.php*
