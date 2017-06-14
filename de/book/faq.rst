FAQ - Häufig gestellte Fragen
=============================

Allgemein
---------

Dienste und in welchen Anwendungen sie genutzt werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich würde gerne wissen, in welchen Anwendungen ein bestimmter WMS Dienst eingebaut ist. Gibt es einen Weg das herauszufinden?

A: Bis wir die Information an der Oberfläche anbieten, hilft Ihnen folgendes SQL Statement:

.. code-block:: sql

                SELECT mb_core_application.* from mb_core_application, mb_core_layerset, mb_core_sourceinstance, mb_wms_wmsinstance, mb_wms_wmssource, mb_core_source
                where
                -- Anwendungen und ihre Layersets
                mb_core_application.id = mb_core_layerset.application_id and
                -- Layersets und ihre Instanzen
                mb_core_layerset.id = mb_core_sourceinstance.layerset and
                -- Layerset-Instanzen und die WMS-Instanz
                mb_core_sourceinstance.id = mb_wms_wmsinstance.id and
                -- WMS-Instanz und WMS-Source
                mb_wms_wmsinstance.wmssource = mb_wms_wmssource.id and
                -- WMS-Source und MB3-Core Source
                mb_wms_wmssource.id = mb_core_source.id and
                mb_core_source.id = <id_of_the_wms>;


Als ID <id_of_the_wms> geben Sie die Nummer ein, die auf der Seite der Datenquellen dem jeweiligen WMS zugeordnet ist.



Performance
-----------

Arbeiten mit größeren WMS Diensten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Beim Laden von größeren WMS (z.B. mehr als 100 Layer) in eine Anwendung werden in der Konfiguration der `Layerset-Instance <../de/bundles/Mapbender/CoreBundle/entities/layerset.html>`_  nur Teile der Layer übernommen und angezeigt. Die WMS Instance kann auch nicht abgespeichert werden. Warum?

A: Mittels des PHP-Parameters `max-input_vars <http://php.net/manual/de/info.configuration.php#ini.max-input-vars>`_ kann die Zahl der Eingabe Variablen erhöht werden. Der Standardwert liegt (je nach PHP Version) bei 1000. Die Zahl der Eingabe Variablen ist bei einem WMS mit vielen Layern sehr hoch, vergleichbar mit der Anzahl der Auswahlmöglichkeiten innerhalb des WMS-Instance Dialogs. Setzen Sie in dem Fall den Parameter hoch, beispielsweise auf 2000. Die Zahl hängt direkt mit der Anzahl der Layer im WMS zusammen.

.. code-block:: ini

   ;; 1000 (default) oder höher
   max_input_vars = 1000 



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


Meine Anwendung kann nicht kopiert werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich habe eine komplexe Anwendung und möchte Sie kopieren. Das schlägt fehl.


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

A: Bitte stellen Sie sicher, dass Sie die php5-gd Bibliothek installiert haben.


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
