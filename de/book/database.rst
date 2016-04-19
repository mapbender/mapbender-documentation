Konfiguration der Datenbank
############################

Allgemein
*********

Zur Konfiguration der Datenbankverbindung werden die Dateien config.yml und parameters.yml verwendet (siehe auch `die Symfony Dokumentation <http://symfony.com/doc/current/best_practices/configuration.html>`_). Während in der config.yml nur die Platzhalter angegeben werden, werden die Werte in der parameters.yml gefüllt.

Beispiele zur Einrichtung finden sich in den `Installationsanleitungen <installation.html>`_, so z.B. im Kapitel `Einrichtung von Mapbender3 unter Ubuntu oder Debian <installation/installation_ubuntu.html#mapbender3-einrichtung>`_.


.. _doctrine:

Doctrine
*************

Mapbender3 verwendet Doctrine. Doctrine ist eine Sammlung von PHP Bibliotheken und bietet einen objektrelationalen Mapper und eine Datenbankabstraktionsschicht. 
Auf der `Doctrine Projektseite <http://www.doctrine-project.org/>`_ finden sich weitere Informationen.


Datenbank Definition
********************

Die Standarddatenbankdefinition erfolgt in der config.yml und sieht folgendermaßen aus:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # Datenbankverbindung default
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
        orm:
            auto_generate_proxy_classes: %kernel_debug%
            auto_mapping:true

Bei Werten, die von dem %-Zeichen umschlossen werden, handelt es sich um Variablen. Diese Variablen werden aus der parameters.yml geladen. Um die Verbindung zur Datenbank zu ändern, müssen daher die Werte der Variablen in der parameters.yml verändert werden.

Der Parameter "default_connection" gibt die Datenbankverbindung an, die standardmäßig von Mapbender3 verwendet werden soll (``default_connection: default``).

* database_driver: Der Datenbanktreiber. Mögliche Werte sind:

  * pdo_sqlite - SQLite PDO driver
  * pdo_mysql - MySQL PDO driver
  * pdo_pgsql - PostgreSQL PDO driver
  * oci8 - Oracle OCI8 driver
  * pdo_oci - Oracle PDO driver

 Beachten Sie, dass Sie den entsprechenden PHP-Treiber installiert bzw. aktiviert haben.

* database_host: Der Host, auf dem die Datenbank läuft. Entweder der Name (z.B. localhost) oder die IP-Adresse (z.B. 127.0.0.1).
* database_port: Der Port, auf dem die Datenbank lauscht (z.B. 5432 für PostgreSQL).
* database_name: Der Name der Datenbank (z.B. mapbender3). Erstellen Sie die Datenbank mit dem Befehl ``doctrine:database:create`` bzw. ``doctrine:schema:create``. Siehe die `Installationsanleitung <installation.html>`_ für Details.
* database_path: Der %database_path% ist der Pfad zur Datei der SQLite-Datenbank. Wenn Sie keine SQLite-Datenbank verwenden, löschen Sie bitte den Parameter trotzdem nicht aus der parameters.yml, sondern schreiben Sie als Wert entweder eine Tilde (~) oder ``null``.
* database_user: Benutzername für die Verbindung zur Datenbank.
* database_password: Das Passwort des Datenbankbenutzers.
* charset: Die Kodierung, die die Datenbank verwendet.
* logging:  Die Option sorgt dafür, das alle SQLs nicht mehr geloggt werden (Standardwert: %kernel.debug%). `Mehr Informationen <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
* profiling: Profiling von SQL Anfragen. Diese Option kann in der Produktion ausgeschaltet werden. (Standardwert: %kernel.debug%)


Verwendung mehrerer Datenbanken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit Mapbender3 können Sie auch mehrere Datenbanken verwenden. Dies wird empfohlen, wenn Sie Ihre eigenen Daten von den Mapbender3-Daten trennen möchten. Das kann nützlich sein, wenn Sie eigenen Code verwenden, der nicht zu einem Mapbender3-Bundle gehört. EIne zweite Datenbank benötigen Sie ebenfalls für die Geodatensuche (über den SearchRouter) und die Datenerfassung (Digitizer). Die Geodaten sollten grundsätzlich in einer anderen DAtenbank vorgehalten werden und nicht in der Mapbender3 Datenbank.

Die Standard-Datenbankverbindung (``default_connection: default``) wird von Mapbender3 verwendet.

Wenn Sie eine weitere Datenbank verwenden möchten, müssen Sie eine zweite Datenbankverbindung mit einem anderen Namen definieren.

Es folgt ein Beispiel mit zwei Datenbankverbindungen in der **config.yml**:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # Datenbankverbindung default
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
                # Datenbankverbindung search_db
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


Die Definition der Datenbank Variablen (Angabe der Zugangsinformationen) wird in der **parameters.yml** Datei vorgenommen.

.. code-block:: yaml
                
    parameters:
        # Datenbankverbindung "default"
        database_driver:   pdo_pgsql
        database_host:     localhost
        database_port:     5432
        database_name:     mapbender3
        database_path:     ~
        database_user:     postgres
        database_password: postgres

        # Datenbankverbindung "search_db"
        database2_driver:   pdo_pgsql
        database2_host:     localhost
        database2_port:     5432
        database2_name:     search_db
        database2_path:     ~
        database2_user:     postgres
        database2_password: postgres

In den Elementen SearchRouter und Digitizer kann nun auf die Datenbankverbindung (connection) mit dem Namen **search_db** verwiesen werden.
