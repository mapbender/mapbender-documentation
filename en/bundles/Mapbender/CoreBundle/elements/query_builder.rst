.. _query_builder:

Query Builder 
**************

The Query Builder  is a query tool that allows you to include, display and edit SQL queries and their result via the application interface.
You can:

* create
* edit,
* save, 
* remove,
* execute, 
* print,
* export and
* search in

the SQL queries.


Configuration
=============


.. image:: ../../../../../figures/query_builder_configuration_1.png
     :scale: 80

You can use the element in the sidepane.This is displayed in the layout list and allows you to distinguish between several elements.

* **Title:** Title of the element.
* **Source:** database source (predefined in the parameters.yml (e.g. mapbender_sqls)
* **SQL field name:** Table column with the SQL query (e.g. sql_definition)
* **Order by field name:** Table column for specifying the order in the SQL query table (e.g. anzeigen_reihenfolge)
* **Title field name:** Table column with the name of the SQL query. Appears later in the SQL query table as the title (e.g. name)
* **Connection field name:** Table column with the database source of the SQL query (e.g. connection_field_name)
* **Allow create:** Gives the permission to create new queries. Not activated per default. 
* **Allow edit:** Gives the permission to edit the queries. Not activated per default.


.. image:: ../../../../../figures/query_builder_configuration_2.png
     :scale: 80

* **Allow save:** Gives the permission to save changes in the queries. Not activated per default.
* **Allow remove:** Gives the permission to remove queries. Not activated per default.
* **Allow execute:** Gives the permission to execute queries. Activated per default.
* **Allow print:** Gives the permission to print the results of queries. Activated per default.
* **Allow export:** Gives the permission to export the results of queries. Activated per default.
* **Allow search:** Gives the permission to search for a query/ results of queries. Not activated per default.

Define a Database Connection
-----------------------------

The query tool requires access to the database in which the tables to be edited are located. 
To use the function, a database connection and a DataStore connection to this database must be set up in the parameters.yml.
For more information on database access, see http://doc.mapbender3.org/en/book/database.html

Configuration example for the parameters.yml:

.. code-block:: yaml

    ...
    database2_driver:   pdo_pgsql
    database2_host:     localhost
    database2_port:     5432
    database2_name:     search_db
    database2_path:     ~
    database2_user:     postgres
    database2_password: [secret]
    
    ...
    # insert the following definition at end of the parameters.yml              
    # for the DataStore connection
    ...

    dataStores:
        mapbender_sqls:
            connection: search_db
            table: search_db.mapbender_sqls
            uniqueId: id
            #filter: anzeigen = '1'   #optionally a filter can be integrated for later display

After this connection has been entered, an administration table for the query definitions can be created in the database, 
which is then queried via the query tool in Mapbender3.

table to store the query definitions and metadata
--------------------------------------------------

This administration table can be created in an existing database using the following SQL command:

.. image:: ../../../../../figures/query_builder_abfrage_tabelle.png
     :scale: 80

Diese Administrationstabelle kann über den folgenden SQL-Befehl in einer bestehenden Datenbank angelegt werden: 

.. code-block:: yaml

    CREATE TABLE abfragen
    ( 
      id serial NOT NULL,   
      name character varying,  -- name of the query
      sql_definition text,     -- SQL definition for the query
      anzeigen integer,        -- specify whether query should appear in the list
      anzeigen_reihenfolge integer, -- order of the query display
      CONSTRAINT pk_abfragen_id PRIMARY KEY (id)
    )
    WITH (
      OIDS=TRUE
    );


The following demodata with SQL queries can be used for the exemplary use.
The SQL commands for the creation of the queried tables can be found in the documentation for the digitizer element.

.. code-block:: yaml
                
    INSERT INTO abfragen (name, sql_definition, anzeigen, anzeigen_reihenfolge) VALUES ('Point', 'SELECT * FROM public.poi;', NULL, 2);
    INSERT INTO abfragen (name, sql_definition, anzeigen, anzeigen_reihenfolge) VALUES ('Polygon', 'SELECT * FROM public.polygon;', NULL, 3);
    INSERT INTO abfragen (name, sql_definition, anzeigen, anzeigen_reihenfolge) VALUES ('Line', 'SELECT * FROM public.line;', NULL, 4);
    INSERT INTO abfragen (name, sql_definition, anzeigen, anzeigen_reihenfolge) VALUES ('Interests', 'SELECT * FROM public.interests;', NULL, 1);

+------------+---------------------------------+----------------------+
|    name    |         sql_definition          | anzeigen_reihenfolge |
+============+=================================+======================+
|    Point   | SELECT * FROM public.poi;       |          2           |
+------------+---------------------------------+----------------------+
|  Polygon   | SELECT * FROM public.lines;     |          3           |
+------------+---------------------------------+----------------------+
|    Line    | SELECT * FROM public.polygons;  |          4           |
+------------+---------------------------------+----------------------+
| Interests  | SELECT * FROM public.interests; |          1           |
+------------+---------------------------------+----------------------+

After the administration table has been created and already contains demodata, you must now include the element in the sidepane of the Mapbender3 application. 
To do this, you can use the settings described in the "Configuration" section.


Functions
-----------

After embedding in the sidebar, the queries are displayed in a list and all the activated functions can be used via buttons.
Simultaneously to the activated functions in Mapbender3, the queries can be edited and adapted directly in the database.

.. image:: ../../../../../figures/query_builder_sidepane.png
     :scale: 80

The buttons to the right of an entry have the following functions:

* **Export:** The results of the query can be exported in EXCEL format.
* **HTML-Export:**  The results of the query can be displayed in HTML format. This opens a new dialog with the tabular display of the results.
* **Execute:** The results of the query can be displayed in a dialog. The results listed in the table can be sorted in descending or ascending order. You can use the buttons *export* and *HTML-Export** to export the results.
* **Change:** The SQL query can be edited (like "create new queries"). 
* **Delete:** The query can be deleted.

.. image:: ../../../../../figures/query_builder_buttons.png
     :scale: 80

The *plus-button* allows you to **create new queries**. 

.. image:: ../../../../../figures/query_builder.png
     :scale: 80

The title, the connection name to the database, and the sort number must be specified. Optionally, the checkbox *display* can be activated.
An SQL query can now be written into the large input field. *Save* will save the query and then you can select it from the list. 
Clicking on *Run* opens a dialog box with the results of the query. Here you can test whether the query works and all results are displayed correctly.

.. image:: ../../../../../figures/query_builder_anzeige.png
     :scale: 80

You can export the results of the query with the button *export* and *HTML-export*. 

The *delete* button can be used to delete the query and you can cancel the creation via the *cancel* button.

Under the button to create a query is the *search* function. Here you can search for a query from the list. 


YAML-Definition
-----------------

.. code-block:: yaml
                
 title: Abfragen                              # Title of the element.
  configuration:
    source: mapbender_sqls                    # name of the dataStore (predefined in the parameters.yml).
    allowedSchemas: {  }                      # Optional feature: name of the queryable schemas in the source, like public. 
    allowRemove: true                         # Gives the permission to remove queries. Defaul is false.
    allowEdit: true                           # Gives the permission to edit the queries. Default is false.
    allowExecute: true                        # Gives the permission to execute queries. True is default.
    allowSave: true                           # Gives the permission to save changes in the queries. False is default.
    allowCreate: true                         # Gives the permission to create new queries. False is default.
    allowExport: true                         # Gives the permission to export the results of queries in EXCEL format. True is default.
    allowHtmlExport: true                     # Gives the permission to export the results of queries in HTML format. True is default.
    allowPrint: true                          # Gives the permission to print the results of queries. True is default.
    allowUserPublishing: true                 # Gives the permission to publish the results of queries.
    idFieldName: id                           # Table column with the ID.
    sqlFieldName: sql_definition              # Table column with the SQL query.
    orderByFieldName: anzeigen_reihenfolge    # Table column for specifying the order in the SQL query table. 
    connectionFieldName: connection_field_name      # Table column with the database source of the SQL query. 
    titleFieldName: name                      # Table column with the name of the SQL query. Appears later in the SQL query table as the title.
    tableColumns:                             # Table columns with title of the SQL query.
      -
        data: name
        title: Title
    allowSearch: true                         # Gives the permission to search for a query/ results of queries. False is default.


Class, Widget & Style
======================

* **Class:** Mapbender\DataSourceBundle\Element\QueryBuilderElement
* **Widget:** mapbender.element.QueryBuilderElement.js
* **Style:** mapbender.elements.css


HTTP Callbacks
==============

none.

JavaScript API
==============

none.


JavaScript Signals
==================

none.
