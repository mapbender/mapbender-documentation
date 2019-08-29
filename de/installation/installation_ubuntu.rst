.. _installation_ubuntu_de:

Installation auf Ubuntu und Debian
##################################

Der schnelle Weg und die vorkonfigurierte Datenbank
---------------------------------------------------

Die folgende Installationsanleitung beschreibt die notwendigen Schritte auf einem aktuellen Ubuntu- oder Debian-System mit PHP 5.5 oder 5.6.  Wir nehmen an, dass Apache 2.4 auf dem System läuft. Anmerkungen `zu PHP 7 <installation_ubuntu.html#php-7>`_ und `zu Apache 2.2 <installation_ubuntu.html#einrichtung-fur-apache-2-2>`_ finden sich weiter unten.

Falls Sie einen schnellen Test ohne Einrichtung eines Webservers bevorzugen, schauen Sie in das Kapitel `Installation auf dem Symfony eigenen Webserver <installation_symfony.html>`_.

Mapbender wird seit Version 3.0.6.0 mit einer vorkonfigurierten Datenbank auf Basis von SQLite mitgeliefert, in der schon Anwendungen realisiert sind (die Datenbank liegt unter **<mapbender>/app/db/demo.sqlite**). Die Datenbank enthält die Mapbender-Konfiguration, wie Anwendungen, Nutzer und registrierte Dienste, sie enthält keine Geodaten.

Falls Sie eine andere Datenbank wie PostgreSQL vorliegen haben und nutzen möchten, finden Sie im Kapitel `Mapbender Einrichtung auf PostgreSQL <#mapbender-einrichtung-auf-postgresql>`_ die notwendigen Schritte.



Vorbereitung
------------

Beachten Sie die `Systemvoraussetzungen <systemrequirements.html>`_, wo Sie auch die Download-Links für Mapbender finden.

Dort sind auch die notwendigen Komponenten für Mapbender aufgelistet, die Sie folgendermaßen installieren können:

.. code-block:: bash

 apt install php5 php5-gd php5-curl php5-cli php5-sqlite sqlite php5-intl php5-mbstring curl openssl

Beachten Sie, dass diese Pakete eine Nutzung von PHP5 erfordern, die meisten aktuellen Systeme (Ubuntu ab Version 16.04) jedoch PHP7 nutzen. Siehe unten im Bereich **PHP7** welche Pakete für eine Nutzung von Mapbender mit PHP7 installiert werden müssen.


Zusätzlich für die Entwicklung:
 
.. code-block:: bash

 apt install php5-bz2


Laden Sie das Apache Modul rewrite.

.. code-block:: bash

 sudo a2enmod rewrite



PHP 7
-----

Für PHP 7 werden weitere Quellen benötigt. Die Paketliste bei Verwendung von PHP 7:

.. code-block:: bash

   sudo apt install php php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-intl openssl php-zip php-mbstring php-bz2


Unter Ubuntu 16.04 muss zusätzlich das passende Modul für den Apache Webserver manuell nachinstalliert werden:

.. code-block:: bash

   sudo apt install libapache2-mod-php7.0


Zur Nutzung von PostgreSQL zusätzlich:

.. code-block:: bash

   sudo apt install php-pgsql


Für MySQL:

.. code-block:: bash

   sudo apt install php-mysql
  

Zusätzlich muss PHP 7 in Apache aktiviert werden:

.. code-block:: bash

   a2enmod php7.0



Entpacken und im Webserver registrieren
---------------------------------------

Entpacken Sie das Mapbender Archiv (tar.gz oder zip) beispielsweise im Verzeichnis **/var/www/mapbender** (siehe das Kapitel `Systemvoraussetzungen und den Download <systemrequirements.html#download-von-mapbender>`_ für Details).

Erstellen Sie den Apache Alias. Sie können Mapbender in ein beliebiges anderes Verzeichnis entpacken und müssen dann nur die folgende Datei anpassen und auf den richtigen Ordner verweisen lassen.

Legen Sie die Datei **/etc/apache2/sites-available/mapbender.conf** mit dem folgenden Inhalt an.

.. code-block:: apache
                
 Alias /mapbender /var/www/mapbender/web/
 <Directory /var/www/mapbender/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
   
  RewriteEngine On
  RewriteBase /mapbender/
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>

Aktivieren Sie danach die Seite mit:

.. code-block:: bash

 a2ensite mapbender.conf

Laden Sie den Apache Server neu.

.. code-block:: bash

 service apache2 reload


Verzeichnisrechte
-----------------

Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (o). Weisen Sie die Rechte dem Apache User (www-data) zu.

.. code-block:: bash

 sudo chown -R www-data:www-data /var/www/mapbender/app/logs
 sudo chown -R www-data:www-data /var/www/mapbender/app/cache
 sudo chown -R www-data:www-data /var/www/mapbender/web/uploads

 # wenn Sie die vorkonfigurierte dateibasierte Datenbank nutzen möchten
 sudo chmod -R ug+w /var/www/mapbender/app/db/demo.sqlite


Der Apache Nutzer benötigt v.a. Schreibrechte auf app/cache, app/logs, web/uploads und app/db/demo.sqlite (wenn Sie die mitgelieferte dateibasierte Datenbank nutzen möchten) und Leserechte auf dem web Verzeichnis.


 
Start und Anmelden am Mapbender
-------------------------------

Sie können nun auf Ihre Mapbender Installation mit **http://hostname/mapbender/** zugreifen.
  
Klicken Sie auf den Anmelden-Link oben rechts, um zur Anmeldung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an. Per Voreinstellung lauten die Anmeldedaten root/root.

Starten Sie Mapbender im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen: http://localhost/mapbender/app_dev.php

Wenn Sie mehr über Mapbender erfahren möchten, schauen Sie sich das `Mapbender Quickstart Dokument <../quickstart.html>`_ an.


 
Mapbender Einrichtung auf PostgreSQL
------------------------------------

Falls Sie die Mapbender Konfiguration in einer anderen Datenbank statt der SQLite Datenbank ablegen möchten (und da spricht nichts dagegen), sind hier die notwendigen Schritte beschrieben. Als Datenbank-Umgebung wird in diesem Beispiel PostgreSQL verwendet.

Sie benötigen den PHP-PostgreSQL Treiber.

.. code-block:: bash

   apt install php5-pgsql
 

Passen Sie die Mapbender Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen und nutzen möchten. Mehr Informationen dazu finden Sie im Kapitel :ref:`database_de`.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: geheim
 
Setzen Sie die app/console Befehle ab. Details zu diesen Befehlen finden Sie im Kapitel :ref:`installation_configuration_de`.

.. code-block:: bash

 cd /var/www/mapbender
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console assets:install web --symlink --relative
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Hiermit ist die Konfiguration von Mapbender für PostgreSQL fertig und Sie enthält nun auch die drei Beispielanwendung wie auch die unterstützten EPSG-codes.



Mapbender Einrichtung auf MySQL
-------------------------------

Die Einrichtung von Mapbender auf MySQL ist ähnlich der auf PostgreSQL, Sie benötigen nur einen anderen PHP-Treiber und einen anderen Parameter in der parameters.yml. Falls Sie also die Mapbender Konfiguration in einer anderen Datenbank statt der SQLite Datenbank ablegen möchten (und da spricht nichts dagegen), sind hier die notwendigen Schritte beschrieben.

Sie benötigen den PHP-MySQL Treiber.

.. code-block:: bash

   apt install php-mysql


Passen Sie die Mapbender Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen und nutzen möchten. Mehr Informationen dazu finden Sie im Kapitel :ref:`database_de`.

.. code-block:: yaml

                    database_driver:   pdo_mysql
                    database_host:     localhost
                    database_port:     3306
                    database_name:     mapbender
                    database_path:     null
                    database_user:     root
                    database_password: geheim

Setzen Sie die app/console Befehle ab. Details zu diesen Befehlen finden Sie im Kapitel :ref:`installation_configuration_de`.

.. code-block:: bash

 cd /var/www/mapbender
 app/console doctrine:database:create
 app/console doctrine:schema:create
 # app/console assets:install web # nicht notwendig
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append



PHP 7
-----

Für PHP 7 werden weitere Quellen benötigt. Die Paketliste bei Verwendung von PHP 7:

.. code-block:: bash

   sudo apt install php php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-intl openssl php-zip php-mbstring php-bz2

Unter Ubuntu 16.04 muss zusätzlich das passende Modul für den Apache Webserver manuell nachinstalliert werden:

.. code-block:: bash

   sudo apt install libapache2-mod-php7.0


Zur Nutzung von PostgreSQL zusätzlich:

.. code-block:: bash

   sudo apt install php-pgsql
   
  
Zur Nutzung von LDAP zusätzlich:

.. code-block:: bash

   sudo apt install php-ldap


Für MySQL:

.. code-block:: bash

   sudo apt install php-mysql
  

Zusätzlich muss PHP 7 in Apache aktiviert werden:

.. code-block:: bash

   a2enmod php7.0

Einrichtung für Apache 2.2
--------------------------

Einige Debian Versionen unterstützen für Apache 2.2 die Ablage der mapbender.conf Datei im Verzeichnis ``/etc/apache2/sites-available`` und die Aktivierung über den Befehl ``a2ensite``. Je nach Betriebssystem muss die Datei aber im Verzeichnis ``/etc/apache2/conf.d/`` abgelegt werden.

Aktivieren Sie das Rewrite-Modul von Apache.

.. code-block:: bash

 sudo a2enmod rewrite

Im Unterschied zu Apache 2.4 gibt es für Apache 2.2 unterschiedliche Direktiven und andere Standardwerte (``Order`` und ``Allow``, ``AllowOverride``), die in die mapbender.conf Datei eingetragen werden. Diese Unterschiede sind `im Upgrade-Guide von Apache 2.2 zu Apache 2.4 <http://httpd.apache.org/docs/2.4/upgrading.html>`_ beschrieben.
 
Apache 2.2 Konfiguration ``mapbender.conf``:

.. code-block:: apache

  ALIAS /mapbender /var/www/mapbender/web/
  <Directory /var/www/mapbender/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    AllowOverride none
    Order allow,deny
    Allow from all
    
    RewriteEngine On
    RewriteBase /mapbender/
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>




Überprüfung
-----------

Prüfen Sie, ob der Alias erreichbar ist:

* http://localhost/mapbender/

Öffnen Sie das Symfony Welcome Script config.php. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender/config.php


.. image:: ../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80
