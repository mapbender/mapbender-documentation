.. _installation_symfony_de:

Aufruf von Mapbender unter Verwendung des lokalen Symfony Webservers
####################################################################

Der Aufruf von Mapbender im lokalen Symfony Webserver ermöglicht eine schnelle Konfiguration mithilfe von Symfony-eigenen Mechanismen. Das ermöglicht Ihnen einen schnellen Test, ohne eine Integration in einen eigens aufgesetzen Webserver vorzunehmen. 

.. note:: Das lokale Webserver-Bundle wurde entfernt und durch den lokalen Symfony Web Server ersetzt. Installiere das `Symfony CLI Entwicklungswerkzeug <https://symfony.com/download>`_, um diesen zu nutzen. 

.. hint:: Der Symfony-eigene Webserver eignet sich nicht für die Produktivumgebungen.
 
In dieser Anleitung wird die im Installationspaket mitgelieferte SQLite-Datenbank verwendet.

* Bitte prüfen Sie die Systemvoraussetzungen unter :ref:`Linux <installation_ubuntu_de>` bzw. :ref:`Windows <installation_windows_de>`.
* Laden Sie die aktuellen Mapbender-Version herunter https://mapbender.org/builds/.
* Entpacken in ein beliebiges Verzeichnis.
* Starten Sie den installierten lokalen Symfony Webserver.

.. code-block:: bash

    symfony server:start --no-tls


Der Befehl führt einen lokalen Webserver aus, sodass Mapbender nun auf dem lokalen Rechner erreichbar ist und die Konsole den Status des Servers mitprotokolliert.

.. note:: Beachten Sie, dass über diesen Aufruf die Anwendungsumgebung (`prod` oder `dev`) definiert werden kann:

.. code-block:: bash

    APP_ENV=prod symfony server:start --no-tls


Der gewünschte Server-Port kann auch als Argument mitgegeben werden (siehe unten). Weitere Optionen werden ausgegeben, wenn der ``--help`` Parameter mitgegeben wurde.

.. code-block:: bash

    symfony server:start --no-tls -port=8002


.. code-block:: yaml

 [OK] Web server listening
      The Web server is using PHP CLI 8.2.10
      http://127.0.0.1:8002
