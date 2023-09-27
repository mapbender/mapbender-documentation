.. _installation_symfony:

Installation of Mapbender using Symfony built-in webserver
##########################################################

Mapbender is built on the `Symfony <http://symfony.com/>`_ Framework and therefore can make use of the `Symfony CLI developer tool <https://symfony.com/download>`_, which needs to be installed first. 
This setup allows a quick test of Mapbender without an integration into an external webserver. 

.. hint:: The use of the Symfony built-in webserver is not suitable for production environments. 

In this document we assume that the SQLite database is used.

* Please check the installation documentation for :ref:`Linux <installation_ubuntu>` respectively :ref:`Windows <installation_windows>`. 
* Download the current Mapbender version https://mapbender.org/builds/.
* Extract Mapbender in an arbitrary directory.
* Start the Symfony webserver:

.. code-block:: bash

    symfony server:start --no-tls


The command runs a local web server. By default, the server listens on 127.0.0.1 address and the port number is automatically selected as the first free port starting from 8000.

Now Mapbender is available on the local machine with the address http://127.0.0.1:8000/. 

.. note:: Please note that you can pass the application environment (`prod` or `dev`) with the command below.

.. code-block:: bash

    APP_ENV=prod symfony server:start --no-tls


You could also change the default port by passing it as an argument. For more options, check the ``--help`` flag:

.. code-block:: bash

    symfony server:start --no-tls -port=8002


.. code-block:: yaml

 [OK] Web server listening
      The Web server is using PHP CLI 8.2.10
      http://127.0.0.1:8002
