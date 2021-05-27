.. _simplesearch:

SimpleSearch
************

SimpleSearch offers a one-step solution for geo-data querying. Giving only one input field which can be directly embedded into the toolbar,
it will send the entered search term to a configurable URL where it expects to receive a JSON-formatted data back which includes a label and a geometry attribute for each entry.

Geometry data can be encoded as WKT or in GeoJSON format.

.. image:: ../../../figures/simplesearch.png
     :scale: 80


Configuration
=============

.. image:: ../../../figures/simplesearch_configuration_a.png
     :scale: 80

.. image:: ../../../figures/simplesearch_configuration_b.png
     :scale: 80


* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Query URL:** Solr URL for the search (e.g. ``http://localhost:8080/solr/core0/select?wt=json&indent=true``).
* **Query URL key:** The query parameter key to append  (e.g. ``q``).
* **Query Whitespace replacement pattern:** Pattern for replacing white spaces.
* **Query key format:** Simple search format  (e.g. ``%s``).
* **Token search/ replace (JavaScript regex):** Tokenizer split/ search/ replace regexp.

  * Token, e.g.: ``[^a-zA-Z0-9äöüÄÖÜß]``
  * Token search, e.g.: ``([a-zA-ZäöüÄÖÜß]{3,})``
  * Token replace, e.g.: ``$1*``
  
* **Collection path:** Can be a dotted attribute path to extract from the query result (e.g. ``response.docs``).
* **Label attribute:** Name of the attribute to use for entry labeling (e.g. ``label``).
* **Geom attribute:** Name of the geometry data attribute (e.g. ``geom``).
* **Geom format:** Geometry data format, can be WKT or GeoJSON (e.g. ``WKT``).
* **Source SRS:** EPSG code of the spatial reference system
* **Delay:** Autocomplete delay. Use 0 to disable autocomplete (e.g. ``300``).
* **Result buffer:** Buffer result geometry with this (map units) before zooming (e.g. ``10``).
* **Result minscale/ maxscale:** Scale restrictions for zooming, ~ for none  (e.g. ``1000`` und ``5000``).
* **Result icon url:** Icon to display as result marker (e.g. ``http://demo.mapbender.org/bundles/mapbendercore/image/pin_red.png``).
* **Result icon offset:**  Offset x and y for the icon (e.g. ``0,0``).


  
YAML-Definition
--------------------

.. code-block:: yaml

   query_url: http://example.com/solr/core/0/select?wt=json&indent=true&rows=8   # Example Solr URL (e.g. ``http://localhost:8080/solr/core/0/select?wt=json&indent=true``).
   query_key: q                                                                  # The query parameter key to append
   query_ws_replace:                                                             # Pattern for replacing white spaces.
   query_format: '%s'                                                            # Simple search format.
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
   result_maxscale: 5000                                                         # scale restrictions for zooming, ~ for none
   result_icon_url: http://demo.mapbender.org/bundles/mapbendercore/image/pin_red.png # icon to display as result marker
   result_icon_offset: -6,-38                                                    # Offset x and y for the icon
   

How to setup Solr
==================

* **Download**: http://lucene.apache.org/solr/
* **Documentation**: http://lucene.apache.org/solr/resources.html#documentation 
* **Quickstart**: http://lucene.apache.org/solr/quickstart.html

Class, Widget & Style
=========================

* **Class:** Mapbender\\CoreBundle\\Element\\SimpleSearch
* **Widget:** mapbender.element.simplesearch.js

HTTP Callbacks
==============

- /search: Widget proxy which then queries configured URL. In dev-mode the final query URL will be returned as a x-mapbender-simplesearch-url header for easier debugging.
