Daten Laden
***********

Mit dem Daten Laden können Polygone, Multipolygone hochgeladen werden, die schon in einem Format gespeichert sind, ohne diese dann in Mapbender händisch gezeichnet werden müssen. 

Sie können Dateien im GeoJSON-, KML-, GML- und GPX-Format per Drag & Drop oder aus Ihren Dateien hochladen.
Zusätzlich wählen Sie entweder ein CRS oder lassen Mapbender 'Projektion automatisch bestimmen'. Die Dateigröße sollte 10 MB nicht überschreiten.

Konfiguration
-------------

.. image:: ../../../figures/dataupload_configuration.png
     :scale: 100

* **Beschriftung anzeigen (Show label)**: Zeigt ein Lable mit dem Titel und erscheint neben den Koordinaten.
* **Title**: Title des Elements. Es wird neben den Koordinaten erscheinen, wenn 'Beschriftung anzeigen' aktiviert ist.
* **Target**: ID des Kartenelements.
* **Gruppe**: Optionaler Gruppenname.
* **Tooltip**: Der eingegebene Text wird angezeigt, wenn mit dem Cursor über ein Element geht.
* **Icon**: Sie können ein Icon für den Knopf in der Anwendung wählen.

Nach der Wahl der Applikation steht in den Einstellungen das Daten Laden unter der Sektion des Seitenpanels als oder an der oberen Leiste.
Anschließend wird das Daten Laden in Mapbender auf der Seite angezeigt und neue Dateien können über drag and drop oder auf 'Datei wählen' klicken, um im Ordnersystem nach einer Datei zu suchen.

.. image:: ../../../figures/dataupload.png
     :scale: 100

Nachdem das Polygon hochgeladen wurde, wird es auf der Karte und Sidepane angezeigt.
Dort können Sie es (un)sichtbar machen, auf den Punkt, die Linie oder das Polygon zoomen oder den Layer löschen.

YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml
     
     dataupload:
     class: Mapbender\CoreBundle\Element\DataUpload
     target: map
     maxFileSize: 10
     helpText: mb.core.dataupload.admin.helpText