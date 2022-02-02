.. _installation_symfony:

Installation of Mapbender using Symfony built-in webserver
##############################################

Mapbender is built on the `Symfony <http://symfony.com/>`_ Framework and therefore 
can make use of the `Symfony built-in webserver <http://symfony.com/doc/current/cookbook/web_server/built_in.html>`_. 
This setup allows a quick test of Mapbender without an integration into an external webserver. 

.. hint:: The use of the Symfony built-in webserver is not suitable for production environments. 

In this document we assume that the SQLite database is used.

* Please check the installation documentation for `Linux <installation_ubuntu.html>`_ respectively `Windows <installation_windows.html>`_ 
* Download the current Mapbender version https://mapbender.org/builds/.
* Extract Mapbender in an arbitrary directory.
* Start the Symfony webserver.

.. code-block:: bash

    app/console server:run

The command runs a local web server. By default, the server listens on 127.0.0.1 address 
and the port number is automatically selected as the first free port starting from 8000.

Now Mapbender is available on the local machine with the address http://127.0.0.1:8001/. 
Please note that Mapbender runs in the developer mode per default.



If you run the command several times Symfony will choose the next available port.


You also could change the default address and port by passing them as an argument:

.. code-block:: bash

    app/console server:run 127.0.0.1:80002
                                                                                                                                                                                                                                         
    [OK] Server listening on http://127.0.0.1:8002                                                                         
         
    // Quit the server with CONTROL-C.                                                                                     

    [Mon Jan 31 15:56:57 2022] PHP 7.4.3 Development Server (http://127.0.0.1:8002) started
