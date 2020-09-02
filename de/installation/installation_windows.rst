.. _installation_windows_de:

Installation auf Windows
########################

Für eine schnelle Installation als Testsystem kann der MS4W-Installer (https://ms4w.com/download.html) benutzt werden. 
Nachfolgend beschreiben wir die Installation für eine Produktivumgebung.


Voraussetzungen
---------------

* PHP NTS (ab Version 5.6, maximal 7.2, https://windows.php.net/download/)
* Apache Installation, als Dienst eingerichtet (https://www.apachelounge.com/download/)   
  mit folgenden aktivierten Modulen:
 
  * mod_rewrite
  * mod_fcgid
 
* eingerichtete PostgreSQL Datenbank (Version < 10, https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 
  
  * vorhandene Datenbank für die Mapbender Konfiguration
  * ggf. eigenen Benutzer für Zugriff


Als Webserver kann auch nginx verwendet werden. In dieser Anleitung wird darauf nicht weiter eingegangen.


Konfiguration PHP
-----------------

* Entpacken des Zip-Archives, z.B. nach c:\php
* Abhängig von der PHP-Version werden unter Windows PHP-Variablen für ein Temp-Verzeichnis nicht richtig gesetzt.

* Es muss deshalb geprüft werden, ob die folgenden Variablen (php.ini) gesetzt sind:

.. code-block:: ini

    sys_temp_dir
    upload_tmp_dir
    date.timezone

* der Pfad vom PHP-bin Verzeichnis zur PATH-Variable (Windows-Umgebungsvariable) muss hinzugefügt werden

* Aktivierung der benötigten PHP-Erweiterungen in der php.ini Konfigurationsdatei:

.. code-block:: ini

    # php.ini
    extension=php_curl.dll
    extension=php_fileinfo.dll
    extension=php_gd2.dll
    extension=php_intl.dll
    extension=php_pdo_pgsql.dll
    extension=php_pdo_sqlite.dll
    extension=php_pgsql.dll
    extension=php_openssl.dll
    extension=php_mbstring.dll
    extension=php_zip.dll
    extension=php_bz2.dll
    
    
Entpacken und im Webserver registrieren
---------------------------------------

Download der aktuellen Mapbender Version (https://mapbender.org/builds/mapbender-starter-current.zip) und entpacken nach c:\mapbender\
    

Konfiguration Apache 
--------------------

* ein Unterordner "conf.d" muss im Verzeichnis <apache>/conf erstellt werden



In der httpd.conf am Ende einfügen:

.. code-block:: apache

                # Include directory conf.d
                Include "conf/conf.d/*.conf"

Datei **<apache>\conf\conf.d\mapbender.conf** mit dem folgenden Inhalt anlegen:
  
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

Datei **<apache>\conf\conf.d\fcgi.conf** mit dem folgenden Inhalt anlegen:

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

Konfiguration der Datenbankverbindung in (app/config/parameters.yml).
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
    php.exe app/console assets:install web
    php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
    php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Weitere Informationen zur Konfiguration: :ref:`installation_configuration_de`


Der erste Start
---------------

Die Mapbender Installation kann unter **http://hostname/mapbender/** aufgerufen werden.
  
Per Voreinstellung lauten die Anmeldedaten:

Benutzername: "root", Passwort: "root"

Weitere Schritte unter:  `Mapbender Quickstart Dokument <../quickstart.html>`_.



**Überprüfung**

Überprüfen Sie, ob der Alias erreichbar ist:

* http://localhost/mapbender/

Überprüfen Sie in der Konfiguration, ob bestimmte Abhängigkeiten nicht erfüllt werden mit:


.. code-block:: text

    app/console mapbender:config:check
    
     
Weitere Informationen dazu finden Sie unter: https://doc.mapbender.org/de/customization/commands.html#app-console-mapbender-config-check
    




