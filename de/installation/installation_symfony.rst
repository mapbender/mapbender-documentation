.. _installation_symfony_de:

Installation von Mapbender unter Verwendung des Symfony-eigenen Webservers
##########################################################################

Mapbender baut auf das `Symfony <http://symfony.com/>`_ Framework auf und kann 
daher den `Symfony-eigenen Webserver <http://symfony.com/doc/current/cookbook/web_server/built_in.html>`_ nutzen. 
Das ermöglicht Ihnen einen schnellen Test von Mapbender, ohne eine Integration in einen Webserver vorzunehmen. 

.. hint:: Der Symfony-eigenen Webserver eignet sich nicht für die Produktivumgebungen.
 
In dieser Anleitung wird die im Installationspaket mitgelieferte SQLite-Datenbank verwendet.

* Bitte prüfen Sie die Systemvoraussetzungen in der Installationsanleitung `Linux <installation_ubuntu.html>`_ bzw. `Windows <installation_windows.html>`_ 
* Laden Sie die aktuellen Mapbender-Version herunter https://mapbender.org/builds/
* Entpacken in ein beliebiges Verzeichnis.
* Starten Sie den Symfony-eigenen Webserver.

.. code-block:: bash

    app/console server:run

Der Befehl führt einen lokalen Webserver aus. 

Standardmäßig lauscht der Server auf die Adresse 127.0.0.1 und den ersten freien Port ab 8000.

Mapbender ist nun auf dem lokalen Rechner über die Adresse  http://127.0.0.1:8001/ erreichbar. 
Beachten Sie, dass über diesen Aufruf standardmäßig der Entwickler-Modus gestartet wird.

Sie können den Aufruf auch mehrfach ausführen. Es wird dann der nächste freie Port verwendet.

Die gewünschte Adresse kann auch über die Angabe der IP und des Ports angegeben werden:

.. code-block:: bash

    app/console server:run 127.0.0.1:80002
                                                                                                                                                                                                                                         
    [OK] Server listening on http://127.0.0.1:8002                                                                         
         
    // Quit the server with CONTROL-C.                                                                                     

    [Mon Jan 31 15:56:57 2022] PHP 7.4.3 Development Server (http://127.0.0.1:8002) started
