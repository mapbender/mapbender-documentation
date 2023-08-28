.. _installation_windows_de:

Installation unter Windows
##########################

Für eine schnelle Installation als Testsystem kann der MS4W-Installer (https://ms4w.com/download.html) benutzt werden. 

Nachfolgend beschreiben wir die Installation für eine Produktivumgebung.

Mapbender benötigt eine Datenbank zur Speicherung der Administrationsinformation. Das Installationspaket enthält bereits eine SQLite Datenbank, die direkt verwendet werden kann. Für den produktiven Einsatz wird allerdings die Nutzung einer PostgreSQL Datenbank empfohlen.


Voraussetzungen
---------------

* PHP NTS >= 7.4 https://windows.php.net/download/)
* Apache Installation, als Dienst eingerichtet (https://www.apachelounge.com/download/)   
  mit folgenden aktivierten Modulen:
 
  * mod_rewrite
  * mod_fcgid
 
* PostgreSQL Installation (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 
  
  * Es wird empfohlen eine PostgreSQL Datenbank für Mapbender zu verwenden.
  * Es wird empfohlen einen eigenen Datenbankbenutzer für den Zugriff auf die Mapbender Datenbank anzulegen.


Als Webserver kann auch Nginx verwendet werden. In dieser Anleitung wird darauf nicht weiter eingegangen.


Konfiguration PHP
-----------------

* Entpacken des Zip-Archives, z.B. nach c:\\php
* Abhängig von der PHP-Version werden unter Windows PHP-Variablen für ein Temp-Verzeichnis nicht richtig gesetzt.

* Es muss deshalb geprüft werden, ob die folgenden Variablen (php.ini) gesetzt sind:

.. code-block:: ini

    sys_temp_dir
    upload_tmp_dir
    date.timezone

* der Pfad vom PHP-bin Verzeichnis zur PATH-Variable (Windows-Umgebungsvariable) muss hinzugefügt werden

* Aktivieren Sie die benötigten PHP-Erweiterungen in der php.ini Konfigurationsdatei:

.. code-block:: ini

    # php.ini
    extension=php_curl
    extension=php_fileinfo
    extension=php_gd
    extension=php_intl
    extension=php_pdo_pgsql
    extension=php_pdo_sqlite
    extension=php_pgsql
    extension=php_openssl
    extension=php_mbstring
    extension=php_zip
    extension=php_bz2

* Bitte prüfen Sie die :ref:`faq_de` für weitere PHP-Einstellungen. 


Mapbender entpacken und im Webserver registrieren
-------------------------------------------------

Download der aktuellen Mapbender Version (https://mapbender.org/builds/mapbender-starter-current.zip) und entpacken nach c:\\mapbender\\
    

Konfiguration Apache
--------------------

* ein Unterordner "conf.d" muss im Verzeichnis <apache>/conf erstellt werden



In der httpd.conf am Ende einfügen:

.. code-block:: apache

                # Include directory conf.d
                Include "conf/conf.d/*.conf"

Datei **<apache>\\conf\\conf.d\\mapbender.conf** mit dem folgenden Inhalt anlegen:
  
.. code-block:: apache

 Alias /mapbender c:/mapbender/web/
 <Directory c:/mapbender/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>


Der Apache Webserverdienst muss im Anschluss neu gestartet werden.


mod_fcgid
---------

Datei **<apache>\\conf\\conf.d\\fcgi.conf** mit dem folgenden Inhalt anlegen:

.. code-block:: apacheconf

    LoadModule fcgid_module modules/mod_fcgid.so
    
    FcgidInitialEnv PHPRC "c:/php/"
    FcgidInitialEnv PATH "c:/php;C:/WINDOWS/system32;C:/WINDOWS;C:/WINDOWS/System32/Wbem"
    FcgidInitialEnv SystemRoot "C:/Windows"
    FcgidInitialEnv TEMP "C:/WINDOWS/TEMP"
    FcgidInitialEnv TMP "C:/WINDOWS/TEMP"
    FcgidInitialEnv windir "C:/WINDOWS"

    FcgidPassHeader Authorization
    FcgidIOTimeout 1200
    FcgidConnectTimeout 1200
    FcgidBusyScanInterval 1200
    FcgidBusyTimeout 1200
    FcgidErrorScanInterval 1200
    FcgidIdleScanInterval 1200
    FcgidIdleTimeout 1200
    FcgidZombieScanInterval 1200
    FcgidMaxProcesses 1000
    FcgidOutputBufferSize 64
    FcgidProcessLifeTime 3600
    FcgidMaxRequestsPerProcess 10000
    FcgidMinProcessesPerClass 0
    FcgidFixPathinfo 0
    MaxRequestLen 200000

    <Files ~ "\.php$">
        Options Indexes FollowSymLinks ExecCGI
        AddHandler fcgid-script .php
        FcgidWrapper "c:/php/php-cgi.exe" .php
    </Files>


Konfiguration PostgreSQL
------------------------

Konfiguration der Datenbankverbindung erfolgt in der Datei app/config/parameters.yml.

Weitere Informationen im Kapitel :ref:`yaml_de`.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: geheim
    
Die Eingabeaufforderung öffnen. Zur Initialisierung der Datenbank folgende Befehle eingeben: 

.. code-block:: text
 
    cd c:\mapbender
    php.exe app/console doctrine:database:create
    php.exe app/console doctrine:schema:create
    php.exe app/console mapbender:database:init -v
    php.exe bin/composer run reimport-example-apps

Für die Administration von Mapbedner wird ein Root-Benutzer benötigt. Dieser Benutzer wird über den folgende Befehl angelegt:

.. code-block:: text

    php.exe app/console fom:user:resetroot

Weitere Informationen zur Konfiguration im Kapitel :ref:`installation_configuration_de`


Der erste Start
---------------

Die Mapbender Installation kann unter **http://[hostname]/mapbender/** aufgerufen werden.


**Überprüfung**

Überprüfen Sie, ob der Alias erreichbar ist:

* http://localhost/mapbender/

Per Voreinstellung lauten die Anmeldedaten (wenn die SQLite Datenbank verwendet wurde)

Benutzername: "root", Passwort: "root"

Zur Überprüfung der Konfiguration dient der folgende Befehl:

.. code-block:: yaml

	php.exe app/console mapbender:config:check

.. hint:: Bitte beachten Sie, dass der Befehl mapbender:config:check die PHP-CLI Version nutzt. Die Einstellungen der CLI-Version können sich von denen der Webserver PHP-Version unterscheiden. Nutzen Sie beispielsweise php -r 'phpinfo();' zur Ausgabe der PHP-Webserver Einstellungen.

Weitere Informationen dazu finden Sie unter :ref:`mapbender_config_check_de`.

Glückwunsch! Mapbender wurde erfolgreich installiert.
Informationen zu den ersten Schritten mit Mapbender finden sich im :ref:`Mapbender Schnellstart <quickstart_de>`.
