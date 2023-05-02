.. _faq_de:

FAQ - Häufig gestellte Fragen
=============================

Allgemein
---------

Dienste und in welchen Anwendungen sie genutzt werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich würde gerne wissen, in welchen Anwendungen ein bestimmter WMS Dienst eingebaut ist. Gibt es einen Weg das herauszufinden?

A: Die Information ist über die Web-Administration im Bereich der Datenquellen verfügbar.

* Gehen Sie im oberen Menü zu Datenquellen
* Wählen Sie per Klick auf den Button Show Metadata eine Datenquelle aus und Klicken anschließend den Link Anwendungen
* Unter Anwendungen sehen Sie, in welchen Anwendungen sich der Dienst befindet
* Sie sehen, ob der Dienst als freie Instance oder private Instanz eingebunden wurde und ob der Dienst aktiviert oder deaktiviert ist
* Per Klick auf die den Anwendungs- oder den Datenquellentitel gelangen Sie bequem zur Konfiguratoin der Anwendung bzw. der Instanz

Wenn Sie SQL bevorzugen, können Sie die WMS-ID der Datenquelle im folgenden SQL unter ``<id_of_the_wms>`` eintragen und das SQL ausführen:

.. code-block:: postgres

                SELECT mb_core_application.* from mb_core_application, mb_core_layerset, mb_core_sourceinstance, mb_wms_wmsinstance, mb_wms_wmssource, mb_c           where
                -- applications and their layersets
                mb_core_application.id = mb_core_layerset.application_id and
                -- layersets and their instances
                mb_core_layerset.id = mb_core_sourceinstance.layerset and
                -- layerset-instances and wms-instance
        ore_source
             mb_core_sourceinstance.id = mb_wms_wmsinstance.id and
                -- wms-instance and wms-source
                mb_wms_wmsinstance.wmssource = mb_wms_wmssource.id and
                -- wms-source and mb3-core source
                mb_wms_wmssource.id = mb_core_source.id and
                mb_core_source.id = <id_of_the_wms>;


app.php und app_dev.php: Wozu sind diese da?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Siehe die `Details zur Konfiguration von Mapbender <installation/configuration.html>`_, im Kapitel `Produktions- und Enwicklungsumgebung und Caches: app.php und app_dev.php <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_.

Im produktiven Einsatz rufen Sie Mapbender über die app.php-Datei auf. 
Erst wenn Sie selbst etwas entwickeln (an den Twig-Dateien, CSS oder JS-Dateien) oder 
zu Debugzwecken, nutzen Sie den Aufruf über die app_dev.php-Datei.
Der Entwicklermodus gibt mehr informationen aus und zeigt ausführliche Fehlermeldungen. 


Was ist der Cache und wann muss ich ihn löschen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auch für diese Frage, siehe die `Details zur Konfiguration von Mapbender <installation/configuration.html>`_, im Kapitel `Produktions- und Entwicklungsumgebung und Caches: app.php und app_dev.php <installation/configuration.html#produktions-und-entwicklerumgebung-und-caches-app-php-und-app-dev-php>`_.

Sie löschen die Inhalte vom ``mapbender/app/cache/`` Ordner, nicht den cache-Ordner selbst. Also das ``prod``- und - falls vorhanden - das ``dev``-Verzeichnis. Die zwei Verzeichnisse können ohne Bedenken gelöscht werden. 
Beim nächsten Aufruf von Mapbedner werden im Cache erneut Dateien abgelegt.


Performance
-----------

Arbeiten mit WMS-Diensten mit zahlreichen Layern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Beim Laden von WMS mit vielen Layern (mehr als 100 Layer) in eine Anwendung werden in der Konfiguration der `Layerset-Instance <functions/backend/layerset.html>`_  nur Teile der Layer übernommen und angezeigt. Die WMS-Instance kann auch nicht abgespeichert werden. Warum?

A: Mittels des PHP-Parameters `max-input_vars <http://php.net/manual/de/info.configuration.php#ini.max-input-vars>`_ kann die Zahl der Eingabe-Variablen erhöht werden. 
Der Standardwert liegt bei 1000. 
Die Zahl der Eingabe Variablen ist bei einem WMS mit vielen Layern sehr hoch, vergleichbar mit der Anzahl der Auswahlmöglichkeiten innerhalb des WMS-Instance Dialogs. 
Setzen Sie in dem Fall den Parameter hoch, beispielsweise auf 2000. Die Zahl hängt direkt mit der Anzahl der Layer im WMS zusammen.

.. code-block:: ini

   ;; 1000 (default)
   max_input_vars = 1000


Maximale WMS-Kachelgröße für Druck und Export anpassen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Wenn ich eine Karte mit einem WMS-Dienst als Bild exportieren oder drucken möchte, erscheint der Dienst anschließend nicht in meiner Datei.

A: Dies kann verschiedene Gründe haben. Unter bestimmten Umständen kann die angeforderte Pixelabmessung eines WMS zu groß sein, sodass der Dienst in diesem Fall keine Bilder mehr liefert.

In diesem Fall fügen Sie zu Ihrer ``parameters.yml`` den ``mapbender.imaageexport.renderer.wms.max_getmap_size`` (Standard: 8192) Parameter hinzu. Durch diesen werden die größtmöglichen ``WIDTH=``- und ``HEIGHT=``-Werte für WMS-Druck/Export-Anfragen festgelegt. Im GetCapabilities-Request des jeweiligen Dienstes wird die maximale Auflösung unter ``MaxWidth`` bzw. ``MaxHeight`` definiert, sodass der der GetCapabilities-Request den einzutragenen Wert bereits vorgibt.

Die ``WIDTH=``- und ``HEIGHT=``-Parameter können auch unabhängig voneinander definiert werden. Verwenden Sie ``mapbender.imaageexport.renderer.wms.max_getmap_size.x`` für den ``WIDTH=``- und ``mapbender.imaageexport.renderer.wms.max_getmap_size.y`` für den ``HEIGHT=``-Parameter.


Meine Anwendung kann nicht kopiert werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich habe eine komplexe Anwendung und möchte sie kopieren. Das schlägt fehl.

A: Eine mögliche Ursache ist, dass PHP nicht das Arbeiten mit großen Dateien (YAML-Export/Import, etc.) erlaubt. Das tritt v.a. bei Fast-CGI auf. Dafür dient der PHP Parameter MaxRequestLen, den Sie in der Konfiguration von FCGI anpassen können.

.. code-block:: bash

   # mod_fcgi.conf (Windows)
   # set value to 2 MB
   MaxRequestLen = 2000000
   
   # fcgid.conf (Linux)
   # set value to 2 MB
   MaxRequestLen 2000000


Analog dazu können Sie die PHP-Werte in der php.ini überprüfen:

.. code-block:: bash

   max_execution_time = 240
   memory_limit = 1024M
   upload_max_filesize = 2M


Entwicklung und manuelle Updates von Modulen
--------------------------------------------

F: Wie kann ich einen speziellen Branch des Mapbender Moduls auschecken und testen? Wie bekomme ich das wieder rückgängig? Hilft mir Composer dabei?

A: Möglichkeit 1: In das Verzeichnis application/mapbender gehen und den speziellen Branch auschecken. Danach wieder den aktuellen Branch auschecken. Leeren Sie das Cache Verzeichnis zwischendurch (app/cache für Symfony 2, var/cache für das kommende Symfony 3))

Möglichkeit 2: Im Composer: "mapbender/mapbender": "dev-fix/meinfix" eintragen und ein Composer Update ausführen. Dabei werden aber auch alle anderen Vendor-Pakete aktualisiert (für Developer ist das OK). Rückgängig wieder mit der Angabe des vorherigen Branches. Dazu nochmal in appliaction/mapbender gehen und den Branch mit der Hand auschecken.


Installation
------------

Attempted to call function "imagecreatefrompng"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme einen Fehler beim Drucken. Ich habe in das Log geschaut (app/logs/prod.log) und da steht so ungefähr folgendes drin.

.. code-block:: php

                CRITICAL - Uncaught PHP Exception Symfony\Component\Debug\Exception\UndefinedFunctionException:
                "Attempted to call function "imagecreatefrompng"
                from namespace "Mapbender\PrintBundle\Component"."
                at /srv/mapbender-starter/application/mapbender/src/Mapbender/PrintBundle/Component/PrintService.php line 310

A: Bitte stellen Sie sicher, dass Sie die php-gd Bibliothek installiert haben.


Deprecation Notices bei composer oder bootstrap Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme beim Ausführen von bootstrap bzw. von composer Update eine Deprecation Warnung:

.. code-block:: php
                
                Deprecation Notice: The callback ComposerBootstrap::checkConfiguration declared at
                /srv//mapbender-starter/application/src/ComposerBootstrap.php accepts a Composer\Script\CommandEvent
                but post-update-cmd events use a Composer\Script\Event instance.
                Please adjust your type hint accordingly, see https://getcomposer.org/doc/articles/scripts.md#event-classes
                in phar:///srv/mapbender-starter/composer.phar/src/Composer/EventDispatcher/EventDispatcher.php:290

A: Das ist abhängig von der PHP Version, auf der Sie diese Kommandos aufrufen und taucht bei PHP Versionen < 7 auf.


SSL-Zertifikatsfehler
~~~~~~~~~~~~~~~~~~~~~

F: Wie kann ein SSL-Zertifikatsfehler behoben werden?

A: Wenn beim Laden oder Aktualisieren einer OGC WMS-Datenquelle auf Windows-basierten Mapbender-Servern ein SSL-Zertifikatsproblem auftritt, müssen Sie die Datei ``cacert.pem`` aktualisieren und in Ihrer ``php.ini`` auf die Datei verweisen.

Das Problem kann beim Zugriff auf einen Dienst über https auftreten. Der Fehler sieht wie folgt aus:

.. code-block:: bash

    cURL error 60: SSL certificate problem: unable to get local issuer certificate


.. note:: Es gibt eine Datei ``cacert.pem``, die alle vertrauenswürdigen Zertifizierungsstellen auflistet. ``cacert.pem`` ist eine base64-kodierte Textdatei mit einer Definition aller vertrauenswürdigen Zertifizierungsstellen. Sie können die Datei unter https://curl.haxx.se/docs/caextract.html herunterladen.

Der Fehler tritt auf, wenn die Datei nicht in der ``php.ini`` referenziert oder die ``cacert.pem`` nicht aktuell ist.

Verweisen Sie auf ``cacert.pem`` in der ``php.ini``, um das Problem zu beheben:

.. code-block:: bash

    curl.cainfo="C:\[Ihr Pfad]\cacert.pem"

    openssl.cafile="C:\[Ihr Pfad]\cacert.pem"


Weitere Informationen finden Sie in der PHP-Dokumentation unter: https://www.php.net/manual/en/curl.configuration.php

Wenn Sie ein individuelles, selbstsigniertes Zertifikat verwenden, können Sie die Informationen Ihrer Zertifizierungsstelle in der Datei ``cacert.pem`` hinzufügen. 


Oracle
------

Einstellungen für die Oracle Datenbank - Punkt und Komma
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich bekomme bei Oracle einen Fehler, wenn ich doctrine:schema:create ausführe. Warum? Hier ist meine Fehlermeldung:

.. code-block:: bash

                [Doctrine\DBAL\Exception\DriverException]
                An exception occurred while executing
                'CREATE TABLE mb_wms_wmsinstance (id NUMBER(10) NOT NULL,
                                                  [...]
                                                  PRIMARY KEY(id))':
                ORA-01722: Ungültige Zahl

A: Wahrscheinlich kommt Oracle nicht mit den Dezimaltrennern zurecht und erwartet ein Komma statt einem Punkt (also 1,25 statt 1.25). Das Einsetzen des nachfolgenden Statements am Ende der config.yml verhindert dies (Cache danach leeren):

.. code-block:: yaml

                services:
                  oracle.session.listener:
                    class: Doctrine\DBAL\Event\Listeners\OracleSessionInit
                    tags:
                      - { name: doctrine.event_listener, event: postConnect }

Es handelt sich dabei um die Verknüpfung zu einer Service-Klasse, die von Doctrine bereitgestellt wird. Die setzt nach der Verbindung zur Datenbank Session-Variablen (ALTER SESSION), so dass PHP und Oracle zusammenarbeiten können.

Ursachen können sein: Ländereinstellungen des Betriebssystems sein (z.B. Windows), Einstellungen des Oracle-Clients, Einstellungen während der Installation von Oracle.

Mehr Informationen auf der Doctrine Seite: `http://www.doctrine-project.org/api/dbal/2.0/class-Doctrine.DBAL.Event.Listeners.OracleSessionInit.html <http://www.doctrine-project.org/api/dbal/2.0/class-Doctrine.DBAL.Event.Listeners.OracleSessionInit.html>`_


Welche Rechte benötigt der Mapbender User auf der Oracle-Datenbank?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create Sequence
- Create Session
- Create Table
- Create Trigger
- Create View


Der Zugriff auf Oracle-Datenbanken ist langsam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Beim Zugriff auf Oracle-Datenbanken reagiert Mapbender teilweise recht langsam, Abfragen dauern länger als gewöhnlich. Was kann ich anpassen?

A: Es gibt zwei Parameter in der php.ini, mit der die Zugriffe auf die Oracle Datenbanken verbessert werden können: `oci8.max_persistent <http://php.net/manual/de/oci8.configuration.php#ini.oci8.max-persistent>`_ und `oci8.default_prefetch <http://php.net/manual/de/oci8.configuration.php#ini.oci8.default-prefetch>`_. Passen Sie diese an.

.. code-block:: bash

   oci8.max_persistent = 15
   oci8.default_prefetch = 100000


Des weiteren stellen Sie in der config.yml in der jeweiligen Datenbank-Verbindung den persistent Parameter auf true.

.. code-block:: bash

   persistent=true

