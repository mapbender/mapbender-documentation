.. _digitizer:

Digitizer
**********************************

The Digitizer element allows building editing-interfaces. Currently you can build up your interface for point, line and point editing with a YAML-definition. Right now PostgreSQL is supported as a database. Oracle and SpatialLize can be used experimentally. The development of the data-sources allow other data sources so that it can be extended to support - for example - OGC WFS services.

The Digitizer-Element offers complex editing functionality:

  * move objects
  * add vertices (lines, polygons)
  * generation of enclaves, exclaves, circles and ellipses

You can define very complex formss for the attributes. This follows the capabilities of Mapbender 2.x.

    

.. image:: ../../../../../figures/digitizer.png
     :scale: 80

The following option for the construction of the forms are available:

  * define more then one feature types for digitalisation. You can switch from one feature type to the other with a select box
  * use a table as source. You can also define a filter to get a subset of the table
  * Textfields
  * Selectboxes, Multiselectboxes
  * Radiobuttons, Checkboxes
  * Textareas
  * Datepicker
  * File upload
  * Definition of tabs
  * Definition breaklines
  * Definition of Text 
  * Mandatory fields, regular expressions to valida the content are possible
  * Help textes


.. image:: ../../../../../figures/digitizer_with_tabs.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/digitizer_configuration.png
     :scale: 80

You can use the element in the sidepane or as a dialog with a button.

The Ditigitzer needs access to a database where the editable tables are. You have to define a new database configuration to be able to connect with the geo database. Read more about this at http://doc.mapbender3.org/en/book/database.html

The definition of the digitizer is done in YAML syntax in the textarea configuration at schemes. Here you define the database connection, the editable table, the form to display the table, the attribute form and other behaviour.

Element definition in web interface in the configuration area:

YAML-Definition for the element digitizer in mapbender.yml:

.. code-block:: yaml

                sidepane:
                    digitizer:
                        class: Mapbender\DigitizerBundle\Element\Digitizer
                        title: Digitalisation
                        target: map
                        schemes:
                            ...


YAML-Definition for the element digitizer in the textarea schemes
-----------------------------------------------------------------------------------------

.. code-block:: yaml

    poi:
        label: point digitizing
        maxResults: 500
        featureType:
            connection: search_db
            table: poi
            uniqueId: gid
            geomType: point
            geomField: geom
            srid: 4326
        openFormAfterEdit: true
        zoomScaleDenominator: 500
        allowEditData: true 
        allowDelete: true
        allowDigitize: true 
        toolset:
            - type: drawPoint
            - type: modifyFeature
            - type: moveFeature
            - type: selectFeature
            - type: removeSelected 
        popup:
            title: point test suite
            width: 500px
        searchType: currentExtent   # currentExtent|all - default is currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        formItems:
           - type: tabs
             children:
               - type: form
                 title: Basic information
                 css: {padding: 10px}
                 children:
                     - type: label
                       title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                     - type: input
                       title: Name
                       mandatory: true
                       name: name
                       mandatoryText: Please give a name to the poi.
                       infoText: "Help: Please give a name to the new object."
                     - type: input
                       title: Title
                       mandatory: false
                       name: title
                       mandatoryText: Please give a title to the poi.
                     - type: textArea
                       name: abstract
                       title: Abstract
                       placeholder: 'please edit this field'
                     - type: select
                       title: Type
                       name: type
                       options: 
                           - A: A
                           - B: B
                           - C: C
                           - D: D
                           - E: E
                     - type: breakLine
               - type: form
                 title: Personal information
                 css: {padding: 10px}
                 children:
                     - type: label
                       title: Please give us some information about yourself.
                     - type: fieldSet
                       children:
                           - type: input
                             title: Firstname
                             name: firstname
                             css: {width: 30%}
                           - type: input
                             title: Lastname
                             name: lastname
                             css: {width: 30%}
                           - type: input
                             title: E-Mail
                             name: email
                             css: {width: 40%}
                     - type: select
                       multiple: false
                       title: Interests
                       name: interests
                       options: {maps: maps, reading: reading, swimming: swimming, dancing: dancing, beer: beer, flowers: flowers}
                     - type: date
                       title: favorite Date
                       name: date_favorite
                       mandatory: true
                       css: {width: 25%}
                     - type: breakLine
                     - type: breakLine
                     - type: checkbox
                       name: public
                       value: true
                       title: public (this new object is public)               
    line:
        label: line digitizing
        maxResults: 1500
        featureType:
            connection: search_db
            table: lines
            uniqueId: gid
            geomType: line
            geomField: geom
            srid: 4326
        openFormAfterEdit: true
        allowDelete: true
        toolset:
            - type: drawLine
            - type: modifyFeature
            - type: moveFeature
            - type: selectFeature
            - type: removeSelected 
        popup:
            title: line test suite
            width: 500px
        searchType: currentExtent   # currentExtent|all - default is currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        formItems:
           - type: form
             title: Basic information
             css: {padding: 10px}
             children:
                 - type: label
                   title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                 - type: input
                   title: Name
                   name: name
                   mandatory: true
                   mandatoryText: Please give a name to the new object.
                   infoText: "Help: Please give a name to the new object."
                 - type: select
                   title: Type
                   name: type
                   options: {A: A, B: B, C: C, D: D, E: E}
    polygon:
        label: polygon digitizing
        maxResults: 1500
        featureType:
            connection: search_db
            table: polygons
            uniqueId: gid
            geomType: polygon
            geomField: geom
            srid: 4326
        openFormAfterEdit: true
        allowDelete: false
        toolset:
            - type: drawPolygon
            - type: drawRectangle
            - type: drawDonut
            - type: drawEllipse
            - type: drawCircle
            - type: modifyFeature
            - type: moveFeature
            - type: selectFeature
            - type: removeSelected 
        popup:
            title: polygon test suite
            width: 500px
        searchType: currentExtent   # currentExtent|all - default is currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        formItems:
           - type: form
             title: Basic information
             css: {padding: 10px}
             children:
                 - type: label
                   title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                 - type: input
                   title: Name
                   mandatory: true
                   name: name
                   mandatoryText: Please give a name to the new object.
                   infoText: "Help: Please give a name to the new object."
                 - type: select
                   title: Type
                   name: type
                   options: {A: A, B: B, C: C, D: D, E: E} 


SQL for the demo tables
------------------------------

.. code-block:: yaml

    Create table public.poi (
        gid serial,
        name varchar,
        type varchar,
        abstract varchar,
        public boolean,
        date_favorite date,
        title varchar,
        firstname varchar,
        lastname varchar,
        email varchar,
        interests varchar,
        x float,
        y float,
        geom geometry(point,4326),
        CONSTRAINT pk_poi_gid PRIMARY KEY (gid)
    );

.. code-block:: yaml

    Create table public.lines (
        gid serial,
        name varchar,
        type varchar,
        abstract varchar,
        public boolean,
        date_favorite date,
        title varchar,
        firstname varchar,
        lastname varchar,
        email varchar,
        interests varchar,
        length float,
        category varchar,
        x float,
        y float,
        geom geometry(linestring,4326),
        CONSTRAINT pk_lines_gid PRIMARY KEY (gid)
    ); 

.. code-block:: yaml

    Create table public.polygons (
        gid serial,
        name varchar,
        type varchar,
        abstract varchar,
        public boolean,
        date_favorite date,
        title varchar,
        firstname varchar,
        lastname varchar,
        email varchar,
        interests varchar,
        area float,
        category varchar,
        x float,
        y float,
        geom geometry(polygon,4326),
        CONSTRAINT pk_polygons_gid PRIMARY KEY (gid)
    );
    
  

Feature basic definition
--------------------------

.. code-block:: yaml

    poi:
        label: point digitizing        # Name for the 
        maxResults: 500
        featureType:
            connection: search_db
            table: poi
            uniqueId: gid
            geomType: point
            geomField: geom
            srid: 4326
        openFormAfterEdit: true                #Set to true (default): after creating a geometry the form popup is opened automatically to insert the attribute data.
        zoomScaleDenominator: 500
        allowEditData: true 
        allowDelete: true
        allowDigitize: true 
        popup:
            [...]


Definition of the popup
-----------------------

.. code-block:: yaml

                                popup: 
                                    # Options description: 
                                    # http://api.jqueryui.com/dialog/
                                    title: POI                       # define the title of the popup
                                    height: 400
                                    width: 500
                                    # modal: true
                                    # position: {at: "left+20px",  my: "left top-460px"}



Definition of the feature table
------------------------------------------------------------------------

The Digitizer provides a feature table to navigate to features and select features for editing. The columns are sortable by default. You can define width (% or px) for each column.

* tableFields - define the columns for the feature table. 

* searchType
* **all** - lists all features in the table
* **currentExtent** - list only the features displayed in the current extent in the table (default) 

.. code-block:: yaml

        searchType: currentExtent   # currentExtent|all - default is currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}



Definition of tabs (type tabs)
------------------------------

.. code-block:: yaml

        formItems:
           - type: tabs
             children:
               - type: form
                 title: Basic information
                 css: {padding: 10px}
                 children:
                     - type: label
                       title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                       ...


Definition of a textfield (type input)
--------------------------------------

.. code-block:: yaml

                                                 - type: input                    # element type definition
                                                   title: Title for the field      # labeling (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   mandatory: true                # mandatpory field (optional)
                                                   mandatoryText: You have to provide information.
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # define a default value  (optional)
                                                   placeholder: 'please edit this field' # placeholder appears in the field as information (optional)


Definition of a selectbox or multiselect (type select)
------------------------------------------------------

select
.. code-block:: yaml

                                                 - type: select                     # element type definition
                                                   title: select some types         # labeling (optional)
                                                   name: my_type                    # reference to table column (optional)                    
                                                   multiple: false                  # define a multiselect, default is false
                                                   options:                         # definition of the options (key, value)
                                                       1: pub
                                                       2: bar
                                                       3: pool
                                                       4: garden
                                                       5: playground

multiselect
.. code-block:: yaml

                                                 - type: select                       # element type definition
                                                   title: select some types           # labeling (optional)
                                                   name: my_type                      # reference to table column (optional)
                                                   multiple: true                     # define a multiselect, default is false
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)


Get the options for the select box via SQL
--------------------------------------------------

.. code-block:: yaml

                                                 - type: select                     # element type definition
                                                   title: select some types         # labeling (optional)
                                                   name: my_type                    # reference to table column
                                                   connection: connectionName       # Define a connection selectbox via SQL
                                                   sql: 'SELECT DISTINCT key, value FROM tableName order by value' # get the options of the



Definition of a text (type label)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: label                        # element type definition, will write a text
                                                   text: 'Please give information about the poi.' # define a text 

Definition of a text
-------------------------------

You can define a label and refer to colums of your datasource. You also can use JavaScript.

.. code-block:: yaml

                                                - type:        text                  # element Type definition

                                                  # Label (optional)
                                                  title:       Name 

                                                  # Name of the field (optional)
                                                  name:        name 

                                                  # CSS definition (optional)
                                                  css:         {width: 80%} 

                                                  # CSS class definition (optional)
                                                  cssClass:    input-css  

                                                  # text definition in JavaScript
                                                  # data - data is the object, that gives access to all fields.
                                                  # f.E.: data.id will show the id of the Objekt as text
                                                  text: data.id + ':' + data.name


Definition of a textarea (type textarea)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: textarea
                                                   title: Bestandsaufnahme Bemerkung


Definition of a breakline (type breakline)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: breakline                     # element type definition, will draw a line 


Definition of a checkbox (type checkbox)
----------------------------------------

.. code-block:: yaml

                                                 - type:  checkbox 
                                                   title: Is this true?
                                                   name:  public
                                                   value: true


Definition of a mandatory field
--------------------------------------------------

.. code-block:: yaml

                                                   mandatory: true                    # true - field has to be set. Else you can't save the object. Regular expressions are possible too - see below.
                                                   mandatoryText: Please choose a type! # define a text that will be displayed if the field is not set or is filled with an invalid value.

                                                   mandatory: /^\w+$/gi               # You can define a regular expression to check the input for a field. You can check f.e. for email or numbers. Read more http://wiki.selfhtml.org/wiki/JavaScript/Objekte/RegExp
                                                   # Check if input is a number
                                                   mandatory: /^[0-9]+$/
                                                   mandatoryText: Only numbers are valid for this field!


Definition of a infotext 
-------------------------------

An i-Icon will be displayed. On mouse-over the defined infotext will appear. Infotext can be defined for every field type.

.. code-block:: yaml

                                                 - type:  checkbox                        # infotext can be defined for every element type
                                                   title: Is this true?
                                                   name:  public
                                                   value: true
                                                   infoText: Please read the information. 



Definition of a datepicker
--------------------------------------------------

.. image:: ../../../../../figures/digitizer_datepicker.png
     :scale: 80

.. code-block:: yaml

                                                    type: datepicker               # on click in the textfield a datepicker will open
                                                    value: 2015-01-01              # define a start value for the datepicker (optional)
                                                    format: YYYY-MM-DD             # define a dateformat (optional), default is YYYY-MM-DD


Definition of information (type infotext)
------------------------------------------------------------------------------------------

.. code-block:: yaml

                                                 - type: input                    # element type definition
                                                   title: Title for the field     # labeling (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   mandatory: /^[0-9]+$/          # mandatroy field (optional)
                                                   mandatoryText: Only numbers are valid for this field!
                                                   infoText: Please note - only numbers are valid for this field. # Notice which will be displayed by i-symbol


Definition of element groups (type: fieldSet)
--------------------------------------------------

Elements can be grouped together in one row to provide logical connections or save space. To define a group you have to set type fieldSet and afterwards define the children which shall be grouped.

For each children you can define a width to controll the pace for each element.

.. code-block:: yaml

                     - type: fieldSet
                       children:
                           - type: input
                             title: Firstname
                             name: firstname
                             css: {width: 30%}
                           - type: input
                             title: Lastname
                             name: lastname
                             css: {width: 30%}
                           - type: input
                             title: E-Mail
                             name: email
                             css: {width: 40%}


Definition of a file upload field
--------------------------------------------------

.. code-block:: yaml
  
                    - type: upload
                      title: upload an image
                      name: file1
                      path: digitizer           # base location is "web/uploads", like this the files are saved at web/uploads/digitizer
                                                # also absolute path is possible like /data/webgis/digitizer
                      format: %gid%-%name%      # file will be renamed to the definition (%name% is file1, %gid% - is ID fieldname)
                      url:  /digitizer/         # optional, if ALIAS is defined
                      allowedFormats: [jpg,png,gif,pdf]


Definition of toolset types
------------------------------------------------------------------------

Toolset types

  * **drawPoint** - draw point
  * **drawLine** - draw a line
  * **drawPolygon** - draw polygon
  * **drawRectangle** - draw rectangle
  * **drawCircle** - draw circle
  * **drawEllipse** - draw ellipse
  * **drawDonut** - draw a donut (enclave)
  * **modifyFeature** - move vertices of a geometry
  * **moveFeature** - move geometry
  * **selectFeature** - geometry de/select
  * **removeSelected** - delete selected geometry
  * **removeAll** - remove all geometries

Definition of toolset types

.. code-block:: yaml

    polygon:
        label: polygon digitizing
        maxResults: 1500
        featureType:
            connection: search_db
            table: polygons
            uniqueId: gid
            geomType: polygon
            geomField: geom
            srid: 4326
        openFormAfterEdit: true
        allowDelete: false
        toolset:
            - type: drawPolygon
            - type: drawRectangle
            - type: drawDonut
            - type: removeSelected


Class, Widget & Style
===========================

* Class: Mapbender\\DigitizerBundle\\Element\\Digitizer
* Widget: mapbender.element.digitizer.js
* Style: sass\\element\\digitizer.scss


HTTP Callbacks
==============



<action>
--------------------------------


JavaScript API
==============


<function>
----------


JavaScript Signals
==================

<signal>
--------


