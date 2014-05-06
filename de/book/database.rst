Konfiguration der Datenbank
############################

.. _doctrine:
Doctrine
*************
Mapbender3 verwendet Doctrine. Doctrine ist eine Sammlung von PHP Bibliotheken und beitet einen objektrelationalen Mapper und eine Datenbankabstraktionsschicht. 
Auf der `Doctrine Projektseite <http://www.doctrine-project.org/>`_ finden sich weitere Informationen.

Database Definition
********************

Die Standarddatenbankdefinition erfolgt in der config.yml und sieht folgendermaßen aus:

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
        orm:
            auto_generate_proxy_classes: %kernel_debug%

Bei Werten, die von dem %-Zeichen umschlossen werden, handelt es sich um Parameter. Diese Parameter werden von der  parameters.yml geladen. Um die Art der Datenbank zu ändern, müssen daher die Parameterwerte in der parameters.yml verändert werden. Mögliche Werte für den Parameter %database_driver% sind:

* pdo_sqlite - SQLite PDO driver
* pdo_mysql - MySQL PDO driver
* pdo_pgsql - PostgreSQL PDO driver
* oci8 - Oracle OCI8 driver
* pdo_oci - Oracle PDO driver

Die Parameter sollten selbsterklärend sein. Der %database_path% ist der Pfad zur Datei der  SQLite-Datenbank. Wenn Sie keine SQLite-Datenbank verwenden, löschen Sie bitte den Parameter trotzdem nicht aus der parameters.yml. Es würde ein Fehler erzeugt


Verwendung mehrerer Datenbanken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit Mapbender3 können Sie auch mehrere Datenbanken verwenden. Dies wird empfohlen, wenn Sie Ihre eigenen Daten von den Mapbender3-Daten trennen möchten. Das kann nützlich sein, wenn Sie eigenen Code verwenden, der nicht zu einem Mapbender3-Bundle gehört.

Es gibt eine Standard-Datenbankverbindung, die vom Mapbender3 verwendet wird.

Wenn Sie eine andere Datenbank verwenden möchten, müssen Sie eine zweite Datenbankverbindung mit einem anderen Namen definieren und diese verwenden. Weiter ist nichts zu tun.

Es folgt ein Beispiel mit zwei Datenbankverbindungen in der **config.yml**:

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
                search_db:
                    driver:   %database2_driver%
                    host:     %database2_host%
                    port:     %database2_port%
                    dbname:   %database2_name%
                    path:     %database2_path%
                    user:     %database2_user%
                    password: %database2_password%
                    charset:  UTF8


The definition of the database variables is done in the file **parameters.yml**.

.. code-block:: yaml

    database2_driver:   pdo_pgsql
    database2_host:     localhost
    database2_port:     5432
    database2_name:     geodatabase
    database2_path:     ~
    database2_user:     postgres
    database2_password: postgres


