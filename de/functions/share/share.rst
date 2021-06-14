.. _share_de:

Share
*****





















Ansichtsverwaltung
==================

Das Element erlaubt die Speicherung und Wiederverwendung von Kartenansichten. Folgende Kartenparameter sind hierin inbegriffen: Kartenposition, Maßstab, Koordinatenreferenzsystem, Drehung, Layer, Layerauswahl sowie Transparenz. Geänderte Kartenansichten bleiben dabei auch nach Neuladung der Ansicht erhalten.

Hinweis: Der View Manager wird bisher nur in der Sidepane unterstützt.

.. image:: ../../../figures/de/view_manager_overview.png
     :scale: 80

Nutzung
-------

Um eine neue Kartenansicht zu speichern, muss zunächst eine Titel für deren Re-Identifikation vergeben werden. Danach kann die Kartenansicht durch einen Klick auf den "Speicher"-Button übernommen werden.

.. image:: ../../../figures/de/view_manager_create_map_state.png
     :scale: 80

In seiner einfachsten Form kann das Element zur Wiederverwendung von Kartenansichten verwendet werden. Diese Option ist immer vorhanden. Hinweis: Der jeweilige Button erlaubt auch gängige Browser-Kontext-Interaktionen wie "Url kopieren", "Öffnen in einem neuen Tab" etc. Gespeicherte Ansichten können außerdem überschrieben sowie gelöscht werden. Die Einträge in der Sidepane werden dabei entsprechend aktualisiert.

Hinweis: Aktuell unterstützt die Ansichtsverwaltung *nicht* folgende Konfigurationen:

* interaktiv hinzugefügte Instanzen (WMS laden)
* interaktiv entfernte Instanzen (Ebenenbaum Kontextmenü)
* alle Werte für WMS-Dimensionen
* dynamisch veränderte Geometrien (Digitizer etc.)

Zugriffsrechte
--------------

Jede Kartenansicht ist einer Anwendung zugeordnet und wird weiter unterteilt in ein öffentlich und privat. Die Elementkonfiguration enthält die Rechte zum Speichern, Löschen sowie Wiederverwenden von Kartenansichten. Weiterhin kann hier definiert werden, ob private Ansichten und Daten angezeigt sowie Speicherrechte für anonyme Besucher gesetzt werden sollen.

Zugriffsrechte müssen generell für den root Nutzer nicht für öffentliche Ansichten gesetzt werden. Der Superuser kann diese automatisch erzeugen, überschreiben sowie löschen. Anonyme Nutzer sind generell von der Arbeit mit privaten Ansichten ausgeschlossen. Sie können öffentliche Einträge außerdem niemals löschen. Ihre Zugriffsrechte für das Speichern sowie Überschreiben von öffentlichen Ansichten wird durch die allowAnonymousSave Option gesteuert. Wenn diese auf FALSE gesetzt ist, dann haben diese nur noch einen Lesezugriff. Sollen Anonyme Nutzer komplett ausgeschlossen werden, dann kann eine ROLE_USER Zugriffsbeschränkung für das gesamte Element gesetzt werden.

YAML-Definition:
----------------

.. code-block:: yaml

   publicEntries       #String oder leer (Falsche Werte deaktivieren öffentliche Ansichten komplett); andere erlaubte Werte sind ro (nur Lesezugriff), rw (Lese- und Schreibzugriff), rwd (Lese- und Schreibzugriff sowie Löscherlaubnis) (Standard: ro).
   privateEntries      #Schaltet Privatnutzerzustände an mit vollem Zugriff auf Optionen "Speichern", "Wiederverwenden" sowie "Löschen" (Standard: true).
   allowAnonymousSave  #Gibt Speicherrecht für öffentliche Ansichten auch an anonyme Nutzer (Standard: false).
   showDate:		#Zeigt Datum der Erzeugung bzw. Aktualisierung (Standard: true)

