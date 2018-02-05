.. _systemrequirements:

System requirements and download
################################

System requirements
*******************

Mapbender needs the following components in order to run:

* PHP 5.5.4 or later (php5)
* PHP CLI interpreter (php5-cli)
* PHP SQLite extension (php5-sqlite)
* PHP cURL extension (php5-curl)
* PHP Internationalization (php5-intl)
* PHP GD for printing (php5-gd)
* PHP Multibyte String (php5-mbstring)
* PHP FileInfo for printing to check image format
* APACHE mod_rewrite 
* OpenSSL
* For development, particular the phantomjs helper, you need also the BZ2 extension. (php-bz2)

For Suse SLES and PHP 7 you also have to install (extra packages in SLES):
* php7-zlib
* php7-fileinfo


PHP 7
-----

Mapbender supports also PHP 7. You'll need the above listed libraries for PHP 7 and the following additional ones:

* PHP Zip (php-zip)
* PHP Bz2 (php-bz2)
* PHP XML (php-xml)


Databases
---------

Optionally, in order to use a database other than the preconfigured SQLite one, you need a matching PHP extension supported by `Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. For PostgreSQL for example: php5-pgsql.

If you want to use the developer mode or for creating create profiler data to be used to analyze errors you will still need the SQLite extension!


System requirements Windows
***************************

For Windows you also need `PHP <http://www.php.net/>`_ and therefore a PHP-supporting webserver like `Apache <http://httpd.apache.org/>`_.

We have good experiences with the 64-bit downloads of Apache und PHP.

* `Apache Download <http://www.apachelounge.com/download/>`_: The downloads of the Apache Lounge are customized for different Versions of Windows. For newer versions choose the "VC11" or "VC14" variant (this requires the Visual C++ Redistributable für Visual Studio 2012 resp. 2015) and the Win64 version (64-bit).

* `PHP Download <http://windows.php.net/download#php-5.6>`_: Choose the "Non Thread Safe" variant of the PHP downloads as the x64 version (64-bit).


Comments on Windows
-------------------

The Apache downloads differ on the version of Visual Studio which was used to compile them and therefore of the right version of the Microsoft Visual C++ Redistributable. With newer versions of Windows this is usualy without problems. Three different variants exist:

* **VC 14**: Requires Visual C++ Redistributable for Visual Studio 2015.
* **VC 11**: Requires Visual C++ Redistributable for Visual Studio 2012. PHP usually needs this version.
* **VC 10**: Requires Visual C++ Redistributable for Visual Studio 2008 SP1.

Additionally 32- and 64-bit versions of Apache für Windows exist.


Download of Mapbender
*********************

Installation packages are distributed as compressed packages and are available for download at the `download <http://mapbender.org/download>`_ page.

After downloading, extract the package in a directory of your choice. In this installation documentation we assume that the package is extracted in the following directories:

* **/var/www** (for Linux) or
* **C:/** (for Windows, not recommended, for this doku only).

For the following installation steps, please rename the unzipped directory (for example: "mapbender3-3.0.5.2") to "mapbender".

You'll find the next steps of the installation in the following chapters:

* `Installation on Ubuntu and Debian <installation_ubuntu.html>`_
* `Installation on Windows <installation_windows.html>`_


For a quick Test you can also follow the `Installation in the Symfony built-in webserver <installation_symfony.html>`_. The `Git-based installation <installation_git.html>`_ does not require theses Download packages but loads Mapbender from the Git-sources. In exchange additional installation steps are neccessary.


Directory structure
-------------------

After unpacking the TAR.GZ- resp. the ZIP-archive, you will see in the Mapbender-folder the following subdirectories:

.. code-block:: bash
                
                .
                ├── app
                ├── bin
                ├── fom
                ├── mapbender
                ├── owsproxy
                ├── src
                ├── vendor
                └── web
