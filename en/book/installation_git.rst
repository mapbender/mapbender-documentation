.. _installation_git:

Git-based installation
######################

If you want to participate in the Mapbender3 development or for some other
reasons want to use the Git repositories from Mapbender3, follow this guide
instead of the normal download. This guide is based on Ubuntu 12.04. For
other distributions, you may need to adapt, especially package names like
sphinx-common.

First check the prerequisites at :doc:`Installation <installation>`. 

For git-based installations you also need:

* git     - have a look at the :doc:`Quick primer on using Git <development/git>` to get familiar with git 
* cURL    - command line tool for transferring data with URL syntax, supporting HTTP, HTTPS and more
* pear    - PHP Extension and Application Repository 
* Phing   - `Phing <http://www.phing.info/>`_ Is Not GNU make; it's a PHP project build system or build tool based on ​Apache Ant.


Cloning the Repository
**********************

Get the code from the git repository. Cloning is easy, just issue the following command in your shell:

.. code-block:: yaml

	git clone -b 3.0 git://github.com/mapbender/mapbender-starter

Developers granted secure access to the code must use the SSH-URL of the
repository: git@github.com:mapbender/mapbender-starter


Fetching the Submodules
***********************

The starter application does not include the Mapbender3 bundles, these are
kept in a repository of their own and are included as a submodule of the
starter repository. To fetch them, issue the following command at the root
directory of your cloned repository:


.. code-block:: yaml

	git submodule update --init --recursive


cURL
====

Our build system uses cURL to fetch some remote components, therefore you need
to install the cURL command line tool:


.. code-block:: yaml

	sudo apt-get install curl

.. _phing:



Build management using Phing
****************************

Build management is done using `Phing` which is installed using Pear. So, first
we need to get Pear, we are assuming a Debian-based system here:

.. code-block:: yaml

	sudo apt-get install php-pear

We then tell Pear where to autodiscover it's repositories and for good measure,
update Pear:


.. code-block:: yaml

    sudo pear config-set auto_discover 1
    sudo pear upgrade-all

Then let's get Phing:


.. code-block:: yaml

    sudo pear channel-discover pear.phing.info 
    sudo pear install phing/phing

PHPUnit
=======

Symfony2 needs a more recent PHPUnit than for example comes with Ubuntu 12.04.
So we will use Pear to install PHPUnit:


.. code-block:: yaml

	sudo pear install phpunit/PHPUnit


Our build scripts need some more dependencies to run unit test, generate
documentation and build installation packages.

Once you have installed the dependencies listed below, you can get an overview
of available build tasks by issuing


.. code-block:: yaml

   phing -l

The first task you want to - actually need to - execute is the deps task, which
uses `Composer http://getcomposer.org`_ to install the runtime dependencies like
Symfony and Doctrine:

.. code-block:: yaml

	phing deps


Next steps from Installation
****************************

Now follow the steps that are described in  :doc:`Installation <installation>`:

* Adapting the configuration file
* Creating the database
* Creating the database schema
* Copying the bundles' assets to the public web directory
* Initializing the role system
* Creating the "root" user
* Inserting srs parameters


Refer to web with a symbolic link
**********************************
As a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier

.. code-block:: yaml

    app/console assets:install web --symlink --relative

Please notice that you might have to activate the :command:`FollowSymLinks` option to your apache Directory like this:


.. code-block:: yaml

  Alias /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>


Learn more about app/console
****************************
The Symfony Console Component makes it possible to create command-line commands. Doctrine for example comes with a couple of command-line commands you can use.

Read more in the Symfony documentation about `Console Commands <http://symfony.com/doc/current/components/console/usage.html>`_.

Here are some commands to help to find information:
.. code-block:: yaml
 app/console                        - lists all assets
 app/console help                   - displays help
 app/console help list              - displays help for a special command
 app/console doctrine               - lists all functions from mapbender 
 app/console mapbender              - lists all functions from mapbender 
 app/console help assets:install    - help for a special command
        
..
 Package Build Tools
 ===================

 TODO: Skipped for now, KMQ has the knowledge.

Update your installation
========================
As development goes on you want to stay up-to-date with the code on github. 

There are following steps you have to do to stay up-to-date

* get the code from the mapbender-starter repository
* update the submodules 
* update your database so that new structures (tables, columns) will be created


.. code-block:: yaml
 
 cd mapbender-starter
 git pull
 git submodule update --init --recursive
 app/console doctrine:schema:update


.. _installation_sphinx:

Sphinx
======

Sphinx is used to build the documentation you are reading right now. On Debian-
based systems, you can use apt to install Sphinx:


.. code-block:: yaml

   sudo apt-get install sphinx-common


You find the Mapbender3 documentation at github at mapbender-documentation. Get the clone like this: 

.. code-block:: yaml

	git clone git://github.com/mapbender/mapbender-documentation

Developers granted secure access to the code must use the SSH-URL of the
repository: git@github.com:mapbender/mapbender-documentation

Read more about :doc:`How to write Mapbender3 Documentation? <development/documentation_howto>`.

ApiGen
======

`ApiGen <http://apigen.org>`_ is our API documentation generator of choice. It can
 also be installed using Pear, so use the following command:


.. code-block:: yaml
    
	 sudo pear install pear.apigen.org/apigen

Read more about :doc:`How to write Mapbender3 API Documentation? <development/apidocumentation>`.


Troubleshooting
***************

* The ApiGen task only works with recent versions of Phing (>= 2.4.12). Check the Phing version with 


.. code-block:: yaml

              phing -v


You can update all your Pear packages with


.. code-block:: yaml

	sudo pear upgrade-all


