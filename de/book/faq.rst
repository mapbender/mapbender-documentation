FAQ - Häufig gestellte Fragen
=============================

Allgemein
---------

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

.. code-block:: ini

   oci8.max_persistent = 15
   oci8.default_prefetch = 100000


Des weiteren stellen Sie in der config.yml in der jeweiligen Datenbank-Verbindung den persistent Parameter auf true.

.. code-block:: yaml

   persistent=true


Meine Anwendung kann nicht kopiert werden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

F: Ich habe eine komplexe Anwendung und möchte Sie kopieren. Das schlägt fehl.


A: Eine mögliche Ursache ist, dass PHP nicht das Arbeiten mit großen Dateien (YAML-Export/Import, etc.) erlaubt. Das tritt v.a. bei Fast-CGI auf. Dafür dient der PHP Parameter MaxRequestLen, den Sie in der Konfiguration von FCGI anpassen können.

.. code-block:: ini

   # mod_fcgi.conf (Windows)
   # set value to 2 MB
   MaxRequestLen = 2000000
   
   # fcgid.conf (Linux)
   # set value to 2 MB
   MaxRequestLen 2000000


Analog dazu können Sie die PHP-Werte in der php.ini überprüfen:

.. code-block:: ini

   max_execution_time = 240
   memory_limit = 1024M
   upload_max_filesize = 2M
