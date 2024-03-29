.. _basesourceswitcher_de:

Hintergrund wechseln
********************

Mit dem Element "Hintergrund wechseln" kann mithilfe von Buttons zwischen den verschiedenen Hintergrundkarten gewechselt werden. Es kann dabei immer nur ein Thema aktiv sein. 
Zu jeder Datenquelle kann im Element eine Gruppe definiert werden. Alle Definitionen einer Gruppe werden als Dropdown-Liste angezeigt, wobei der Gruppenname als übergeordneter Eintrag erscheint.

.. image:: ../../../figures/basesourceswitcher.png
     :scale: 80

Das Element kann auch in der Sidepane eingebunden werden. Dabei ist keine Definition von Gruppen möglich.

.. image:: ../../../figures/de/basesourceswitcher_sidepane.png
     :scale: 80


Konfiguration
=============

**Vorbereitung**: Zur Definition einer Hintergrundkarte mit dem Element müssen zuvor im Backend (Reiter: Layerset) mindestens zwei gewünschte Layer konfiguriert werden. Um sie verwenden zu können, ist in den Layer-Einstellungen das Anhaken der Checkbox "Basesource" erforderlich.
Beachten Sie, dass in der Anwendung beim Start die Themen aktiviert werden, bei denen der root-Layer aktiv ist.

.. image:: ../../../figures/de/basesourceswitcher_basesource.png
     :scale: 80

Konfiguration aktiver ausgewählter root-Layer - Thema ist aktiv beim Start:

.. image:: ../../../figures/de/basesourceswitcher_instance_active.png
     :scale: 80

Konfiguration nicht aktivierter ausgewählter root-Layer - Thema ist beim Start nicht aktiv:

.. image:: ../../../figures/de/basesourceswitcher_instance_not_active.png
     :scale: 80


Die Konfiguration des Elements geschieht in zwei Schritten:

#. Erzeugen eines Elements zum Wechseln der vordefinierten Themen (Titel, Tooltip; bei Einbindung in Kartenbereich: Position)
#. Hinzufügen von Themen mit einer oder mehrerer Quellen und optionaler Definition einer Gruppe

* **Title:** Titel des Elements.
* **Tooltip:** Text, der erscheint, wenn der Mauszeiger längere Zeit über dem Hintergrundwechsler gehalten wird.
* **Instancesets:** Es können eine oder mehrere Themengruppen definiert werden. Diese verweisen auf eine Auswahl an Instanzen und sind mit einem Titel und einem Gruppennamen (optional) zu versehen.

.. image:: ../../../figures/de/basesourceswitcher_de.png
     :scale: 80

Das Konfigurationsbeispiel zeigt, dass entweder ein, kein oder mehrere Einträge pro Instanceset gewählt werden können. Durch eine Group-Angabe lassen sich Gruppen bilden, die dann über eine Dropdown-Liste zusammengefasst werden. Weitere Instancesets können über den + ``Button`` hinzugefügt werden. Ein Instanceset lässt sich mit Drag & Drop verschieben.

* **Title**: Name der Hintergrundkarte.
* **Group**: Optionale Zuweisung zu einer Themengruppe.
* **Position:** Positionierung (nur bei Nutzung im Kartenbereich). Möglichkeiten: 'Oben links', 'Unten links', 'Oben rechts', 'Unten rechts'
* **Instances**: Auswahl der Instanzen für die Hintergrundkarte.


YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

    title:                                              # Titel
    tooltip:                                            # Text des Tooltips
    target: map                                         # ID des Kartenelements
    anchor: 'right-bottom'                              # Positionierung nur bei Nutzung im Kartenbereich (Standard: right-bottom) - Optionen: 'left-top', 'right-top', 'left-bottom', 'right-bottom'
    sourcesets:                                         # Liste der Sourcesets.
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}                        # sourceset: Titel,
                                                        # group: (optional) Gruppenname der Gruppen der Sourcesets über "group name"
                                                        # sources Liste der Sources
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}




