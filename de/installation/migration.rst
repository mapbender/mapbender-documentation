.. _migration_de:

Migrations-Leitfaden
####################

.. hint::

    Diese Seite enthält Migrationsanweisungen für bestimmte Mapbender-Versionen. Allgemeine Tipps zur Aktualisierung finden Sie stattdessen auf der Seite :ref:`installation_update_de`.

.. hint::

    Beschreibungen zu Versionen < 4.0.0 finden Sie in der englischen Version, siehe :ref:`Migration Guide<en/installation/migration:Migration to Mapbender 3.3.4>`.

.. note::

    Für ausführliche Informationen des Mapbender-Entwicklungsteams siehe auch den `Upgrading Guide auf GitHub <https://github.com/mapbender/mapbender/blob/master/docs/UPGRADING.md>`_.


Umstellung auf Mapbender 4.0.0
******************************

* Schauen Sie sich den `Upgrading Guide auf GitHub <https://github.com/mapbender/mapbender/blob/master/docs/UPGRADING.md>`_ sorgfältig an, bevor Sie das Update durchführen.

* Sie werden feststellen, dass sich die Symfony Verzeichnisstruktur stark verändert hat.
* Für Mapbender 4 wurden alle ``.yml``-Dateierweiterungen in ``.yaml`` umgewandelt.
* Die config.yml ist entfallen.
* Öffentliche Dateien wurden von app/web nach public verschoben.
* Anstelle von mehreren Parametern in der Datei parameters.yml wird die Datenbankdefinition durch eine Umgebungsvariable ``MAPBENDER_DATABASE_URL`` ersetzt. Konfigurieren Sie sie, indem Sie diese in Ihrer .env.local-Datei hinzufügen. Wenn Sie mehrere Verbindungen haben, verwenden Sie eine Umgebungsvariable pro Verbindung und konfigurieren diese in der Datei config/packages/doctrine.yaml.
* Der Apache Virtual Host / ALIAS muss geändert werden. Verweisen Sie auf public (statt auf web). Rufen Sie index.php (anstelle von app.php) auf. Siehe Installationsanleitung.
* Die Umgebung kann nun über die Umgebungsvariable ``APP_ENV`` gesetzt werden (siehe .env.local). index_dev.php (vorher app_dev.php) ist weiterhin als Alternative für den Zugriff auf die Entwicklungsumgebung auf entfernten Servern verfügbar.
* Datenbankberechtigungen können mit ``bin/console mapbender:security:migrate-from-acl`` migriert werden. Führen Sie dies aus, bevor Sie den Befehl schema:update ausführen, da sonst Ihre alten ACL-Tabellen nicht mehr vorhanden sind.


Upgrade der Datenbank
---------------------

**Wichtig**: Führen Sie die folgenden Befehle in der angegebenen Reihenfolge aus, um ein Upgrade durchzuführen (nachdem Sie die Verzeichnisstruktur von Symfony auf den neuesten Stand gebracht haben). Erstellen Sie zuerst ein Backup Ihrer Datenbank!

* ``bin/console mapbender:database:upgrade``: Dies ersetzt den aus doctrine entfernten json_array-Typ durch json. Wenn Sie ein anderes DBMS als SQlite, PostgreSQL und MySQL verwenden, müssen Sie dies manuell tun.
* ``bin/console mapbender:security:migrate-from-acl``: Migriert Sicherheitsdefinitionen aus dem ACL-System in das neue Rechtesystem.
* ``bin/console doctrine:schema:update --complete --force``: Aktualisiert den Rest der Datenbank. Dies muss als letzter Schritt ausgeführt werden, da es die alten ACL-Tabellen löscht.
