.. _digitalisation:

Digitalisation
**********************************

<Put short description - 5-6 sentences - here>

.. image:: ../../../../../figures/digitizer.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/digitizer_configuration.png
     :scale: 80

You can use the element in the sidepane or as a dialog with a button.

The Ditigitzer needs access to a database where the editable tables are. You have to define a new database configuration to be able to connect with the geo database. Read more about this at http://doc.mapbender3.org/en/book/database.html

The definition of the digitizer is done in YAML syntax in the textarea configuration at schemes. Here you define the database connection, the editable table, the form to display the table, the attribute form and other behaviour.

Element definition in web interface in the configuration area:

YAML-Definition for mapbender.yml:

.. code-block:: yaml

                sidepane:
                    digitizer:
                        class: Mapbender\DigitizerBundle\Element\Digitizer
                        title: Digitalisation
                        target: map
                        schemes:
                            poi:
                                label: poi
                                featureType: 
                                    connection: digi
                                    table: poi
                                    uniqueId: gid
                                    geomType: point
                                    geomField: geom
                                    srid: 4326
                                    sqlFilter: type = 1 AND name = 'A'
                                    fields: [gid,name,type,abstract,public,date,type_multi]
                                openFormAfterEdit: true
                                popup: 
                                    # Options description: 
                                    # http://api.jqueryui.com/dialog/
                                    title: POI
                                    height: 400
                                    width: 500
                                    # modal: true
                                    # position: {at: "left+20px",  my: "left top-460px"}
                                tableFields:
                                    gid:
                                        label: Number
                                    name:
                                        label: Name
                                formItems:
                                     - type: tabs
                                       items:
                                           - type: form
                                             title: Basic Information
                                             items:
                                                 - type: label
                                                   text: 'Please give information about the poi.'
                                                 - type: input
                                                   text: Name
                                                   name: name
                                                 - type: select                       # element type definition
                                                   text: select some types            # labeling (optional)
                                                   name: type                         # reference to table column (optional)
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)
                                                   mandatory: true                    # true - field has to be set. Else you can't save the object. Regular expressions are possible too - see below.
                                                   mandatoryText: Please chose a type! # define a text that will be displayed if the field is not set.
                                                 - type: input
                                                   text: Abstract
                                                   name: abstract
                                                 - type: checkbox
                                                   text: is public
                                                   name: public
                                                   checked: false
                                                 - type: input
                                                   text: last modified
                                                   name: date
                                                 - type: input                    # element type definition
                                                   text: Title for the field      # labeling (optional)
                                                   mandatory: true                # mandatpory field (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # define a default value  (optional)
                                                   placeholder: 'please edit this field' # placeholder appears in the field as


Definition of the popup

.. code-block:: yaml

                                popup: 
                                    # Options description: 
                                    # http://api.jqueryui.com/dialog/
                                    title: POI                                     # define the title of the popup
                                    height: 400
                                    width: 500
                                    # modal: true
                                    # position: {at: "left+20px",  my: "left top-460px"}


Definition of a textfield (type input)

.. code-block:: yaml

                                                 - type: input                    # element type definition
                                                   text: Title for the field      # labeling (optional)
                                                   mandatory: true                # mandatpory field (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # define a default value  (optional)
                                                   placeholder: 'please edit this field' # placeholder appears in the field as information (optional)


Definition of a selectbox or multiselect (type select) 

.. code-block:: yaml

                                                 - type: select                     # element type definition
                                                   text: select some types          # labeling (optional)
                                                   name: type_multi                 # reference to table column (optional)                    
                                                   multiple: true                   # define a multiselect, default is false
                                                   options:                         # definition of the options (key, value)
                                                       1: pub
                                                       2: bar
                                                       3: pool
                                                       4: garden
                                                       5: playground
                                                 - type: select                       # element type definition
                                                   text: select some types            # labeling (optional)
                                                   name: type                         # reference to table column (optional)
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)


Definition of a text (type label)

.. code-block:: yaml

                                                 - type: label                        # element type definition
                                                   text: 'Please give information about the poi.' # define a text 


Definition of a mandatory field

.. code-block:: yaml

                                                   mandatory: true                    # true - field has to be set. Else you can't save the object. Regular expressions are possible too - see below.

                                                   mandatory: /^\w+$/gi               # You can define a regular expression to check the input for a field. You can check f.e. for email or numbers. Read more http://wiki.selfhtml.org/wiki/JavaScript/Objekte/RegExp
                                                   mandatoryText: Please chose a type! # define a text that will be displayed if the field is not set.


Definition of a file upload field

.. code-block:: yaml
   
                                                    element:
                                                        type: upload


Definition of a datepicker

.. code-block:: yaml

                                                    element:
                                                        type: datepicker               # on click in the textfield a datepicker will open
                                                        value: 2015-01-01              # define a start value for the datepicker (optional)
                                                        format: YYYY-MM-DD             # define a dateformat (optional), default is YYYY-MM-DD



Feature styling
----------------------
* have a look at SearchRouter


Class, Widget & Style
===========================

* Class: <Put PHP class name here>
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


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


