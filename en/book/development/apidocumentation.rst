.. _apidocumentation:

API documentation
#################

Mapbender3 offers an API documentation at http://api.mapbender3.org/.

The API documentation is shipped with Mapbender and can be created with:

.. code-block:: yaml

                bin/composer docs

The documentation is then available at: http://localhost:8000/docs/api/ and the Mapbender-documentation at: http://localhost:8000/docs/

Please see the `Contributing Guide for details on using the built-in server <https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md#start-web-server>`_.

For usage in Apache or Nginx, you may have to adjust the access-rights for the generated files in the web-directory of Mapbender.


How to write Mapbender3 API Documentation?
*******************************************

PHP
~~~~~~

`ApiGen <http://apigen.org>`_ is used to generate API documentation. 'All' you
have to do is to insert docblocks in your code. Below you find an example class
with docbblock annotations:

.. literalinclude:: Example.php
    :language: html+php
    :linenos:

Have a look at the docblocks at `Example.php <https://github.com/mapbender/mapbender-documentation/blob/master/de/book/development/Example.php>`_.


JavaScript
**********

This has not yet been decided as good tools are almost not to be found.
