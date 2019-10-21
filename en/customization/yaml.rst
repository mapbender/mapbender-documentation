.. _yaml_de:

YAML Configuration (Configuration and Application files)
========================================================

The following Configuration files are under application/app/config.


parameters.yml
--------------
Fundamental parameters are specified here.


**Database**
************

To configurate the database the files config.yml and parameters,yml are needed.
The config.yml contains placeholders for variables, which are specified in the parameters.yml.

The  database standard definiton set in the config.yml:

.. code-block:: yaml

    doctrine:                                               # Values, surrounded by %-marks, are variables
        dbal:
            default_connection: default                     # Database connection, used as standard in Mapbender (``default_connection: default``).
            connections:
                default:
                driver:    "%database_driver%"              # More information below the code
                host:      "%database_host%"                # Database host on which the database runs. Either name of the host (e.g. localhost) or IP address (e.g. 127.0.0.1).
                port:      "%database_port%"                # Port, the database listens to (e.g. 5432 for PostgreSQL).
                dbname:    "%database_name%"                # Name of the database (e.g. mapbender). Create a database with the command ``doctrine:database:create`` bzw. ``doctrine:schema:create``. More information:  `Installation<../installation.html>`_.
                path:      "%database_path%"                # %database_path%, path to the file of the SQLite database. If you don't use a SQ-lite database, write (~) or ``null``.
                user:      "%database_user%"                # User name for database connection.
                password:  "%database_password%"            # Password.
                charset:    UTF8                            # Coding of the database.
                logging:   "%kernel.debug%"                 # Option, SQLs won't be logged (standard: %kernel.debug%). `More information: <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
                profiling: "%kernel.debug%"                 # Profiling SQL requests. This option can be turned of in production. (standard: %kernel.debug%)


