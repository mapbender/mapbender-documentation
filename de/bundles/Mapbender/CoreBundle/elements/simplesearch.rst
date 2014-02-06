.. _simplesearch:

SimpleSearch
************

SimpleSearch bietet eine einstufige Lösung für Geodatenabfragen an, betrieben z.B. von Solr. Es wird ein Eingabefeld verwendet, welches direkt in die Toolbar eingebunden werden kann. Es sendet den eingegebenen Suchbegriff an eine konfigurierbare URL. Diese empfängt JSON-formatierte Daten, welche eine Beschriftung und Geometrieattribute für jeden Eintrag beinhaltet.

Die Geometriedaten können in WKT oder in GeoJSON-Format codiert werden.


Konfiguration
=============

YAML-Definition:

.. code-block:: yaml

   query_url: http://example.com/solr/core/0/select?wt=json&indent=true&rows=8   # Beispiel Solr URL
   query_key: q                                                                  # Der Suchparameterschlüssel, der angehängt wird
   collection_path: response.docs                                                # Es kann ein Attributspfad sein, der vom Abfrageergebnis extrahiert wird.
   label_attribute: label                                                        # Name des Attributs, das für die Beschriftung verwendet wird.
   geom_attribute: geom                                                          # Name der Attribute der Geometriedaten 
   geom_format: WKT                                                              # Geometiedatenformat,kann WKT oder GeoJSON sein
   delay: 300                                                                    # Automatische Vervollständigungs-Verzögerung. 0 wird zum Ausschalten der Automatischen Vervollständigung verwendet.

Class, Widget & Style
=========================

* Class: Mapbender\\PrintBundle\\Element\\SimpleSearch
* Widget: mapbender.element.simplesearch.js

HTTP Callbacks
==============

- /search: Proxy-Element, welches die konfigurierbare URL abfragt. Im Entwicklungsmodus wird die endgültige Abfrage-URL zum einfachen Debugging als ein x-mapbender-simplesearch-url header zurückgegeben.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
