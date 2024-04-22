.. _share_overview_de:

Share-Elemente: Überblick
=========================

Mapbender bietet eine Vielzahl an Elementen, die die gemeinsame Arbeit mit Kartenanwendungen erleichtern:

* :ref:`shareurl_de` ermöglicht das schnelle Teilen von selbstkonfigurierten Kartenanwendungszuständen via URL,
* :ref:`view_manager_de` speichert Kartenzustände und erstellt eine Liste dieser in der Sidepane,
* :ref:`applicationswitcher_de` ermöglicht den einfachen Wechsel zwischen Anwendungen,
* :ref:`persistent_map_view_de` ermöglicht das Speichern des Kartenzustands im Browser.

Außerdem übergibt Mapbender einige Parameter automatisch in der Anwendungs-URL. 
Dadurch ist es möglich, aktuell gewählte Einstellungen durch Teilen der URL an andere weiterzuleiten. 

Die URL beinhaltet folgende Parameter:

* Kartenposition
* Maßstab
* Drehung
* Räumliches Referenzsystem

Diese Funktion muss nicht extra konfiguriert werden. Sie ist immer aktiviert.

Wenn eine URL in einem neuen Browserfenster geöffnet wird, dann erfolgt auch die Übernahme der genannten Kartenparameter. Änderungen können über die Browsernavigation vor- bzw. zurückgenommen ("Weiter" oder "Zurück") werden.

Nach dem Neuladen des Browserfensters werden Anwender zum jeweiligen Kartenausschnitt zurückgesetzt, sofern die Parameter nicht in der URL übergeben werden. Soll zur Start-Konfiguration zurück navigiert werden, dann muss die Anwendung entweder neu geöffnet werden oder eine manuelle Anpassung der URL erfolgen.

.. note:: Folgende Eigenschaften werden nicht in der URL hinterlegt: temporäre Layer-Auswahl und Layer-Sortierung, temporäre Geometrien, angepasste Transparenzwerte, interaktiv hinzugefügte Instanzen oder andere Laufzeitergänzungen.
