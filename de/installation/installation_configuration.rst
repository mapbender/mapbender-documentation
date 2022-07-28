.. _installation_configuration_de:

Details zur Konfiguration von Mapbender
=======================================

Konfigurationsschritte
----------------------

Im Folgenden werden die für die Mapbender-Installation aufgeführten Konfigurationsschritte von Mapbender näher erläutert. Es sind sechs Schritte notwendig:

* Erzeugen der Datenbank
* Erzeugen der Datenbankschemas
* Kopieren des bundle Assets in das öffentliche web-Verzeichnis
* Erzeugen des "root" Benutzers
* Initialisieren der Datenbank
* Laden der Anwendungen der mapbender.yml Definition in die Datenbank

Diese Schritte werden mit dem console-Hilfsprogramm des `Symfony <http://symfony.com/>`_ Frameworks durchgeführt, auf dem Mapbender aufbaut. Hier noch ein wichtiger Hinweis, bevor Sie fortfahren: 

.. note:: Das console-Hilfsprogramm wird Dateien in die Verzeichnisse app/cache und app/logs schreiben. Für diese Operationen werden die Benutzerrechte des Benutzers benötigt, mit dem Sie angemeldet sind. Sie benötigen ebenfalls Benutzerrechte für das Verzeichnis app/db und die SQLite Datenbank.  Wenn Sie die Applikation in Ihrem Browser öffnen, wird der Server-PHP- Prozess versuchen, auf  diese Dateien zuzugreifen oder in die Verzeichnisse zu schreiben mit anderen Benutzerrechten. Stellen Sie sicher,  dass Sie den Verzeichnissen und Dateien Schreib- und Leserechte zugewiesen haben. 

.. note:: **Wichtiger Hinweis:** Die folgenden app/console Schritte gehen davon aus, dass Sie sich oberhalb des app-Verzeichnisses befinden (für die git-Installation bedeutet das mapbender/application/ , andernfalls mapbender/).

.. code-block:: yaml

   cd mapbender/
   oder für die git-basierte Installation 
   cd mapbender/application



Anpassen der Konfigurationsdatei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Parameter der Datenbankverbindung sind zusammen mit einigen anderen Konfigurationsparametern in der Datei ``app/config/parameters.yml`` gespeichert.

Mehr Informationen dazu finden Sie im Kapitel : :ref:`yaml_de`.

    
Erzeugen der Datenbank
^^^^^^^^^^^^^^^^^^^^^^ 

Mit Symfony kann die Datenbank erzeugt werden. Beachten Sie, dass dazu die benötigten Datenbank-Benutzerrechte vorliegen. Rufen Sie folgenden Befehl mit dem console-Hilfsprogramm auf:

.. code-block:: yaml

   app/console doctrine:database:create


Erzeugen des Datenbankschemas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Erzeugen des Datenbankschemas über Symfony:

.. code-block:: yaml

    app/console doctrine:schema:create

    
Kopieren des Asset Bundles
^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Jedes Bundle hat seine eigenen Abhängigkeiten - CSS-Dateien, JavaScript-Dateien, Bilder und mehr – diese müssen in das öffentliche web-Verzeichnis kopiert werden:

.. code-block:: yaml

    app/console assets:install web


Sie können auch einen symbolischen Link verwenden, statt die Dateien zu kopieren.  Dies erleichtert die Bearbeitung der abhängigen Dateien in den bundle-Verzeichnissen.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Erzeugen des administrativen Benutzers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Der erste Benutzer, der alle Privilegien hat, wird mit folgendem Kommando erzeugt:

.. code-block:: yaml

    app/console fom:user:resetroot

Dieses Kommando wird interaktiv alle notwendigen Informationen abfragen und den Benutzer in der Datenbank erzeugen.

Sie können auch den Modus "silent" verwenden, wenn Sie ein Skript nutzen möchten, um Mapbender zu installieren und dabei nicht nach Parametern gefragt werden wollen.

.. code-block:: yaml

    app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent


Initialisieren der Datenbank
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Führen Sie das nachfolgende Kommando aus, um die Datenbank zu initialisieren und startbereit zu machen:

.. code-block:: yaml

    app/console mapbender:database:init


Importieren von Anwendungen aus application/app/config/applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Sie können die Anwendungen, die in dem Ordner applications definiert sind, in die Datenbank importieren:

.. code-block:: yaml

    bin/composer run reimport-example-apps


Konfigurationsdateien
---------------------

Die Konfiguratuionsdateien liegen unter **app/config**. 

Mehr Informationen dazu finden Sie im Kapitel : :ref:`yaml_de`.


Produktions- und Entwicklerumgebung und Caches: app.php und app_dev.php
-----------------------------------------------------------------------

Mapbender bietet zwei Umgebungen an: eine Produktionsumgebung für den
normalen Betrieb- und eine Entwicklerumgebung, in dem die Anwendungen
getestet werden können. Dieses Konzept orientiert sich an den
`"Environments" im Symfony Framework
<http://symfony.com/doc/current/book/configuration.html>`_.

Die Produktionsumgebung wird mit der URL http://localhost/app.php
aufgerufen, die Entwicklungsumgebung mit der URL
http://localhost/app_dev.php. Der Aufruf über app_dev.php kann
und sollte nur vom localhost erfolgen.

Es gibt Unterschiede im Verhalten von app.php und app_dev.php:

* Der Cache-Mechanismus verhält sich in der Entwicklungsumgebung anders: Es
  werden nicht alle Dateien gecacht, so dass vorgenommene Änderungen direkt
  sichtbar sind. Dadurch ist der Aufruf einer Anwendung über app_dev.php
  immer langsamer als im Produktivbetrieb.

  Im Detail werden in der Entwicklerumgebung von Mapbender u.a. die CSS,
  JavaScript und Übersetzungsdateien nicht gecacht.

  In der Produktionsumgebung werden diese aber in app/cache abgelegt.

* In der Entwicklerumgebung werden Fehlermeldungen und ihr Stacktrace direkt
  an der Oberfläche angezeigt. In der Produktionsumgebung werden die
  Fehlermeldungen in die Datei app/log/prod.log geschrieben.

* Die Entwicklungsumgebung zeigt den Symfony Profiler an. Dort werden Dinge
  protokolliert, die nur für die Entwickler, aber nicht für Außenstehende
  sichtbar sein sollten.

Das Verzeichnis app/cache enthält die einzelnen Cache-Dateien. Es werden
Verzeichnisse für jede Umgebung (prod und dev) angelegt, das Verhalten des
dev-Caches ist aber, wie angesprochen, anders.

Bei Änderungen an der Oberfläche oder im Code von Mapbender ist das Cache
Verzeichnis (app/cache) zu leeren, damit die Änderungen in der
Produktionsumgebung sichtbar werden.

