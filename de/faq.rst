.. _faq_de:

FAQ - Häufig gestellte Fragen
=============================

Allgemeines
-----------

Umgebungen: `prod` und `dev`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Wozu sind diese Umgebungen da?

A: Für den produktiven Einsatz rufen Sie Mapbender über die `prod`-Umgebung auf. Erst wenn Sie selbst etwas (an den Twig-, CSS- oder JS-Dateien) entwickeln, nutzen Sie den Aufruf über die `dev`-Umgebung. Der dahinterstehende Entwicklungsmodus gibt mehr Informationen aus, indem er z. B. detailliertere Fehlermeldungen anzeigt. 

Mehr Details zu den Umgebungen gibt es im Kapitel :ref:`de/quickstart:Starten von Mapbender als Produktivumgebung`.


Cache
~~~~~

F: Was ist der Cache und wann muss ich ihn löschen?

A: Der Cache ist ein Zwischenspeicher, aus dem Mapbender auf häufig benutzte Dateien zugreift. Der Cache kann ohne Weiteres gelöscht werden. Sie löschen dabei jedoch nur die Inhalte innerhalb des ``mapbender/var/cache/`` Ordners. In der Mapbender-Verzeichnisstruktur sind das das ``prod``- und - falls vorhanden - das ``dev``-Verzeichnis.

Diese zwei Verzeichnisse können ohne Bedenken gelöscht werden. Beim nächsten Aufruf von Mapbender werden im Cache der entsprechenden Umgebung erneut Dateien abgelegt.

Mehr Details zum Cache gibt es im Kapitel :ref:`de/installation/installation_configuration:Produktions- und Entwicklungsumgebung und Caches`.


Dienste in Anwendungen
~~~~~~~~~~~~~~~~~~~~~~

F: In welchen meiner Anwendungen ist ein bestimmter WMS-Dienst eingebaut?

A: Diese Information ist für angemeldete Nutzer mit entsprechenden Berechtigungen über das :ref:`backend_de` im Bereich :ref:`sources_de` verfügbar:

* Gehen Sie im oberen Menü zu Datenquellen,
* Wählen Sie per Klick auf den Button ``Metadaten anzeigen`` eine Datenquelle aus und klicken anschließend auf den Reiter ``Anwendungen``,
* Hier sehen Sie, in welchen Anwendungen sich der Dienst befindet. Zusätzlich gibt der Reiter über ein entsprechendes Symbol Informationen darüber aus, ob der Dienst als freie oder private Instanz eingebunden wurde und ob die Datenquelle aktiviert oder deaktiviert ist.
* Per Klick auf den Anwendungs- oder Datenquellentitel gelangen Sie bequem zur Konfiguration der Layersets bzw. der Dienst-Instanz.

Wenn Sie SQL bevorzugen, können Sie die WMS-ID der Datenquelle im folgenden SQL unter ``<id_of_the_wms>`` eintragen und die Abfrage ausführen, um sich die auf den Dienst zugreifenden Anwendungen tabellarisch anzeigen zu lassen:

.. code-block:: postgres

                SELECT mb_core_application.* from mb_core_application, mb_core_layerset, mb_core_sourceinstance, mb_wms_wmsinstance, mb_wms_wmssource, mb_core_source where
                -- applications and their layersets
                mb_core_application.id = mb_core_layerset.application_id and
                -- layersets and their instances
                mb_core_layerset.id = mb_core_sourceinstance.layerset and
                -- layerset-instances and wms-instance      
                mb_core_sourceinstance.id = mb_wms_wmsinstance.id and
                -- wms-instance and wms-source
                mb_wms_wmsinstance.wmssource = mb_wms_wmssource.id and
                -- wms-source and mb-core source
                mb_wms_wmssource.id = mb_core_source.id and
                mb_core_source.id = <id_of_the_wms>;


Performance
-----------

Fehlermeldung beim Kopieren von Anwendungen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich habe eine komplexe Anwendung, die ich kopieren möchte, was aber fehlschlägt. Woran liegt das?

A: Eine mögliche Ursache kann sein, dass PHP das Arbeiten mit großen Dateien nicht erlaubt. Das tritt vor allem bei FastCGI auf. Dafür dient der Parameter ``MaxRequestLen``, den Sie in der FastCGI-Konfigurationsdatei anpassen können.

.. code-block:: bash

   # mod_fcgi.conf (Windows)
   # set value to 2 MB
   MaxRequestLen = 2000000
   
   # fcgid.conf (Linux)
   # set value to 2 MB
   MaxRequestLen 2000000


Analog dazu können Sie die Werte in der ``php.ini`` Datei überprüfen:

.. code-block:: bash

   max_execution_time = 240
   memory_limit = 1024M
   upload_max_filesize = 2M
   

Maximale WMS-Kachelgröße für Druck und Export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Wenn ich eine Karte mit einem WMS-Dienst als Bild exportieren oder drucken möchte, erscheint der Dienst anschließend nicht in meiner Datei. Woran kann das liegen?

A: Dies kann verschiedene Gründe haben. Unter bestimmten Umständen kann die angeforderte Pixelausdehnung für den WMS zu groß sein, sodass der Dienst in diesem Fall keine Bilder mehr liefert.

In diesem Fall fügen Sie zu Ihrer ``parameters.yaml`` folgenden Parameter hinzu, wobei der hier eingetragene Standardwert dem Dienst entsprechend konfiguriert werden kann:

.. code-block:: bash

   mapbender.imaageexport.renderer.wms.max_getmap_size: 8192
   
Durch diesen werden die größtmöglichen ``WIDTH=``- und ``HEIGHT=``-Werte für WMS-Druck/Export-Anfragen festgelegt. Im GetCapabilities-Request des jeweiligen Dienstes wird die maximale Auflösung unter ``MaxWidth`` bzw. ``MaxHeight`` definiert, sodass der getCapabilities-Request das Limit bereits vorgibt. Die Parameter können auch unabhängig voneinander definiert werden:

Weisen Sie zur Veränderung der Breite diesem Parameter ihnen einen Wert zu:

.. code-block:: bash

   mapbender.imaageexport.renderer.wms.max_getmap_size.x:


Weisen Sie zur Veränderung der Höhe diesem Parameter einen Wert zu:

.. code-block:: bash

   mapbender.imaageexport.renderer.wms.max_getmap_size.y:


Problem bei WMS-Diensten mit vielen Layern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Beim Laden eines WMS mit vielen Layern (über 100) in eine Anwendung werden in der :ref:`layerset`-Konfiguration nur Teile der Layer übernommen und angezeigt. Die WMS-Instance kann außerdem nicht abgespeichert werden. Gibt es einen Weg, den WMS dennoch zu verwenden?

A: Mittels des PHP-Parameters `max-input_vars <https://php.net/manual/de/info.configuration.php#ini.max-input-vars>`_ kann die Zahl der Eingabe-Variablen erhöht werden. Der Standardwert liegt bei 1000. 
Die Zahl der Eingabe-Variablen ist bei einem WMS mit vielen Layern sehr hoch, vergleichbar mit der Anzahl der Auswahlmöglichkeiten innerhalb des WMS-Instance-Dialogs. Setzen Sie bei der Arbeit mit großen WMS mit vielen Layern den Parameter hoch, beispielsweise auf 2000. Die Zahl hängt direkt mit der Anzahl der Layer im WMS zusammen.

.. code-block:: ini

   ;; 1000 (default)
   max_input_vars = 1000


Installation
------------

Fehlermeldung beim Drucken
~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme einen Fehler beim Drucken. Das Log (var/log/prod.log) wirft folgende Fehlermeldung:

.. code-block:: php

                CRITICAL - Uncaught PHP Exception Symfony\Component\Debug\Exception\UndefinedFunctionException:
                "Attempted to call function "imagecreatefrompng"
                from namespace "Mapbender\PrintBundle\Component"."
                at /srv/mapbender-starter/application/mapbender/src/Mapbender/PrintBundle/Component/PrintService.php line 310

A: Bitte stellen Sie sicher, dass Sie die php-gd-Bibliothek installiert haben. Wir empfehlen, die Extension bereits vor dem Download von Mapbender zu installieren.
Auf Linux-Systemen können Sie die Erweiterung wie folgt nachinstallieren:

.. code-block:: bash

    sudo apt-get install php-gd


SSL-Zertifikatsfehler
~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme einen SSL-Zertifikatsfehler angezeigt, wie kann ich diesen beheben?

A: Das Problem kann beim Zugriff auf einen Dienst über https auftreten. Wenn beim Laden oder Aktualisieren einer OGC WMS-Datenquelle auf Windows-basierten Mapbender-Servern ein SSL-Zertifikatsproblem auftritt, müssen Sie die Datei ``cacert.pem`` aktualisieren und in Ihrer ``php.ini`` auf sie verweisen.

Der Fehler sieht wie folgt aus:

.. code-block:: bash

    cURL error 60: SSL certificate problem: unable to get local issuer certificate


.. note:: Es gibt eine ``cacert.pem`` Datei, die alle vertrauenswürdigen Zertifizierungsstellen auflistet. ``cacert.pem`` ist base64-kodiert und definiert alle vertrauenswürdigen Zertifizierungsstellen. Sie können die Datei unter https://curl.haxx.se/docs/caextract.html herunterladen.

Der Fehler tritt auf, wenn die Datei nicht in der ``php.ini`` referenziert oder die ``cacert.pem`` nicht aktuell ist.

Verweisen Sie auf ``cacert.pem`` in der ``php.ini``, um das Problem zu beheben:

.. code-block:: bash

    curl.cainfo="C:\[Ihr Pfad]\cacert.pem"

    openssl.cafile="C:\[Ihr Pfad]\cacert.pem"


Wenn Sie ein individuelles, selbstsigniertes Zertifikat verwenden, können Sie die Informationen Ihrer Zertifizierungsstelle in der Datei ``cacert.pem`` hinzufügen. 

Weitere Informationen finden Sie in der PHP-Dokumentation unter: https://www.php.net/manual/en/curl.configuration.php


Symfony Abhängigkeiten nachinstallieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Nach dem Update von Mapbender muss für meine Installation eine Symfony Komponente nachinstalliert werden. Wie erreiche ich das?

A: Es ist möglich, Symfony Komponenten über die Kommandozeile manuell nachzuinstallieren. Dies geschieht mithilfe des Befehls
 
.. code-block:: bash
   
   ./bin/composer install symfony/your-bundle


Ersetzen Sie einfach ``your-bundle`` mit dem Komponentennamen.

Im `GitHub-Symfony-Projekt <https://github.com/symfony/symfony/blob/5.4/composer.json#L58>`_ finden Sie eine entsprechende Auflistung über die Abhängigkeiten.


Warnungen im composer oder bootstrap Skript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme beim Ausführen von bootstrap bzw. von composer update eine Deprecation-Warnung:

.. code-block:: php
                
                Deprecation Notice: The callback ComposerBootstrap::checkConfiguration declared at
                /srv//mapbender-starter/application/src/ComposerBootstrap.php accepts a Composer\Script\CommandEvent
                but post-update-cmd events use a Composer\Script\Event instance.
                Please adjust your type hint accordingly, see https://getcomposer.org/doc/articles/scripts.md#event-classes
                in phar:///srv/mapbender-starter/composer.phar/src/Composer/EventDispatcher/EventDispatcher.php:290

A: Das ist abhängig von der PHP-Version, auf der Sie diese Kommandos aufrufen und taucht bei PHP Versionen < 7 auf. Je nach Mapbender-Release empfehlen wir unterschiedliche PHP-Versionen, die die Warnungen nicht auslösen.


Entwicklung
-----------

Updates von Modulen
~~~~~~~~~~~~~~~~~~~

F: Wie kann ich einen speziellen Branch des Mapbender-Moduls auschecken und testen? Wie bekomme ich das wieder rückgängig? Hilft mir Composer dabei?

A: Möglichkeit 1 (über Git): Über die Konsole in das Verzeichnis application/mapbender gehen und den gewünschten Branch auschecken. Nach dem Testen wieder den aktuellen Branch auschecken. Leeren Sie zwischendurch das Symfony-Cache-Verzeichnis.

Möglichkeit 2 (über Composer): "mapbender/mapbender": "dev-fix/meinfix" eintragen und ein Composer Update ausführen. Dabei werden aber auch alle anderen Vendor-Pakete aktualisiert. Rückgängig kann dies mit der Angabe des vorherigen Branches gemacht werden: Dazu erneut in application/mapbender gehen und den Branch auschecken.


Überschreiben von Twig-Dateien
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Wie kann ich Twig-Dateien in Bundles überschreiben und auf diese Weise das Design bestimmter Elemente anpassen?

A: Um Twig-Dateien zu überschreiben, legen Sie einfach eine Twig-Datei mit dem gleichen Namen im Verzeichnis `templates/bundles/<bundlename>` ab. Wenn Sie z.B. das Erscheinungsbild der Koordinatenanzeige anpassen möchten (zu finden unter `Resources/views/Element/coordinatesdisplay.html.twig` im Mapbender CoreBundle), erstellen Sie eine Kopie, passen diese an und legen sie unter `templates/bundles/MapbenderCoreBundle/Element/coordinatesdisplay.html.twig` ab. Diese neue Datei wird anstelle der ursprünglichen verwendet.


Oracle
------

Einstellungen für die Oracle Datenbank - Punkt und Komma
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme bei Oracle einen Fehler, wenn ich ``doctrine:schema:create`` ausführe. Warum? Hier ist meine Fehlermeldung:

.. code-block:: bash

                [Doctrine\DBAL\Exception\DriverException]
                An exception occurred while executing
                'CREATE TABLE mb_wms_wmsinstance (id NUMBER(10) NOT NULL,
                                                  [...]
                                                  PRIMARY KEY(id))':
                ORA-01722: Ungültige Zahl

A: Wahrscheinlich kommt Oracle nicht mit den Dezimaltrennern zurecht und erwartet ein Komma statt einem Punkt (also 1,25 statt 1.25). Das Einsetzen des nachfolgenden Statements am Ende der ``doctrine.yaml`` verhindert dies (Cache danach leeren):

.. code-block:: yaml

                services:
                  oracle.session.listener:
                    class: Doctrine\DBAL\Event\Listeners\OracleSessionInit
                    tags:
                      - { name: doctrine.event_listener, event: postConnect }

Es handelt sich dabei um die Verknüpfung zu einer Service-Klasse, die von Doctrine bereitgestellt wird. Die setzt nach der Verbindung zur Datenbank Session-Variablen (ALTER SESSION), sodass PHP und Oracle zusammenarbeiten können.

Ursachen können sein: Länder- und Spracheinstellungen des Betriebssystems (z. B. unter Windows), Einstellungen des Oracle-Clients, Einstellungen während der Installation von Oracle.


Rechtevergabe bei der Oracle-Datenbank
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Welche Rechte benötigt der Mapbender User auf der Oracle-Datenbank?

A: Mapbender benötigt Zugriff auf:

.. code-block:: bash

   - Create Sequence
   - Create Session
   - Create Table
   - Create Trigger
   - Create View


Langsamer Zugriff auf Oracle-Datenbanken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Beim Zugriff auf Oracle-Datenbanken reagiert Mapbender teilweise recht langsam, Abfragen dauern länger als gewöhnlich. Was kann ich anpassen?

A: Es gibt zwei Parameter in der ``php.ini``, mit der die Zugriffe auf die Oracle Datenbanken verbessert werden können: `oci8.max_persistent <http://php.net/manual/de/oci8.configuration.php#ini.oci8.max-persistent>`_ und `oci8.default_prefetch <http://php.net/manual/de/oci8.configuration.php#ini.oci8.default-prefetch>`_. Passen Sie diese an.


.. code-block:: bash

   oci8.max_persistent = 15
   oci8.default_prefetch = 100000


Des Weiteren stellen Sie in der ``doctrine.yaml`` in der jeweiligen Datenbank-Verbindung den persistent-Parameter auf true.

.. code-block:: bash

   persistent=true
