.. _owsproxy3:

OWSProxy3
***********************

OWSProxy3 allows you to hide your services behind a proxy.


Class, Widget & Style
==============

* Class: <Put PHP class name here>
* Widget: <Put Widget name here>
* Style: <Put name of css file here>

Configuration
=============

The configuration is done in the file config.yml at the section ows_proxy3_core.

.. code-block:: yaml

ows_proxy3_core:
    logging: true
    obfuscate_client_ip: true  
    proxy:
        host: localhost
        port: 8888
        user: user
        password: password
        noproxy:
            - host_a
            - host_b
