.. _installation_ubuntu_de:

Installation auf Ubuntu/Debian
##############################

Die mitgelieferte SQLite Datenbank ist für Testinstallationen geeignet. In dieser Datenbank befinden sich bereits vorkonfigurierte Demoanwendungen (sie liegt unter <mapbender>/app/db/demo.sqlite).
Eine Anleitung für eine Testinstallation auf Basis des Symfony Webservers finden Sie unter :ref:`installation_symfony_de`.

.. hint:: Für den Produktiveinsatz wird PostgreSQL empfohlen. Weitere Installationshinweise finden Sie im Kapitel `Optional > Mapbender Einrichtung auf PostgreSQL <#optional>`_.


Voraussetzungen
---------------

* PHP >= 7.4
* Apache Installation mit folgenden aktivierten Modulen:
    * mod_rewrite
    * libapache2-mod-php
* PostgreSQL Installation
    * Es wird empfohlen, eine PostgreSQL Datenbank für Mapbender zu verwenden.
    * Es wird empfohlen, einen eigenen Datenbankbenutzer für den Zugriff auf die Mapbender Datenbank anzulegen.

Als Webserver kann auch nginx verwendet werden. In dieser Anleitung wird darauf nicht weiter eingegangen.


Vorbereitung
------------

Installation der benötigten PHP-Extensions:

.. code-block:: bash

    sudo apt install php-gd php-curl php-cli php-xml php-sqlite3 sqlite3 php-apcu php-intl openssl php-zip php-mbstring php-bz2

* Bitte prüfen Sie die :ref:`faq_de` für weitere PHP-Einstellungen. 


Entpacken und im Webserver registrieren
---------------------------------------

Download der aktuellen Mapbender Version und entpacken nach /var/www/mapbender oder ein anderes Verzeichnis:

.. code-block:: bash

    wget https://mapbender.org/builds/mapbender-starter-current.tar.gz -O /var/www/mapbender-starter-current.tar.gz
    tar -zxf /var/www/mapbender-starter-current.tar.gz -C /var/www
    mv $(ls -d /var/www/*/ | grep mapbender) /var/www/mapbender/


Konfiguration Apache 2.4
------------------------

Datei **/etc/apache2/sites-available/mapbender.conf** mit dem folgenden Inhalt anlegen:

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

Aktivieren der Seite und Apache neu starten:

.. code-block:: bash

 a2ensite mapbender.conf
 service apache2 reload


Verzeichnisrechte
-----------------

.. code-block:: bash

 sudo chown -R :www-data /var/www/mapbender

 sudo chmod -R ug+w /var/www/mapbender/app/logs
 sudo chmod -R ug+w /var/www/mapbender/app/cache
 sudo chmod -R ug+w /var/www/mapbender/web/uploads

 sudo chmod -R ug+w /var/www/mapbender/app/db/demo.sqlite


Nächste Schritte
----------------

Es kann nun auf die Mapbender Installation unter **http://[hostname]/mapbender/** zugegriffen werden.

Per Voreinstellung lauten die Anmeldedaten

Benutzername: "root", Passwort: "root"


Zur Überprüfung der Konfiguration dient der folgende Befehl:

.. code-block:: yaml

	app/console mapbender:config:check

.. hint:: Bitte beachten Sie, dass der Befehl mapbender:config:check die PHP-CLI Version nutzt. Die Einstellungen der CLI-Version können sich von denen der Webserver PHP-Version unterscheiden. Nutzen Sie beispielsweise php -r 'phpinfo();' zur Ausgabe der PHP-Webserver Einstellungen.

Glückwunsch! Mapbender wurde erfolgreich installiert.
Informationen zu den ersten Schritten mit Mapbender finden sich im :ref:`Mapbender Schnellstart <quickstart_de>`.


Optional
--------

**LDAP**

Zur Nutzung der optionalen LDAP-Anbindung wird die PHP-LDAP-Extension benötigt:

.. code-block:: bash

   sudo apt install php-ldap


**Mapbender Einrichtung auf PostgreSQL**

Für den Einsatz in einer Produktivumgebung wird nachfolgend die Konfiguration einer PostgreSQL Datenbank beschrieben.

Voraussetzungen:

- eingerichtete PostgreSQL Datenbank
- vorhandene Datenbank zur Mapbender Konfiguration
- ggf. eigenen Benutzer für Zugriff

Installation PHP-PostgreSQL Treiber:

.. code-block:: bash

   sudo apt install php-pgsql


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

Initialisierung der Datenbank:

.. code-block:: bash

    cd /var/www/mapbender
    app/console doctrine:database:create
    app/console doctrine:schema:create
    app/console mapbender:database:init -v
    bin/composer run reimport-example-apps

Root-Benutzer für Zugriff anlegen:

.. code-block:: bash

   app/console fom:user:resetroot

Weitere Informationen zur Konfiguration im Kapitel :ref:`installation_configuration_de`.


**Mapbender Einrichtung auf MySQL**

Analog zur Konfiguration mit PostgreSQL.

Installation MySQL Treiber:

.. code-block:: bash

   apt install php-mysql


Abweichend von der PostgreSQL-Konfiguration müssen für MySQL folgende Parameter (parameters.yml) angepasst werden:

.. code-block:: yaml

                    database_driver:   pdo_mysql
                    database_port:     3306

Nachfolgend muss die Datenbank initialisiert werden, siehe PostgreSQL.
