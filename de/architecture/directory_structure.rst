.. _directory_structure_de:

Verzeichnisstruktur in Mapbender
################################

app
***
Dieses Verzeichnis beinhaltet:

* php-Cache (app/cache)
* log-Verzeichnis (app/logs)
* Konfigurationsdateien (app/config)
* applicationkernel (app/AppKernel.php) (wird über die FrontendController aufgerufen; darüber wird die gesamte Anwendung kontrolliert)
* das Autoladen (autoload.php)
* spezielle Ressourcen für die Anwendungen (Resources)
* die Kommandozeilen-Anwendungen für Pflege und Management (app/console)


app/config
----------

Grundlegende Konfigurationsdateien von Mapbender liegen im Verzeichnis app/config. Zwei Dateien sind dabei von besonderer Bedeutung:

* parameters.yml
* config.yml

Weitere Informationen im Kapitel :ref:`yaml_de`.


app/config/applications
-----------------------

Als YAML definierte Anwendungen können in dem Verzeichnis app/config/applications abgelegt werden. Die bekannten Beispielanwendungen "Mapbender mobile", "Mapbender Demo Map" und "Mapbender Demo Map basic" liegen dort als einzelne YAML Dateien.

Weitere Informationen im Kapitel :ref:`yaml_de`.



bin
***

Hier sind symbolische Links zu den folgenden Binaries hinterlegt:

* apigen
* composer
* coveralls
* doctrine
* doctrine.php
* phantomjs
* phing
* phpunit


documentation
*************

Verzeichnis für diese Dokumentation


fom
***

Verzeichnis des `FOM Submoduls <https://github.com/mapbender/fom>`_.


mapbender
*********

Verzeichnis des `Mapbender Submoduls <https://github.com/mapbender/mapbender>`_. Liefert die Mapbender-spezifischen Bundles und den Mapbender-Code.



mapbender/...../translations
----------------------------

Verzeichnis: mapbender/src/Mapbender/CoreBundle/Resources/translations/


Die Übersetzungen werden in `XLIFF Textdateien <https://en.wikipedia.org/wiki/XLIFF>`_ gespeichert. Jede Sprache benötigt eine xliff-Datei wie z.B. messages.de.xlf für die deutsche Übersetzung



owsproxy
********

Verzeichnis des `OWSProxy Submoduls <https://github.com/mapbender/owsproxy3>`_.


vendor
******

Verzeichnis für externe Bibliotheken (vom Composer geladen) und weitere Mapbender Module (u.a. Digitizer, Mapbender-Icons).



web
***

Dieses Verzeichnis muss vom Webserver veröffentlicht werden. Der ALIAS muss auf dieses Verzeichnis verweisen.


Es kontrolliert:

* den FrontendController (PHP-Script, welches aufgerufen werden kann). Das sind **app.php** für die Produktiv-Umgebung und **app_dev.php** für die Entwicklungsversion. Die Entwicklungsversion beinhaltet z.B. die Instrumente für Performance-Tests.

* dieses Verzeichnis beinhaltet die statischen Ressourcen wie css, js, favicon etc.


web/bundles
-----------

* Hier sind die statischen Ressourcen der einzelnen Bundles gespeichert.
* Das folgende Kommando kopiert die Ressourcen von den Bundles zu dem Ordner.

.. code-block:: yaml

     app/console assets:install --symlink web

* **Hinweis**: Wenn Sie Windows benutzen, können Sie keine symbolischen Links verwenden. Daher müssen Sie das folgende Kommando (**app/console assets:install web**) nach jeder Änderung im Code aufrufen, um die Dateien in das Verzeichnis zu kopieren.


src
***

* Verzeichnis für anwendungsspezifische Bundles (ähnlich der x-directories in Mapbender 2.x)


vendor
******
* Verzeichnis, in dem alle Bundles, die von Symfony verwendet werden, gespeichert werden. Ressourcen werden von Symfony durch das Autoladen verwendet.
