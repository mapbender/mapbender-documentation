.. _digitizer:

Digitalisierung (Digitizer) 
**********************************

Das Digitizer-Element ermöglicht den Aufbau von Erfassungsoberflächen. Derzeit kann über eine YAML-Definition eine Erfassungsmaske für Punkte, Linien oder Flächen aufgebaut werden. Dabei wird bisher PostgreSQL als Datenquelle unterstützt. Oracle und SpatiaLite sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen wie z.B. OGC WFS erweitert werden kann.

Das Digitizer-Element bietet komplexe Editier­funktionalitäten an:

  * Verschieben von Objekten
  * Einfügen von Stützpunkten (Linien, Flächen)
  * Erfassung von Flächen mit Enklaven und/oder Exklaven sowie Kreisen und Ellipsen

In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden. Hierbei wurde sich an den Möglichkeiten, die in Mapbender 2.x zur Verfügung stehen, orientiert.

Folgende Optionen stehen für den Aufbau von Formularen zur Verfügung:

  * Definition von mehreren Datenquellen für die Erfassung (diese werden über eine Selectbox zur Auswahl angeboten)
  * Als Datenquelle kann eine Tabelle angesprochen werden, wobei auch nur eine Auswahl der Daten über einen Filter herangezogen werden kann
  * Textfelder
  * Selectboxen, Multiselectboxen (Füllen der Auswahlbox über eine feste Definition von Werten in der YAML-Definition oder über ein Select auf eine Tabelle)
  * Radiobuttons, Checkboxen
  * Textblöcke
  * Datumsauswahl
  * Dateiupload
  * Definition von Reitern
  * Definition von Trennlinien
  * Definition von beschreibenden Texten
  * Pflichtfelder, Definition von regulären Ausdrücken für die Formatvorgabe des Feldinhalts
  * Hilfetexte
.. image:: ../../../../../figures/digitizer.png
     :scale: 80

Konfiguration
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
                                                   title: 'Please give information about the poi.'
                                                 - type: input
                                                   title: Name
                                                   name: name
                                                 - type: select                       # element type definition
                                                   title: select some types            # labeling (optional)
                                                   name: type                         # reference to table column (optional)
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)
                                                   mandatory: true                    # true - field has to be set. Else you can't save the object. Regular expressions are possible too - see below.
                                                   mandatorytitle: Please chose a type! # define a text that will be displayed if the field is not set.
                                                 - type: input
                                                   title: Abstract
                                                   name: abstract
                                                 - type: checkbox
                                                   title: is public
                                                   name: public
                                                   checked: false
                                                 - type: input
                                                   title: last modified
                                                   name: date
                                                 - type: input                    # element type definition
                                                   title: Title for the field      # labeling (optional)
                                                   mandatory: true                # mandatpory field (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # define a default value  (optional)
                                                   placeholder: 'please edit this field' # placeholder appears in the field as


Definition Popup

.. code-block:: yaml

                                popup: 
                                    # Options description: 
                                    # http://api.jqueryui.com/dialog/
                                    title: POI                                     # define the title of the popup
                                    height: 400
                                    width: 500
                                    # modal: true
                                    # position: {at: "left+20px",  my: "left top-460px"}


Definition von Textfeldern (type input)

.. code-block:: yaml

                                                 - type: input                    # element type definition
                                                   title: Title for the field      # labeling (optional)
                                                   mandatory: true                # mandatpory field (optional)
                                                   name: column_name              # reference to table column (optional)
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # define a default value  (optional)
                                                   placeholder: 'please edit this field' # placeholder appears in the field as information (optional)


Definition von Auswahlboxen (selectbox oder multiselect (type select))

.. code-block:: yaml

                                                 - type: select                     # element type definition
                                                   title: select some types          # labeling (optional)
                                                   name: type_multi                 # reference to table column (optional)                    
                                                   multiple: true                   # define a multiselect, default is false
                                                   options:                         # definition of the options (key, value)
                                                       1: pub
                                                       2: bar
                                                       3: pool
                                                       4: garden
                                                       5: playground
                                                 - type: select                       # element type definition
                                                   title: select some types            # labeling (optional)
                                                   name: type                         # reference to table column (optional)
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)


Definition von Texten (type label)

.. code-block:: yaml

                                                 - type: label                        # element type definition
                                                   title: 'Please give information about the poi.' # define a text 


Definition von Pflichtfeldern

.. code-block:: yaml

                                                   mandatory: true                    # true - field has to be set. Else you can't save the object. Regular expressions are possible too - see below.

                                                   mandatory: /^\w+$/gi               # You can define a regular expression to check the input for a field. You can check f.e. for email or numbers. Read more http://wiki.selfhtml.org/wiki/JavaScript/Objekte/RegExp
                                                   mandatorytitle: Please chose a type! # define a text that will be displayed if the field is not set.


Definition von Feldern für den Dateiupload

.. code-block:: yaml
   
                                                    element:
                                                        type: upload


Definition von Datumfeldern (Datepicker)

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

* Class: Mapbender\\CoreBundle\\Element\\Digitizer
* Widget: mapbender.element.digitizer.js
* Style: mapbender.elements.css


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


