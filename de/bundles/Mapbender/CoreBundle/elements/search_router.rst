.. _search_router:

Search Router
***********************

Dieses Element ist eine Such-Frontend Oberfläche für Suchmaschinen-Module. Zur Zeit wird eine generische SQL Suchmaschine unterstützt, weitere Entwicklungen werden folgen (z.B. Lucene Suche)

.. image:: ../../../../../figures/search_router.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/search_router_configuration.png
     :scale: 80

Für das Element wird ein Button verwendet. Siehe unter :doc:`button` für die Konfiguration.

Die Suche greift auf Tabellen in einer Datenbank zu. Dafür muss die Datenbank in Mapbender bekannt gegeben werden. Informationen dazu finden sich unter http://doc.mapbender3.org/de/book/database.html

Es können über den Button + mehrere Suchen (routes) erstellt werden. Jede Suche erhält im Feld titel einen Titel, über den die Suche nachher in einer Auswahlbox selektierbar ist.

Die Definition der Suche erfolgt im yaml-Syntax in einem Textfeld. Hier wird die Suchtabelle/Abfrage, die Datenverbindung, der Formularaufbau und die Trefferausgabe definiert. 


Element Definition im Web Administrationstool im Textfeld configuration:

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
        headers:
            gid: ID
            ortsname: Name
        callback:
            event: click
            options:
                buffer: 10
                minScale: null
                maxScale: null


YAML-Definition in der mapbender.yml Datei:

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
               headers:  # hash of table headers and the corresponding result columns
                   id: ID  # column name -> header label
                   name: Name
               callback:  # What to do on hover/click
                   event: click  # result row event to listen for (click or mouseover)
                   options:
                       buffer: 10  # buffer result geometry with this (map units) before zooming
                       minScale: ~  # scale restrictions for zooming, ~ for none
                       maxScale: ~

                       
Vergleichsmodus
--------------------------

Jedes Feld kann für einen Vergleichsmodus bestimmt werden, welcher von der Engine ausgewertet wird, wenn die Suchabfrage gestellt wird. Die SQL Suche Engine hat die folgenden Modi:


* exact: genauer Vergleich, Schlüssel = Wert (key = val)
* iexact: Vergleich, bei der Groß- / Kleinschreibung nicht unterschieden wird (case-insensitive)
* like: Standard, zweiseitiges 'like'
* like-left: linksseitiges 'like'
* like-right: rechtsseitiges 'like'
* **ilike**: zweiseitiges 'like', bei dem Groß- / Kleinschreibung nicht unterschieden wird (case-insensitive)
* ilike-left: linksseitiges 'like', bei dem Groß- / Kleinschreibung nicht unterschieden wird (case-insensitive)
* ilike-right: rechtsseitiges 'like', bei dem Groß- / Kleinschreibung nicht unterschieden wird (case-insensitive)
                       

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\SearchRouter
* Widget: mapbender.element.searchRouter.js, mapbender.element.searchRouter.Feature.js, mapbender.element.searchRouter.Search.js
* Style: mapbender.element.searchRouter.css

HTTP Callbacks
==============

<route_id>/autocomplete
-----------------------

Automatisch vervollständigter Ajax Endpunkt für die vorgegebene Suchroute. Die Autovervollständigung  wird unter Verwendung von Backbone.js eingesetzt. Das Autovervollständigung-Modul ist implementiert in mapbender.element.searchRouter.Search.js.

<route_id>/search
-----------------

Automatisch vervollständigter Ajax Endpunkt für die vorgegebene Suchroute. Die Suche  wird unter Verwendung von Backbone.js eingesetzt. Das Such-Modul ist implementiert in mapbender.element.searchRouter.Search.js.


JavaScript API
==============

open
----
Wenn das Modul als Dialog konfiguriert wird: open.

close
-----
Wenn das Modul als Dialog konfiguriert wird: close.

JavaScript Signals
==================

Keine.
