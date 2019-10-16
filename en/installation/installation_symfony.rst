.. _installation_symfony:

Installation in the Symfony built-in webserver
##############################################

Mapbender is built on the `Symfony <http://symfony.com/>`_ Framework and therefore can take usage of the `Symfony built-in webserver <http://symfony.com/doc/current/cookbook/web_server/built_in.html>`_. This allows a quick test of Mapbender without an integration into an external webserver. This is not suited for production environments. In this document we assume that the SQLite database is used.

* Take notice of the installation documentation `Linux <installation_ubuntu.html>`_ bzw. `Windows <installation_windows.html>`_ 
* Download the current Mapbender version https://mapbender.org/builds/.
* Extract Mapbender in an arbitrary directory.
* Start the Symfony webserver:

  .. code-block:: bash

                  app/console server:run 0.0.0.0:8000

After that Mapbender ist available from the host-machine with the URL http://ip-adresse:8000/app.php.
