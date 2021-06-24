.. _update_de:

Aktualisierung von Mapbender auf eine neuere Version
====================================================

Um Mapbender zu aktualisieren, müssen Sie die folgenden Schritte durchführen:

* Laden Sie die neuste Version von http://mapbender.org/builds/ herunter
* Sichern Sie Ihre Konfigurationsdateien (parameters.yml und config.yml) und Ihre alte Mapbender Version (Dateien und Datenbank)
* Ersetzen Sie die Dateien durch die neuen Mapbender Dateien
* Vergleichen Sie die Konfigurationsdateien und prüfen diese auf neue Parameter und Änderungen
* Aktualisieren Sie Ihre Mapbender Datenbank
* Übernahme Ihrer Screenshots: Kopieren Sie die Dateien Ihrer alten Mapbender Version von /web/uploads/ in das /web/uploads Verzeichnis Ihrer neuen Mapbender Version
* Wenn Sie Ihre eigenen Templates verwenden sollten, müssen Sie diese mit denen der neuen Version vergleichen (kam es zu Änderungen?)
* Importieren Sie die Anwendungen aus der mapbender.yml Datei, um sich den neusten Stand der Entwicklungen anzuschauen
* Abhängig von Ihrer alten Mapbender Version, muss unter Umständen noch der Apache Alias für Mapbender in der Datei **/etc/apache2/sites-available/mapbender.conf** angepasst werden
* Unter https://doc.mapbender.org/de/installation/installation_ubuntu.html im Bereich **Entpacken und im Webserver registrieren** ist beschrieben, wie die Konfigurationsdatei für den Apache Alias aussehen sollte
* Das war's auch schon! Schauen Sie sich Ihre neue Mapbender Version an.


Aktualisierungsbeispiel für Linux
------------------------------------
Im Folgenden sind die einzelnen Schritte als Befehle aufgeführt.

.. code-block:: bash

 # Laden Sie die neue Version herunter
 wget -O http://mapbender.org/builds/mapbender-starter-current.tar.gz /tmp/build_mapbender/
 tar xfz /tmp/build_mapbender/mapbender-starter-current.tar.gz 
 
 # Sichern Sie die alte Version
 mv /var/www/mapbender /var/www/mapbender_save
 
 # Aktivieren Sie den Code der neuen Version
 cp -R /tmp/build_mapbender/mapbender-starter-v3.2.5 /var/www/
 mv /var/www/mapbender-starter-v3.2.5 /var/www/mapbender
 
 # Übernehmen Sie die Konfigurationsdateien in die neue Version von Mapbender
 cp /var/www/mapbender_save/app/config/parameters.yml /var/www/mapbender/app/config/parameters.yml
 cp /var/www/mapbender_save/app/config/config.yml /var/www/mapbender/app/config/config.yml 
 
 # Händisch müssen Sie nun die Konfigurationsdateien auf neue Parameter überprüfen.
 # Vergleichen Sie die Dateien parameters.yml, config.yml und sofern verwendet die mapbender.yml.
 # Sofern Sie eigene Templates angelegt haben, vergleichen Sie diese mit der neuen Mapbender Version.
 # Sofern Sie Vorschaubilder hochgeladen haben: Kopieren Sie diese von der alten Version wieder nach mapbender/web/uploads.
 # Sofern Sie eigene Druckvorlagen verwenden: Kopieren Sie diese wieder nach mapbender/app/Resources/MapbenderPrintBundle/templates/.

 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 sudo chmod -R ugo+r /var/www/mapbender
 sudo chown -R www-data:www-data /var/www/mapbender

 # Aktualisieren Sie Ihre Mapbender Datenbank
 cd /var/www/mapbender/
 app/console doctrine:schema:update --dump-sql
 app/console doctrine:schema:update --force

 # Aufbau der symbolischen Links
 app/console assets:install web --symlink --relative
 
 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 sudo chmod -R ugo+r /var/www/mapbender
 sudo chown -R www-data:www-data /var/www/mapbender

 # Sie benötigen Schreibrechte für die Verzeichnisse app/cache und app/logs.
 sudo chmod -R ug+w /var/www/mapbender/app/cache
 sudo chmod -R ug+w /var/www/mapbender/app/logs
 sudo chmod -R ug+w /var/www/mapbender/web/uploads


Aktualisierungsbeispiel für Windows
------------------------------------
 
.. code-block:: bash

 # Laden Sie die neue Version herunter http://mapbender.org/builds/
  
 # Sichern Sie die alte Version (Dateien und Datenbank)
 
 # Übernehmen Sie die Konfigurationsdateien in die neue Version von Mapbender.
 # Vorher müssen Sie diese händisch auf neue Parameter und Änderungen überprüfen.
 
 # Rufen Sie die app/console Befehle über die php.exe auf.
 # Hierzu müssen Sie ein Standardeingabefenster öffnen.
 c:
 cd mapbender
 
 # Aktualisieren Sie Ihre Mapbender Datenbank
 php.exe app/console doctrine:schema:update --dump-sql
 php.exe app/console doctrine:schema:update --force
 
 # Hinweise für MS4W Anwender:
 #     - stellen Sie sicher, dass Sie die setenv.bat-Datei ausführen, um die benötigten PATH-Variablen für PHP zu setzen
 #     - ggf. müssen Sie die benötigte Erweiterung auf der Kommandozeile im Aufruf übergeben z.B. 
 #            php -d extension=C:\ms4w\Apache\php\ext\php_pdo_pgsql.dll app/console doctrine:schema:update --dump-sql
  
 # Ausspielen in den web-Bereich
 php.exe app/console assets:install web

 # Löschen Sie den Cache und die Logdateien unter mapbender/app/cache und mapbender/app/logs

 # Sofern Sie eigene Templates angelegt haben, vergleichen Sie diese mit der neuen Mapbender Version.
 # Sofern Sie Vorschaubilder hochgeladen haben: Kopieren Sie diese von der alten Version wieder nach mapbender/web/uploads.
 # Sofern Sie eigene Druckvorlagen verwenden: Kopieren Sie diese wieder nach mapbender/app/Resources/MapbenderPrintBundle/templates/



