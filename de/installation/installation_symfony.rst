.. _installation_symfony_de:

Installation von Mapbender unter Verwendung des Symfony-eigenen Webservers
##########################################################################

Mapbender baut auf das `Symfony <https://symfony.com/>`_ Framework auf und kann daher das `Symfony CLI Entwicklungswerkzeug <https://symfony.com/download>`_ für einen lokalen Webserver nutzen. 
Das ermöglicht Ihnen einen schnellen Test von Mapbender, ohne eine Integration in einen Webserver vorzunehmen. 

.. hint:: Der Symfony-eigene Webserver eignet sich nicht für die Produktivumgebungen.
 
In dieser Anleitung wird die im Installationspaket mitgelieferte SQLite-Datenbank verwendet.

* Bitte prüfen Sie die Systemvoraussetzungen unter :ref:`Linux <installation_ubuntu_de>` bzw. :ref:`Windows <installation_windows_de>`.
* Laden Sie die aktuellen Mapbender-Version herunter https://mapbender.org/builds/.
* Entpacken in ein beliebiges Verzeichnis.
* Starten Sie den Symfony-eigenen Webserver:

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
