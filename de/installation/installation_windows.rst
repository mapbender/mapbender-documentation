.. _installation_windows_de:

Installation auf Windows
########################

Für eine schnelle Installation als Testsystem kann der MS4W-Installer (https://ms4w.com/download.html) benutzt werden. 
Nachfolgend beschreiben wir die Installation für eine Produktivumgebung.


Vorausetzungen
---------------

- PHP NTS (ab Version 5.6, maximal 7.1, https://windows.php.net/download/)
- APACHE Installation mit mod_rewrite als Dienst eingerichtet (https://www.apachelounge.com/download/)

Als Webserver kann auch nginx verwendet werden. In dieser Anleitung wird darauf nicht weiter eingegangen.


Konfiguration PHP
-----------------

Entpacken des Zip-Archives z.B. nach C:\php
Abhängig von der PHP-Version werden unter Windows PHP-Variablen für ein Temp-Verzeichnis nicht richtig gesetzt.

 * Es muss geprüft werden, ob die beiden Variablen (php.ini) gesetzt sind:

.. code-block:: ini

    sys_temp_dir
    upload_tmp_dir

* der Pfad vom PHP-bin Verzeichnis zur PATH-Variable (Windows-Umgebungsvariable) muss hinzugefügt werden
* Aktivierung der benötigten PHP-Erweiterungen in der php.ini Konfigurationsdatei

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

Download der aktuellen Mapbender Version (https://mapbender.org/builds/mapbender-starter-current.zip) und entpacken nach C:\mapbender\
    

Konfiguration Apache 
--------------------

* ein Unterordner "conf.d" muss im Verzeichnis <apache>/conf erstellt werden



In der httpd.conf am Ende einfügen:

.. code-block:: apache

                # Include directory conf.d
                Include "conf/conf.d/*.conf"

Datei **<apache>\conf\conf.d\mapbender.conf** mit dem folgenden Inhalt anlegen:

In der mapbender.conf:
  
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


Starten Sie den Apache Webserverdienst neu.


mod_fcgid
---------

Der Handler "mod_fcgid" ist für Windows Installationen mit Apache empfehlenswert, weil darüber Serveranfragen parallel ausgeführt werden können. Diese Anleitung ist ein Vorschlag des Deployments, es gibt dabei aber auch mehrere Variationen, auf die wir im Rahmen dieser Doku nicht eingehen können.

Der gängige Weg ist, PHP einfach als Modul in den Apache einzuhängen:

.. code-block:: apache

                # LoadModule php5_module "c:/bin/php/5.6.30/php5apache2_4.dll"
                # AddHandler application/x-httpd-php .php

                # configure the path to php.ini
                # PHPIniDir "c:/bin/php/5.6.30"


Diese Methode wird gegen die FCGID Methode ausgetauscht. Sie benötigt etwas Vorbereitung, da das Modul nicht automatisch bei den Apache Installationen mitgegeben wird.

* Webseite: https://httpd.apache.org/mod_fcgid/
* Download für Windows (VC 11, bitte Abhängigkeit beachten): https://www.apachelounge.com/download/VC11/ und dort die **modules-...zip** Datei.
* die mod_fcgid.so Datei aus dem Archiv muss in das module-Verzeichnis von Apache entpackt werden

In der httpd.conf:

.. code-block:: apacheconf

                # FCGI
                LoadModule fcgid_module "modules/mod_fcgid.so"
                FcgidInitialEnv PHPRC "c:/bin/php/5.6.30"
                AddHandler fcgid-script .php
                FcgidWrapper "c:/bin/php/5.6.30/php-cgi.exe" .php


In die Mapbender-Apache-Site Datei (mapbender.conf) muss der "ExecCGI" Parameter hinzugefügt werden, zum Beispiel:

.. code-block:: apacheconf

                <Directory c:/srv/mapbender-starter-3.0.6.0/web/>
                    # [...]
                    Options MultiViews FollowSymLinks ExecCGI
                    # [...]
                </Directory>


Konfiguration PostgreSQL
------------------------

Die Mapbender Konfigurationsdatei parameters.yml (app/config/parameters.yml) muss angepasst werden und die Datenbank definiert, welche erstellt werden soll. Weitere Informationen dazu befinden sich im Kapitel `Konfiguration der Datenbank <../customization/database.html>`_.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: geheim
    
Aufruf app/console Befehl über die php.exe. Hierzu muss ein Standardeingabefenster geöffnet werden.

.. code-block:: text
 
 c:
 cd mapbender
 php.exe app/console doctrine:database:create
 php.exe app/console doctrine:schema:create
 php.exe app/console assets:install web
 php.exe app/console fom:user:resetroot
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append



Der erste Start
---------------

Die Mapbender Installation kann unter **http://hostname/mapbender/** aufgerufen werden.
  
Per Voreinstellung lauten die Anmeldedaten Benutzername: "root", Passwort: "root"

Weitere Schritte unter:  `Mapbender Quickstart Dokument <../quickstart.html>`_.



Überprüfung
===========

Ob der Alias erreichbar ist:

* http://localhost/mapbender/

Das Symfony Welcome Script config.php öffnen. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 
