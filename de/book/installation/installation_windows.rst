.. _installation_windows:

Installation auf Windows
########################

Beachten Sie die `Systemvoraussetzungen <systemrequirements.html>`_ wo Sie auch die Download-Links für Mapbender3 finden. Installieren Sie die notwendigen Komponenten:

* fügen Sie den Pfad zum PHP-bin Verzeichnis zu Ihrer PATH Variable hinzu 
* aktivieren Sie die PHP Erweiterungen in der php.ini Konfigurationsdatei
* laden Sie das Apache Modul rewrite

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


Zusätzlich für PHP 7:

.. code-block:: ini

 # php.ini
 extension=php_zip.dll
 extension=php_bz2.dll
 extension=php_mbstring.dll
  

.. code-block:: apache

    # unter Windows Datei httpd.conf (Kommentar # entfernen) und Apache neu starten
    LoadModule rewrite_module modules/mod_rewrite.so

Erstellen Sie den Apache Alias. Es gibt für Windows mehrere Möglichkeiten. Eine übersichtliche Möglichkeit ist, eine Datei mapbender3.conf zu erstellen und auf diese in der httpd.conf zu verweisen.

* Erstellen Sie einen Unterordner "alias" im Verzeichnis <apache>/conf. Legen Sie die Datei mapbender3.conf dort ab. (Dieses Verzeichnis können Sie dann auch nutzen, um dort weitere Alias-Definitionen übersichtlich abzulegen.)
* Verweisen Sie in der Datei httpd.conf (im Verzeichnis <apache>/conf/) auf diese Datei mapbender3.conf.

In der httpd.conf:

.. code-block:: apache

                # Verweis auf Mapbender3 Alias
                Include "conf/alias/mapbender3.conf"

In der mapbender3.conf:
  
.. code-block:: apache

 Alias /mapbender3 c:/mapbender3/web/
 <Directory c:/mapbender3/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender3/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>

Wir gehen in diesem Beispiel davon aus, dass Mapbender3 direkt unter **C:/** entpackt wurde (siehe das Kapitel `Systemvoraussetzungen und den Download <systemrequirements.html#download-von-mapbender3>`_ für Details). Sie können auch einfach ein anderes Verzeichnis wählen. Passen Sie dann nur diese Apache mapbender3.conf Datei oben an, indem Sie auf das richtige Verzeichnis verweisen.

Starten Sie den Apache Webserver neu und prüfen Sie, ob der Alias erreichbar ist:

* http://localhost/mapbender3/

Öffnen Sie das Symfony Welcome Script config.php. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender3/config.php


.. image:: ../../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80 

Passen Sie die Mapbender3 Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen möchten. Mehr Informationen dazu finden Sie im Kapitel `Konfiguration der Datenbank <../database.html>`_.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:     ~
    database_user:     postgres
    database_password: geheim

Rufen Sie die app/console Befehle über die php.exe auf. Hierzu müssen Sie ein Standardeingabefenster öffnen.

.. code-block:: text
 
 c:
 cd mapbender3
 php.exe app/console doctrine:database:create
 php.exe app/console doctrine:schema:create
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

Wenn Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das `Mapbender3 Quickstart Dokument <../quickstart.html>`_ an.

