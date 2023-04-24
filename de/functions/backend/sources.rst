.. _sources_de:

  .. |mapbender-button-update| image:: ../../../figures/mapbender_button_update.png

Datenquellen (Sources)
======================

Über die Datenquellen können Sie OGC-WMS Dienste in der Version 1.1.1 und 1.3.0 in Mapbender registrieren. Informationen zum Einbinden von Diensten und der Nutzung in Mapbender finden Sie im `Quickstart Dokument <../../quickstart.html#laden-von-web-map-services>`_.

.. image:: ../../../figures/de/source_wms.png
     :width: 100%

* **Typ**: Vordefinierte Datentypauswahl (OGC WMS bzw. OGC WMTS / TMS).

* **Dienst-URL**: URL zum Capabilities-Dokument des Dienstes (z.B.: ``http://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities``)

* **Benutzername / Passwort**: Eingabe von Benutzername und Passwort bei gesicherten Diensten.


In der Regel verweisen OGC-WMS Capabilities auf ``xsi:schemaLocation="http://www.opengis.net/wms http://schemas.opengis.net/wms/1.3.0/capabilities_1_3_0.xsd``. Die dort unterstützen Namensräume sind:
  
  * http://www.w3.org/1999/xlink,
  * http://www.opengis.net/wms,
  * http://www.w3.org/2001/XMLSchema


Datenquellen aktualisieren
--------------------------
Die Aktualisierung einer Datenquelle erfolgt zunächst über den Aufruf der Seite ``Datenquellen`` im Backend.
Wählen Sie aus der Liste die zu aktualisierende Datenquelle aus. Es ist möglich, die Liste anhand des Suchfelds nach Diensten zu filtern.
Klicken Sie anschließend neben der gewünschten Datenquelle auf den |mapbender-button-update| ``Datenquelle aktualisieren``-Button.
Dadurch öffnet sich die Aktualisierungsmaske. Hier können Sie die URL oder Benutzername / Passwort des Dienstes aktualisieren.

.. hint:: Datenquellen lassen sich über diese Maske auch aktualisieren, ohne dass Änderungen vorgenommen wurden.

Zusätzlich bietet die Maske zwei Checkboxen an:

* **Neu hinzugefügte Layer aktivieren**: Ist der Haken an dieser Checkbox gesetzt, werden durch die Aktualisierung neu geladene Dienst-Layer automatisch in eingebundenen Anwendungen aktiv.
* **Neu hinzugefügte Layer auswählen**: Ist der Haken an dieser Checkbox gesetzt, werden durch die Aktualisierung neu geladene Dienst-Layer automatisch in Anwendungen sichtbar. Hinweis: Zur Anzeige im Kartenbereich müssen sie zusätzlich aktiviert werden.

Sofern die Datenquelle nicht aktualisiert werden soll, kann der ``Abbrechen``-Button genutzt werden, um alle getätigten Änderungen zu verwerfen.
Falls die Änderungen vorgenommen werden sollen, klicken Sie auf den ``Laden``-Button, um die Datenquelle zu aktualisieren. Die aktualisierte Version wird anschließend in den Konfigurationseinstellungen angezeigt.