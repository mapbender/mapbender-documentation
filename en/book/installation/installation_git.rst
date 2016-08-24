.. _installation_git:

Git-based installation
######################

If you want to participate in the Mapbender3 development or for some other reasons want to use the Git repositories from Mapbender3, follow this guide instead of the normal download. This guide is based on Ubuntu 12.04. For other distributions, you may need to adapt, especially package names like sphinx-common.

First check the `System Requirements <systemrequirements.html>`_. 

For the Git-based installations you also need:

* git     - have a look at the `Quick primer on using Git <../development/git.html>`_ to get familiar with git 
* cURL    - command line tool for transferring data with URL syntax, supporting HTTP, HTTPS and more
* pear    - PHP Extension and Application Repository 
* Phing   - `Phing <http://www.phing.info/>`_ Is Not GNU make; it's a PHP project build system or build tool based on ​Apache Ant.
* php5-dev - Of course the files for PHP5 module development.


Cloning the Repository
**********************

Get the code from the git repository. Cloning is easy, just issue the following command in your shell:

.. code-block:: bash

    git clone https://github.com/mapbender/mapbender-starter.git mapbender3
    cd mapbender3

If you have granted secure access you can use the SSH-URL: git@github.com:mapbender/mapbender-starter


Git-branches and the possibilities
**********************************

* master: The master-branch contains the current stabile version.
* Tags: We tag the releases in the source-code so you have the ability to check out the recent and the previous versions for yourself.
* release/3.0.5: This release branch contains the current bugfixes on which the next 3.0.5 release is built upon.
* release/3.0.6: This release-branch will contain the next version and includes the bugfixes of 3.0.5 and new functionality. At this time we don't recommend to use this branch.
* release/3.1: This branch will contain the future 3.1 version including new functionality. At this time we don't recommend to use this branch.


Therefore you can checkout different versions of Mapbender:

If you want to use the current version, check out the master-branch, like described above.

If you want to have a specific version, clone the repository and checkout a tag, for example 3.0.5.3:

.. code-block:: bash

                git tag -l
                git checkout v3.0.5.3

If you want to checkout the current 3.0.5 code, which will lead to the next 3.0.5.x version, clone the release/3.0.5 branch directly with -b

.. code-block:: bash

    git clone https://github.com/mapbender/mapbender-starter.git -b release/3.0.5 mapbender3


Fetching the Submodules
***********************

The starter application does not include the Mapbender3 bundles, these are
kept in a repository of their own and are included as a submodule of the
starter repository. To fetch them, issue the following command at the root
directory of your cloned repository:


.. code-block:: bash

	git submodule update --init --recursive



Composer
********

Mapbender3 requires additional libraries for runtime, like for example Symfony and Doctrine. Therefore Composer has to be configured and called (more information at http://getcomposer.org/download/):

.. code-block:: bash

    cd application
    curl -sS https://getcomposer.org/installer | php

Create a configuration file called parameters.yml. Copy the file application/app/config/parameters.yml.dist.


.. code-block:: bash

  cp app/config/parameters.yml.dist app/config/parameters.yml

Please read the chapter `Adapting the configuration file <configuration.html#adapting-the-configuration-file>`_ for details about the adjustments in the parameters.yml file.

And afterwards get the runtime dependencies like Symfony and Doctrine:

.. code-block:: bash

  ./composer.phar update 


Next steps from Installation
****************************

Now follow the steps that are described in  `Installation <installation_ubuntu.html>`_:

**Notice:** Please note that the git based code has an additional directory *application* (mapbender3/application/...). 

* Adapting the configuration file parameters.yml
* Creating the database
* Creating the database schema
* Copying/Linking the bundles' assets to the public web directory
* Initializing the role system
* Creating the "root" user
* Inserting srs parameters
* Inserting of applications from mapbender.yml into the database


Refer to web with a symbolic link
**********************************
As a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier

.. code-block:: bash

    app/console assets:install web --symlink --relative


Please notice that you might have to activate the :command:`FollowSymLinks` option to your apache Directory like this:


.. code-block:: apache

  Alias /mapbender3 /var/www/mapbender-starter/application/web/
  <Directory /var/www/mapbender-starter/application/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    Require all granted
    
    RewriteEngine On
    RewriteBase /mapbender3/
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>


Learn more about app/console
****************************
The Symfony Console Component makes it possible to create command-line commands. Doctrine for example comes with a couple of command-line commands you can use.

Read more in the Symfony documentation about `Console Commands <http://symfony.com/doc/current/components/console/usage.html>`_.

Here are some commands to help to find information:

.. code-block:: bash

 app/console                        - lists all assets
 app/console help                   - displays help
 app/console help list              - displays help for a special command
 app/console doctrine               - lists all functions from Doctrine 
 app/console mapbender              - lists all functions from mapbender 
 app/console help assets:install    - help for a special command

Learn how to generate Mapbender elements with *app/console mapbender:generate:element* at `How to create your own Element? <../development/element_generate.html>`_.
        

Update your installation
************************

As development goes on you want to stay up-to-date with the code on github. 

There are following steps you have to do to stay up-to-date

* get the code from the mapbender-starter repository
* update the submodules 
* update your database so that new structures (tables, columns) will be created


.. code-block:: bash
 
 cd mapbender-starter
 git pull
 git submodule update --init --recursive
 cd application
 ./composer.phar update --dev
 app/console doctrine:schema:update


.. _installation_sphinx:

Sphinx (documentation)
**********************

Sphinx is used to build the documentation you are reading right now. On Debian-
based systems, you can use apt to install Sphinx:


.. code-block:: bash

   sudo apt-get install python-sphinx


You find the Mapbender3 documentation at github at mapbender-documentation. Get the clone like this: 

.. code-block:: bash

	git clone git://github.com/mapbender/mapbender-documentation

Developers granted secure access to the code must use the SSH-URL of the
repository: git@github.com:mapbender/mapbender-documentation

Read more about `How to write Mapbender3 Documentation? <../development/documentation_howto.html>`_.


ApiGen
******

`ApiGen <http://apigen.org>`_ is our API documentation generator of choice. It can also be installed using Pear (php-pear), so use the following command:

.. code-block:: bash
    
	 sudo pear install pear.apigen.org/apigen

Read more about `How to write Mapbender3 API Documentation? <../development/apidocumentation.html>`_.


Troubleshooting
***************

* The ApiGen task only works with recent versions of Phing (>= 2.4.12) which needs the Pear-Library. So, first
we need to get Pear, we are assuming a Debian-based system here:


.. code-block:: bash

	sudo apt-get install php-pear


We then tell Pear where to autodiscover it's repositories and for good measure, update Pear:


.. code-block:: bash

    sudo pear config-set auto_discover 1
    
    sudo pear upgrade-all
      Enable full APC compatibility [yes] : yes
      Enable internal debugging in APCu [no] : yes 

Then let's get Phing:

.. code-block:: bash

    sudo pear channel-discover pear.phing.info 
    sudo pear install phing/phing
     

Check the Phing version with:


.. code-block:: bash

              phing -v
