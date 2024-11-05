.. _routing:

Routing
*******

The routing element adds a routing tool to an application. After specifying the start, destination and any intermediate points, a suitable route is displayed on the map. Information about the route can also be displayed.

.. image:: ../../../figures/de/routing.png
     :scale: 70

Configuration
=============


.. image:: ../../../figures/de/routing_configuration.png
     :scale: 70

* **Advanced route settings:** Allows you to make further settings.
* **Title:** Elements Title.
* **Route immediately:** Configuration to deactivate/activate automatic routing without the users interaction (default: false).
* **Allow intermediate points:** Configuration for deactivating/activating intermediate points (default: false).
* **Enable Search:** Configuration to deactivate/activate the search option (default: false).
* **Reverse Geocoding:** 
* **Zoom buffer (m):** Definition of a zoom buffer for the result display in meters (default: 0).
* **Line color:** Option to adjust the line color (default: #4286F4).
* **Line width:** Option to adjust the line width (default: 3).
* **Line opacity:** Adjust the line opacity via a slider (default: max).
* **Route info text:** Option to add an info text for the rout (default: {start} → {destination} </br> {length} will take {time}).
* **Time output format:** Adjust the time format (default: ms).

.. image:: ../../../figures/de/routing_configuration_icons.png
     :scale: 70

* **Path start icon:** Customize the start icon (default: /bundles/mapbenderrouting/image/start.png).
* **Path intermediate icon:** Customize the intermediate icon
* **Path destination icon:** Customize the destination icon (default: /bundles/mapbenderrouting/image/destination.png).
* **Size Icon:** Adjust the size of the different icons.
* **Offset Icon:** Adjust the offset of the different icons.

.. image:: ../../../figures/de/routing_configuration_service.png
     :scale: 70

* **Routing software:** Select the routing software (OSRM, GraphHopper, PgRouting, Trias).
* **URL:** Set the URL address for the routing software.
* **Services:** Select from various services (route, matrix, round trip, Mapbox Vector Tiles, next, match).
* **Transportation mode:** Select the routing profiles (car, bicycle, pedestrian). It is also possible to select more than one.
* **API-Version:** Determine the version of the API.
* **Alternative Route:**
* **Route description:** Select the routing description.
* **Annotations:**
* **Overview:**
* **continue Straight:**

.. image:: ../../../figures/de/routing_configuration_search.png
     :scale: 100

* **Search software:** Select the search service (currently only Solr).
* **Search URL:** Set the URL address for the search software (Solr).
* **Search parameter key:** Set the search parameter key.
* **Whitespace replacement pattern:**  Set parameters to replace the search term.
* **Search format:** Set the search format (in this example the SimpleSearch format is: %s). 
* **Tokenizer split/search/replace:** Set RegexFormat-split pattern/search pattern/replacement parameter (default: false).
* **Collection path:** Set the attribute path that is extracted from the query result (default: response.docs).
* **Label attribute:**
* **Geom attribute:**
* **Projection Geom:**
* **Geom format:**
* **Zoom buffer (m):**
* **Zoom buffer min./max.:**
* **Icon pfad:**
* **Icon offset (x,y):**



YAML-Definition
---------------

