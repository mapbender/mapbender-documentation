.. _update:

Aktualisierung von Mapbender3 auf eine neuere Version
=====================================================

Um Mapbender3 zu aktualisieren, müssen Sie die folgenden Schritte durchführen:

* Laden Sie die neuste Version von http://mapbender3.org/builds/ herunter. Aktuelle Snapshots finden Sie unter http://mapbender3.org/builds/nightly/
* Sichern Sie Ihre Konfigurationsdateien (parameters.yml und config.yml) und Ihre alte Mapbender Version (Dateien und Datenbank)
* Ersetzen Sie die Dateien durch die neuen Mapbender Dateien
* Vergleichen Sie die Konfigurationsdateien und prüfen diese auf neue Parameter und Änderungen.
* Aktualisieren Sie Ihre Mapbender Datenbank
* Übernahme Ihrer Screenshots: Kopieren Sie die Dateien Ihrer alten Mapbender Version von /web/uploads/ in das /web/uploads Verzeichnis Ihrer neuen Mapbender Version
* Wenn Sie eigenen Templates verwenden sollten, müssen Sie Ihre Templates mit denen der neuen Version vergleichen (kam es zu Änderungen?)
* Importieren Sie die Anwendungen aus der mapbender.yml Datei, um sich den neusten Stand der Entwicklungen anzuschauen
* Das war's auch schon! Schauen Sie sich Ihre neue Mapbender3 Version an.


Aktualisierungsbeispiel für Linux
------------------------------------
Im Folgenden sind die einzelnen Schritte als Befehle aufgeführt.

.. code-block:: bash

 # Laden Sie die neue Version herunter
 wget -O http://mapbender3.org/builds/mapbender3-3.0.4.0.tar.gz /tmp/build_mapbender3/
 tar xfz /tmp/build_mapbender3/mapbender3-3.0.4.0.tar.gz
 
 # Sichern Sie die alte Version
 mv -R /var/www/mapbender3 /var/www/mapbender3_save
 
 # Aktivieren Sie den Code der neuen Version
 cp -R /tmp/build_mapbender3/mapbender3-3.0.4.0 /var/www/
 mv /var/www/mapbender3-3.0.4.0 /var/www/mapbender3
 
 # Übernehmen Sie die Konfigurationsdateien in die neue Version von Mapbender
 cp /var/www/mapbender3_save/app/config/parameters.yml /var/www/mapbender3/app/config/parameters.yml
 cp /var/www/mapbender3/app/config/config.yml /var/www/mapbender3/app/config/config.yml-dist
 cp /var/www/mapbender3_save/app/config/config.yml /var/www/mapbender3/app/config/config.yml 
 
 # Händisch müssen Sie nun die Konfigurationsdateien auf neue Parameter überprüfen.
 # Vergleichen Sie die Dateien parameters.yml, config.yml und sofern verwendet die mapbender.yml.
 # Sofern Sie eigene Templates angelegt haben, vergeleichen Sie diese mit der neuen Mapbender Version.
 # Sofern Sie Vorschaubilder hochgeladen haben: Kopieren Sie diese von der alten Version wieder nach mapbender3/web/uploads.
 # Sofern Sie eigene Druckvorlagen verwenden: Kopieren Sie diese wieder nach mapbender3/app/Resources/MapbenderPrintBundle/templates/.

 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 sudo chmod -R ugo+r /var/www/mapbender3
 sudo chown -R www-data:www-data /var/www/mapbender3

 # Aktualisieren Sie Ihre Mapbender Datenbank
 cd /var/www/mapbender3/
 app/console doctrine:schema:update --dump-sql
 app/console doctrine:schema:update --force

 # Importieren Sie die Anwendungen aus der mapbender.yml Datei, um sich den neusten Stand der Entwicklungen anzuschauen
 app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append

 app/console assets:install web
 
 # Setzen Sie die Schreibrechte für Besitzer (u), Gruppe (g) und Andere (a). Weisen Sie die Skripte dem Apache User (www-data) zu.
 sudo chmod -R ugo+r /var/www/mapbender3
 sudo chown -R www-data:www-data /var/www/mapbender3

 # Sie benötigen Schreibrechte für die Verzeichnisse app/cache und app/logs.
 sudo chmod -R ug+w /var/www/mapbender3/app/cache
 sudo chmod -R ug+w /var/www/mapbender3/app/logs
 sudo chmod -R ug+w /var/www/mapbender3/web/assets
 sudo chmod -R ug+w /var/www/mapbender3/web/uploads


Aktualisierungsbeispiel für Windows
------------------------------------
 
.. code-block:: bash

 # Laden Sie die neue Version herunter http://mapbender3.org/builds/
  
 # Sichern Sie die alte Version (Dateien und Datenbank)
 
 # Übernehmen Sie die Konfigurationsdateien in die neue Version von Mapbender.
 # Vorher müssen Sie diese händisch auf neue Parameter und Änderungen überprüfen.
 
 # Rufen Sie die app/console Befehle über die php.exe auf.
 # Hierzu müssen Sie ein Standardeingabefenster öffnen.
 c:
 cd mapbender3
 
 # Aktualisieren Sie Ihre Mapbender Datenbank
 php.exe app/console doctrine:schema:update --dump-sql
 php.exe app/console doctrine:schema:update --force
  
 # Importieren Sie die Anwendungen aus der mapbender.yml Datei, um sich den neusten Stand der Entwicklungen anzuschauen
 php.exe app/console doctrine:fixtures:load --fixtures=./mapbender/src/Mapbender/CoreBundle/DataFixtures/ORM/Application/ --append
 php.exe app/console assets:install web

 # Löschen Sie den Cache und die Logdateien unter mapbender3/app/cache und mapbender3/app/logs

 # Sofern Sie eigene Templates angelegt haben, vergleichen Sie diese mit der neuen Mapbender Version.
 # Sofern Sie Vorschaubilder hochgeladen haben: Kopieren Sie diese von der alten Version wieder nach mapbender3/web/uploads.
 # Sofern Sie eigene Druckvorlagen verwenden: Kopieren Sie diese wieder nach mapbender3/app/Resources/MapbenderPrintBundle/templates/



