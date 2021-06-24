.. _digitizer_functionality_de:

Funktionalitäten des Digitizers
*******************************

Das Digitizer-Element bietet komplexe Editierfunktionalitäten an:

* Verschieben von Objekten
* Einfügen von Stützpunkten (Linien, Flächen)
* Erfassung von Flächen mit Enklaven und/oder Exklaven sowie Kreisen und Ellipsen

In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden.


.. image:: ../../../figures/digitizer.png
     :scale: 80

Folgende Optionen stehen für den Aufbau von Formularen zur Verfügung:

* Definition von mehreren Datenquellen und Geometrieformaten für die Erfassung. Die verschiedenen Quellen werden über eine Auswahlbox angeboten.
* Als Datenquelle wird eine Tabelle angesprochen, wobei auch nur eine Auswahl der Daten über einen Filter herangezogen werden kann
* Textfelder
* Textblöcke (mehrzeilige Textfelder)
* Selectboxen, Multiselectboxen (Füllen der Auswahlbox über eine feste Definition von Werten in der YAML-Definition oder über ein Select auf eine Tabelle)
* Radiobuttons und Checkboxen
* Datumsauswahl
* Dateiupload und Bildanzeige
* Definition von Reitern
* Definition von Trennlinien (breakLine)
* Definition von beschreibenden Texten zur Information
* Definition von Hilfetexten
* Pflichtfelder, Definition von regulären Ausdrücken für die Formatvorgabe bestimmter Feldinhalte
* Möglichkeit, in Formulare eingegebene Inhalte per Buttonklick in die Zwischenablage zu kopieren
* Karten-Refresh nach Speichern


.. image:: ../../../figures/digitizer_with_tabs.png
     :scale: 80


Nutzung
=======

Allgemein
---------

Der Digitizer ermöglicht das Editieren von FeatureTypes. Diese basieren auf Punkt, Linien oder Polygongeometrien und ihren Sachdaten. Die Sachdaten werden in dem Formular des Digitizers angezeigt. Das Editieren der Geometrien geschieht über die Karte.


Geometrien erstellen
--------------------

Jeder FeatureType kann unterschiedliche `Toolsets <#definition-der-zur-verfugung-stehenden-werkzeuge-toolset-type>`_ freischalten, die dann in der Schaltflächenleiste des Digitizers sichtbar sind.

In dem FeatureType "poi" wird mit dem "drawPoint" Toolset beispielsweise die Schaltfläche zum Erstellen eines neuen Punktes freigeschaltet, mit dem Toolset "modifyFeature" die Verschieben-Schaltfläche eingeblendet.


.. image:: ../../../figures/digitizer_buttons_poi.png
     :scale: 80



Speichern, Löschen, Abbrechen
-----------------------------

Es stehen drei Schaltflächen im Dialog zur Verfügung: Speichern, Löschen, Abbrechen.

Das *Speichern* der Änderungen geschieht erst, wenn die Schaltfläche "Speichern" im Attributdialog gedrückt worden ist. Ein Verschieben einer Geometrie alleine speichert das Feature also nicht sofort (um unnötige Änderungen in der Datenbank zu verhindern). Es ist bislang noch notwendig, den Attributdialog zu öffnen und Speichern zu klicken.

.. image:: ../../../figures/digitizer_save_delete_cancel.png
     :scale: 80

* **Speichern:** Speichert die Geometrie und die Attributdaten in die Datenbank.
* **Löschen:** Löscht die Daten.
* **Abbrechen:** Speichert und löscht die Daten nicht, behält die Geometrie aber für eine weitere Bearbeitung im internen Speicher. Sie ist weiterhin in der Karte zu sehen und kann angepasst werden (z.B. bei Polygonen). Attributdaten werden nicht vorgehalten.

Es gibt mehrere Optionen in den `Basisdefinitionen <#basisdefinition>`_, die das Verhalten bestimmen:

* allowEditData: Speichern Schaltfläche anzeigen.
* allowDelete: Löschen Schaltfläche anzeigen.
* allowCancelButton: Abbrechen Schaltfläche anzeigen.
* allowDeleteByCancelNewGeometry: Verhalten des Abbrechen Knopfes.

Das *Löschen* eines Features kann sowohl über den Dialog, als auch die Tabelle geschehen.


Stützpunkte
-----------

Das Bearbeiten von Polygonen und Linien erlaubt das Erstellen, Verschieben und Löschen von Stützpunkten. Die Schaltfläche zum Editieren von Stützpunkten erwartet, dass man ein Polygon selektiert. Dieses wird dann mit den Stützpunkten angezeigt.

.. image:: ../../../figures/digitizer_edit_vertices.png
           :scale: 80

Die vorhandenen Stützpunkte werden deckend dargestellt, mögliche neue Stützpunkte befinden sich immer in der Mitte einer Kante, sind leicht transparent dargestellt und können per Klick auf diesen Punkt hinzugefügt werden.

Vorhandene Stützpunkte werden mit der Entfernen-Taste auf der Tastatur gelöscht. Dafür bewegt man sich mit dem Mauszeiger über einen Stützpunkt und drückt die Entf-Taste. *Anmerkung*: Falls das Löschen einen Stützpunktes nicht reagiert, hilft ein Klick mit der rechten Maustaste auf die Karte. Speziell mit dem aktivierten Kontextmenü können sich z.Z. noch Events verhaken.

