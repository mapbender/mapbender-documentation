.. _search_router:

Search Router
***********************

Search frontend GUI for plugable search engine modules. Right now a generic SQL search engine
is provided, with more to come (think Lucene enhanced search, etc.)

.. image:: ../../../../../figures/search_router.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/search_router_configuration.png
     :scale: 80

You need a button to show this element. See :doc:`button` for inherited configuration options.

The SearcRouter needs access to the database where the search tables are. You have to define a new database configuration to be able to connect with the geo database. Read more about this at http://doc.mapbender3.org/en/book/database.html

You can define Searches (Routes) with the + Button. Each Search has a titel which will show up in the search form in a selectbox where you can choose the search you want to use.

The definition of the search is done in YAML syntax in the textarea configuration. Here you define the database connection, the Search tables/views, the desihn of the form and of the result table.

Element definition in web interface in the configuration area:

.. code-block:: yaml

    class: Mapbender\CoreBundle\Component\SQLSearchEngine
    class_options:
        connection: germany
        relation: ortschaften
        attributes:
            - gid
            - ortsname
        geometry_attribute: geom
    form:
        ortsname:
            type: text
            options:
                required: true
            compare: exact
    results:
        view: table
        count: true
        headers:
            gid: ID
            ortsname: Name
        callback:
            event: click
            options:
                buffer: 10
                minScale: null
                maxScale: null


YAML-Definition for mapbender.yml:

.. code-block:: yaml

   target: map  # for result visualization
   asDialog: true  # render inside a dialog or not
   timeoutFactor:  2  # timeout factor (multiplied with autcomplete delay) to prevent autocomplete right after a search has been started
   routes:      # collection of search routes
       demo_a:  # machine readable name
           title: Demo A  # human readable title
           class: Mapbender\CoreBundle\Component\SQLSearchEngine  # Search engine to use
           class_options:  # these are forwarded to the search engine
               connection: search_db  # DBAL connection name to use, use ~ for the default one
               relation: test.demo_a  # Relation to select from, you can use subqueries
               attributes: [id, name]  # array of columns to select, expressions are possible
               geometry_attribute: geom  # name of the geometry column to query
           form:  # search form configuration
               the_name:  # field name, use relation column name to query or anything else for splitted fields (see below)
                   type: text  # field type, usually text or integer
                   options:  # field options
                       required: true  # HTML5 required attribute
                       label: Custom Label  # Enter a custom label, otherwise the label will be derived off the field name
                       attr:  # HTML attributes to inject
                           data-autocomplete: on  # this triggers autocomplete
                           data-autocomplete-distinct: on  # This forces DISTINCT select
                           data-autocomplete-using: field_a,field_b  # comma-separated list of other field values to use in WHERE clause for autocomplete
                   split: [name, zusatz]  # optional field contents, might be split
                   autocomplete-key: id  # column name to return as autocomplete key instead of column value
                   compare: ~  # See note below for compare modes
               my_select:
                   type: choice
                   options:
                       empty_value: Please select a sex
                       choices:
                           m: Male
                           f: Female
                           u: Unknown
           results:
               view: table  # only result view type for now
               count: true # show number of results
               headers:  # hash of table headers and the corresponding result columns
                   id: ID  # column name -> header label
                   name: Name
               styleMap: ~  # See below
               callback:  # What to do on hover/click
                   event: click  # result row event to listen for (click or mouseover)
                   options:
                       buffer: 10  # buffer result geometry with this (map units) before zooming
                       minScale: ~  # scale restrictions for zooming, ~ for none
                       maxScale: ~

Compare modes
-------------

Each field can be assigned a compare mode which is evaluated by the engine when building the search query. The SQL search
engine has the following modes:

* exact: exact comparison (key = val)
* iexact: case-insensitive comparison
* like: default, uses two-sided like
* like-left: uses left-sided like
* like-right: uses right-sided like
* **ilike**: uses two-sided case-insensitive like
* ilike-left: uses left-sided case-insensitive like
* ilike-right: uses right-sided case-insensitive like


Result feature styling
----------------------

By default, the result features are styled using the default styles OpenLayers provides. This gives the
well-known orange look and blue look for the selected feature. If you want to override that, you can
provide a styleMap configuration for the results like this:

.. code-block:: yaml

    results:
        styleMap:
            default:
                fillOpacity: 0
            select:
                fillOpacity: 0.4

This will not draw polygon interiors, but only their outlines in default mode. The selected feature will
have it's interior drawn with 60% transparency.

The default style properties will override the properties OpenLayers uses for the default style, therefore
you only need to set properties you wish to change. If you omit the default part, OpenLayers default style
will be used as is.

A similar logic applies to the select style – any property you provide will override the corresponding
property of the *final* default style. Therefore the example above will *not* yield a blue look for the
selected feature!

Keep in mind to quote hex color codes as the pound sign will otherwise be treated as a inline comment!

A more elaborate example with green (hollow) features and the selected one in red:

.. code-block:: yaml

    results:
        styleMap:
            default:
                strokeColor: '#00ff00'
                strokeOpacity: 1
                fillOpacity: 0
            select:
                strokeColor: '#ff0000'
                fillColor: '#ff0000'
                fillOpacity: 0.4


Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\SearchRouter
* Widget: mapbender.element.searchRouter.js, mapbender.element.searchRouter.Feature.js, mapbender.element.searchRouter.Search.js
* Style: mapbender.element.searchRouter.css

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

JavaScript API
==============

open
----
If configured as dialog, open.

close
-----
If configured as dialog, close.

JavaScript Signals
==================

None.
