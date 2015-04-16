.. _digitalisation:

Digitalisation
**********************************

<Put short description - 5-6 sentences - here>

.. image:: ../../../../../figures/digitization.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/digitization_configuration.png
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
                                    fields: [gid,name,type,abstract,public,date,type_multi]
                                openFormAfterEdit: true
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

<Check the PHP class' httpAction method to find out the actions and what they
 do. If no httpAction method is defined put "None." into this section.>

<action>
--------------------------------

<Put description here, including required and optional HTTP parameters, HTTP
 method restrictions if any and return values and format. Repeat for every
 callback action>

JavaScript API
==============

<Check the widgets methods which don't start with an underscore.>

<function>
----------

<Put description here, including required and optional parameters and return
 value if any>

JavaScript Signals
==================

<signal>
--------

<Put description here.>
