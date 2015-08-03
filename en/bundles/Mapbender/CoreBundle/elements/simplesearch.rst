.. _simplesearch:

SimpleSearch
************

SimpleSearch offers a one-step solution for geodata querying, powered by Solr for example. Giving only one input field
which can be directly embedded into the toolbar, it will send the entered search term to a configurable URL where it
expects to receive a JSON-formatted data back which inclucdes a label and a geometry attribute for each entry.

Geometry data can be encoded as WKT or in GeoJSON format.


Configuration
=============

.. image:: ../../../../../figures/simplesearch_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Query URL:** Solr URL for the search.
* **Query URL key:** The query parameter key to append.
* **QUery key format:** Simpe search format.
* **Token search/ replace (JavaScript regex):** Tokenizer split/ search/ replace regexp.
* **Collection path:** Can be a dotted attribute path to extract from the query result.
* **Label attribut:** Name of the attribute to use for entry labeling.
* **Geom attribut:** Name of the geometry data attribute. 
* **Geom format:** geometry data format, can be WKT or GeoJSON.
* **Delay:** Autocomplete delay. Use 0 to disable autocomplete.
* **Result buffer:** buffer result geometry with this (map units) before zooming.
* **Result minscale/ maxscale:** scale restrictions for zooming, ~ for none.
* **Result icon url:** icon to display as result marker.
* **Result ion offset:**  Offset x and y for the Icon.

YAML-Definition:
----

.. code-block:: yaml

   query_url: http://example.com/solr/core/0/select?wt=json&indent=true&rows=8   # Example Solr URL
   query_key: q                                                                  # The query parameter key to append
   query_ws_replace:                                                             # Parameter name to send search term with.
   query_format: '%s'                                                            # Simpe search format.
   token_regex: [^a-zA-Z0-9äöüÄÖÜß]                                              # Tokenizer split regexp.
   token_regex_in: ([a-zA-ZäöüÄÖÜß]{3,})                                         # Tokenizer search regexp.
   token_regex_out: '$1*'                                                        # Tokenizer replace regexp.
   collection_path: response.docs                                                # Can be a dotted attribute path to extract from the query result.                                             
   label_attribute: label                                                        # Name of the attribute to use for entry labeling
   geom_attribute: geom                                                          # Name of the geometry data attribute
   geom_format: WKT                                                              # geometry data format, can be WKT or GeoJSON
   delay: 300                                                                    # Autocomplete delay. Use 0 to disable autocomplete.
   result_buffer: 50                                                             # buffer result geometry with this (map units) before zooming
   result_minscale: 1000                                                         # scale restrictions for zooming, ~ for none
   result_maxscale: 5000
   result_icon_url: http://demo.mapbender3.org/bundles/mapbendercore/image/pin_red.png # icon to display as result marker
   result_icon_offset: -6,-38                                                    # Offset x and y for the Icon
   

Class, Widget & Style
=========================

* **Class:** Mapbender\\PrintBundle\\Element\\SimpleSearch
* **Widget:** mapbender.element.simplesearch.js

HTTP Callbacks
==============

- /search: Widget proxy which then queries configured URL. In dev mode the final query URL will be returned as a
  x-mapbender-simplesearch-url header for easier debugging.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
