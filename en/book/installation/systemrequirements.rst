.. _systemrequirements:

System requirements and download
################################

System requirements
*************

Mapbender3 needs the following components in order to run:

* PHP 5.4 or later (php5)
* PHP CLI interpreter (php5-cli)
* PHP SQLite extension (php5-sqlite)
* PHP cURL extension (php5-curl)
* PHP Alternative PHP Cache (php-apc)
* PHP Internationalization (php5-intl)
* PHP GD for printing (php5-gd)
* PHP FileInfo for printing to check image format
* APACHE mod_rewrite 
* OpenSSL

Optionally, in order to use a database other than the preconfigured SQLite one, you need a matching PHP extension supported by `Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. For PostgreSQL for example: php5-pgsql.

If you want to use the developer mode or for creating create profiler data to be used to analyze errors you will still need the SQLite extension!


System requirements Windows
***************************

For Windows you also need `PHP <http://www.php.net/>`_ and therefore a PHP-supporting webserver like `Apache <http://httpd.apache.org/>`_.

We have good experiences with the 64-bit downloads of Apache und PHP.

* `Apache Download <http://www.apachelounge.com/download/>`_: The downloads of the Apache Lounge are customized for different Versions of Windows. For newer versions choose the "VC11" or "VC14" variant (this requires the Visual C++ Redistributable für Visual Studio 2012 resp. 2015) and the Win64 version (64-bit).

* `PHP Download <http://windows.php.net/download#php-5.6>`_: Choose the "Thread Safe" variant of the PHP downloads as the x64 version (64-bit).


Comments on Windows
-------------------

The Apache downloads differ on the version of Visual Studio which was used to compile them and therefore of the right version of the Microsoft Visual C++ Redistributable. With newer versions of Windows this is usualy without problems. Three different variants exist:

* **VC 14**: Requires Visual C++ Redistributable for Visual Studio 2015.
* **VC 11**: Requires Visual C++ Redistributable for Visual Studio 2012. PHP usually needs this version.
* **VC 10**: Requires Visual C++ Redistributable for Visual Studio 2008 SP1.

Additionally 32- and 64-bit versions of Apache für Windows exist.


Download of Mapbender3
**********************

Installation packages are distributed as compressed packages and are available
for download at the `download <http://mapbender3.org/download>`_ page.

After downloading, extract the package in a directory of your choice. In this installation documentation we assume that the package is extracted in the directory /var/www.

