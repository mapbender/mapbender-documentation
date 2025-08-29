.. _directory_structure_de:

Verzeichnisstruktur in Mapbender
################################

application
***********

Bei einer :ref:`Git-basierten Installation <de/installation/installation_git:Git-basierte Installation>` enthält das `application`-Verzeichnis beinahe sämtliche Mapbender-Komponenten. Wichtige Unterverzeichnisse und Dateien sind:

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

Dieses Verzeichnis muss vom Webserver veröffentlicht werden. Ein entsprechendes Alias muss auf dieses Verzeichnis verweisen.


Es kontrolliert:

* *index.php*: FrontendController (PHP-Script, welches aufgerufen werden kann). Benutzt je nach Definition der Variable ``APP_ENV`` den Produktiv- oder Entwicklungsmodus (siehe :ref:`.env bzw. .env.local <de/customization/yaml:.env bzw. .env.local>`).
* *index_dev.php*: Benutzt immer die Entwicklungsumgebung. Kann standardmäßig nur von der lokalen Hostumgebung aufgerufen werden. Lesen Sie mehr dazu, wie auch andere IPs für den Zugriff freigegeben werden können, unter :ref:`Produktions- und Entwicklungsumgebung und Caches<de/installation/installation_configuration:Produktions- und Entwicklungsumgebung und Caches>`.
* `public/` beinhaltet öffentlich verfügbare Ressourcen wie css, js, favicon etc.

public/bundles
--------------

* Hier sind die statischen Ressourcen der einzelnen Bundles gespeichert.
* Das folgende Kommando kopiert die Ressourcen der Bundles in den Ordner:

.. code-block:: yaml

     bin/console assets:install --symlink --relative public

.. note:: **Hinweis**: Wenn Sie Windows benutzen, können Sie keine symbolischen Links verwenden. Daher müssen Sie das Kommando ``php.exe bin/console assets:install public`` nach jeder Änderung von JavaScript-, css- oder twig- sowie Bilddateien aufrufen, um die Dateien in das öffentliche Verzeichnis zu kopieren.


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
