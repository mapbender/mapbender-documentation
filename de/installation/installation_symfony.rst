.. _installation_symfony_de:

Installation im Symfony Webserver
#################################

Mapbender baut auf dem `Symfony <http://symfony.com/>`_ Framework auf und kann daher den in `Symfony eingebauten Webserver <http://symfony.com/doc/current/cookbook/web_server/built_in.html>`_ nutzen. Das ermöglicht Ihnen einen schnellen Test von Mapbender, ohne eine Integration in einen Webserver vorzunehmen. Dies eignet sich nicht für Produktivumgebungen. In dieser Anleitung wird die SQLite Datenbank verwendet.

* Systemvoraussetzungen in der Installationsanleitung `Linux <installation_ubuntu.html>`_ bzw. `Windows <installation_windows.html>`_ 
* Download der aktuellen Mapbender Version unter https://mapbender.org/builds/
* Entpacken in ein beliebiges Verzeichnis.
* Start des Symfony Webserver:

  .. code-block:: bash

                  app/console server:run 0.0.0.0:8000

Mapbender ist dann vom Host-Rechner aus über http://ip-adresse:8000/app.php erreichbar.
