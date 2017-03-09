.. _data_manager:

Data Manager
************

The Data Manager element allows to edit data without geometry. Currently you can build up your formular-interface for data editing with a YAML-definition (like in the Digitizer element). 

The Data Manager-Element offers complex functionality:

  * add data
  * delete data
  * change data attributes 

Comparable to the Digitizer, you can define complex forms for the attributes.

.. image:: ../../../../../figures/datamanager/data_manager.png
     :scale: 90


Configuration
=============

.. image:: ../../../../../figures/datamanager/data_manager_configuration.png
     :scale: 80


* **Title:** Title of the element. 
* **Schemes:** YAML-Definition of the element.

The Data Manager needs access to a database where the editable tables are. You have to define a new database configuration to be able to connect with the geo database. Read more about this at http://doc.mapbender3.org/en/book/database.html



DataStore in der parameters.yml
===============================

Additionally the Data Manager needs the definition of a "dataStore" in der parameters.yml. This dataStore is used in the YAML-definition of the element itself. In this definition you can define the fields, which should be available for the Data Manager.

Extract from the **parameters.yml** for a simple example:

.. code-block:: yaml

            parameters:
                [...]

                # datastore connection
                dataStores:
                    interests:
                    connection: search_db
                    table: interests_datastore
                    uniqueId: gid
                    fields: [name, sports, healthy, comment, username]  # table fields to use for the datastore

YAML-Definition
===============

The definition of the Data Manager is done in YAML syntax in the textarea configuration at schemes. Here you define the database connection, the editable table, the form to display the table, the attribute form and other behavior.

.. code-block:: yaml

    Interests:
	    dataStore: 
	        connection: search_db
	        table: public.interests_datastore       # name of the table
	        uniqueId: gid
	    allowEdit: true
	    allowCreate: true
	    allowDelete: true
	    allowRefresh: false
	    popup:
	        title: Interests
	        width: 375px
	    formItems:    
	           - type: input
	             title: Interest
	             placeholder: Please enter the name of the interest.
	             name: name
	           - type: checkbox
	             title: Is your interest sport?
	             name: sports
	             value: true
	           - type: checkbox
	             title: Is this interest good for your health?
	             name: healthy
	             value: true
	           - type: textArea
	             title: Comment
	             placeholder: Please enter a comment.
	             name: comment
	    table:
	        autoWidth: false
	        columns:
	            - data: name
	              title: Interest
	        info: true
	        lenghtChange: false
	        ordering: true      
	        pageLength: 10
	        paging: true
	        processing: true
	        searching: true

* **dataManager:** database source (predefined in the parameters.yml).
* **Allow create:** Gives the permission to create new data entries. Activated per default. 
* **Allow edit:** Gives the permission to edit the data. Activated per default.
* **Allow delete:** Gives the permission to remove data entries. Activated per default.
* **Allow refresh:** Gives the permission to update the data entries without reloading the whole application. Not activated per default.

SQL for the demo table
------------------------------

.. code-block:: yaml

    Create table public.interests_datastore (
	    gid serial PRIMARY KEY,
	    name varchar,
	    sports boolean,
	    healthy boolean,
	    comment varchar, 
	    user_name varchar,
      group_name varchar,
      modification_date date
	);
  
	INSERT INTO interests_datastore (name, sports, healthy, comment) VALUES ('reading',false,false,'nice');   
  INSERT INTO interests_datastore (name, sports, healthy, comment) VALUES ('yoga',true,true,'nice');   
  INSERT INTO interests_datastore (name, sports, healthy, comment) VALUES ('surfing',true,true,'needs water');   
  INSERT INTO interests_datastore (name, sports, healthy, comment) VALUES ('swimming',true,true,'needs water');   
  INSERT INTO interests_datastore (name, sports, healthy, comment) VALUES ('painting',false,false,'needs water'); 



Definition of the object table
----------------------------------

The Data Manager provides an object table. With this you can open the fomular to edit the data and sort the data entries. The width of each column can be optionally specified in percent or pixels.

.. code-block:: yaml
     
              - dataStore: 
			        connection: search_db
			        table: public.interests_datastore
			        uniqueId: gid               # Data store name
                allowCreate: true
                allowEdit: true
                allowDelete: true
                allowRefresh: false
			    table:                     # Table configuration
			        autoWidth: false
			        columns:
			            - data: name
			              title: Interests
			        info: true
			        lenghtChange: false
			        ordering: true          # Allows you to sort the table entries. Default is true.
			        pageLength: 10          # Number of entries to be shown on one page.
			        paging: true            # Allows the paging of the entries. Default is true. 
			        processing: true 
			        searching: true         # Allows you to search for entries. Default is true.

To display the table, various elements can be defined.
All items that can be used, can be found at:
https://datatables.net/reference/option/ 


Definition Popup
--------------------

.. code-block:: yaml
              
              - dataStore:
			        connection: search_db
			        table: public.interests_datastore
			        uniqueId: gid 
                ...
                popup:                        # definition of the popup field
			        title: Interests
			        width: 375px
                ...



Class, Widget & Style
=====================

* **Class:** Mapbender\DataSourceBundle\Element\DataManagerElement
* **Widget:** datamanager.element.js
* **Style:** sass\element\data.manager.element.scss
 
HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
