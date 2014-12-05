.. _basesourceswitcher:

BaseSourceSwitcher (Themenwechsel)
*********************************************************************

Mit diesem Element kann zwischen vordefinierten Themen (BaseSources) z.B. Hintergrundkarten gewechselt werden. Über Buttons kann zwischen den Themen gewechselt werden. Es kann dabei immer nur ein Thema aktiv sein.

Zu jedem Sourceset kann eine Gruppe definiert werden. Alle Definitionen einer Gruppe werden als Dropdown-liste angezeigt, wobei der Gruppenname als übergeordneter Eintrag erscheint.

.. image:: ../../../../../figures/basesourceswitcher.png
     :scale: 80

Konfiguration
=============

Die Konfiguration geschieht in zwei Schritten:

* Erzeugen eines Elements zum Wechseln der vordefinierten Themen mit Titel, Tooltip und Target
* Hinzufügen von Themen mit einer oder mehrerer Quellen und optionaler Definition einer Gruppe


.. image:: ../../../../../figures/basesourceswitcher_configuration.png
     :scale: 80
     

YAML-Definition:

.. code-block:: yaml

    title:                                              # Titel
    tooltip:                                            # Text des Tooltips
    target: map                                         # ID des Kartenelements
    sourcesets:                                         # Liste der Sourcesets.
        - { title: sourcesetname, group: groupname,
            sources: [sourceId]}                        # sourceset: Titel,
                                                        # group: (optional) Gruppenname der Gruppen der Sourcesets über "group name"
                                                        # sources Liste der Sources
        
        

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\BaseSourceSwitcher
* Widget: mapbender.element.basesourceswitcher.js


HTTP Callbacks
==============

Keine.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
