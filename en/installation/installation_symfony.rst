.. _installation_symfony:

Installation in the Symfony built-in webserver
##############################################

Mapbender is built on the `Symfony <http://symfony.com/>`_ Framework and therefore can take usage of the `Symfony built-in webserver <http://symfony.com/doc/current/cookbook/web_server/built_in.html>`_. This allows a quick test of Mapbender without an integration into an external webserver. This is not suited for production environments. In this document we assume that the SQLite database is used.

* Take notice of the `system requirements <systemrequirements.html>`_
* Download Mapbender.
* Extract Mapbender in an arbitrary directory.
* Copy the parameters.yml.dist to parameters.yml.

  .. code-block:: bash

                  cp app/config/parameters.yml.dist app/config/parameters.yml


* Start the Symfony built-in webserver:

  .. code-block:: bash

                  app/console server:run

* After that Mapbender is available at the URL http://localhost:8000/app.php.


In virtual environments
************************

If you want to run Mapbender on a virtual machine and access it from your hosting machine, use the following command:

.. code-block:: bash

                app/console server:run 0.0.0.0:8000

After that Mapbender ist available from the host-machine with the URL http://ip-adresse:8000/app.php.
