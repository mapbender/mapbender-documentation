.. _sources_de:

Datenquellen (Sources)
======================

Über den Backend-Menübereich Datenquellen können OGC WMS- und WMTS/TMS-Dienste in den Versionen 1.1.1 und 1.3.0 registriert werden.

Informationen zum Einbinden von Diensten und die Nutzung in Anwendungen finden Sie im Schnellstart-Kapitel :ref:`load_sources_de`.


Datenquelle laden
-----------------

.. tip:: **Hinweis**: Es ist wichtig, dass die Datenquelle vor dem Hochladen auf ihre Richtigkeit überprüft wird. Dies erfolgt über den Aufruf des getCapabilities-Requests im Browser.

  .. |mapbender-button-add| image:: ../../figures/mapbender_button_add.png
    
Um einen Dienst zu laden, drücken Sie auf |mapbender-button-add| **Datenquelle hinzufügen**. Dies öffnet einen Konfigurationsbereich mit folgenden Parametern:

* **Typ**: Dropdown-Auswahl zwischen Datentyp OGC WMS und OGC WMTS / TMS (Pflichtangabe).

* **Dienst-URL**: URL zum Capabilities-Dokument des Dienstes (z. B. für `OGC WMS Version 1.3.0 <https://osm-demo.wheregroup.com/service?SERVICE=WMS&Version=1.3.0&REQUEST=GetCapabilities>`_)

* **Benutzername / Passwort**: Eingabe von Benutzername und Passwort bei gesicherten Diensten.


Mit einem Klick auf ``Laden`` wird der Dienst registriert.


  .. image:: ../../figures/de/mapbender_add_source.png
     :width: 100%


Nach einer erfolgreichen Dienstregistrierung zeigt Mapbender Informationen zum Dienst in einem Übersichtsfenster an.


Datenquellen - Übersicht
------------------------

Die Bereiche Datenquellen und Freie Instanzen listen die erfolgreich geladenen und konfigurierten Dienste auf:

* **Filter**: Filtert die Dienste nach kontextspezifischer Eingabe, berücksichtigt Name, URL, Typ und Beschreibung.
* **Metadaten anzeigen**: Zeigt die Metadaten eines ausgewählten Dienstes an. Öffnet einen neuen Bereich, der in mehreren Reitern Metadaten, Mapbender-Anwendungen mit Zugriff, Kontaktinformationen, Details (z.B. Version) und die Layer des Dienstes ausgibt.
* **Datenquelle aktualisieren**: Aktualisiert die Dienst-Informationen durch erneutes Laden des getCapabilities-Dokuments.
* **Datenquelle entfernen**: Entfernt den Dienst aus Mapbender.


  .. image:: ../../figures/de/mapbender_sources.png
     :width: 100%


Datenquellen-Kontextmenü
------------------------

Im Metadatendialog eines Dienstes befindet sich oben rechts außerdem das Datenquellen-Kontextmenü. Es ermöglicht folgende Funktionen:

* **Datenquelle aktualisieren**: Aktualisiert die Dienst-Informationen durch erneutes Laden des getCapabilities-Dokuments.
* **Freie Instanz erzeugen**: Erzeugt eine freie Instanz aus der Datenquelle. Diese wird im Bereich "Freie Instanzen" angezeigt. 
* **Löschen**: Entfernt die freie Instanz aus Mapbender.


  .. image:: ../../figures/de/source_overview.png
     :width: 100%


Datenquellen aktualisieren
--------------------------
  .. |mapbender-button-update| image:: ../../figures/mapbender_button_update.png

Die Aktualisierung einer Datenquelle erfolgt zunächst über den Aufruf der Seite ``Datenquellen`` im Backend.
Wählen Sie aus der Liste die zu aktualisierende Datenquelle aus. Es ist möglich, die Liste anhand des Suchfelds nach Diensten zu filtern.
Klicken Sie anschließend neben der gewünschten Datenquelle auf den |mapbender-button-update| **Datenquelle aktualisieren**-Button.
Dadurch öffnet sich die Aktualisierungsmaske. Hier können Sie auch die URL oder Benutzername / Passwort des Dienstes anpassen.

.. hint:: Datenquellen lassen sich auch aktualisieren, ohne dass Änderungen vorgenommen wurden. Das Capabilities-Dokument wird neu eingelesen.

Zusätzlich bietet die Maske zwei Checkboxen an:

.. image:: ../../figures/de/mapbender_update_source.png
     :width: 100%


* **Neu hinzugefügte Layer aktivieren**: Ist der Haken an dieser Checkbox gesetzt, sind durch die Aktualisierung neu geladene Dienst-Layer automatisch in Anwendungen aktiv. Ist der Haken nicht gesetzt, erscheinen neue Layer nicht im Ebenenbaum.
* **Neu hinzugefügte Layer auswählen**: Ist der Haken an dieser Checkbox gesetzt, werden durch die Aktualisierung neu geladene Dienst-Layer automatisch in Anwendungen sichtbar und sind aktiv. Dazu muss allerdings auch ``Neu hinzugefügte Layer aktivieren`` gesetzt sein. Ist ``Neu hinzugefügte Layer auswählen`` nicht gesetzt, erscheint der Layer zwar im Ebenenbaum, ist aber nicht aktiviert.

Falls die Änderungen vorgenommen werden sollen, klicken Sie auf den ``Laden``-Button, um die Datenquelle zu aktualisieren. Dabei wird das getCapabilities-Dokument neu ausgelesen. Die aktualisierte Version wird anschließend in den Konfigurationseinstellungen angezeigt und Änderungen werden in Anwendungen, in denen der Dienst verwendet wird, angewandt.

