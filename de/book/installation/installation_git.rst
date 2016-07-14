.. _installation_git:

Git-basierte Installation
##########################


Wenn Sie sich an der Mapbender3-Entwicklung beteiligen möchten oder aus anderen Gründen die Git Repositories für Mapbender3 verwenden, folgen Sie dieser Anleitung statt des normalen Downloads. Diese Anleitung basiert auf Ubuntu 12.04.  Für andere Distributionen benötigen Sie vielleicht spezielle Pakete wie z.B. sphinx-common.

Prüfen Sie zuerst die `Systemvoraussetzungen <systemrequirements.html>`_.

Für die Git-basierte Installation benötigen Sie:

* git     - schauen Sie sich das Dokument `Quick primer on using Git <../../../en/book/development/git.html>`_ an, um mit Git vertraut zu werden.
* cURL    - kommandozeilen basiertes Tool für die Übertragung von Daten über URL Syntax,unterstützt HTTP, HTTPS und mehr.
* pear    - PHP Erweiterung und Anwendungs-Repository.
* Phing   - `Phing <http://www.phing.info/>`_ ist nicht GNU make; es ist ein  PHP Projekt Build System oder Build-Werkzeug basierend auf Apache Ant.
* php-dev - Und natürlich die Dateien zur Entwicklung von PHP5-Modulen.


Klonen des Repositories
*************************

Klonen ist einfach, geben Sie das folgende Kommando auf Ihrer Shell ein:

.. code-block:: bash

    git clone https://github.com/mapbender/mapbender-starter.git mapbender3
    cd mapbender3

Entwickler, die Zugriff auf den Code haben möchten, müssen die SSH-URL verwenden: git@github.com:mapbender/mapbender-starter


Klonen Sie direkt einen bestimmten Branch mit -b

.. code-block:: bash

    git clone https://github.com/mapbender/mapbender-starter.git -b release/3.0.5 mapbender3
    cd mapbender3


Zu einem Tag eines Mapbender3 Releases wechseln
***********************************************

Um mit einer Release Branch von Mapbender3 zu arbeiten, wechseln Sie bitte zu dem spezifischen Tag. Zum Beispiel den Branch release/3.0.5: 

.. code-block:: bash

    git branch -a
    git checkout release/3.0.5


Submodule abrufen
*****************

Die Starter-Applikation enthält nicht die Mapbender3 bundles, diese sind in einem eigenen Repository gespeichert und werden als Submodule in das Starter-Repository eingefügt. Rufen Sie das folgende Kommando im root-Verzeichnis ihres geklonten Repositories auf.

.. code-block:: bash

    git submodule update --init --recursive



Composer
********

Mapbender3 benötigt weitere Bibliotheken für die Laufzeit-Abhängigkeiten, wie z.B. Symfony und Doctrine. Daher muss zuerst der Composer eingerichtet und ausgeführt werden (weitere Information unter http://getcomposer.org/download/):

.. code-block:: bash

    cd application
    curl -sS https://getcomposer.org/installer | php


Erzeugen Sie eine Konfigurationsdatei mit Namen parameters.yml. Kopieren Sie dazu die Datei application/app/config/parameters.yml.dist.

.. code-block:: bash

  cp app/config/parameters.yml.dist app/config/parameters.yml


Zur Anpassung der parameters.yml lesen Sie bitte das Kapitel `Anpassen der Konfigurationsdatei <configuration.html#anpassen-der-konfigurationsdatei>`_.

Laden Sie anschließend die Laufzeit-Umgebungen wie Symfony und Doctrine:

.. code-block:: bash

  ./composer.phar update 



Die nächsten Schritte der Installation
**************************************

Folgen Sie nun den Schritten, die unter `Installation <installation_ubuntu.html>`_ beschrieben werden:

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

.. code-block:: bash

    app/console assets:install web --symlink --relative


Bitte beachten Sie, dass Sie die Option :command:`FollowSymLinks` in der Apache Directory Definition angeben müssen:


.. code-block:: apache

  Alias /mapbender3 /var/www/mapbender-starter/application/web/
  <Directory /var/www/mapbender-starter/application/web/>
    Options MultiViews FollowSymLinks
    DirectoryIndex app.php
    Require all granted
    
    RewriteEngine On
    RewriteBase /mapbender3/
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ app.php [QSA,L]
 </Directory>


Lernen Sie mehr über app/console
********************************
Die Symfony Console Komponenten ermöglichen es, kommandozeilen basierte Befehle zu erzeugen. Doctrine verfügt beispielsweise über einige kommandozeilen basierte Befehle, die Sie verwenden können.

Lesen Sie mehr in der Symfony Dokumentation über `Console Commands <http://symfony.com/doc/current/components/console/usage.html>`_.

Hier finden Sie einige Kommandos zum Auffinden von Informationen:

.. code-block:: bash

 app/console                        - lists all assets
 app/console help                   - Anzeige der Hilfe
 app/console help list              - Anzeige der Hilfe für einzelne Kommandos
 app/console doctrine               - Anzeige aller Funktionen von Doctrine 
 app/console mapbender              - Anzeige aller Funktionen von Mapbender
 app/console help assets:install    - Anzeige der Hilfe zu speziellen Kommandos


Lernen Sie wie Sie eigene Elemente über *app/console mapbender:generate:element* erzeugen können `How to create your own Element? <../../../en/book/development/element_generate.html>`_.
        

Aktualisierung der Installation
*******************************

Da die Entwicklungen voranschreiten, wollen Sie ihren Code aktuell halten. 

Folgende Schritte müssen durchgeführt werden:

* Holen Sie den Code vom mapbender-starter Repository
* Aktualisieren Sie die Submodule
* Aktualisieren Sie die Datenbank, um gegebenenfalls neue Strukturen (Tabellen, Spalten) zu erzeugen


.. code-block:: bash
 
 cd mapbender-starter
 git pull
 git submodule update --init --recursive
 cd application
 ./composer.phar update --dev
 app/console doctrine:schema:update


.. _installation_sphinx:

Sphinx (Dokumentation)
**********************

Sphinx wird für die Dokumentation benötigt, die Sie gerade lesen. In Debian-basierten Systemen wird Sphinx folgendermaßen installiert.


.. code-block:: bash

   sudo apt-get install python-sphinx


Sie finden die Mapbender3 Dokumentation auf github unter  mapbender-documentation. Sie könnnen den Klon über den Befehl holen: 

.. code-block:: bash

	git clone git://github.com/mapbender/mapbender-documentation

Entwickler mit Schreibrechten müssen die SSH-URL verwenden: git@github.com:mapbender/mapbender-documentation

Lesen Sie mehr über `How to write Mapbender3 Documentation? <../../../en/book/development/documentation_howto.html>`_.

ApiGen
******

`ApiGen <http://apigen.org>`_ ist der API-Dokumentations-Generator erster Wahl. Es wird mit Pear (php-pear) installiert: 


.. code-block:: bash
    
	 sudo pear install pear.apigen.org/apigen
     
Lesen Sie mehr in `How to write Mapbender3 Documentation? <../../../en/book/development/documentation_howto.html>`_.


Troubleshooting
***************

* Die ApiGen-Bestandteile laufen nur mit neueren Versionen von Phing (>= 2.4.12), welches die Pear-Bibliothek benötigt. Zunächst muss Pear installiert werden.  Hier wird ein Debian-basiertes System verwendet:

.. code-block:: bash

    sudo apt-get install php-pear


Dann muss Pear gezeigt werden, wie ein Autodiscover seiner Repositories erzeugt wird.  Vorsichtshalber wird ein Update von Pear gemacht.

.. code-block:: bash

    sudo pear config-set auto_discover 1
    
    sudo pear upgrade-all
      Enable full APC compatibility [yes] : yes
      Enable internal debugging in APCu [no] : yes 

Dann wird Phing installiert:

.. code-block:: bash

    sudo pear channel-discover pear.phing.info 
    sudo pear install phing/phing

Testen Sie die Phing Version mit: 

.. code-block:: bash

              phing -v


