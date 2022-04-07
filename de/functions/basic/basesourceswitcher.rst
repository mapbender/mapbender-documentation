.. _basesourceswitcher_de:

Themenwechsel (BaseSourceSwitcher)
**********************************

Mit diesem Element kann zwischen vordefinierten Themen (BaseSources), z. B. Hintergrundkarten, gewechselt werden. Die Definition der BaseSources erfolgt in der Anwendung im Reiter Layersets für den entsprechenden Layer. Die Bearbeitungsoberfläche des gewünschten Layers muss dazu geöffnet werden. Um diesen als BaseSource verwenden zu können, ist es notwendig, ein Häkchen bei Basesource zu setzen.

Über Buttons kann zwischen den verschiedenen Themen gewechselt werden. Es kann dabei immer nur ein Thema aktiv sein.

Zu jeder Datenquelle kann eine Gruppe definiert werden. Alle Definitionen einer Gruppe werden als Dropdown-Liste angezeigt, wobei der Gruppenname als übergeordneter Eintrag erscheint.

.. image:: ../../../figures/basesourceswitcher.png
     :scale: 80

Der BaseSourceSwitcher kann auch in der Seitenleiste eingebunden werden. Dabei ist keine Definition von Gruppen möglich.

.. image:: ../../../figures/de/basesourceswitcher_sidepane.png
     :scale: 80


Konfiguration
=============

**Vorbereitung**: Um den BaseSourceSwitcher konfigurieren zu können, 
müssen WMS-Instanzen als BaseSource definiert sein (Checkbox BaseSource: aktiv). 
Beachten Sie, dass in der Anwendung beim Start die Themen aktiviert werden, 
bei denen der root-Layer aktiv ist.

.. image:: ../../../figures/basesourceswitcher_basesource.png
     :scale: 80

Konfiguration aktiver ausgewählter root-Layer - Thema ist aktiv beim Start:

.. image:: ../../../figures/de/basesourceswitcher_instance_active.png
     :scale: 80

Konfiguration nicht aktivierter ausgewählter root-Layer - Thema ist beim Start nicht aktiv:

.. image:: ../../../figures/de/basesourceswitcher_instance_not_active.png
     :scale: 80


Die Konfiguration geschieht in zwei Schritten im Content-Bereich:

#. Erzeugen eines Elements zum Wechseln der vordefinierten Themen (Titel, Tooltip und Target)
#. Hinzufügen von Themen mit einer oder mehrerer Quellen und optionaler Definition einer Gruppe


.. image:: ../../../figures/de/basesourceswitcher_de.png
     :scale: 80


* **Title:** Titel des Elements.
* **Tooltip:** Text, der erscheint, wenn der Mauszeiger längere Zeit über dem Hintergrundwechsler gehalten wird.
* **Target:** Zielelement des Buttons, das bei Anklicken des Buttons ausgelöst wird.
* **Instancesets:** Es können eine oder mehrere Themengruppen definiert werden. Diese verweisen auf eine Auswahl an Instanzen und sind mit einem Titel und einem Gruppennamen (optional) versehen.

Das Konfigurationsbeispiel zeigt, dass entweder ein, kein oder mehrere Einträge pro Instanceset gewählt werden können. Durch eine Group-Angabe lassen sich Gruppen bilden, die dann über eine Dropdown-Liste zusammengefasst werden.

* **Title**: Name der Themenkarte.
* **Group**: Optionale Zuweisung zu einer Themengruppe.
* **Instances**: Auswahl der Instanzen für die Themenkarte.


YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

    title:                                              # Titel
    tooltip:                                            # Text des Tooltips
    target: map                                         # ID des Kartenelements
    sourcesets:                                         # Liste der Sourcesets.
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}                        # sourceset: Titel,
                                                        # group: (optional) Gruppenname der Gruppen der Sourcesets über "group name"
                                                        # sources Liste der Sources
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}




