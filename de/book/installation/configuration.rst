.. _configuration:


Details zur Konfiguration von Mapbender3
========================================

Konfigurationsschritte
----------------------

Im Folgenden werden die für die Mapbender3-Installation aufgeführten Konfigurationsschritte von Mapbender3 näher erläutert. Es sind sechs Schritte notwendig:

* Erzeugen der Datenbank
* Erzeugen der Datenbankschemas
* Kopieren des bundle Assets in das öffentliche web-Verzeichnis
* Erzeugen des "root" Benutzers
* Laden der SRS Parameters (EPSG-Code Definition)
* Laden der Anwendungen der mapbender.yml Definition in die Datenbank

Diese Schritte werden mit dem console-Hilfsprogramm des `Symfony <http://symfony.com/>`_ Frameworks durchgeführt, auf dem Mapbender3 aufbaut. Hier noch ein wichtiger Hinweis, bevor Sie fortfahren: 

  | Das console-Hilfsprogramm wird Dateien in die Verzeichnisse app/cache und app/logs schreiben. Für diese Operationen werden die Benutzerrechte des Benutzers benötigt, mit dem Sie angemeldet sind. Sie benötigen ebenfalls Benutzerrechte für das Verzeichnis app/db und die SQLite Datenbank.  Wenn Sie die Applikation in Ihrem Browser öffnen, wird der Server-PHP- Prozess versuchen, auf  diese Dateien zuzugreifen oder in die Verzeichnisse zu schreiben mit anderen Benutzerrechten. Stellen Sie sicher,  dass Sie den Verzeichnissen und Dateien Schreib- und Leserechte zugewiesen haben. 

**Wichtiger Hinweis:** Die folgenden app/console Schritte gehen davon aus dass Sie sich oberhalb des app-Verzeichnisses befinden (für die git-Installation bedeutet das mapbender3/application/ andernfalls mapbender3/).

.. code-block:: yaml

   cd mapbender3/
   oder für die git-basierte Installation 
   cd mapbender3/application



Anpassen der Konfigurationsdatei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Parameter der Datenbankverbindung sind zusammen mit einigen anderen Konfigurationsparametern in der Datei app/config/parameters.yml gespeichert. In dieser Datei wird YAML Syntax verwendet. Achten Sie darauf **keine** Tabulatoren für Einrückungen zu verwenden. Verwenden Sie stattdessen Leerzeichen.

Ihre Datenbankkonfiguration könnte in der parameters.yml könnte folgendermaßen aussehen, wenn Sie PostgreSQL verwenden:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: geheim


    
Erzeugen der Datenbank
^^^^^^^^^^^^^^^^^^^^^^^^ 

Mit Symfony2 kann die Datenbank erzeugt werden. Beachten Sie, dass dazu die benötigten Datenbank-Benutzerrechte vorliegen. Rufen Sie folgenden Befehl mit dem console-Hilfsprogramm auf:

.. code-block:: yaml

   app/console doctrine:database:create


Erzeugen des Datenbankschemas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Erzeugen des Datenbankschemas über Symfony2:

.. code-block:: yaml

    app/console doctrine:schema:create

    
Kopieren des Bundles assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Jedes Bundle hat seine eigenen Abhängigkeiten - CSS-Dateien, JavaScript-Dateien, Bilder und mehr – diese müssen in das öffentliche web-Verzeichnis kopiert werden:

.. code-block:: yaml

    app/console assets:install web


Sie können auch einen symbolischen Link verwenden, statt die Dateien zu kopieren.  Dies erleichtert die Bearbeitung der abhängigen Dateien in den bundle-Verzeichnissen.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Erzeugen des administrativen Benutzers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Der erste Benutzer, der alle Privilegien hat, wird mit folgendem Kommando erzeugt:

.. code-block:: yaml

    app/console fom:user:resetroot

Dieses Kommando wird interaktiv alle notwendigen Informationen abfragen und den Benutzer in der Datenbank erzeugen.

Sie können auch den Modus "silent" verwenden, wenn Sie ein Skript nutzen möchten, um Mapbender3 zu installieren und dabei nicht nach Parametern gefragt werden wollen.

.. code-block:: yaml

    app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent


Einfügen den SRS Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^

Fügen Sie die Informationen zu SRS Parametern über den folgenden Aufruf in die Datenbank:

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append


Importieren von Anwendungen aus der mapbender.yml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sie können die Anwendungen, die in der mapbender.yml definiert sind, in die Datenbank importieren:

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append




Konfigurationsdateien
---------------------

Die Basiskonfiguration erfolgt in der Datei **app/config/parameters.yml**. Eine Vorlage app/config/parameters.yml.dist liegt vor. 

Die Konfigurationsdatei **app/config/config.yml** stellt weitere Parameter bereit, z.B. zur Konfiguration der Portalfunktion, Einrichtung des Owsproxy oder Einrichtung einer weiteren Datenbank.


parameters.yml
^^^^^^^^^^^^^^

* Datenbank: Parameter, die mit **database** beginnen, definieren die Databankverbindung. 
* Mailer: Die Mailerangaben starten mit **mailer**. Nutzen Sie z.B. smtp oder sendmail. 
* Spracheinstellung: Sie können eine Sprache (locale) für Ihre Anwendung angeben (Standardwert ist en, de ist verfügbar). Unter http://doc.mapbender3.org/en/book/translation.html erfahren Sie mehr über die Anpassung von Übersetzungen und wie neue Sprachen hinzugefügt werden können.

**Hinweis:** Sie benötigen einen Mailer, wenn Sie die Selbstregistrierung und das Paßwortsetzen nutzen möchten.


config.yml
^^^^^^^^^^

* fom_user.selfregistration: Um die Selbstregistrierung zu de/aktivieren, passen Sie den fom_user.selfregistration Parameter an. Sie müssen unter self_registration_groups eine/mehrere Gruppen angeeben, so dass selbstregistriere Anwender automatisch (bei der Registrierung) diesen Gruppen zugewiesen werden. Über die Gruppe bekommen Sie dann entsprechend Rechte zugewiesen.
* fom_user.reset_password: Über diesen Parameter kann die Möglichkeit de/aktiviert werden, das Passwort neu zu setzen.
* framework.session.cookie_httponly: Stellen Sie für HTTP-only session cookies sicher, dass der Parameter framework.session.cookie_httponly auf true steht.

**Hinweis:** Sie benötigen einen Mailer, wenn Sie die Selbstregistrierung und das Paßwortsetzen nutzen möchten.

Sofern Sie einen Proxy verwenden, müssen Sie diesen in der Datei config.yml im Bereich *ows_proxy3_core* angeben.

Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml

    ows_proxy3_core:
        logging: true
        obfuscate_client_ip: true
        proxy:
            host: myproxy
            port: 8080
            connecttimeout: 60
            timeout: 90
            noproxy:
                - 192.168.1.123



mapbender.yml
^^^^^^^^^^^^^

Eine Anwendung kann auf zwei Arten konfiguriert werden. Entweder über die mapbender.yml Datei oder über die Mapbender3 Administration im Browser.

* Das Mapbender Team stellt mit jeder Version eine mapbender.yml mit Demoanwendungen mit den aktuellen Elementdefinitionen zur Verfügung (Sie können die Anwendungen deaktivieren indem Sie published: false setzen oder indem Sie die Datei leeren).
* Anwendungen, die in der mapbender.yml definiert werden, können nicht über die Mapbender3 Administration im Browser bearbeitet werden.
* Sie können allerdings die Anwendungen über einen app/console Befehl in die Datenbank übertragen.

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append
