.. _share_de:

Share
=====

Das Share-Tool bietet eine Vielzahl von Funktionen, die die gemeinsame Arbeit mit Kartenanwendungen erleichtern: URL teilen ermöglicht das schnelle Teilen von selbstkonfigurierten Kartenanwendungszuständen via URL, Ansichtsverwaltung speichert Kartenzustände und erstellt eine Liste dieser in der Sidepane, Anwendung wechseln ermöglicht schnelle Applikationssprünge und Persistente Kartenzustände erleichtert die Anwendungskompatibilität mit dem Webbrowser.

Mapbender hinterlegt bestimmte Kartenparameter automatisch in jeder Anwendungs-URL. 
Dadurch ist es möglich, aktuell gewählte Kartenparameter durch Teilen der URL an andere weiterzuleiten. 

Die URL beinhaltet folgende Kartenparameter:

* Kartenposition
* Maßstab
* Drehung
* Räumliches Referenzsystem

Diese Funktion muss nicht extra konfiguriert werden. Sie ist immer aktiviert.

Wenn eine URL in einem neuen Browserfenster geöffnet wird, dann erfolgt auch die Übernahme der genannten Kartenparameter. Änderungen können über die Browsernavigation vor- bzw. zurückgenommen ("Weiter" oder "Zurück") werden.

Nach dem Neuladen des Browserfensters werden Anwender zum jeweiligen Kartenausschnitt zurückgeschickt. Soll zur Start-Konfiguration zurück navigiert werden, dann muss die Anwendung entweder komplett neu geöffnet werden oder eine manuelle Anpassung der URL erfolgen.

.. note:: **Hinweis:** Folgende Informationen werden nicht hinterlegt: Layer-Auswahl, Layer-Sortierung, temporäre Geometrien, Laufzeitergänzungen, Transparenz sowie interaktiv hinzugefügte Instanzen.

.. toctree::
   :maxdepth: 1

   share/shareurl.rst
   share/view_manager.rst
   share/applicationswitcher.rst
   share/persistant_map_view.rst

