.. _overview_de:

Übersichtskarte (Overview)
**************************

Mapbender bietet neben der Hauptkarte auch eine Übersichtskarte an. Dieses Element kann in Größe, Position und Zoom-Verhalten individuell angepasst werden. Es bezieht sich auf ein bestimmtes Layerset und die darin definierten Instanz(en). 

.. image:: ../../../figures/overview.png
     :scale: 80

Konfiguration
=============

Der Konfigurationsdialog:

.. image:: ../../../figures/de/overview_configuration.png
     :scale: 70

* **Fixieren:** Definiert, ob die Übersichtskarte in ihrem Maßstab fixiert sein soll (Standard: false).
* **Title:** Titel des Elements, wird in der Layouts-Liste angezeigt.
* **Layerset:** Layerset, das im Kartenrahmen angezeigt werden soll.
* **Sichtbarkeit:** Definiert, ob der Kartenrahmen beim Start maximiert (Initial offen) oder minimiert (Initial geschlossen) oder Dauerhaft offen (kein Button zum schließen) ist (Standard: Initial offen). 
* **Width/Height:** Breite und Höhe der Übersichtskarte.
* **Position:** Position des Übersichtskartenrahmens in der Anwendung; Auswahlmöglichkeiten: oben links, unten links, oben rechts, unten rechts.

Konfigurationsbeispiele
=======================

.. image:: ../../../figures/de/overview_configuration_example.png
     :scale: 80

Das Element bietet verschiedene Konfigurationsmöglichkeiten. Im Beispiel sind die Einstellungen *Sichtbarkeit Initial offen* sowie *Fixieren* gesetzt. Dadurch wird das Element beim Öffnen der Anwendung direkt angezeigt (d.h. maximiert), zusätzlich ist die Ansicht der Karte fixiert.
Ist die Übersicht nicht fixiert, dann passt sich die Übersichtskarte dem entsprechenden Kartenausschnitt der Hauptkarte an, sobald diese verschoben oder ihr Maßstab verändert wird. Als Startansicht beim Öffnen der Anwendung wird der Startextent angezeigt.
Das Element hat im Beispiel den Standardtitel "Übersicht (overview)". Es ist außerdem notwendig, dass die Übersichtskarte mit einem Layerset verknüpft wird. In diesem Beispiel stehen folgende Layersets zur Auswahl:

.. image:: ../../../figures/de/map_example_layersets.png
     :width: 100%

Für die Übersicht wurde das Layerset "overview" gewählt. Breite (*Width*) sowie Höhe (*Height*) des Elements entsprechen der Standardeinstellung. Die Position ist als "Unten rechts" definiert. Das Element sieht in der Anwendung folgendermaßen aus:

.. image:: ../../../figures/de/overview_example_right-bottom_fixed.png
     :scale: 80

Ein alternatives Konfigurationsbeispiel kann die Anpassung der folgenden Parameter (*Fixieren*: nicht aktiv, *Position*: unten links, *Width*: 400, *Height*: 200) sein, die eine andere Übersichtskarte (nach Einklappen der Sidepane) generiert:

.. image:: ../../../figures/de/overview_example_left-bottom.png
     :width: 100%


YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

   tooltip: 'Overview'          # Text des Tooltips
   target: ~                    # ID des Kartenelements
   layerset: ~                  # vorher definiertes Layerset, das angezeigt werden soll.
   width: 200                   # Breite der Übersicht
   height: 100                  # Höhe der Übersicht
   anchor: 'right-top'          # Ausrichtung der Übersicht (Standard: right-top)
                                # Benutzen Sie inline z.B. für die Sidebar
                                # Optionen: 'inline', 'left-top', 'right-top', 'left-bottom', 'right-bottom'
   visibility: open             # open/closed/open-permanent - open/closed zeigt einen Button zum Öffnen/Schließen (default: open), open-permanent zeigt den Button nicht an
   fixed: true                  # true/false um den Übersichtsbereich zu fixieren (Standard: true)

