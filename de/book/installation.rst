.. _installation:

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
* PHP GD (php5-gd) für den Druck
* PHP FileInfo für den Druck zur Prüfung der Bilder


Um optional eine andere Datenbank als die vorkonfigurierte SQLite zu verwenden, wird eine PHP-Erweiterung benötigt, die von Doctrine unterstützt wird:
`Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. 

Beachten Sie, dass die SQLite Erweiterung auf jeden Fall benötigt wird. Sie benötigen diese, um im Entwicklermodus zu arbeiten, um den Web Installer zu verwenden oder um Profiler-Daten zu erzeugen sowie um Fehler zu analysieren.


Download 
********** 

Installationspakete werden als komprimierte Pakete ausgegeben und sind auf der Download-Seite verfügbar unter http://mapbender3.org/download.

Nach dem Herunterladen extrahieren Sie die komprimierten Pakete in ein Verzeichnis Ihrer Wahl. Stellen Sie sicher, dass der Webserver auf das gerade dekomprimierte Webverzeichnis in dem Mapbender Verzeichnis zeigt. Sorgen Sie dafür, dass *app.php* als Verzeichnis-Index eingestellt ist.

Beispiel für eine Apache ALIAS Konfiguration in der Datei /etc/apache2/conf.d/mapbender3 (bitte beachten Sie, dass Apache 2.4 `andere Direktiven zur Access Control verwendet <http://httpd.apache.org/docs/2.4/upgrading.html>`_)

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
******************** 



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
* Laden der Anwendungen der mapbender.yml Definition in die Datenbank

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

.. code-block:: yaml

   app/console doctrine:database:create


Erzeugen des Datenbankschemas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Erzeugen des Datenbankschemas über Symfony2:

.. code-block:: yaml

    app/console doctrine:schema:create

Sie müssen die Tabellen des Sicherheitssystems separat initialisieren:

.. code-block:: yaml

  app/console init:acl

Kopieren des bundles' assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Jedes Bundle hat seine eigenen Abhängigkeiten - CSS-Dateien, JavaScript-Dateien, Bilder und mehr – diese müssen in das öffentliche web-Verzeichnis kopiert werden:

.. code-block:: yaml

    app/console assets:install web


Sie können auch einen symbolischen Link verwenden, statt die Dateien zu kopieren.  Dies erleichtert die Bearbeitung der abhängigen Dateien in den bundle-Verzeichnissen.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Erzeugen des administrativen Benutzers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Der erste Benutzer, der alle Privilegien hat, wird mit folgendem Kommando erzeugt:

.. code-block:: yaml

    app/console fom:user:resetroot

Dieses Kommando wird interaktiv alle notwendigen Informationen abfragen und den Benutzer in der Datenbank erzeugen.

Sie können auch den Modus silent verwenden, wenn Sie ein Skript nutzen möchten, um Mapbender3 zu installieren und dabei nicht nach Parametern gefragt werden wollen.

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


Prüfen Sie die Schreibberechtigungen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Weisen Sie die Dateien dem Apache Benutzer (www-data) zu.

.. code-block:: yaml

 chmod -R ugo+r /var/www/mapbender3
 chown -R www-data:www-data /var/www/mapbender3


Sie benötigen Schreibrechte für die Verzeichnisse app/cache und app/logs.

.. code-block:: yaml

 chmod -R ug+w /var/www/mapbender3/app/cache
 chmod -R ug+w /var/www/mapbender3/app/logs
 chmod -R ug+w /var/www/mapbender3/web/assets


Prüfen Sie Symfony config.php
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* http://localhost/mapbender3/config.php

Sie können Mapbender3 nun nutzen. Starten Sie Mapbender3 im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen.

* http://localhost/mapbender3/app_dev.php

**Notice:** Klicken Sie auf den Loginlink oben rechts, um zur Abmedlung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an. 

Wenn Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das :doc:`Mapbender3 Quickstart Dokument <quickstart>` an.



Installationsbeispiel für Ubuntu
**************************************** 

Installieren Sie die notwendigen Komponenten:

.. code-block:: yaml

  apt-get install php5 php5-pgsql php5-gd php5-curl php5-cli php5-sqlite sqlite php-apc php5-intl curl


Erstellen Sie den Apache ALIAS. Legen Sie die Datei /etc/apache2/conf.d/mapbender3 mit dem folgenden Inhalt an und starten Sie den Apache Server neu. Apache 2.4 benutzt andere Direktiven für die Access Control (zum Beispiel: "Require all granted"). Für Details schauen Sie bitte in die `Apache Documentation: Upgrading to 2.4 from 2.2 <http://httpd.apache.org/docs/2.4/upgrading.html>`_.

.. code-block:: yaml

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

Prüfen Sie, ob der ALIAS erreichbar ist:

* http://localhost/mapbender3/

Öffnen Sie das Symfony Welcome Script config.php. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender3/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 

Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.

.. code-block:: yaml

 chmod -R ugo+r /var/www/mapbender3
 chown -R www-data:www-data /var/www/mapbender3

Passen Sie die Mapbender3 Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen möchten.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: 1xyz45ab
 
Setzen Sie die app/console Befehle ab

.. code-block:: yaml

 cd /var/www/mapbender3
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console init:acl
 app/console assets:install web
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Hiermit ist die Installation von Mapbender3 fertig. 

Prüfen Sie die config.php erneut 

* http://localhost/mapbender3/config.php

Sie müssen Schreibrechte für die Verzeichnisse app/cache und app/logs sowie web/assets vergeben.

.. code-block:: yaml

 chmod -R ug+w /var/www/mapbender3/app/cache
 chmod -R ug+w /var/www/mapbender3/app/logs
 chmod -R ug+w /var/www/mapbender3/web/assets


Sie können Mapbender3 nun nutzen. Starten Sie Mapbender3 im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen.

* http://localhost/mapbender3/app_dev.php

**Hinweis:** Klicken Sie auf den Login-Link oben rechts, um zur Abmeldung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an. 

Wenn Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das :doc:`Mapbender3 Quickstart Dokument <quickstart>` an.


Installationsbeispiel für Windows
**************************************** 

Installieren Sie die notwendigen Komponenten:

 * fügen Sie den Pfad zum PHP-bin Verzeichnis zu Ihrer PATH Variable hinzu 
 * aktivieren Sie die PHP Erweiterunge in der php.ini Konfigurationsdatei

.. code-block:: yaml

 extension=php_curl.dll
 extension=php_gd2.dll
 extension=php_intl.dll
 extension=php_pdo_pgsql.dll
 extension=php_pdo_sqlite.dll
 extension=php_pgsql.dll

Erstellen Sie den Apache ALIAS. Legen Sie die Datei /etc/apache2/conf.d/mapbender3 mit dem folgenden Inhalt an und starten Sie den Apache Server neu (bitte beachten Sie, dass Apache 2.4 `andere Direktiven zur Access Control verwendet <http://httpd.apache.org/docs/2.4/upgrading.html>`_)

.. code-block:: yaml

  ALIAS /mapbender3 c:/mapbender3/web/
  <Directory c:/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>

Prüfen Sie, ob der ALIAS erreichbar ist:

* http://localhost/mapbender3/

Öffnen Sie das Symfony Welcome Script config.php. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender3/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 

Passen Sie die Mapbender3 Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen möchten.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:
    database_user:     postgres
    database_password: 1xyz45ab

Rufen Sie die app/console Befehle über die php.exe auf.

.. code-block:: yaml
 
 c:
 cd mapbender3
 php.exe app/console doctrine:database:create
 php.exe app/console doctrine:schema:create
 php.exe app/console init:acl
 php.exe app/console assets:install web
 php.exe app/console fom:user:resetroot
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append


Hiermit ist die Installation von Mapbender3 fertig. 

Prüfen Sie die config.php erneut 

* http://localhost/mapbender3/config.php


Sie können Mapbender3 nun nutzen. Starten Sie Mapbender3 im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen.

* http://localhost/mapbender3/app_dev.php

**Hinweis:** Klicken Sie auf den Login-Link oben rechts, um zur Abmeldung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an. 

Wenn Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das :doc:`Mapbender3 Quickstart Dokument <quickstart>` an.


Konfigurationsdateien
********************** 

Die Basiskonfiguration erfolgt in der Datei **app/config/parameters.yml**. Eine Vorlage app/config/parameters.yml.dist liegt vor. 

Die Konfigurationsdatei **app/config/config.yml** stellt weitere Parameter bereit, z.B. zur Konfiguration der Portalfunktion, Einrichtung des Owsproxy oder Einrichtung einer weiteren Datenbank.


parameters.yml
------------------

* Datenbank: Parameter, die mit **database** beginnen, definieren die Databankverbindung. 
* Mailer: Die Mailerangaben starten mit **mailer**. Nutzen Sie z.B. smtp oder sendmail. 
* Spracheinstellung: Sie können eine Sprache (locale) für Ihre Anwendung angeben (Standardwert ist en, de ist verfügbar). Unter http://doc.mapbender3.org/en/book/translation.html erfahren Sie mehr über die Anpassung von Übersetzungen und wie neue Sprachen hinzugefügt werden können.

**Hinweis:** Sie benötigen einen Mailer, wenn Sie die Selbstregistrierung und das Paßwortsetzen nutzen möchten.


config.yml
-----------

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
------------------
Eine Anwendung kann auf zwei Arten konfiguriert werden. Entweder über die mapbender.yml Datei oder über die Mapbender3 Administration im Browser.

* Das Mapbender Team stellt mit jeder Version eine aktuelle mapbender.yml mit den Elementdefinitionen zur Verfügung.
* Anwendungen, die in der mapbender.yml definiert werden, können nicht über die Mapbender3 Administration im Browser bearbeitet werden.
* Sie können allerdings die Anwendungen über einen app/console Befehl in die Datenbank übertragen.

.. code-block:: yaml

    app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append


Aktualisierung von Mapbender3 auf eine neuere Version
********************************************************** 

Um Mapbender3 zu aktualisieren, müssen Sie die folgenden Schritte durchführen:

* Laden Sie die neuste Version von http://mapbender3.org/builds/ herunter. Aktuelle Snapshots finden Sie unter http://mapbender3.org/builds/nightly/
* Sichern Sie Ihre Konfigurationsdateien und ihre alte Mapbender Version
* Ersetzen Sie die Dateien durch die neuen Mapbender Skripte
* Vergleichen Sie die Konfigurationsdateien und prüfen diese auf neue Parameter.
* Aktualisieren Sie Ihre Mapbender Datenbank
* Das war's auch schon! Schauen Sie sich Ihre neue Mapbender3 Version an.


Aktualisierungsbeispiel für Linux
------------------------------------
Im Folgenden sind die einzelnen Schritte als Befehle aufgeführt.

.. code-block:: yaml

 # Laden Sie die neue Version herunter
 wget -O http://mapbender3.org/builds/mapbender3-3.0.1.tar.gz /tmp/build_mapbender3/
 tar xfz /tmp/build_mapbender3/mapbender3-3.0.tar.gz
 
 # Sichern Sie die alte Version
 mv -R /var/www/mapbender3 /var/www/mapbender3_save
 
 # Aktivieren Sie den Code der neuen Version
 cp -R /tmp/build_mapbender3/mapbender3-3.0.1 /var/www/
 mv /var/www/mapbender3-3.0.1 /var/www/mapbender3
 
 # copy your old configuration files to the new version
 cp /var/www/mapbender3_save/app/config/parameters.yml /var/www/mapbender3/app/config/parameters.yml
 cp /var/www/mapbender3/app/config/parameters.yml /var/www/mapbender3/app/config/config.yml-dist
 cp /var/www/mapbender3_save/app/config/config.yml /var/www/mapbender3/app/config/config.yml 
 
 # händisch müssen Sie nun die Konfigirationsdateien auf neue Parameter überprüfen
 # vergleichen Sie die Dateien parameters.yml, config.yml und sofern verwendet die mapbender.yml
 
 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 chmod -R uga+r /var/www/mapbender3
 chown -R www-data:www-data /var/www/mapbender3


Aktualisieren Sie Ihre Mapbender Datenbank

.. code-block:: yaml

 cd /var/www/mapbender3/
 app/console doctrine:schema:update --dump-sql
 app/console doctrine:schema:update --force
 app/console assets:install web
 
 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 chmod -R ugo+r /var/www/mapbender3
 chown -R www-data:www-data /var/www/mapbender3

 # Sie benötigen Schreibrechte für die Verzeichnisse app/cache und app/logs.
 chmod -R ug+w /var/www/mapbender3/app/cache
 chmod -R ug+w /var/www/mapbender3/app/logs
 chmod -R ug+w /var/www/mapbender3/web/assets

