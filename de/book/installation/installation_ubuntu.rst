.. _installation_ubuntu:

Installation auf Ubuntu und Debian
##################################

Die folgende Installationsanleitung beschreibt die notwendigen Schritte auf einem aktuellen Ubuntu- oder Debian-System. Wir nehmen an, dass Apache 2.4 auf dem System läuft. Eine `Dokumentation zu Apache 2.2 <installation_ubuntu.html#einrichtung-fur-apache-2-2>`_ findet sich am Ende des Dokuments. Als Datenbank-Umgebung wird PostgreSQL verwendet.

Beachten Sie die `Systemvoraussetzungen <systemrequirements.html>`_, wo Sie auch die Download-Links für Mapbender3 finden.

Dort sind auch die notwendigen Komponenten für Mapbender3 aufgelistet, die Sie folgendermaßen installieren können:

.. code-block:: bash

 apt-get install php5 php5-pgsql php5-gd php5-curl php5-cli php5-sqlite sqlite php-apc php5-intl curl openssl

Laden Sie das Apache Modul rewrite.

.. code-block:: bash

 sudo a2enmod rewrite

Erstellen Sie den Apache Alias. Wir gehen davon aus, dass Mapbender3 im Verzeichnis **/var/www/mapbender3** entpackt wurde (siehe das Kapitel `Systemvoraussetzungen und den Download <systemrequirements.html#download-von-mapbender3>`_ für Details). Sie können Mapbender3 in ein beliebiges anderes Verzeichnis entpacken und müssen dann nur die folgende Datei anpassen und auf den richtigen Ordner verweisen lassen.


Legen Sie die Datei **/etc/apache2/sites-available/mabender3.conf** mit dem folgenden Inhalt an. 

.. code-block:: apache
                
 Alias /mapbender3 /var/www/mapbender3/web/
 <Directory /var/www/mapbender3/web/>
  Options MultiViews FollowSymLinks
  DirectoryIndex app.php
  Require all granted
 
  RewriteEngine On
  RewriteBase /mapbender3/
  RewriteCond %{ENV:REDIRECT_STATUS} ^$
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule ^(.*)$ app.php/$1 [PT,L,QSA]
 </Directory>

Aktivieren Sie danch die Seite mit

.. code-block:: bash

 a2ensite mapbender3.conf

Laden Sie den Apache Server neu.

.. code-block:: bash

 service apache2 reload


Überprüfung
-----------
 

Prüfen Sie, ob der Alias erreichbar ist:

* http://localhost/mapbender3/

Öffnen Sie das Symfony Welcome Script config.php. Das Skript prüft, ob alle notwendigen Komponenten installiert wurden und ob die Konfiguration erfolgte. Sofern noch Probleme vorliegen, sollten diese behoben werden.
 
* http://localhost/mapbender3/config.php


.. image:: ../../../figures/mapbender3_symfony_check_configphp.png
     :scale: 80


Mapbender3 Einrichtung
-----------------------

Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (o). Weisen Sie die Skripte dem Apache User (www-data) zu.

.. code-block:: bash

 sudo chmod -R ugo+r /var/www/mapbender3
 sudo chown -R www-data:www-data /var/www/mapbender3
 sudo chmod -R ug+w /var/www/mapbender3/web/uploads

.. sudo chmod -R ug+w /var/www/mapbender3/web/assets

Passen Sie die Mapbender3 Konfigurationsdatei parameters.yml (app/config/parameters.yml) an und definieren Sie die Datenbank, die Sie erzeugen möchten. Mehr Informationen dazu finden Sie im Kapitel `Konfiguration der Datenbank <../database.html>`_.

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender3
    database_path:     ~
    database_user:     postgres
    database_password: geheim
 
Setzen Sie die app/console Befehle ab. Details zu diesen Befehlen finden Sie im Kapitel `Details zur Konfiguration von Mapbender3 <configuration.html>`_.

.. code-block:: bash

 cd /var/www/mapbender3
 app/console doctrine:database:create
 app/console doctrine:schema:create
 app/console assets:install web
 app/console fom:user:resetroot
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Epsg/ --append
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

Hiermit ist die Installation von Mapbender3 fertig. 

Prüfen Sie die config.php erneut 

* http://localhost/mapbender3/config.php

Sie müssen Schreibrechte für die Verzeichnisse app/cache und app/logs sowie web/uploads vergeben.

.. code-block:: bash

 sudo chmod -R ug+w /var/www/mapbender3/app/cache
 sudo chmod -R ug+w /var/www/mapbender3/app/logs
 sudo chmod -R ug+w /var/www/mapbender3/web/uploads

.. sudo chmod -R ug+w /var/www/mapbender3/web/assets

Sie können Mapbender3 nun nutzen.

* http://localhost/mapbender3/


**Hinweis:** Klicken Sie auf den Login-Link oben rechts, um zur Abmeldung zu gelangen. Melden Sie sich mit dem neu erstellten Benutzer an.

Starten Sie Mapbender3 im Entwicklermodus, indem Sie das Skript app_dev.php aufrufen: http://localhost/mapbender3/app_dev.php


Wenn Sie mehr über Mapbender3 erfahren möchten, schauen Sie sich das `Mapbender3 Quickstart Dokument <../quickstart.html>`_ an.


Einrichtung für Apache 2.2
--------------------------

Im Unterschied zu Apache 2.4 wird für Apache 2.2 die mapbender3.conf im Verzeichnis /etc/apache2/conf.d/ abgelegt.

Apache 2.2 Konfiguration:

.. code-block:: apache

  ALIAS /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
    
    RewriteEngine On
    RewriteBase /mapbender3/
    RewriteCond %{ENV:REDIRECT_STATUS} ^$
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ app.php/$1 [PT,L,QSA]
 </Directory>



Bitte beachten Sie dabei, dass Apache 2.2 im Gegensatz zu Apache 2.4 `andere Direktiven zur Access Control verwendet <http://httpd.apache.org/docs/2.4/upgrading.html>`_ (Allow from all).
