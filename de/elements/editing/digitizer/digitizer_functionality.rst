.. _digitizer_functionality_de:

Funktionen des Digitizers
=========================

Der Digitizer ermöglicht die Erstellung und Bearbeitung von Features. Die Features basieren auf Punkt-, Linien-, oder Polygongeometrien und ihren Sachdaten. Die Geometrien können über die Karte editiert werden. Die Sachdaten werden im Digitizer-Formular angezeigt. Insgesamt ermöglicht der Digitizer eine Vielzahl von Funktionen zur Erstellung und Bearbeitung von Geometrien:

* Erstellen von Punkten, Linien und Polygonen (Rechtecke, Kreise und Ellipsen),
* Verschieben von Geoobjekten,
* Einfügen von Stützpunkten (bei Linien und Polygonen),
* Erfassung von Polygonen mit Enklaven,
* Snappen an Stützpunkten von angezeigten Objekten.

.. image:: ../../../../figures/Digitizer_geometries.png
     :width: 100%

Die folgenden Abschnitte stellen die Arbeit mit Digitizer gemäß der Standardkonfiguration genauer vor.

Geometrien erstellen
--------------------

In der Standardkonfiguration kann der Nutzer über ein Dropdown-Menü zwischen drei verschiedenen Geometrietypen wählen: Punkt, Linie und Polygon.

Punkte
^^^^^^

Durch einen Klick auf den Button **Punkt erstellen** wird die Funktion aktiviert/deaktiviert.

.. image:: ../../../../figures/Digitizer_create_points.png
     :scale: 100

Linien
^^^^^^

Durch einen Klick auf den Button **Linie erstellen** wird die Funktion aktiviert/deaktiviert.

.. image:: ../../../../figures/Digitizer_create_lines.png
     :scale: 100

Polygone
^^^^^^^^

Es können unterschiedliche Arten von Polygonen erstellt werden. Dies ist über eine Aktivierung des jeweiligen Buttons für **Flächen**, **Rechtecke**, **Enklaven**, **Ellipsen** oder **Kreise** möglich.

.. image:: ../../../../figures/Digitizer_create_polygons.png
     :scale: 100

Mithilfe der Maus kann nun die zuvor ausgewählte Geometrieart in der Karte erstellt werden. Anschließend öffnet sich ein Pop-up-Fenster, welches das vordefinierte Sachdatenformular gemäß der Yaml-Konfiguration ausgibt und die Erfassung dieser zulässt.


Geometrien bearbeiten, speichern oder löschen
---------------------------------------------

Die Speicherung der Geometrien erfolgt in der jeweils definierten Datenbanktabelle. Die Objekte werden in der Karte angezeigt und darüber hinaus im Digitizer-Element in Form einer Tabelle aufgelistet. Dies erleichtert die Verwaltung der Geometrien. 

In der Tabelle können beliebige Spalten ausgegeben werden. Im Beispiel werden die Nummer (ID wird automatisch erzeugt) sowie der Name jedes Objekts angezeigt. Es ist möglich, die Sortierung der Spalten zu ändern und die Tabelle zu durchsuchen.

Die Grundfunktionen in der Digitizer-Tabelle sind (von links nach rechts und von oben nach unten):

* Mit der Checkbox **Nur Objekte des aktuellen Kartenausschnitts anzeigen** können Sie diee Tabelle so filtern, dass nur Geometrien aus dem aktuellen Kartenausschnitt angezeigt werden.
* Es ist möglich, alle Features **neu zu laden**.
* Es ist ebenfalls möglich, alle Objekte auf der Karte **auszublenden** oder **einzublenden**.
* Sie können Änderungen für mehrere Objekte **Speichern**.
* Eine Schaltfläche zum **Zeichnen** von Geometrien (siehe oben).
* Ein Button, um Objekte zu **Bearbeiten**.
* Sie können Geometrien auch mit der Maus **Verschieben**.

.. image:: ../../../../figures/Digitizer_editing.png
     :scale: 100

Neben jedem Tabelleneintrag befinden sich außerdem Bearbeitungsfunktionen für einzelne Objekte. Diese Funktionen sind für alle Geometrietypen gleich. Folgende Funktionen stehen (von links nach rechts) zur Verfügung:

* Objekte **duplizieren**,
* **Stil bearbeiten**,
* Objekt **ausblenden** (und wieder **einblenden**),
* **Sachdaten ändern**,
* Bearbeitete Geometrien **Speichern**,
* Geometrien **Löschen**.

Es gibt außerdem noch die Option, Linien und Polygone zu modifizieren. Mit dieser Funktion können **Stützpunkte** eingefügt oder **Eckpunkte** verschoben werden. Durch Klick auf **Bearbeiten** wird die Funktion aktiviert. Um ein Objekt zu modifizieren, muss es durch einen Klick ausgewählt werden. 

.. image:: ../../../../figures/Digitizer_move.png
     :scale: 80


Kontextmenü
-----------

Für jede Funktion ist standardmäßig ein Kontextmenü verfügbar. Sie können das Kontextmenü über den rechten Mausklick auf ein Objekt öffnen.

.. image:: ../../../../figures/digitizer_contextmenu.png
     :scale: 80
