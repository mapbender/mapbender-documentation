.. _installation_git:

Git-basierte Installation
##########################


Wenn Sie sich an der Mapbender3-Entwicklung beteiligen möchten oder aus anderen Gründen die Git Repositories für Mapbender3 verwenden, folgen Sie dieser Anleitung statt des normalen Downloads. Diese Anleitung basiert auf Ubuntu 12.04.  Für andere Distributionen benötigen Sie vielleicht spezielle Pakete wie z.B. sphinx-common.

Prüfen Sie zuerst die Systemvoraussetzungen :doc:`Installation <installation>`. 

Für die Gitt-basierte Installation benötigen Sie:

* git     - schauen Sie sich das Dokument :doc:`Quick primer on using Git <development/git>` an, um mit GIt vertraut zu werde 
* cURL    - kommandozeilen basiertes Tool für die Übertragung von Daten über URL Syntax,unterstützt HTTP, HTTPS und mehr
* pear    - PHP Erweiterung und Anwendungs-Repository 
* Phing   - `Phing <http://www.phing.info/>`_ ist nicht GNU make; es ist ein  PHP Projekt Build System oder Build-Werkzeug basierend auf ​Apache Ant.
* php5-dev - Und natürlich die Dateien zur Entwicklung von PHP5-Modulen.


Klonen des Repositories
*************************

Klonen ist einfach, geben Sie das folgende Kommando auf Ihrer Shell ein:

.. code-block:: yaml

	git clone -b develop git://github.com/mapbender/mapbender-starter mapbender3

Entwickler, die Zugriff auf den Code haben möchten, müssen die SSH-URL verwenden: git@github.com:mapbender/mapbender-starter


Submodule abrufen
*****************

Die Starter-Applikation enthält nicht die Mapbender3 bundles, diese sind in einem eigenen Repository gespeichert und werden als Submodule in das Starter-Repository eingefügt. Rufen Sie das folgende Kommando im root-Verzeichnis ihres geklonten Repositories auf.

.. code-block:: yaml

    cd mapbender3
	git submodule update --init --recursive


cURL
====

Das build-System benutzt cURL, um einige Remote-Komponenten abzurufen. Dazu müssen Sie das cURL-Kommandozeilen-Werkzeug installieren:

.. code-block:: yaml

	sudo apt-get install curl

.. _phing:


Build-Management mit Phing
****************************


Das Build-Management wird mit Phing vorgenommen, welches die Pear-Bibliothek benötigt. Zunächst muss Pear installiert werden.  Hier wird ein Debian-basiertes System verwendet:


.. code-block:: yaml

    sudo apt-get install php-pear


Dann muss Pear gezeigt werden, wie ein Autodiscover seiner Repositories erzeugt wird.  Vorsichtshalber wird ein Update von Pear gemacht.


.. code-block:: yaml

    sudo pear config-set auto_discover 1
    sudo pear upgrade-all
      Enable full APC compatibility [yes] : yes
      Enable internal debugging in APCu [no] : yes 


Dann wird Phing installiert:


.. code-block:: yaml

    sudo pear channel-discover pear.phing.info 
    sudo pear install phing/phing


PHPUnit
=======

Symfony2 benötigt ein neueres PHPUnit als z.B. Ubuntu 12.04 enthält. Pear wird verwendet, um  PHPUnit zu installieren:


.. code-block:: yaml

	sudo pear install phpunit/PHPUnit

Die Build-Skripte  benötigen weitere Abhängigkeiten, um Unit-Tests durchzuführen, die Dokumentation zu generieren und die Installationspakete zu erstellen.

Daher muss zuerst der Composer installiert werden (weitere Information unter http://getcomposer.org/download/):

.. code-block:: yaml

    curl -sS https://getcomposer.org/installer | php


Erzeugen Sie eine Konfigurationsdatei mit Namen parameters.yml. Kopieren Sie dazu die Datei application/app/config/parameters.yml.dist.

.. code-block:: yaml

  cd application/app/config/
  cp parameters.yml.dist parameters.yml


And afterwards get the runtime dependencies like Symfony and Doctrine:

.. code-block:: yaml

  ./composer.phar update 



Die nächsten Schritte der Installation
**************************************

Folgen Sie nun den Schritten, die unter :doc:`Installation <installation>` beschrieben werden.:

**Hinweis:** Beachten Sie dabei, dass Mapbender3 in dem git-basierten Aufbau über eines zusätzliches Verzeichnis *application* verfügt (mapbender3/application/...). Dieses zuätzliche Verzeichnis muss bei den Befehlen beachtet werden.

* Anpassung der Konfigurationsdatei parameters.yml
* Erzeugen der Datenbank
* Erzeugen des Datenbank Schemas
* Kopieren/Verlinken der Bundle' Assets in das öffentliche web-Verzeichnis
* Initialisierung des Rollen-Systems
* Erzeugen des "root"-Benutzers
* Einfügen  der Projektions-Definitionen
* Einfügen der Anwendungen aus der mapbender.yml in die Datenbank


Referenzieren Sie auf der Verzeichnis web über einen Symbolischen Link
**********************************************************************

Als Entwickler werden Sie es bevorzugen, über einen Symbolischen Link auf das Verzeichnis web zu verweisen statt die DAteien zu kopieren. 
Dies vereinfacht das Editieren von Assets innerhalb der Bundle-Verzeichnisse.

.. code-block:: yaml

    app/console assets:install web --symlink --relative


Bitte beachten Sie, dass Sie die Option :command:`FollowSymLinks` in der Apache Directory Definition angeben müssen:


.. code-block:: yaml

  Alias /mapbender3 /var/www/mapbender3/web/
  <Directory /var/www/mapbender3/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    Order allow,deny
    Allow from all
  </Directory>


Lernen Sie mehr über app/console
********************************
Die Symfony Console Komponenten ermöglichen es, kommandozeilen basierte Befehle zu erzeugen. Doctrine verfügt beispielsweise über einige kommandozeilen basierte Befehle, die Sie verwenden können.

Lesen Sie mehr in der Symfony Dokumentation über `Console Commands <http://symfony.com/doc/current/components/console/usage.html>`_.

Hier finden Sie einige Kommandos zum Auffinden von Informationen:

.. code-block:: yaml

 app/console                        - lists all assets
 app/console help                   - Anzeige der Hilfe
 app/console help list              - Anzeige der Hilfe für einzelne Kommandos
 app/console doctrine               - Anzeige aller Funktionen von Doctrine 
 app/console mapbender              - Anzeige aller Funktionen von Mapbender
 app/console help assets:install    - Anzeige der Hilfe zu speziellen Kommandos


Lernen Sie wie Sie eigene Elemente über *app/console mapbender:generate:element* erzeugen können :doc:`How to create your own Element? <element_generate>`.
        
..
 Package Build Tools
 ===================

 TODO: Skipped for now, KMQ has the knowledge.

Aktualisierung der Installation
===============================
Da die Entwicklungen voranschreiten, wollen Sie ihren Code aktuell halten. 

Folgende Schritte müssen durchgeführt werden:

* Holen Sie den Code vom mapbender-starter Repository
* Aktualisieren Sie die Submodule
* Aktualisieren Sie die Datenbank, um gegebenenfalls neue Strukturen (Tabellen, Spalten) zu erzeugen


.. code-block:: yaml
 
 cd mapbender-starter
 git pull
 git submodule update --init --recursive
 cd application
  ./composer.phar update --dev
 app/console doctrine:schema:update


.. _installation_sphinx:

Sphinx
======

Sphinx wird für die Dokumentation benötigt, die Sie gerade lesen. In Debian-basierten Systemen wird Sphinx folgendermaßen installiert.


.. code-block:: yaml

   sudo apt-get install sphinx-common


Sie finden die Mapbender3 Dokumentation auf github unter  mapbender-documentation. Sie könnnen den Klon über den Befehl holen: 

.. code-block:: yaml

	git clone git://github.com/mapbender/mapbender-documentation

Entwickler mit Schreibrechten müssen die SSH-URL verwenden: git@github.com:mapbender/mapbender-documentation

Lesen Sie mehr über :doc:`How to write Mapbender3 Documentation? <development/documentation_howto>`.

ApiGen
======

`ApiGen <http://apigen.org>`_ ist der API-Dokumentations-Generator erster Wahl. Es wird auch mit Pear installiert: 


.. code-block:: yaml
    
	 sudo pear install pear.apigen.org/apigen


Troubleshooting
***************

* Die ApiGen-Bestandteile laufen nur in der neusten Version von Phing. 2.4.12  ist ausreichend,  2.4.9 reicht nicht aus! 
Testen Sie mit: 


.. code-block:: yaml

              phing -v


Mit dem folgenden Befehl können Sie ein Update all Ihrer Pear-Pakete vornehmen: 


.. code-block:: yaml
    
	 sudo pear install pear.apigen.org/apigen


Lesen Sie mehr über :doc:`How to write Mapbender3 API Documentation? <development/apidocumentation>`.


Troubleshooting
***************

* The ApiGen task only works with recent versions of Phing (>= 2.4.12). Check the Phing version with 


.. code-block:: yaml

              phing -v


You can update all your Pear packages with


.. code-block:: yaml

	sudo pear upgrade-all


