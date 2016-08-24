FAQ - Frequently Asked Questions
=============================


Performance
-----------

Working with large wms clients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: During the upload of large wms into an application (e.g. wms with more than 100 layers), the configuration of the `Layerset-Instance <../de/bundles/Mapbender/CoreBundle/entities/layerset.html>`_ only takes and presents an incorrect amount of layers. In addition, the wms instance cannot be saved. Why?

A: To solve the problem, navigate to the php parameter `max-input_vars <http://php.net/manual/de/info.configuration.php#ini.max-input-vars>`_. It defines the number of possible input variables. The default value is 1000 (depending on the php version). In a wms with many layers, the number of input values is higher than the default value. You have to change the parameter to a higher value (e.g. 2000). Notice that the number is directly dependent to the amount of layers in a wms.

.. code-block:: ini

   ;; 1000 (default) oder höher
   max_input_vars = 1000 



The access to an Oracle database is too slow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: Mapbender seems to have a poor performance while accessing Oracle
databases. I noticed this because queries need more time than usual. Can I accelerate the process?

A: There are two parameters in php.ini which may tweak the performance of Mapbender with Oracle databases: `oci8.max_persistent <http://php.net/manual/de/oci8.configuration.php#ini.oci8.max-persistent>`_ and `oci8.default_prefetch <http://php.net/manual/de/oci8.configuration.php#ini.oci8.default-prefetch>`_. Adjust these parameters to:

.. code-block:: ini

   oci8.max_persistent = 15
   oci8.default_prefetch = 100000

Furthermore, change the respective persistent database connection parameter in config.yml to true.

.. code-block:: yaml

   persistent=true


My application cannot be duplicated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Q: I made a highly complex application and want to duplicate it, but it does not work.

A: A possible reason for this is that php does not allow a workflow with big files (YAML-export/import/etc.). The problem occurs especially in FastCGI. Just adjust the php parameter MaxRequestLen (you can do that in the configuration of FCGI).

.. code-block:: ini

   # mod_fcgi.conf (Windows)
   # set value to 2 MB
   MaxRequestLen = 2000000
   
   # fcgid.conf (Linux)
   # set value to 2 MB
   MaxRequestLen 2000000


Simutaneously, you should check the php values in php.ini:

.. code-block:: ini

   max_execution_time = 240
   memory_limit = 1024M
   upload_max_filesize = 2M
