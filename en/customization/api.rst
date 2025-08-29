.. _api:

API
***

Mapbender provides an API that allows you to run several commands.

With the API clients can administrate Mapbender without the need to use the web administration interface. The API provides commands to get information for example about services and it also provides commands to publish or update services.

.. image:: ../../figures/customization/api.png
     :width: 100%


Documentation
-------------

The API documentation is integrated in every Mapbender installation and it is publicly available via http://localhost/mapbender/api/doc/

You find examples for each endpoint in the documentation. Please note that you need to login and authorize to run the examples. You also need the right "API" (see ACL).

You can browse through the documentation at the Mapbender demo: 

https://demo.mapbender.org/api/doc/

Further information about the API is provided in the Developer Documentation:

https://github.com/mapbender/mapbender/blob/develop/docs/api/setup.md


Apache Authorisation
--------------------

By default, Apache does not forward the Authorization header to the client for security reasons. However, this is necessary to use the API. The following must therefore be set in the VirtualHost or the configuration:

.. code-block:: apacheconf
     
   SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1


Configure Upload Directory
--------------------------

You can configure the upload directory using the 

.. code-block:: yaml

     api_upload_dir: /data/qgis_server_projects/ 
     
parameter in the *parameters.yaml* file.


Disable the API page from public access
---------------------------------------

You can disable the public access to the API documentation page by modifing the *security.yaml*. Please change

.. code-block:: yaml

   { path: ^/api/doc, roles: PUBLIC_ACCESS }

to

.. code-block:: yaml

   { path: ^/api/doc, roles: ROLE_ADMIN }