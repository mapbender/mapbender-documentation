.. _installation_symfony:

Launching Mapbender using the local Symfony web server
######################################################

Launching Mapbender on the local Symfony web server allows for quick configuration using Symfony's native mechanisms. This enables you to perform tests without the need to integrate it into a separately set up web server.

.. note:: The local web server bundle has been removed and replaced with the local Symfony web server. Install the `Symfony CLI development tool <https://symfony.com/download>`_ to use it.

.. hint:: The use of the Symfony built-in web server is not suitable for production environments. 

In this document we assume that the SQLite database is used.

* Please check the installation documentation for :ref:`Linux <installation_ubuntu>` respectively :ref:`Windows <installation_windows>`. 
* Download the current `Mapbender build <https://mapbender.org/builds/>`.
* Extract Mapbender in an arbitrary directory.
* Start the installed local Symfony web server.

.. code-block:: bash

    symfony server:start --no-tls


The command runs a local web server, so that Mapbender is available on the local machine. By default, the server listens on 127.0.0.1 address and the port number is automatically selected as the first free port starting from 8000.

.. note:: Please note that you can pass the application environment (``prod`` or ``dev``) with the command below.

.. code-block:: bash

    APP_ENV=prod symfony server:start --no-tls


You could also change the default port by passing it as an argument. For more options, check the ``--help`` flag:

.. code-block:: bash

    symfony server:start --no-tls -port=8002


.. code-block:: yaml

 [OK] Web server listening
      The Web server is using PHP CLI 8.2.10
      http://127.0.0.1:8002
