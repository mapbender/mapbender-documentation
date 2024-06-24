.. _installation_configuration_de:

Details zur Konfiguration von Mapbender
=======================================

Konfigurationsschritte
----------------------

Im Folgenden werden die für die Mapbender-Installation aufgeführten Konfigurationsschritte von Mapbender näher erläutert. Es sind sechs Schritte notwendig:

* Erzeugen der Datenbank
* Erzeugen der Datenbankschemas
* Kopieren des bundle Assets in das öffentlich zugängliche public-Verzeichnis
* Erzeugen des "root" Benutzers
* Initialisieren der Datenbank
* Laden der Demo-Anwendungen in die Datenbank

Diese Schritte werden mit dem console-Hilfsprogramm des `Symfony <https://symfony.com/>`_ Frameworks durchgeführt, auf dem Mapbender aufbaut. Hier noch einige wichtige Hinweise, bevor Sie fortfahren: 

.. note:: **Hinweis:** Das console-Hilfsprogramm wird Dateien in die Verzeichnisse var/cache und var/log schreiben. Für diese Operationen werden die Benutzerrechte des Benutzers benötigt, mit dem Sie angemeldet sind. Sie benötigen ebenfalls Benutzerrechte für das Verzeichnis var/db und die SQLite Datenbank. Wenn Sie die Applikation in Ihrem Browser öffnen, wird die SQLite-Datenbank mit Server-PHP-Prozess versuchen, auf diese Dateien zuzugreifen oder in die Verzeichnisse mit anderen Benutzerrechten zu schreiben. Stellen Sie sicher, dass Sie den Verzeichnissen und Dateien Schreib- und Leserechte zugewiesen haben. 

.. note:: **Wichtiger Hinweis:** Die folgenden bin/console Schritte gehen davon aus, dass Sie sich oberhalb des app-Verzeichnisses befinden (für die git-Installation bedeutet das mapbender/application/ , andernfalls mapbender/).

.. code-block:: yaml

   cd mapbender/
   oder für die git-basierte Installation 
   cd mapbender/application


Anpassen der Konfigurationsdatei
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die Parameter der Datenbankverbindung sind in der Datei .env.local gespeichert. Weitere Konfigurationsparameter finden sich in der Datei ``application/config/parameters.yaml`` und anderen Dateien im config-Verzeichnis.

Mehr Informationen dazu finden Sie im Kapitel : :ref:`yaml_de`.

    
Erzeugen der Datenbank
^^^^^^^^^^^^^^^^^^^^^^

.. hint:: Generell wird empfohlen, das Erzeugen der Datenbanken extern, etwa über ein graphisches Datenbank-Werkzeug wie bspw. `pgAdmin <https://www.pgadmin.org/>`_ vorzunehmen.

Alternativ kann die Datenbank mit Symfony erzeugt werden. Beachten Sie, dass dazu die benötigten Datenbank-Benutzerrechte vorliegen müssen.

Rufen Sie dazu folgenden Befehl mit dem console-Hilfsprogramm auf:

.. code-block:: yaml

   bin/console doctrine:database:create


Erzeugen des Datenbankschemas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Erzeugen des Datenbankschemas über Symfony:

.. code-block:: yaml

    bin/console doctrine:schema:create

    
Kopieren des Asset Bundles
^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedes Bundle hat seine eigenen Abhängigkeiten - CSS-Dateien, JavaScript-Dateien, Bilder und mehr – diese müssen in das öffentliche public-Verzeichnis kopiert werden:

.. code-block:: yaml

    bin/console assets:install public


Sie können auch einen symbolischen Link verwenden, statt die Dateien zu kopieren.  Dies erleichtert die Bearbeitung der abhängigen Dateien in den bundle-Verzeichnissen.

.. code-block:: yaml

   bin/console assets:install public --symlink --relative


Erzeugen des administrativen Benutzers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Der erste Benutzer, der alle Privilegien hat, wird mit folgendem Kommando erzeugt:

.. code-block:: yaml

    bin/console fom:user:resetroot

Dieses Kommando wird interaktiv alle notwendigen Informationen abfragen und den Benutzer in der Datenbank erzeugen.

Sie können auch den Modus "silent" verwenden, wenn Sie ein Skript nutzen möchten, um Mapbender zu installieren und dabei nicht nach Parametern gefragt werden wollen.

.. code-block:: yaml

    bin/console fom:user:resetroot --username="root" --password="root" --email="root@example.com" --silent


Initialisieren der Datenbank
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Führen Sie das nachfolgende Kommando aus, um die Datenbank zu initialisieren und startbereit zu machen:

.. code-block:: yaml

    bin/console mapbender:database:init


Importieren von Anwendungen aus application/config/applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Sie können die Anwendungen, die in dem Ordner applications definiert sind, in die Datenbank importieren:

.. code-block:: yaml

    bin/composer run reimport-example-apps


Konfigurationsdateien
---------------------

Die Konfigurationsdateien liegen unter ``application/config``. 

Mehr Informationen dazu finden Sie im Kapitel: :ref:`yaml_de`.

Außerdem die Datei env.local und .env im Verzeichnis application.


Produktions- und Entwicklungsumgebung und Caches
------------------------------------------------

Mapbender bietet zwei Umgebungen an: eine Produktionsumgebung für den
normalen Betrieb und eine Entwicklungsumgebung, in dem die Anwendungen
getestet werden können. Dieses Konzept orientiert sich an den
`"Environments" im Symfony Framework
<https://symfony.com/doc/current/book/configuration.html>`_.

Die Produktionsumgebung wird mit der URL http://localhost/index.php
aufgerufen, die Entwicklungsumgebung mit der URL
http://localhost/index_dev.php. Der Aufruf über index_dev.php kann
und sollte nur vom localhost erfolgen.
Sie können die Datei index_dev.php anpassen und IP-Adressen hinzufügen, so dass auch von diesen Adressen der Entwicklungsmodus erreicbar ist.

Es gibt Unterschiede im Verhalten von index.php und index_dev.php:

* Der Cache-Mechanismus verhält sich in der Entwicklungsumgebung anders: Es
  werden nicht alle Dateien gecacht, so dass vorgenommene Änderungen direkt
  sichtbar sind. Dadurch ist der Aufruf einer Anwendung über index_dev.php
  immer langsamer als im Produktivbetrieb.

  Im Detail werden in der Entwicklungsumgebung von Mapbender u.a. die CSS,
  JavaScript und Übersetzungsdateien nicht gecacht.

  In der Produktionsumgebung werden diese aber in var/cache abgelegt.

* In der Entwicklungsumgebung werden Fehlermeldungen und ihr Stacktrace direkt
  an der Oberfläche angezeigt. In der Produktionsumgebung werden die
  Fehlermeldungen in die Datei var/log/prod.log geschrieben.

* Die Entwicklungsumgebung zeigt den Symfony Profiler an. Dort werden Dinge
  protokolliert, die nur für die Entwickler, aber nicht für Außenstehende
  sichtbar sein sollten.

Das Verzeichnis var/cache enthält die einzelnen Cache-Dateien. Es werden
Verzeichnisse für jede Umgebung (prod und dev) angelegt, das Verhalten des
dev-Caches ist aber, wie angesprochen, anders.

Eine Umgebung kann über die Variable ``APP_ENV`` explizit festgelegt werden. Stellen Sie sicher, dass Sie dies auf `prod` ändern, wenn Sie Ihre Anwendung für die Öffentlichkeit bereitstellen. Der Wert kann auf verschiedene Arten geändert werden:

* durch Bearbeiten der ``APP_ENV``-Variable in der `.env`-Datei,
* durch Überschreiben des Werts in einer `.env.local`-Datei,
* durch Festlegen einer Umgebungsvariable in Ihrer Apache2-vHost-Konfiguration: ``SetEnv APP_ENV prod``,
* durch explizites Festlegen beim Starten des lokalen Webservers:

.. code-block:: bash

    APP_ENV=prod symfony server:start --no-tls
