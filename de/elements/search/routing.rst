.. _routing_de:

Routing
*******

Das Routing-Element fügt einer Anwendung ein Streckenführung-Werkzeug hinzu. Nach Angabe von Start, Ziel und ggf. Zwischenpunkten wird eine geeignete Streckenführung in der Karte angezeigt. Zusätzlich können Informationen zur Strecke ausgegeben werden.

.. image:: ../../../figures/de/routing.png
     :scale: 70


Konfiguration
=============

.. image:: ../../../figures/de/routing_configuration.png
     :scale: 70

* **Erweiterte Einstellung:** Ermöglicht es weitere Einstellungen vorzunehmen (Standard: false).
* **Titel:** Titel des Elements.
* **Route direkt ausgeben:** Konfiguration zum Deaktivieren/Aktivieren des automatischen Routings ohne Interaktion des Nutzers (Standard: false).
* **Zwischenpunkte erlauben:** Konfiguration zum Deaktivieren/Aktivieren der Zwischenpunkten (Standard: false).
* **Suche aktivieren:** Konfiguration zum Deaktivieren/Aktivieren der Suchoption (Standard: false).
* **Geokodierung aktivieren:** Konfiguration zum Deaktivieren/Aktivieren der Geokodierung (Standard: false).
* **Zoompuffer(m):** Definition eines Zoompuffers für die Ergebnisanzeige in Meter (Standard: 0).
* **Linienfarbe:** Anpassen der Lineinfarbe (Standard: #4286F4).
* **Linienbreite:** Anpassen der Linienbreite (Standard: 3).
* **Liniendeckkraft:** Anpassen der Liniendeckkraft per Schieberegler (Standard: max).
* **Infotext zur Route:** Option einen Infotext zur Route zu implementieren (Standard: {start} → {destination} </br> {length} will take {time}).
* **Zeitformat:** Anpassen des Zeitformats (Standard: ms).

.. image:: ../../../figures/de/routing_configuration_icons.png
     :scale: 70

* **Pfad Starticon:** Anpassen des Starticons (Standard: /bundles/mapbenderrouting/image/start.png).
* **Pfad Zwischenicon:** Anpassen des Zwischenicons.
* **Pfad Zielicon:** Anpassen des Zielicons (Standard: /bundles/mapbenderrouting/image/destination.png).
* **Größe Icons:** Die Größe der verschiedenen Icons ist anpassbar.
* **Offset icons:** Das Offset der verschiedenen Icons ist anpassbar.

.. image:: ../../../figures/de/routing_configuration_service.png
     :scale: 70

* **Routingsoftware:** Auswählen der Routingsoftware (OSRM, GraphHopper, PgRouting, Trias).
* **URL:** Setzen der URL-Adresse für die Routingsoftware.
* **Services:** Auswahl aus verschiedenen Services (Route, matrix, Rundreise, Mapbox Vector Tiles, nächste, übereinstimmen).
* **Transportmodus:** Auswählen der Routing-Profile (Auto, Fahhrad, Füßgänger). Auch die Auswahl mehrerer ist möglich.
* **API-Version:** Version der API bestimmen.
* **Alternativ Route:** 
* **Routingeschreibung:** Auswählen der Routingbeschreibung.
* **Anmerkungen:** 
* **Übersicht:**
* **direkt weitermachen:** 

.. image:: ../../../figures/de/routing_configuration_search.png
     :scale: 100

* **Suchsoftware:** Auswählen des Such-Dienstes (derzeit nur Solr).
* **Such-URL:** Setzen der URL-Adresse für die Suchsoftware (Solr).
* **Suchparameterschlüssel:** Setzen des Suchparameterschlüssels.
* **Leerzeichenersetzung:** Setzen von Paramteren zum Ersetzung im Such-Therm.
* **Suchformat:** Setzen des Such-Formats (Im diesem SimpleSearch Format Beispiel: %s).
* **Tokenizer spaltet/sucht/ersetzt:** Setzen von RegexFormat-Teilungsmuster/-Suchmuster/-Ersetzungsparameter(Standard: false).
* **Attributspfad:** Setzen des Attributspfads, der vom Abfrageergebnis extrahiert wird (Standard: response.docs).
* **Attributname:** 
* **Attributname Geodaten:** 
* **Projektion Geodaten:** 
* **Geodatenformat:** 
* **Zoompuffer (m):** 
* **Zoompuffer min./max.:** 
* **Symbol-Pfad:** 
* **Versatz des Symbols (x,y):** 


YAML-Definition
---------------


