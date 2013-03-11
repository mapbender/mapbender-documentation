Installation 
############ 

Dieses Dokument beschreibt die wichtigsten Schritte, um Mapbender3 zu installieren. 


Voraussetzungen
***************

Mapbender3 benötigt die folgenden Komponenten:

* >= PHP 5.3.10 (php5) 
* PHP CLI Interpreter (php5-cli) 
* PHP SQLite Erweiterung (php5-sqlite) 
* PHP cURL Erweiterung (php5-curl) 
* PHP Alternative PHP Cache (php-apc)
* PHP Internationalisierungserweiterung (php5-intl)


Um optional eine andere Datenbank als die vorkonfigurierte SQLite zu verwenden, wird eine PHP-Erweiterung benötigt, die von Doctrine unterstützt wird:
`Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. 

Beachten Sie, dass die SQLite Erweiterung auf jeden Fall benötigt wird. Sie benötigen diese, um im Entwicklermodus zu arbeiten, um den Web Installer zu verwenden oder um Profiler-Daten zu erzeugen sowie um Fehler zu analysieren.


Download 
********** 

Installationspakete werden als komprimierte Pakete ausgegeben und sind auf der Download-Seite verfügbar unter http://mapbender3.org/download.

Nach dem Herunterladen extrahieren Sie die komprimierten Pakete in ein Verzeichnis Ihrer Wahl. Stellen Sie sicher, dass der Webserver auf das gerade dekomprimierte Webverzeichnis in dem Mapbender Verzeichnis zeigt. Sorgen Sie dafür, dass *app.php* als Verzeichnis-Index eingestellt ist.

Beispiel für eine Apache ALIAS Konfiguration in der Datei /etc/apache2/conf.d/mapbender3

.. code-block:: yaml

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

Eine :doc:`Git-basierte <installation_git>`-Installation - vorwiegend für Entwickler - ist ebenso möglich.


Konfiguration
============= 



Verwendung des Web-Installer
---------------------------------------

Die Konfiguration direkt über den Browser ist bisher nicht verfügbar. Bitte benutzen Sie derzeit die kommandozeilenbasierte Methode.



Verwendung der  Kommandozeile
----------------------------------------

Um die Mapbender3-Installation zu konfigurieren, sind die folgenden Schritte notwendig:

* Erzeugen der Datenbank
* Erzeugen der Datenbankschemas
* Kopieren des bundle Assets in das öffentliche web-Verzeichnis
* Initialisieren der Rollen
* Erzeugen des "root" Benutzers
* Laden der SRS Parameters (EPSG-Code Definition)

Diese Schritte können mit dem console-Hilfsprogramm von Symfonie2 durchgeführt werden, auf dem das Mapbender3 Framework aufbaut. Hier noch ein wichtiger Hinweis, bevor Sie fortfahren: 


  | Das console-Hilfsprogramm wird Dateien in die Verzeichnisse app/cache und app/logs schreiben. 
  | Für diese Operationen werden die Benutzerrechte des Benutzers benötigt, mit dem Sie 
  | angemeldet sind. Sie benötigen ebenfalls Benutzerrechte für das Verzeichnis app/db und die
  | SQLite Datenbank.  Wenn Sie die Applikation in Ihrem Browser öffnen, wird der Server-PHP-
  | Prozess versuchen, auf  diese Dateien zuzugreifen oder in die Verzeichnisse zu schreiben mit
  |  anderen Benutzerrechten. Stellen Sie sicher,  dass Sie den Verzeichnissen und Dateien Schreib-
  |  und Leserechte zugewiesen haben. 


Anpassen der Konfigurationsdatei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
Die Parameter der Datenbankverbindung sind zusammen mit einigen anderen Konfigurationsparametern in der Datei app/config/parameters.yml gespeichert. In dieser Datei  wird YAML Syntax verwendet. Achten Sie darauf **keine** Tabulatoren für Einrückungen zu verwenden. Verwenden Sie stattdessen Leerzeichen.

Ihre Datenbankkonfiguration könnte in der parameters.yml könnte folgendermaßen aussehen, wenn Sie PostgreSQL verwenden:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: 1xyz45ab

Erzeugen der Datenbank
^^^^^^^^^^^^^^^^^^^^^^^^ 

Mit Symfony2 kann die Datenbank erzeugt werden. Beachten Sie, dass dazu die benötigten Datenbank-Benutzerrechte vorliegen. Rufen Sie folgenden Befehl mit dem console-Hilfsprogramm auf:

    :command:`app/console doctrine:database:create` 


Erzeugen des Datenbankschemas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Erzeugen des Datenbankschemas über Symfony2:

    :command:`app/console doctrine:schema:create` 

Sie müssen die Tabellen des Sicherheitssystems separat initialisieren:

.. code-block:: yaml

  app/console init:acl


Kopieren des bundles' assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Jedes Bundle hat seine eigenen Abhängigkeiten - CSS-Dateien, JavaScript-Dateien, Bilder und mehr – diese müssen in das öffentliche web-Verzeichnis kopiert werden:

.. code-block:: yaml

    :command:`app/console assets:install web` 


Sie können auch einen symbolischen Link verwenden, statt die Dateien zu kopieren.  Dies erleichtert die Bearbeitung der abhängigen Dateien in den bundle-Verzeichnissen.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Erzeugen des administrativen Benutzers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Der erste Benutzer, der alle Privilegien hat, wird mit folgendem Kommando erzeugt:

    :command:`app/console fom:user:resetroot` 


Dieses Kommando wird interaktiv alle notwendigen Informationen abfragen und den Benutzer in der Datenbank erzeugen.

Sie können auch den Modus silent verwenden, wenn Sie ein Skript nutzen möchten, um Mapbender3 zu installieren und dabei nicht nach Parametern gefragt werden wollen.

.. code-block:: yaml

    app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent


Einfügen den SRS Parameter
^^^^^^^^^^^^^^^^^^^^^^^^

Fügen Sie die Informationen zu SRS Parametern über den folgenden Aufruf in die Datenbank:

.. code-block:: yaml

    app/console doctrine:fixtures:load  --append


Prüfen Sie die config.php und Schreibberechtigungen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* http://localhost/mapbender3/config.php

Sie benötigen Schreibrechte für die Verzeichnisse app/cache und app/logs.

.. code-block:: yaml

 chmod -R o+w /var/www/mapbender3/app/cache
 chmod -R o+w /var/www/mapbender3/app/logs


Sie können nun Mapbender3 nutzen. Starten Sie Mapbender3 im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen.

* http://localhost/mapbender3/app_dev.php

**Hinweis:** Klicken Sie auf das Mapbender3-Logo, um zur Anmeldung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an. 

Wen Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das :doc:`Mapbender3 Quickstart Dokument <quickstart>` an.

