.. _share_overview_de:

Share-Funktionen: Überblick
===========================

Mapbender bietet eine Vielzahl von Funktionen, die die gemeinsame Arbeit mit Kartenanwendungen erleichtern:

* :ref:`shareurl_de` ermöglicht das schnelle Teilen von selbstkonfigurierten Kartenanwendungszuständen via URL,
* :ref:`view_manager_de` speichert Kartenzustände und erstellt eine Liste dieser in der Sidepane,
* :ref:`applicationswitcher_de` ermöglicht schnelle Applikationssprünge,
* :ref:`persistent_map_view_de` erleichtert die Anwendungskompatibilität mit dem Webbrowser.

Außerdem hinterlegt Mapbender bestimmte Kartenparameter automatisch in jeder Anwendungs-URL. 
Dadurch ist es möglich, aktuell gewählte Kartenparameter durch Teilen der URL an andere weiterzuleiten. 

Die URL beinhaltet folgende Parameter:

* Kartenposition
* Maßstab
* Drehung
* Räumliches Referenzsystem

Diese Funktion muss nicht extra konfiguriert werden. Sie ist immer aktiviert.

Wenn eine URL in einem neuen Browserfenster geöffnet wird, dann erfolgt auch die Übernahme der genannten Kartenparameter. Änderungen können über die Browsernavigation vor- bzw. zurückgenommen ("Weiter" oder "Zurück") werden.

Nach dem Neuladen des Browserfensters werden Anwender zum jeweiligen Kartenausschnitt zurückgeschickt. Soll zur Start-Konfiguration zurück navigiert werden, dann muss die Anwendung entweder komplett neu geöffnet werden oder eine manuelle Anpassung der URL erfolgen.

.. note:: Folgende Eigenschaften werden nicht in der URL hinterlegt: Layer-Auswahl, Layer-Sortierung, temporäre Geometrien, Laufzeitergänzungen, Transparenz, sowie interaktiv hinzugefügte Instanzen.
