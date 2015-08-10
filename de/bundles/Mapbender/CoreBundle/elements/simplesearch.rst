.. _simplesearch:

SimpleSearch
************

SimpleSearch bietet eine einstufige Lösung für Geodatenabfragen an, betrieben wird diese z.B. von Solr. Es wird ein Eingabefeld verwendet, welches direkt in die Toolbar eingebunden werden kann. Es sendet den eingegebenen Suchbegriff an eine konfigurierbare URL. Diese empfängt JSON-formatierte Daten, welche eine Beschriftung und Geometrieattribute für jeden Eintrag beinhaltet.

Die Geometriedaten können in WKT oder in GeoJSON-Format codiert werden.

.. image:: ../../../../../figures/simplesearch.png
     :scale: 80


Konfiguration
=============

.. image:: ../../../../../figures/de/simplesearch_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Query URL:** Solr URL, an die der eingegebene Suchbegriff gesendet wird.
* **Query URL key:** Der Suchparameterschlüssel, der angehängt wird.
* **QUery key format:** Einfaches Suchformat.
* **Token search/ replace (JavaScript regex):** Tokenizer spaltet/ sucht/ ersetzt regexp.
* **Collection path:** Dies kann ein Attributspfad sein, der vom Abfrageergebnis extrahiert wird.
* **Label attribut:** Attrubutname der zur Beschriftung genutzt wird.
* **Geom attribut:** Name der Attribute der Geometriedaten 
* **Geom format:** Geometiedatenformat,kann WKT oder GeoJSON sein
* **Delay:** Automatische Vervollständigungs-Verzögerung. 0  
* **Result buffer:** Buffert die Geometrieergebnise (Karteneinheiten) vor dem Zoomen
* **Result minscale/ maxscale:** Maßstabsbegrenzung beim Zoomen
* **Result icon url:** Symbol, das zur Trefferanzeige verwendet werden soll
* **Result ion offset:** Offset x und y des Symbols



YAML-Definition:
----

.. code-block:: yaml

   query_url: http://example.com/solr/core/0/select?wt=json&indent=true&rows=8   # Beispiel Solr URL
   query_key: q                                                                  # Der Suchparameterschlüssel, der angehängt wird
   query_ws_replace:                                                             # Parameter Name to send search term with.
   query_format: '%s'                                                            # Einfaches Suchformat.
   token_regex: [^a-zA-Z0-9äöüÄÖÜß]                                              # Tokenizer split regexp.
   token_regex_in: ([a-zA-ZäöüÄÖÜß]{3,})                                         # Tokenizer search regexp.
   token_regex_out: '$1*'                                                        # Tokenizer replace regexp.
   collection_path: response.docs                                                # Es kann ein Attributspfad sein, der vom Abfrageergebnis extrahiert wird.
   label_attribute: label                                                        # Attrubutname der zur Beschriftung genutzt wird 
   geom_attribute: geom                                                          # Name der Attribute der Geometriedaten 
   geom_format: WKT                                                              # Geometiedatenformat,kann WKT oder GeoJSON sein
   delay: 300                                                                    # Automatische Vervollständigungs-Verzögerung. 0   result_buffer: 50                                                             # Buffert die Geometrieergebnise (Karteneinheiten) vor dem Zoomen
   result_minscale: 1000                                                         # Maßstabsbegrenzung beim Zoomen, ~ für keine Begrenzung
   result_maxscale: 5000
   result_icon_url: http://demo.mapbender3.org/bundles/mapbendercore/image/pin_red.png # Marker, der zur Trefferanzeige verwendet werden soll
   result_icon_offset: -6,-38                                                    # Offset x und y des Symbols
   

Class, Widget & Style
=========================

* **Class:** Mapbender\\PrintBundle\\Element\\SimpleSearch
* **Widget:** mapbender.element.simplesearch.js

HTTP Callbacks
==============

- /search: Proxy-Element, welches die konfigurierbare URL abfragt. Im Entwicklungsmodus wird die endgültige Abfrage-URL zum einfachen Debugging als ein x-mapbender-simplesearch-url header zurückgegeben.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.
