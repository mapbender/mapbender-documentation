.. _directory_structure_de:

Verzeichnisstruktur in Mapbender
################################

application
***********

Dieses Verzeichnis enthält beinahe sämtliche Mapbender-Komponenten. Wichtige Unterverzeichnisse und Dateien sind:

* Das :ref:`config<de/architecture/directory_structure:config>`-Verzeichnis,
* Der Anwendungskernel (`src/Kernel.php`) als Zugangspunkt zu Symfony,
* Autoloading (`vendor/autoload.php`) generiert von Composer,
* Kommandozeilen-Anwendungen für Pflege und Management (``bin/console``, ``bin/phpunit``) und
* *.env* und *.env.local*: Globale Konfigurationsdateien, z.B. für Datenbank-URLs und SMTP-Server-Verbindungen.

bin
===

Hier liegen diverse Bibliotheken.

config
======

Grundlegende Konfigurationsdateien von Mapbender liegen im Verzeichnis `config/` sowie im Verzeichnis `config/packages`. Diese Dateien sind dabei von besonderer Bedeutung:

* :ref:`doctrine.yaml<de/customization/yaml:doctrine.yaml>`
* :ref:`parameters.yaml<de/customization/yaml:parameters.yaml>`
* *services.yaml*: Dient als Einstiegspunkt zur Konfiguration von Diensten.

config/applications
-------------------

Als YAML definierte Anwendungen können in dem Verzeichnis `config/applications` abgelegt werden. Die bekannten Beispielanwendungen **Mapbender mobile**, **Mapbender Demo Map** und **Mapbender Demo Map basic** liegen dort als einzelne YAML Dateien.

Weitere Informationen im Kapitel :ref:`yaml_de`.

mapbender
=========

* Verzeichnis des `Mapbender Submoduls <https://github.com/mapbender/mapbender>`_. Liefert die Mapbender-spezifischen Bundles und den Mapbender-Code.
* Verzeichnis für spezielle Anwendungsressourcen (`Resources/`)

mapbender/...../translations
----------------------------

Die Übersetzungen werden in `YAML-Dateien <https://en.wikipedia.org/wiki/YAML>`_ gespeichert. Jede Sprache benötigt eine YAML-Datei, wie z.B. *messages.fr.yaml* für die französische Übersetzung.

* Verzeichnis: `mapbender/src/Mapbender/CoreBundle/Resources/translations/`


public
======

Dieses Verzeichnis muss vom Webserver veröffentlicht werden. DocumentRoot muss auf dieses Verzeichnis verweisen.


Es kontrolliert:

* *index.php*: FrontendController (PHP-Script, welches aufgerufen werden kann). Benutzt die Umgebung, die in *.env* oder *.env.local* definiert wird.
* *index_dev.php*: Benutzt immer die Entwicklungsumgebung. Kann standardmäßig nur von lokalen Host-Umgebungen aufgerufen werden.
* `public/` beinhaltet außerdem die statischen Ressourcen wie css, js, favicon etc.

public/bundles
--------------

* Hier sind die statischen Ressourcen der einzelnen Bundles gespeichert.
* Das folgende Kommando kopiert die Ressourcen der Bundles in den Ordner:

.. code-block:: yaml

     bin/console assets:install --symlink --relative public

.. note:: **Hinweis**: Wenn Sie Windows benutzen, können Sie keine symbolischen Links verwenden. Daher müssen Sie das Kommando ``php.exe bin/console assets:install public`` nach jeder Änderung im Code aufrufen, um die Dateien in das Verzeichnis zu kopieren.


src
===

Verzeichnis für anwendungsspezifische Bundles (Kunden-Bundle).

* Der Anwendungs-Kernel (`src/Kernel.php`) wird über die FrontendController aufgerufen; darüber wird die gesamte Anwendung kontrolliert.

var
===

Dieses Verzeichnis beinhaltet:

* die php-Caches (`var/cache/dev` and `var/cache/prod`),
* das log-Verzeichnis (`var/log`),
* das SQLite-Datenbank-Verzeichnis (`var/db/`).

vendor
======

Verzeichnis mit externen Bibliotheken, die via Composer geladen wurden. Ressourcen werden von Symfony durch das Autoladen verwendet:

* Autoladen-Datei (*autoload.php*)
