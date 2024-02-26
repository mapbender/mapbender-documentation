.. _faq:

FAQ - Frequently Asked Questions
================================

General
-------

Environments: `prod` and `dev`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: Why does Mapbender offer environments?

A: For productive use, you'll use the `prod` environment. If you develop something (TWIG-files, CSS or JS-files) or want to debug, you should use the `dev` environment. This is because this mode provides more information and error messages. 

For further information on the environments, please take a look at the chapter :ref:`environments`.


Cache
~~~~~

Q: What is the cache and when do I have to clear it?

A: The cache is a small storage area, where Mapbender accesses frequently needed application data. Cache clearing can be useful to refresh your Mapbender installation. You'll delete the contents of the ``mapbender/var/cache/`` directory, not the folder itself. In detail, the ``prod`` and - if present - the ``dev`` directory.

It is no problem to delete these directories. When you run Mapbender again, new files will be stored again in the cache directory.

For further information on the cache, please take a look at the chapter :ref:`app_cache`.


Services and their usage in applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I would like to know in which applications a specific WMS service is registered. Is there a way to achive that?

A: For users with permission, this information is provided in the :ref:`backend`:

* Go to ``Sources`` and find your source,
* Select it with a click on the button ``Show Metadata``, then go to the tab ``Applications``,
* Here, you can see in which application the source is loaded. Moreover, you can see whether the source is integrated as shared or private Instance and whether it is activated or inactive.
* Via click on the application title or the source instance, you can switch to the related layerset or instance setting.

If you prefer SQL, you can also take the WMS ID from the Source, replace the ``<id_of_the_wms>`` with it in the following SQL and run:

.. code-block:: postgres

                SELECT mb_core_application.* from mb_core_application, mb_core_layerset, mb_core_sourceinstance, mb_wms_wmsinstance, mb_wms_wmssource, mb_core_source where
                -- applications and their layersets
                mb_core_application.id = mb_core_layerset.application_id and
                -- layersets and their instances
                mb_core_layerset.id = mb_core_sourceinstance.layerset and
                -- layerset-instances and wms-instance      
                mb_core_sourceinstance.id = mb_wms_wmsinstance.id and
                -- wms-instance and wms-source
                mb_wms_wmsinstance.wmssource = mb_wms_wmssource.id and
                -- wms-source and mb-core source
                mb_wms_wmssource.id = mb_core_source.id and
                mb_core_source.id = <id_of_the_wms>;


Performance
-----------

My application cannot be duplicated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I made a highly complex application and want to duplicate it, but it does not work. Why is that?

A: A possible reason for this is that PHP does not allow a workflow with large files. The problem occurs especially in FastCGI. To fix this, you need to adjust the PHP parameter ``MaxRequestLen`` (you can do that in the FastCGI configuration).

.. code-block:: bash

   # mod_fcgi.conf (Windows)
   # set value to 2 MB
   MaxRequestLen = 2000000

   # fcgid.conf (Linux)
   # set value to 2 MB
   MaxRequestLen 2000000


Simultaneously, you should check if the following PHP values are set in your ``php.ini``:

.. code-block:: bash

   max_execution_time = 240
   memory_limit = 1024M
   upload_max_filesize = 2M


Adjusting WMS tiling values for ImageExport and PrintClient  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: My WMS service does not return images in my ImageExport or my PrintClient. Consequently, my output file does not contain layers from the service. What could be causing this?

A: This can have different reasons. Under some circumstances, the requested pixel dimension of a WMS can get too large.

In this case, add the following parameter to your ``parameters.yaml`` file - note that you have to adjust the default value according to your service.

.. code-block:: bash

   mapbender.imaageexport.renderer.wms.max_getmap_size: 8192


What does it do? The parameter sets the largest possible WIDTH= and HEIGHT= parameter values for WMS requests generated from the ImageExport and PrintClient elements. Moreover, the maximum resolution is defined in the ``MaxWidth`` or ``MaxHeight`` fields of the GetCapabilities request for the service, therefore it's helpful to check the service request for a value to be entered. ``WIDTH=`` and ``HEIGHT=`` parameters can also be limited separately. 


Adjust the width with this parameter and an individual value:

.. code-block:: bash

   mapbender.imaageexport.renderer.wms.max_getmap_size.x:


Adjust the height with this parameter and an individual value:

.. code-block:: bash
 
   mapbender.imaageexport.renderer.wms.max_getmap_size.y:


Working with large WMS Services with many layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: When I try to use a WMS Service with many layers (> 100) into an application, the configuration of the :ref:`layerset` only takes and presents an incorrect amount of layers. In addition, the wms instance cannot be saved. Why?

A: To solve the problem, navigate to the php parameter `max-input_vars <https://php.net/manual/de/info.configuration.php#ini.max-input-vars>`_. It defines the number of possible input variables. The default value is 1000 (depending on the php version). 
For a WMS with many layers, the number of input values is higher than the default value. You have to change the parameter to a higher value (e.g. 2000). 

.. code-block:: ini

   ;; 1000 (default)
   max_input_vars = 1000


Installation
------------

Attempted to call function "imagecreatefrompng"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I get an error while trying to generate a print output. I have looked into Mapbender's logfile (var/log/prod.log) and found something like this:

.. code-block:: php

                CRITICAL - Uncaught PHP Exception Symfony\Component\Debug\Exception\UndefinedFunctionException:
                "Attempted to call function "imagecreatefrompng"
                from namespace "Mapbender\PrintBundle\Component"."
                at /srv/mapbender-starter/application/mapbender/src/Mapbender/PrintBundle/Component/PrintService.php line 310

A: Please make sure you have installed the php-gd library, because it is necessary for this action. We recommend the installation of the extension before installing Mapbender.
However, it is always possible to install it afterwards, on Linux-based systems like this:

.. code-block:: bash

    sudo apt-get install php-gd


SSL certificate problem
~~~~~~~~~~~~~~~~~~~~~~~

Q: How can I fix my SSL certificate problem?

A: When you get an SSL certificate problem error on loading or updating an OGC WMS data source on Windows-based Mapbender servers, you have to update your ``cacert.pem`` file and refer to it in your ``php.ini``.

The problem can occur while accessing a service via https. It looks like this:

.. code-block:: bash
   
    cURL error 60: SSL certificate problem: unable to get local issuer certificate


.. note:: The file ``cacert.pem`` that is available online lists all trusted certificate authority. ``cacert.pem`` is base64-encoded with a definition for all trusted certificate authorities; you can download it from https://curl.haxx.se/docs/caextract.html.

The error above occurs if the file is not referenced in ``php.ini`` or if ``cacert.pem`` is not up-to-date.

How to refer to ``cacert.pem`` in ``php.ini``:
 
.. code-block:: bash

    curl.cainfo="C:\[your path]\cacert.pem"

    openssl.cafile="C:\[your path]\cacert.pem"


If you use an individual self-signed certificate, you can add the information of your certificate authority to ``cacert.pem``. 

Find further information in the PHP documentation at: https://www.php.net/manual/en/curl.configuration.php


Manually install Symfony dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: After updating, I need to install a Symfony component for my Mapbender installation. How can I achieve this?

A: It is possible to manually install Symfony components via the command line. This can be done using the following command:

.. code-block:: bash
   
   ./bin/composer install symfony/your-bundle


Just replace ``your-bundle`` with the corresponding component name.

You can find a list of componentens and dependencies in the `GitHub Symfony project <https://github.com/symfony/symfony/blob/5.4/composer.json#L58>`_.


Deprecation Notices at composer or bootstrap script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I get a deprecation warning when I call bootstrap or composer update:

.. code-block:: php

                Deprecation Notice: The callback ComposerBootstrap::checkConfiguration declared at
                /srv//mapbender-starter/application/src/ComposerBootstrap.php accepts a Composer\Script\CommandEvent
                but post-update-cmd events use a Composer\Script\Event instance.
                Please adjust your type hint accordingly, see https://getcomposer.org/doc/articles/scripts.md#event-classes
                in phar:///srv/mapbender-starter/composer.phar/src/Composer/EventDispatcher/EventDispatcher.php:290

A: This depends on the PHP version the system in running on and occurs on PHP versions < 7. Depending on the Mapbender release, we recommend different PHP versions that do not trigger the notices.


Development
-----------

Manual updates of modules
~~~~~~~~~~~~~~~~~~~~~~~~~

Q: How can I checkout a specific branch of the Mapbender module and test it? How can I revert this again? Does Composer help me with that?

A: Alternative 1 (via Git): Go in the directory application/mapbender and checkout the specific branch. After your tests, checkout the original branch again. Do not forget to clear the Symfony cache directory.

Alternative 2 (via Composer): Change the entry in composer: "mapbender/mapbender": "dev-fix/meinfix" and do a Composer Update. Keep in mind that with that step all other vendor packages will be updated. To go back, specify the original branch. In addition go back to application/mapbender and checkout the original branch.


Overriding twig templates
~~~~~~~~~~~~~~~~~~~~~~~~~

Q: What is the process for overriding twig templates in bundles, and how can I customize the design of specific elements in Mapbender?

A: Twig templates within bundles can be overridden by placing a twig file with the same name in `templates/bundles/<bundlename>`.
If, for example, you want to customise the coordinates display (`Resources/views/Element/coordinatesdisplay.html.twig` within the Mapbender CoreBundle), place a replacement file in `templates/bundles/MapbenderCoreBundle/Element/coordinatesdisplay.html.twig`. The new file will be used instead of the original one.


Oracle
------

Adjustments for Oracle database - point and comma
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I get an error when I run ``doctrine:schema:create`` on Oracle. Why? The error message is:

.. code-block:: bash

                [Doctrine\DBAL\Exception\DriverException]
                An exception occurred while executing
                'CREATE TABLE mb_wms_wmsinstance (id NUMBER(10) NOT NULL,
                                                  [...]
                                                  PRIMARY KEY(id))':
                ORA-01722: Invalid number

A: Probably Oracle can't handle the decimal seperators and expects a comma instead of a point (e.g. 1,25 instead of 1.25). This can be adjusted with the following snippet at the end of the ``doctrine.yaml`` (clear cache afterwards).

.. code-block:: yaml

                services:
                  oracle.session.listener:
                    class: Doctrine\DBAL\Event\Listeners\OracleSessionInit
                    tags:
                      - { name: doctrine.event_listener, event: postConnect }

This is a relation to a service-class provided by Doctrine. After the connection to Oracle, this class sets Session-Variables (ALTER SESSION) so that PHP and Oracle can work together in a better way.

Reasons might be: Language and regional settings of the operating system (for example Windows), settings of the Oracle-client, settings done during the installation of Oracle.


Rights management in Oracle database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: Which rights does the Mapbender user need for the Oracle database?

A: Mapbender needs permission to:

.. code-block:: bash

   - Create Sequence
   - Create Session
   - Create Table
   - Create Trigger
   - Create View


The access to an Oracle database is too slow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: Mapbender seems to have a poor performance while accessing Oracle databases. I noticed this because queries need more time than usual. How can I accelerate the process?

A: There are two parameters in ``php.ini`` which may tweak the performance of Mapbender with Oracle databases: `oci8.max_persistent <http://php.net/manual/de/oci8.configuration.php#ini.oci8.max-persistent>`_ and `oci8.default_prefetch <http://php.net/manual/de/oci8.configuration.php#ini.oci8.default-prefetch>`_. Adjust these parameters to:

.. code-block:: bash

   oci8.max_persistent = 15
   oci8.default_prefetch = 100000


Furthermore, change the respective persistent database connection parameter in ``doctrine.yaml`` to true.

.. code-block:: bash

                persistent: true
