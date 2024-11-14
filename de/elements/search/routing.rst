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
* **Linienfarbe:** Anpassen der Lineinfarbe und Deckkraft per rgba Standard (Standard: rgba(66, 134, 244, 1)).
* **Linienbreite:** Anpassen der Linienbreite (Standard: 3).
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
* **Wegbeschreibung ausgeben:** Auswählen ob es eine Wegbeschreibung geben soll oder nicht (Standard: false).

.. image:: ../../../figures/de/routing_configuration_search.png
     :scale: 87

* **Suchsoftware:** Auswählen des Such-Dienstes (derzeit nur Solr).
* **Query URL:** Setzen der URL-Adresse für die Suchsoftware (Solr).
* **Query URL-Parameter:** Der Suchparameterschlüssel, der angehängt wird (z.B. q).
* **Query Whitespace Ersetzung:** Setzen von Paramteren zum Ersetzung im Such-Therm.
* **Query Key Format:** Setzen des Such-Formats (Im diesem SimpleSearch Format Beispiel: %s).
* **Tokenizer Split/Such/Ersetzungs-Regex:** Setzen von RegexFormat-Teilungsmuster/-Suchmuster/-Ersetzungsparameter(Standard: false).
* **Pfas zu den Ergebnissen:** Setzen des Pfads, der vom Abfrageergebnis extrahiert wird (Standard: response.docs).
* **Attribut für Beschriftung:** Attribut oder mehrere Attribute , die als Ergebnis angezeigt werden sollen.
* **Attributname  für Geometrie:** Attributname der Geometrie (z.B. wgs84).
* **Geometrieformat:** Geometrieformat, kann WKT oder GeoJSON sein (z.B. WKT).
* **Quell-SRS:** EPSG-Code des primären Koordinatenbezugsystems (z.B. EPSG:4326).


YAML-Definition
---------------


