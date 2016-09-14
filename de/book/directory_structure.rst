.. _directory_structure:

Verzeichnisstruktur in Mapbender3
#################################

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


bin
***

* wird im Moment nicht verwendet. Hier können z.B. Installationsskripte abgelegt werden.


mapbender
*********

* liefert die mapbender-spezifischen Bundles und den Mapbender3-Code


web
***

Dieses Verzeichnis muss vom Webserver veröffentlicht werden. Der ALIAS muss auf dieses Verzeichnis verweisen.


Es kontrolliert: 

* den FrontendController (PHP-Script, welches aufgerufen werden kann). Das sind **app.php** für das Produktiv-System und **app_dev.php** für die Entwicklungsversion. Die Entwicklungsversion beinhaltet z.B. die Instrumente für Performance-Tests. 

* dieses Verzeichnis beinhaltet die statischen Ressourcen wie css, js, favicon etc.


web/bundles
***********

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
* Verzeichnis, in dem alle Bundles, die von Symfony verwendet werden, gespeichert werden. Resourcen werden von Symfony durch das Autoladen verwendet.


Übersetzungen
*************
Die Übersetzung wird in xliff-Textdateien gespeichert. Jede Sprache benötigt eine xliff-Datei wie z.B. messages.de.xliff für die deutsche Übersetzung

* mapbender/src/Mapbender/CoreBundle/Resources/translations/
