.. _database:

Configuring the database
########################

General
*******

To configure the database connection both files, config.yml and paramters.yml are used (see also `the Symfony Documentation <http://symfony.com/doc/current/best_practices/configuration.html>`_). While the config.yml file contains only the placeholders, the values for the database connection are placed in the paramters.yml.

You can find examples for the Configuration in our `Installation Instructions <installation.html>`_, for example in the chapter `Configuration of Mapbender3 on Ubuntu and Debian <installation/installation_ubuntu.html#configuration-of-mapbender3>`_.


.. _doctrine:

Doctrine
********

In Mapbender3 we use Doctrine which is a set of PHP libraries and offers an Object Relational Mapper and a Database Abstraction Layer. Visit the `Doctrine project page <http://www.doctrine-project.org/>`_ and read more.


Database definition
*******************

The standard database definition in the config.yml looks like this:

.. code-block:: yaml

    doctrine:
        dbal:
            driver:   %database_driver%
            host:     %database_host%
            port:     %database_port%
            dbname:   %database_name%
            path:     %database_path%
            user:     %database_user%
            password: %database_password%
            charset:  UTF8
            logging: %kernel.debug%
            profiling: %kernel.debug%
        orm:
            auto_generate_proxy_classes: %kernel_debug%
            auto_mapping:true

All values encapsulated in % are parameters, loaded from the parameters.yml. The parameters.yml will load these parameters. Therefore, to change the database, modify the parameters values in the parameters.yml.


* database_driver: The driver of the database. Possible values are:

  * pdo_sqlite - SQLite PDO driver
  * pdo_mysql - MySQL PDO driver
  * pdo_pgsql - PostgreSQL PDO driver
  * oci8 - Oracle OCI8 driver
  * pdo_oci - Oracle PDO driver

 Please keep in mind, that you have installed resp. activated the appropriate PHP-driver.

* database_host: The host, where the database is installed. Either the name (e.g. localhost) or the IP-address (e.g.. 127.0.0.1).
* database_port: The port, on which the database listens (e.g. 5432 for PostgreSQL).
* database_name: The Name of the database (e.g. mapbender3). Create the database and the scheme with ``doctrine:database:create`` resp. ``doctrine:schema:create``, see `Installation Instructions <installation.html>`_ for details.
* database_path: The %database_path% is the path to a SQLite database. If you don't use a SQLite database, don't delete the parameter from the parameters.yml though. Just put in as a value a tilde (~) or ``null``.
* database_user: Username for the connection to the database.
* database_password: The password of the database-user.
* charset: The codepage that the database uses.
* logging: This options sets, that all SQL statements are not  logged. (Default: %kernel.debug%). `Further information <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste/>`_.
* profiling: This option handles the profiling of SQL statements. This option can be switched off in production environments (Default: %kernel.debug%).



Using multiple databases
~~~~~~~~~~~~~~~~~~~~~~~~

Using multiple databases is easy with Mapbender3 and advised if you want to separate your own data from Mapbender's. This is useful in a scenario where you have your own custom code provided by an non-Mapbender bundle.

There's always a default database connection and all Mapbender code assumes that it can access it's data using that default database connection.

So if your code wants to use a different database you have to define a second named database connection and always
use that named database connection.

* Write the additional parameter "default_connection". This is the database-connection that Mapbender3 uses as the default (e.g. ``default_connection: default`` or ``default_connection: search_db``).

Here is an example for a database connection block in the **config.yml** with two connections:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                default:
                    driver:   %database_driver%
                    host:     %database_host%
                    port:     %database_port%
                    dbname:   %database_name%
                    path:     %database_path%
                    user:     %database_user%
                    password: %database_password%
                    charset:  UTF8
                    logging: %kernel.debug%
                    profiling: %kernel.debug%
                search_db:
                    driver:   %database2_driver%
                    host:     %database2_host%
                    port:     %database2_port%
                    dbname:   %database2_name%
                    path:     %database2_path%
                    user:     %database2_user%
                    password: %database2_password%
                    charset:  UTF8
                    logging: %kernel.debug%
                    profiling: %kernel.debug%


The definition of the database variables is done in the file **parameters.yml**.

.. code-block:: yaml

    parameters:
        # database-connection "default"
        database_driver:   pdo_pgsql
        database_host:     localhost
        database_port:     5432
        database_name:     mapbender3
        database_path:     ~
        database_user:     postgres
        database_password: postgres

        # database-connection "search_db"
        database2_driver:   pdo_pgsql
        database2_host:     localhost
        database2_port:     5432
        database2_name:     search_db
        database2_path:     ~
        database2_user:     postgres
        database2_password: postgres
