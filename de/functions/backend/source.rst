.. _source_de:

Datenquellen (Sources)
======================

Über den Backend-Menübereich Datenquellen können OGC WMS-Dienste in der Version 1.1.1 und 1.3.0 in Mapbender registriert werden.

Informationen zum Einbinden von Diensten und der Nutzung in Mapbender finden Sie im `Quickstart Dokument <../../quickstart.html#laden-von-web-map-services>`_.

.. image:: ../../../figures/de/source_wms.png
     :scale: 80

Quellen laden
-------------

.. tip:: **Hinweis**: Am sinnvollsten ist es, die Datenquelle vor dem Hochladen auf ihre Richtigkeit hin zu überprüfen.

#.  ``Datenquelle hinzufügen``: Button zum Hinzufügen eines WMS-Dienstes, öffnet einen Konfigurationsbereich mit folgenden Parametern:


* **Typ**: Dropdown-Auswahl zwischen Datentyp OGC WMS und OGC WMTS / TMS (Pflichtangabe).

* **Dienst-URL**: URL zum Capabilities-Dokument des WMS Dienstes (z.B.: ``http://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities``)

* **Benutzername / Passwort**: Eingabe von Benutzername und Passwort bei gesicherten Diensten.


#. Mit einem Klick auf ``Laden`` wird der Dienst in Mapbender registriert.

Nach einer erfolgreichen Dienstregistrierung zeigt Mapbender Informationen zum Dienst in einem Übersichtsfenster an.

  .. image:: ../figures/mapbender_add_source.png
     :scale: 80


  In der Regel verweisen OGC-WMS Capabilities auf ``xsi:schemaLocation="http://www.opengis.net/wms http://schemas.opengis.net/wms/1.3.0/capabilities_1_3_0.xsd``. Die dort unterstützen Namensräume sind:
  
  * http://www.w3.org/1999/xlink,
  * http://www.opengis.net/wms,
  * http://www.w3.org/2001/XMLSchema


Datenquellen - Übersicht
------------------------

Die Bereiche Datenquellen und Freie Instanzen listen die erfolgreich eingeladenen und konfigurierten Dienste auf:

* **Filter**: Filtert die Dienste nach kontextspezifischer Eingabe, berücksichtigt Name, URL, Typ und Beschreibung.
* **Metadaten anzeigen**: Zeigt die Metadaten eines ausgewählten Dienstes an. Öffnet einen neuen Bereich, der tabbasiert Metadaten, Mapbender-Anwendungen mit Zugriff, Kontaktinformationen, Details (z.B. WMS-Version) und die Dienstlayer ausgibt.
* **Datenquelle aktualisieren**: Bei Buttonklick wird der Bereich "Datenquelle aktualisieren" geöffnet, der den Service und die zugehörigen Metadaten aktualisiert.
* **Datenquelle entfernen**: Entfernt den Dienst aus Mapbender.


Datenquellen-Kontextmenü
------------------------

In the metadata dialog of a specific service, it is also possible to interact with a hamburger button menu (top right) that allows:

* **Datenquelle aktualisieren**: Bei Buttonklick wird der Bereich "Datenquelle aktualisieren" geöffnet, der den Service und die zugehörigen Metadaten aktualisiert.
* **Freie Instanz erzeugen**: Erzeugt eine freie Instanz aus der Datenquelle. Diese wird im Bereich "Freie Instanzen" angezeigt. 
* **Löschen**: Entfernt den Dienst aus Mapbender.
