.. _applicationswitcher_de:

Anwendung wechseln
******************

Dieses Element stellt ein Auswahlbox bereit, über die zwischen Anwendungen gewechselt werden kann. Dabei bleibt der aktuelle Kartenausschnitt erhalten.

.. image:: ../../../figures/de/applicationswitcher.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/applicationswitcher_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird angezeigt, wenn der Mauszeiger eine längere Zeit über der Auswahl verweilt.
* **Anwendungen:** Wählen Sie die Anwendungen, die zur Auswahl erscheinen sollen.
* **In neuem Tab öffnen:** Definiert, ob die Anwendung beim Wechsel in einem neuen Browser-Tab geöffnet werden soll.

Anwendung wechseln Konfiguraton
-------------------------------

Zuerst muss über das ``+`` - Zeichen in der Anwendung unter dem Reiter Layouts im Toolbar Bereich das Element Anwendung wechseln ausgewählt werden.

.. image:: ../../../figures/de/add_toolbar.png
     :scale: 80
     
Nach Auswahl des Elements öffnet sich der Dialog "Element hinzufügen – Anwendung wechseln". Hier werden die Einstellungen zur Konfiguration des Elements vorgenommen.

Im Feld *Title* definieren Sie einen Text, der erscheinen soll, wenn die Maus über den Button fährt.
Unter *Anwendungen* wählen Sie per Klick die Anwendungen aus, die zur Auswahl erscheinen sollen.
Über die Checkbox *In neuem Tab öffnen* definieren Sie, ob die Anwendung beim Wechsel in einem neuen Browser-Tab geöffnet werden soll.

YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

    title: Choose an Application              # Text wird als Tooltip angezeigt
    class: Mapbender\CoreBundle\Element\ApplicationSwitcher
    applications: ["mapbender_user","mapbender_user_basic"]     # Anwendungen, die zur Auswahl stehen sollen
    open_in_new_tab: true   # false/true Anwendung in neuem Browser-Tab öffnen

