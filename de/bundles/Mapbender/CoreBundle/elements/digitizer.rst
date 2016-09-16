.. _digitizer:

Digitalisierung (Digitizer) 
**********************************

Das Digitizer-Element ermöglicht den Aufbau von Erfassungsoberflächen. Derzeit kann über eine YAML-Definition eine Erfassungsmaske für Punkte, Linien oder Flächen aufgebaut werden. Dabei wird bisher PostgreSQL als Datenquelle unterstützt. Oracle und SpatiaLite sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen wie z.B. OGC WFS erweitert werden kann.

Das Digitizer-Element bietet komplexe Editier­funktionalitäten an:

  * Verschieben von Objekten
  * Einfügen von Stützpunkten (Linien, Flächen)
  * Erfassung von Flächen mit Enklaven und/oder Exklaven sowie Kreisen und Ellipsen

In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden.

    

.. image:: ../../../../../figures/digitizer.png
     :scale: 80

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


.. image:: ../../../../../figures/digitizer_with_tabs.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/digitizer_configuration.png
     :scale: 80

Das Element kann in der Sidepane eingebettet werden.

* Title: Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* Target: Zielelement (Titel(ID)) des Buttons, das bei Anklicken des Buttons ausgelöst wird.
* Schemes: YAML-Definition für das Element digitizer

Der Digitizer benötigt einen Zugriff auf die Datenbank, in der die zu editierenden Tabellen liegen. Sie müssen dazu einen Datenbankzugriff konfigurieren. Mehr zu diesem Thema finden Sie unter http://doc.mapbender3.org/de/book/database.html

Die Definition des Digitizers wird in YAML-Syntax durchgeführt. Hier definieren Sie die Datenbankverbindung, die editierbaren Felder, das Formular für die Anzeige und andere Verhaltensweisen.

YAML-Definition für das Element digitizer in der Sidepane in der mapbender.yml
-----------------------------------------------------------------------------------------

.. code-block:: yaml

                sidepane:
                    digitizer:
                        class: Mapbender\DigitizerBundle\Element\Digitizer
                        title: Digitalisation
                        target: map
                        schemes:
                            ...


YAML-Definition für das Element digitizer in der Textarea unter schemes
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
                       options: {A: A, B: B, C: C, D: D, E: E}
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
    

Basisdefinition
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


Definition Popup
----------------

.. code-block:: yaml

                                popup: 
                                    # Options description: 
                                    # http://api.jqueryui.com/dialog/
                                    title: POI     # Definition des Titels des Popups
                                    height: 400    # Höhe Popup
                                    width: 500     # Breite Popup
                                    # modal: true
                                    # position: {at: "left+20px",  my: "left top-460px"}



Definition der Objekttabelle 
------------------------------------------------------------------------

Der Digitizer stellt eine Objekttabelle bereit. Über diese kann auf die Objekte gezoomt werden und das Bearbeitsformular kann geöffnet werden kann. Die Objekttabelle ist sortierbar. Die Breite der einzelnen Spalten kann optional in Prozent oder Pixeln angegeben werden.

* tableFields - Definition der Spalten für die Objekttabelle.

* searchType
* **all** - lists all features in the table
* **currentExtent** - list only the features displayed in the current extent in the table (default) 

.. code-block:: yaml

        searchType: currentExtent   # currentExtent|all - Standard ist currentExtent
        tableFields:    # Definition der Spalten für die Objekttabelle
            gid: {label: Nr. , width: 20%}    # Datenspalte, label - Beschriftung, css z.B. Angabe der Breite
            name: {label: Name , width: 80%}



Definition von Dateireitern (type tabs)
--------------------------------------

.. code-block:: yaml

        formItems:
           - type: tabs                      # Type tabs erzeugt Reiter
             children:                       # tabs enthält Unterobjekte (children) vom Type form
               - type: form
                 title: Basic information    # Titel des Reiters
                 css: {padding: 10px}        
                 children:                   
                     - type: label
                       title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                       ...


Definition von Textfeldern (type input)
.......................................

.. code-block:: yaml

                                                 - type: input                    # Typ Textfeld
                                                   title: Title for the field     # Beschriftung
                                                   name: column_name              # Referenz zur Tabellenspalte
                                                   mandatory: true                # Pflichtfeld (optional)
                                                   mandatoryText: You have to provide information. # Text sofern Pflichtfeld nicht gefüllt ist
                                                   infoText: 'Bitte geben Sie einen Wert an' # Definition eines Informationstextes
                                                   cssClass: 'input-css'          # additional css definition (optional)
                                                   value: 'default Text'          # Definition eines default-Wertes  (optional)
                                                   placeholder: 'please edit this field' # Platzhalter, der vor der Eingabe erscheint (optional)


Definition von Auswahlboxen (selectbox oder multiselect [type select])
-------------------------------------------------------------------------

select - ein Eintrag kann ausgewählt werden
.. code-block:: yaml

                                                 - type: select                     # Typ Auswahlbox
                                                   title: select some types         # Beschriftung (optional)
                                                   name: my_type                    # Referenz zur Tabellenspalte                   
                                                   multiple: false                  # Definition einer Mehrfachauswahl (multiselect), Standard ist false
                                                   options:                         # Definition der Optionen (key, value)
                                                       1: pub
                                                       2: bar
                                                       3: pool
                                                       4: garden
                                                       5: playground

multiselect - mehrere Einträge können ausgewählt werden
.. code-block:: yaml

                                                 - type: select                       # element type definition
                                                   title: select some types           # labeling (optional)
                                                   name: my_type                      # reference to table column (optional)
                                                   multiple: true                     # define a multiselect, default is false
                                                   options: [1: pub, 2: bar, 3: pool] # definition of the options (key, value)


Füllen der Auswahlboxen über eine SQL Abfrage
--------------------------------------------------

.. code-block:: yaml

                                                 - type: select                     # Typ Auswahlbox
                                                   title: select some types         # Beschriftung (optional)
                                                   name: my_type                    # Referenz zu Tabellenspalte
                                                   connection: connectionName       # Definition einer Datenbankverbindung (connection)
                                                   sql: 'SELECT DISTINCT key, value FROM tableName order by value' # Definition SQL, Abfrage der Werte key und value



Definition von Texten (type label)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: label      # Typ Label schreibt einen Text
                                                   title: 'Please give information about the poi.' # Definition eines Textes


Definition eines Textes
-------------------------------

Im Formular können Texte definiert werden. Hierbei kann auf Felder der Datenquelle zugegriffen werden. Darüber hinaus kann JavaScript verwendet werden.

.. code-block:: yaml

                                                - type: text      # Typ text zur Generierung von dynamischen Texten

                                                  # Label (optional)
                                                  title:       Name 

                                                  # Name des Feldes (optional)
                                                  name:        name 

                                                  # CSS Definition (optional)
                                                  css:         {width: 80%} 

                                                  # CSS Klass Definition (optional)
                                                  cssClass:    input-css  

                                                  # Text Definition in JavaScript
                                                  # data - Data ist das Objekt, das alle Felder zur Verfügung stellt.
                                                  # z.B.: Über data.id wird die ID des Obektes im Text angezeigt.
                                                  text: data.id + ':' + data.name

Definition von Textbereichen (type textArea)
--------------------------------------------------------------

.. code-block:: yaml

                                                 - type: textArea      # Typ erzeugt einen Textbereich
                                                   rows: 4             # Anzahl der Zeilen für den Textbereich
                                                   name: beschreibung  # Tabellenspalte  
                                                   title: Bestandsaufnahme Bemerkung


Definition of a Trennlinien (type breakline)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: breakline      # fügt eine Trennlinie ein


Definition von Checkboxen (type checkbox)
--------------------------------------------------

.. code-block:: yaml

                                                 - type:  checkbox 
                                                   title: Is this true?
                                                   name:  public
                                                   value: true


Definition von Pflichtfeldern
--------------------------------------------------

.. code-block:: yaml

                                                   mandatory: true                              # true - Das Feld muss gefüllt werden. Ansonsten kann der Datensatz nicht gespeichert werden. Bei der Definition sind auch Reguläre Ausdrücke möglich.
                                                   
                                                   mandatorytitle: Pflichtfeld - bitte füllen!  # Text der angezeigt wird, wenn das Feld nicht gefüllt wird oder mit einem ungültigen Wert gefüllt wird.
                                                   
                                                   mandatory: /^\w+$/gi               # Es können auch reguläre Ausdrücke angegeben werden, um die Eingabe zu überprüfen (z.B. Email oder numbers) Weitere Informationen unter: http://wiki.selfhtml.org/wiki/JavaScript/Objekte/RegExp
                                                   
                                                   # Prüfung, ob die Eingabe eine Zahl ist
                                                   mandatory: /^[0-9]+$/
                                                   mandatoryText: Bitte eine Zahl eingeben!


Definition eines Textfelds mit Datumsauswahl
--------------------------------------------------

.. image:: ../../../../../figures/digitizer_datepicker.png
     :scale: 80

.. code-block:: yaml

                                                    type: date              # Textfeld, das eine Datumsauswahl bereitstellt
                                                    value: 2015-01-01       # Startwert für die Datumsauswahl (optional)
                                                    format: YYYY-MM-DD      # Datumsformat (optional), Standardformat YYYY-MM-DD


Definition von Hilfetexten zu den Eingabefeldern (type infotext)
------------------------------------------------------------------------------------------

.. code-block:: yaml

                                                 - type: input                    # Elementtyp
                                                   title: Title for the field     # Beschriftung (optional)
                                                   name: column_name              # Tabellenspalte (optional)
                                                   mandatory: /^[0-9]+$/
                                                   mandatoryText: Bitte eine Zahl eingeben!
                                                   infoText: In dieses Feld dürfen nur Zahlen eingegeben werden # Hinweistext, der angezeigt wird über i-Symbol.


Definition von Gruppierungen (type: fieldSet)
--------------------------------------------------

Elemente können in einer Zeile gruppiert werden, um logische Einheiten zu bilden oder um Platz zu sparen. Hierbei muss ein fieldSet definiert werden. Anschließend können die Elemente der Gruppe unter children angegeben werden.

Für jedes Gruppenelement kann eine Breite angegeben werden, um den Platz den jedes Element einnimmt zu kontrollieren.

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


Definition von Feldern für den Dateiupload
--------------------------------------------------

.. code-block:: yaml
  
                    - type: file
                      title: upload an image
                      name: file1
                      path: digitizer           # "web/uploads" ist der Basispfad, nach dieser Definition werden die Dateien nach web/uploads/digitizer hochgeladen
                                                # ein absoluter Pfad ist ebenso möglich wie /data/webgis/digitizer
                      format: %gid%-%name%      # die Datei wird nach der Definition umbenannt (%name% ist der Dateiname [hier file1], %gid% - ist der Feldname)
                      url:  /digitizer/         # optional, wenn ein ALIAS definiert wurde
                      allowedFormats: [jpg,png,gif]


Definition von Bildern
--------------------------------------------------

.. code-block:: yaml
                      
                    - type: image
                      # Feature type field name. optional.
                      # Wenn definiert, wird Pfad zu dem Feld ermittelt und "src" Option ersetzt
                      name: file_reference
                      # URL oder Pfad zum Bild auf dem Server
                      src: "bundles/mapbendercore/image/logo_mb3.png" 
                      # Optional. Standardwert ist false. Wenn true, wird der "src" Pfad ab dem "/web" Verzeichniss ermittelt.
                      relative: true
                      # Image CSS Style
                      imageCss: {width: 100%}
                      # Image Container CSS Style
                      css: {width: 25%}


Definition der zur Verfügung stehenden Werkzeuge (Toolset Type)
------------------------------------------------------------------------

Werkzeugliste

  * **drawPoint** - Punkt erstellen
  * **drawLine** - Line erstellen
  * **drawPolygon** - Polygone erstellen
  * **drawRectangle** - Rechteck erstellen
  * **drawCircle** - Circle erstellen
  * **drawEllipse** - Ellipse erstellen
  * **drawDonut** - Donut erstellen oder die bestehende Geometrien editieren
  * **modifyFeature** - Geometrien einzelne Punkte verschieben
  * **moveFeature** - Geometrien verschieben
  * **selectFeature** - Geometrien de/selektieren
  * **removeSelected** - die selektierten löschen
  * **removeAll** - alle Löschen (aus dem Layer)

Definition der für die Erfassung verwendeten Toolset Typen

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


