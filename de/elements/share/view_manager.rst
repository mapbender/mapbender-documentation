.. _view_manager_de:

Ansichtsverwaltung (View Manager)
*********************************

Das Element Ansichtsverwaltung erlaubt das Speichern und Wiederverwenden von Kartenansichten. Folgende Kartenparameter sind Teil einer Ansicht:

* Drehung
* Kartenposition
* Koordinatenreferenzsystem
* Layer aus :ref:`sources_de`
* Ausgewählte :ref:`Layersets<layerset_de>`
* Maßstab
* Transparenz

Gesetzte Kartenansichten bleiben nach Neuladen der Anwendung erhalten.

.. image:: ../../../figures/de/view_manager_overview.png
     :scale: 80


.. note:: **Hinweis:** Die Ansichtsverwaltung wird bisher nur in der Sidepane unterstützt.


Nutzung
-------

Um eine neue Kartenansicht zu speichern, muss zunächst ein Titel für deren Re-Identifikation vergeben werden. Danach kann die Kartenansicht durch einen Klick auf den Speichern-Button zur Liste hinzugefügt werden.

.. image:: ../../../figures/de/view_manager_create_map_state.png
     :scale: 80

In seiner einfachsten Form kann das Element zur Wiederverwendung von Kartenansichten verwendet werden. Diese Option ist immer vorhanden: Die zuvor gespeicherte Kartenansicht wird nach Klick auf den Abrufen-Button wiederhergestellt. Gespeicherte Ansichten können außerdem überschrieben oder gelöscht werden. Die Einträge in der Sidepane werden dabei entsprechend aktualisiert.

Die folgenden Konfigurationen werden **nicht** in die Ansichtsverwaltung integriert:

* Interaktiv hinzugefügte Instanzen (:ref:`wms_loader_de`)
* Interaktiv entfernte Instanzen (:ref:`layertree_de` Kontextmenü)
* Alle Werte für WMS-Dimensionen
* Dynamisch veränderte Geometrien (:ref:`digitizer_de` etc.)


Zugriffsrechte
--------------

Jede Kartenansicht ist einer Anwendung zugeordnet und wird weiter in öffentlich und privat unterteilt. Die Elementkonfiguration enthält die Rechteeinstellungen zum Lesen, Speichern und Löschen von Kartenansichten in öffentlichen Listen. Weiterhin kann hier über Checkboxen definiert werden, ob private Listen die Anzeige privater Kartenansichten ermöglichen sollen, der beim Speichern erstellte Zeitstempel in der Liste angezeigt wird und ob anonyme Besucher öffentliche Kartenansichten speichern dürfen.

Zugriffsrechte müssen für den root Nutzer nicht für öffentliche Ansichten gesetzt werden. Der Administrator kann diese automatisch erzeugen, überschreiben oder löschen.

Anonyme Nutzer sind generell von der Arbeit mit privaten Ansichten ausgeschlossen. Sie können öffentliche Einträge außerdem niemals löschen. Ihre Zugriffsrechte für das Speichern sowie Überschreiben von öffentlichen Ansichten wird über die Checkbox "Anonyme Besucher dürfen speichern" gesteuert. Bei Deaktivierung der Option verbleibt anonymen Benutzern noch ein Lesezugriff. Sollen Anonyme Nutzer komplett ausgeschlossen werden, dann kann eine ROLE_USER Zugriffsbeschränkung für das gesamte Element gesetzt werden.


Konfiguration
=============

.. image:: ../../../figures/de/view_manager_configuration.png
     :scale: 80


YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

  viewmanager:
    title: View Manager                                # Titel des Elements.
    class: Mapbender\CoreBundle\Element\ViewManager    # Klasse des Elements.
    publicEntries: rw                                  # String oder leer (Falsche Werte deaktivieren öffentliche Ansichten komplett); andere erlaubte Werte sind ro (nur Lesezugriff), rw (Lese- und Schreibzugriff), rwd (Lese- und Schreibzugriff sowie Löscherlaubnis) (Standard: ro).
    privateEntries: true                               # Schaltet Privatnutzerzustände an mit vollem Zugriff auf Optionen "Speichern", "Wiederverwenden" sowie "Löschen" (Standard: true).
    allowAnonymousSave: true                           # Gibt Speicherrecht für öffentliche Ansichten auch an anonyme Nutzer (Standard: false).
    showDate: true                                     # Zeigt Datum der Erzeugung bzw. Aktualisierung (Standard: true)
