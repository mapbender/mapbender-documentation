.. _search_router:

Search Router
*************

Search frontend GUI for plugable search engine modules. Right now a SQL search engine
is provided.

.. image:: ../../../figures/search_router.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/search_router_configuration.png
     :scale: 80


The SearchRouter needs access to the database where the search tables are. You have to define a new database configuration to be able to connect with the geo database. Read more about this at :ref:`database`.

Example for a PostgreSQL database on localhost, called gisdb:


Content in config.yml:

.. code-block:: yaml
   
     doctrine:
         dbal:
             default_connection: default    
             connections:
                 default:
                     [...]
                 gisdb:
                     driver:   %gisdb_database_driver%
                     host:     %gisdb_database_host%
                     port:     %gisdb_database_port%
                     dbname:   %gisdb_database_name%
                     path:     %gisdb_database_path%
                     user:     %gisdb_database_user%
                     password: %gisdb_database_password%
                     persistent: true
                     charset:  UTF8
                     logging: %kernel.debug%
                     profiling: %kernel.debug%
   


Content in parameters.yml

.. code-block:: yaml

    parameters:
        [...]
        gisdb_database_driver:   pdo_pgsql
        gisdb_database_host:     localhost
        gisdb_database_port:     5432
        gisdb_database_name:     gisdb
        gisdb_database_path:     null
        gisdb_database_user:     reader
        gisdb_database_password: mypassword




* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Target:** Id of Map element to query.
* **Dialog:** Render inside a dialog or not.
* **Timeout factor:** Timeout factor (multiplied with autcomplete delay) to prevent autocomplete right after a search has been started.
* **Width:**  Width of the dialog (only for dialog, not sidepane)
* **Height:**  Height of the dialog (only for dialog, not sidepane)
* **Routes:** Collection of search routes.

You can define Searches (Routes) with the ``+`` Button. Each Search has a *Title* and a *Configuration. The title is shown in the application in a drop-down-box to choose from different searches.. The definition of the search is done in the *Configuration* text-field in YAML-syntax. Here you define the search-table and request, the database-connection, the form-elements and the display of the results.

The element can be placed in the sidebar or as a dialog. If you want to use it as a dialog you probably need a button to open that. Refer to :ref:`button` for details.


Example
-------

The following example uses the german geographical names data in 1:250.000 from the `Bundesamt für Kartographie und Geodäsie <http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=deu&gdz_akt_zeile=5&gdz_anz_zeile=1&gdz_unt_zeile=20>`_. The data was extracted to ``gn250_p`` table in the ``gisdb`` database (see parameters.yml above) and can be used for the search. The data has some specific columns:

- id: the id of the dataset
- name: the name of the dataset
- kreis: the administrative county (not for every dataset)
- oba_wert: the type of data (e.g. station, museum, etc.)


Example of a route-configuration in the ``configuration`` area:

.. code-block:: yaml

    class: Mapbender\CoreBundle\Component\SQLSearchEngine
    class_options:
      connection: gisdb
      relation: gn250_p
      attributes:
        - id
        - name
        - kreis
        - oba_wert
      geometry_attribute: geom
    form:
      name:
        type: text
        options:
          required: true
        compare: ilike
    results:
      view: table
      count: true
      headers:
        id: ID
        name: Name
        kreis: Landkreis
        oba_wert: Art
      callback:
        event: click
        options:
          buffer: 10
          minScale: null
          maxScale: null




Compare modes
-------------

Each field can be assigned a compare mode which is evaluated by the engine when building the search query. The SQL search
engine has the following modes:

* **exact:** exact comparison (key = val)
* **iexact:** case-insensitive comparison
* **like:** default, uses two-sided like
* **like-left:** uses left-sided like
* **like-right:** uses right-sided like
* **ilike:** uses two-sided case-insensitive like (*searchstring*)
* **ilike-left:** uses left-sided case-insensitive like (f.e *searchstring*)
* **ilike-right:** uses right-sided case-insensitive like (f.e searchstring*) 



Result feature styling
----------------------

By default, the result features are styled using the default styles OpenLayers provides. This gives the
well-known orange look and blue look for the selected feature.

.. image:: ../../../figures/de/search_router_example_colour_orangeblue.png
     :scale: 80

If you want to override that, you can provide a styleMap configuration for the results like this:

.. code-block:: yaml

    results:
        [...]
        styleMap:
            default:
                strokeColor: '#00ff00'  # Umrandungsfarbe
                strokeOpacity: 1        # 1 - opak (keine Transparenz)
                strokeWidth: 3          # Umrandingsbreite
                fillColor: '#f0f0f0'    # Füllfarbe                
                fillOpacity: 0          # Opazität Füllung, voll transparent, daher keine Füllung
                pointRadius: 6          # Größe des Punktsymbols
            select:
                strokeColor: '#0000ff'
                strokeOpacity: 1
                strokeWidth: 4
                fillColor: '#ff00ff'
                fillOpacity: 0.8
                pointRadius: 10
            temporary:
               strokeColor: '#0000ff'
               fillColor: '#0000ff'
               fillOpacity: 1


Three different styles are configured:


- **default**: The standard-style for all results
- **select**: The style used if a result is clicked.
- **temporary**: The styles used if you hover with the mouse-pointer over a result.der Tabelle bewegt.
               
This will not draw the point-symbol interiors, since the transparency is set to Zero (fillOpacity: 0). Only their outlines will be drawn in green. The selected features will be drawn here in with a purple fill and an opacity of 0.8. The stroke-Color is a blue line. The temporary symbols on mouse-hover are opaque blue points. The following screenshot shows this design:

.. image:: ../../../figures/de/search_router_example_colour_purplegreen.png
     :scale: 80

The default style properties will override the properties OpenLayers uses for the default style, therefore
you only need to set properties you wish to change. If you omit the default part, OpenLayers default style
will be used as is.

A similar logic applies to the select style – any property you provide will override the corresponding
property of the *final* default style. Therefore the example above will *not* yield a blue look for the
selected feature!

Keep in mind to quote hex color codes as the pound sign will otherwise be treated as a inline comment.



                

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\SearchRouter
* **Widget:** mapbender.element.searchRouter.js, mapbender.element.searchRouter.Feature.js, mapbender.element.searchRouter.Search.js
* **Style:** mapbender.element.searchRouter.css

HTTP Callbacks
==============

<route_id>/autocomplete
-----------------------

Autocomplete Ajax endpoint for given search route. Autocomplete is implemented
using Backbone.js with the Mapbender.Autocomplete model implemented in
mapbender.element.searchRouter.Search.js.

<route_id>/search
-----------------

Search Ajax endpoint for given search route. Search is implemented using
Backbone.js with the Mapbender.Search model implemented in
mapbender.element.searchRouter.Search.js.


Example
==================

Example with autocomplete and individual result style:

.. code-block:: yaml

   Create or Replace view brd.qry_gn250_p_ortslage as Select gid, name, gemeinde, bundesland, oba, ewz_ger,  hoehe_ger ,geom from brd.gn250_p where oba = 'AX_Ortslage' order by name;


.. code-block:: yaml

  class: Mapbender\CoreBundle\Component\SQLSearchEngine
  class_options:
      connection: search_db
      relation: brd.qry_gn250_p_ortslage
      attributes:
    - gid
    - name
    - gemeinde
    - bundesland
    - ewz_ger
    - hoehe_ger
      geometry_attribute: geom
  form:
      name:
    type: text
    options:
        required: false
        label: Name
        attr:
            data-autocomplete: on
    compare: ilike
      gemeinde:
    type: text
    options:
        required: false
    compare: ilike
  results:
      view: table
      count: true
      headers:
    name: Name
    gemeinde: Gemeinde
    bundesland: Bundesland
    ewz_ger: Einwohner
    hoehe_ger: Höhe
      callback:
    event: click
    options:
        buffer: 1000
        minScale: null
        maxScale: null
      styleMap:
    default:
        strokeColor: '#00ff00'
        strokeOpacity: 1
        fillOpacity: 0
    select:
        strokeColor: '#ff0000'
        fillColor: '#ff0000'
        fillOpacity: 0.8
    temporary:
        strokeColor: '#0000ff'
        fillColor: '#0000ff'
        fillOpacity: 1


Example with selectbox:

.. code-block:: yaml

   Create or Replace view brd.qry_gn250_p as Select gid, name, gemeinde, bundesland, oba, geom from brd.gn250_p where oba = 'AX_Ortslage' OR oba = 'AX_Wasserlauf' order by name;

.. code-block:: yaml

  class: Mapbender\CoreBundle\Component\SQLSearchEngine
  class_options:
      connection: search_db
      relation: brd.qry_gn250_p_ortslage
      attributes:
    - gid
    - name
    - gemeinde
    - bundesland
    - oba
      geometry_attribute: geom
  form:
      oba:
    type: choice
    options:
        empty_value: 'Bitte wählen...'
        choices:
            AX_Ortslage: Ort
            AX_Wasserlauf: 'Gewässer'
      name:
    type: text
    options:
        required: false
        label: Name
        attr:
            data-autocomplete: on
    compare: ilike
      gemeinde:
    type: text
    options:
        required: false
    compare: ilike
  results:
      view: table
      count: true
      headers:
    name: Name
    gemeinde: Gemeinde
    bundesland: Bundesland
      callback:
    event: click
    options:
        buffer: 1000
        minScale: null
        maxScale: null

