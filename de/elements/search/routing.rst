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
* **Pfad Zwischenicon:** Anpassen des Zwischenicons (Standard: /bundles/mapbenderrouting/image/intermediate.png).
* **Pfad Zielicon:** Anpassen des Zielicons (Standard: /bundles/mapbenderrouting/image/destination.png).
* **Größe Icons:** Die Größe der verschiedenen Icons ist anpassbar.
* **Offset icons:** Das Offset der verschiedenen Icons ist anpassbar.

.. image:: ../../../figures/de/routing_configuration_service.png
     :scale: 70

* **Routingsoftware:** Auswählen der Routingsoftware (OSRM, GraphHopper, PgRouting, Trias).
* **URL:** Setzen der URL-Adresse für die Routingsoftware (Standard: https://).
* **Services:** Auswahl aus verschiedenen Services (Standard: Route).
* **Transportmodus:** Auswählen der Routing-Profile (Auto, Fahhrad, Füßgänger). Auch die Auswahl mehrerer ist möglich (Standard: false).
* **API-Version:** Version der API bestimmen (Standard: v1).
* **Wegbeschreibung ausgeben:** Auswählen ob es eine Wegbeschreibung geben soll oder nicht (Standard: nein).

.. image:: ../../../figures/de/routing_configuration_search.png
     :scale: 87

* **Suchsoftware:** Auswählen des Such-Dienstes (derzeit nur Solr).
* **Query URL:** Setzen der URL-Adresse für die Suchsoftware.
* **Query URL-Parameter:** Der Suchparameterschlüssel, der angehängt wird (Standard: q).
* **Query Whitespace Ersetzung:** Setzen von Paramteren zum Ersetzung im Such-Therm.
* **Query Key Format:** Setzen des Such-Formats (Standard: %s).
* **Tokenizer Split/Such/Ersetzungs-Regex:** Setzen von RegexFormat-Teilungsmuster/-Suchmuster/-Ersetzungsparameter(Standard: false).
* **Pfas zu den Ergebnissen:** Setzen des Pfads, der vom Abfrageergebnis extrahiert wird (Standard: response.docs).
* **Attribut für Beschriftung:** Attribut oder mehrere Attribute , die als Ergebnis angezeigt werden sollen (Standard: label).
* **Attributname  für Geometrie:** Attributname der Geometrie (Standard: geom).
* **Geometrieformat:** Geometrieformat, kann WKT oder GeoJSON sein (Standard WKT).
* **Quell-SRS:** EPSG-Code des primären Koordinatenbezugsystems (Standard EPSG:4326).


YAML-Definition
---------------


