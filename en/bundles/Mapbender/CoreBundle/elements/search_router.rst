Search Router
***********************

Search frontend GUI for plugable search engine modules. Right now a generic SQL search engine
is provided, with more to come (think Lucene enhanced search, etc.)

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\SearchRouter
* Widget: mapbender.element.searchRouter.js, mapbender.element.searchRouter.Feature.js, mapbender.element.searchRouter.Search.js
* Style: mapbender.element.searchRouter.css

Configuration
=============

.. code-block:: yaml

   target: map  # for result visualization
   asDialog: true  # render inside a dialog or not
   timeoutFactor:  2  # timeout factor (multiplied with autcomplete delay) to prevent autocomplete right after a search has been started
   routes:      # collection of search routes
       demo_a:  # machine readable name
           title: Demo A  # human readable title
           class: Mapbender\CoreBundle\Component\SQLSearchEngine  # Search engine to use
           class_options:  # these are forwarded to the search engine
               connection: ~  # DBAL connection name to use, use ~ for the default one
               relation: test.demo_a  # Relation to select from, you can use subqueries
               attributes: [id, name]  # array of columns to select, expressions are possible
               geometry_attribute: geom  # name of the geometry column to query
           form:  # search form configuration
               the_name:  # field name, use relation column name to query or anything else for splitted fields (see below)
                   type: text  # field type, usually text
                   options:  # field options
                       required: true  # HTML5 required attribute
                       attr:  # HTML attributes to inject
                           data-autocomplete: on  # this triggers autocomplete
                   split: [name, zusatz]  # optional field contents, might be split
                   autocomplete-key: id  # column name to return as autocomplete key instead of column value
           results:
               view: table  # only result view type for now
               headers:  # hash of table headers and the corresponding result columns
                   id: ID  # column name -> header label
                   name: Name
               callback:  # What to do on hover/click
                   event: click  # result row event to listen for (click or mouseover)
                   options:
                       buffer: 10  # buffer result geometry with this (map units) before zooming
                       minScale: ~  # scale restrictions for zooming, ~ for none
                       maxScale: ~

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
