.. _digitizer:

Digitalisierung (Digitizer)
***************************

Das Digitizer-Element ermöglicht den Aufbau von Erfassungsoberflächen. Derzeit kann über eine YAML-Definition eine Erfassungsmaske für Punkte, Linien oder Flächen aufgebaut werden.
Dabei wird bisher PostgreSQL als Datenquelle unterstützt. Oracle und SpatiaLite sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen wie z.B. OGC WFS erweitert werden kann.

Das Digitizer-Element bietet komplexe Editierfunktionalitäten an:

* Verschieben von Objekten
* Einfügen von Stützpunkten (Linien, Flächen)
* Erfassung von Flächen mit Enklaven und/oder Exklaven sowie Kreisen und Ellipsen

In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare generiert werden.


.. image:: ../../../../../figures/digitizer.png
     :scale: 80

Folgende Optionen stehen für den Aufbau von Formularen zur Verfügung:

* Definition von mehreren Datenquellen und Geometrieformaten für die Erfassung. Die verschiedenen Quellen werden über eine Auswahlbox angeboten.
* Als Datenquelle wird eine Tabelle angesprochen, wobei auch nur eine Auswahl der Daten über einen Filter herangezogen werden kann
* Textfelder
* Textblöcke (mehrzeilige Textfelder)
* Selectboxen, Multiselectboxen (Füllen der Auswahlbox über eine feste Definition von Werten in der YAML-Definition oder über ein Select auf eine Tabelle)
* Radiobuttons und Checkboxen
* Datumsauswahl
* Dateiupload und Bildanzeige
* Definition von Reitern
* Definition von Trennlinien
* Definition von beschreibenden Texten zur Information
* Pflichtfelder, Definition von regulären Ausdrücken für die Formatvorgabe bestimmter Feldinhalte
* Hilfetexte


.. image:: ../../../../../figures/digitizer_with_tabs.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../../../figures/digitizer_configuration.png
     :scale: 80

Das Element wird in der Sidepane eingebettet.

* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Elemente voneinander zu unterscheiden.
* **Target:** Zielelement (Titel(ID)) der Karte.
* **Schemes:** YAML-Definition für das Element "digitizer"

Der Digitizer benötigt einen Zugriff auf die Datenbank, in der die zu editierenden Tabellen liegen. Sie müssen dazu einen Datenbankzugriff konfigurieren.
Mehr zu diesem Thema finden Sie unter http://doc.mapbender3.org/de/book/database.html

Die Definition des Digitizers wird in einer YAML-Syntax durchgeführt. Hier definieren Sie die Datenbankverbindung, die editierbaren Felder, das Formular für die Anzeige und andere Verhaltensweisen.
Bei fehlerhaften Angaben zur Datenbank, Feldern und Formularfehler erscheinen Fehlermeldungen. Über den normalen Aufruf und app.php kommt eine allgemeine Fehlermeldung.
Falls Sie den genauen Fehler reproduzieren möchten, sollten Sie die Seite über app_dev.php aufrufen. Hier tauchen ausführliche Fehlermeldungen zum Fehlerverhalten auf.

YAML-Definition für das Element "digitizer" in der Sidepane in der mapbender.yml:

.. code-block:: yaml

                sidepane:
                    digitizer:
                        class: Mapbender\DigitizerBundle\Element\Digitizer
                        title: Digitalisation
                        target: map
                        schemes:
                            ...


YAML-Definition für das Element digitizer in der Textarea unter schemes
-----------------------------------------------------------------------

In dem folgenden YAML-Block ist die beispielhafte Definition für drei Erfassungsoberflächen enthalten. Kopieren Sie den folgenden Block in Ihr Digitizer-Element, um die Erfassung von Punkten, Linien und Polygonen zu testen.
Vorher müssen Sie die Datenbankverbindung und die drei Demo-Tabellen anlegen. Die SQL-Befehle für das Anlegen der Tabellen finden Sie weiter unten.
Der Funktionsumfang der eingebauten Features und weitere Funktionen werden nach diesem Beispielaufbau genauer erläutert.

.. code-block:: yaml

    poi:
        label: point digitizing
        inlineSearch: true
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
        useContextMenu: true
        toolset:
            - type: drawPoint
            - type: modifyFeature
            - type: moveFeature
        popup:
            title: point test suite
            width: 500px
        searchType: currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        styles:
            default:
                strokeWidth: 2
                strokeColor: '#0e6a9e'
                fillColor: '#1289CD'
                fillOpacity: 1
                fillWidth: 2
                pointRadius: 10
            select:
                strokeWidth: 3
                strokeColor: '#0e6a9e'
                fillOpacity: 0.7
                pointRadius: 10
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
                       placeholder: Please add a date in the following style dd-mm-yy.
                       dateFormat: dd-mm-yy
                       value: 01-01-2016
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
        inlineSearch: true
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
        useContextMenu: true
        toolset:
            - type: drawLine
            - type: modifyFeature
            - type: moveFeature
            - type: selectFeature
            - type: removeSelected
        popup:
            title: line test suite
            width: 500px
        searchType: currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        styles:
            default:
                strokeWidth: 2
                strokeColor: '#0e6a9e'
                fillColor: '#1289CD'
                fillOpacity: 1
                fillWidth: 2
                pointRadius: 10
            select:
                strokeWidth: 3
                strokeColor: '#0e6a9e'
                fillOpacity: 0.7
                pointRadius: 10
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
        inlineSearch: true
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
        useContextMenu: true
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
        searchType: currentExtent
        tableFields:
            gid: {label: Nr. , width: 20%}
            name: {label: Name , width: 80%}
        styles:
            default:
                strokeWidth: 2
                strokeColor: '#0e6a9e'
                fillColor: '#1289CD'
                fillOpacity: 1
                fillWidth: 2
                pointRadius: 10
            select:
                strokeWidth: 3
                strokeColor: '#0e6a9e'
                fillOpacity: 0.7
                pointRadius: 10
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


SQL für die Demo-Tabellen
-------------------------

Die folgenden SQL-Befehle müssen in Ihrer Datenbank ausgeführt werden. Sie legen drei Demo-Tabellen an, damit mit der oben gezeigte YAML-Definition die einzelnen Funktionen getestet werden können. Die PostGIS Extension muss aktiviert sein.


.. code-block:: sql

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
        user_name varchar,
        group_name varchar,
        modification_date date,
        my_type varchar,
        file_reference varchar,
        x float,
        y float,
        geom geometry(point,4326),
        CONSTRAINT pk_poi_gid PRIMARY KEY (gid)
    );

.. code-block:: sql

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
        user_name varchar,
        group_name varchar,
        modification_date date,
        my_type varchar,
        file_reference varchar,
        x float,
        y float,
        geom geometry(linestring,4326),
        CONSTRAINT pk_lines_gid PRIMARY KEY (gid)
    );

.. code-block:: sql

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
        user_name varchar,
        group_name varchar,
        modification_date date,
        my_type varchar,
        file_reference varchar,
        x float,
        y float,
        geom geometry(polygon,4326),
        CONSTRAINT pk_polygons_gid PRIMARY KEY (gid)
    );


Basisdefinition
---------------

.. code-block:: yaml

    poi:
        label: point digitizing        # Beschriftung mit dem Namen der Erfassungsoberfläche
        maxResults: 500                # maximale Trefferanzahl
        featureType:                   # Verbindung zur Datenbank aus der parameters/config.yml
            connection: search_db
            table: poi
            uniqueId: gid
            geomType: point
            geomField: geom
            srid: 4326
        openFormAfterEdit: true        # Nach der Erfassung einer Geometrie öffnet sich das Erfassungsformular. Standard ist true.
        zoomScaleDenominator: 500
        allowEditData: true            # Durch Angabe von den Parametern allow[Parameter] wird definiert, ob Daten und Geometrien erfasst und verändert werden dürfen.
        allowDelete: true
        allowDigitize: true
        popup:
            [...]


Definition Popup
----------------

.. code-block:: yaml

        popup:                  # Definition des Formularfensters als PopUp-Fenster. Siehe http://api.jqueryui.com/dialog/
            title: POI     # Definition des Titels vom Formularfensters
            height: 400    # Höhe des Formularfensters
            width: 500     # Breite des Formularfensters

            #modal: true   # Alles außer dem Formularfensters wird ausgegraut und die Position und Größe des Fensters ist für die Dauer der Datenaufnahme fixiert
            #position: {at: "left+20px",  my: "left top-460px"}  #Positionierung des Formularfensters im Browserbereich



Definition der Objekttabelle
----------------------------

Der Digitizer stellt eine Objekttabelle bereit. Über diese kann auf die Objekte gezoomt werden und das Bearbeitsformular kann geöffnet werden. Die Objekttabelle ist sortierbar. Die Breite der einzelnen Spalten kann optional in Prozent oder Pixeln angegeben werden.

* tableFields - Definition der Spalten für die Objekttabelle.
* searchType **all** oder **currentExtent**

.. code-block:: yaml

        searchType: currentExtent   # [currentExtent|all] currentExtent listet alle Objekte im derzeitigen Kartenausschnitt. all listet alle Objekte in der Tabelle. Standard ist currentExtent.
        tableFields:    # Definition der Spalten für die Objekttabelle
            gid: {label: Nr. , width: 20%}    # [Tabellenspalte]: {label: [Beschriftung], width: [css-Angabe z.B. Angabe der Breite]}  # Definition einer Spalte
            name: {label: Name , width: 80%}



Definition von Dateireitern (type tabs)
---------------------------------------

.. code-block:: yaml

        formItems:
           - type: tabs                      # Type tabs erzeugt Reiter im Erfassungsformular
             children:                       # Die Reiter werden als Unterobjekte (children) vom Type form definiert.
               - type: form
                 title: Basic information    # Titel des Reiters
                 css: {padding: 10px}
                 children:                   # Durch mehrere Unterobjekte in Gruppen können Angaben im Formular nebeneinander angeordnet werden.
                     - type: label
                       title: Welcome to the digitize demo. Try the new Mapbender3 feature!
                       ...


Definition von Textfeldern (type input)
.......................................

.. code-block:: yaml

                                                 - type: input                    # Typ Textfeld
                                                   title: Title for the field     # Beschriftung mit dem Titel des Feldes (optional)
                                                   name: column_name              # Referenz zur Tabellenspalte
                                                   mandatory: true                # Angabe ob Pflichtfeld (optional)
                                                   mandatoryText: You have to provide information. # Text sofern Pflichtfeld nicht gefüllt ist
                                                   infoText: 'Bitte geben Sie einen Wert an' # Definition eines Informationstextes
                                                   value: 'default Text'          # Definition eines Standard-Wertes  (optional)
                                                   placeholder: 'please edit this field' # Platzhalter, der vor der Eingabe erscheint (optional)


Definition von Auswahlboxen (selectbox oder multiselect [type select])
-------------------------------------------------------------------------

Durch die Definition einer Auswahlbox können vordefinierte Werte im Formular genutzt werden.
Hier wird in eine Auswahlbox mit einem wählbaren Eintrag (type select) und einer Auswahlbox mit mehreren auswählbaren Einträgen (type multiselect) unterschieden.

1) **select** - ein Eintrag kann ausgewählt werden

.. code-block:: yaml

                                                 - type: select                     # Typ Auswahlbox
                                                   title: select some types         # Beschriftung mit dem Titel des Feldes (optional)
                                                   name: my_type                    # Referenz zur Tabellenspalte
                                                   multiple: false                  # Definition einer Mehrfachauswahl (multiselect), Standard ist false
                                                   options:                         # Definition der Optionen (key: value)
                                                       1: pub
                                                       2: bar
                                                       3: pool
                                                       4: garden
                                                       5: playground

2) **multiselect** - mehrere Einträge können ausgewählt werden

Die Nutzung der Multiselect-Box ist noch experimentell. Bei dem Abspeichern von Einträgen werden nur Zahlen abgespeichert (Bsp.: Auswahl a und b --> 1,2).
Es kann keine Angabe zur Beschriftung gemacht werden (Bsp.: options:  [1: pub,2: bar, 3: pool]).

.. code-block:: yaml


                                                 - type: select                       # Typ Auswahlbox
                                                   title: Wählen Sie einen Typ aus    # Beschriftung mit dem Titel des Feldes (optional)
                                                   name: my_type                      # Referenz zur Tabellenspalte
                                                   multiple: true                     # Definition einer Mehrfachauswahl (multiselect), Standard ist false
                                                   options: [a,b,c]                   # Definition der Optionen (key: value)

                                                   # Beispielhafte Angabe einer Liste über Paramter seperator
                                                   separatator: ','
                                                   fieldType: 'array'
                                                   options:  ['Prof.','Dr.', 'med.', 'jur.','vet.','habil.']


**Füllen der Auswahlboxen über eine SQL Abfrage**

.. code-block:: yaml

                                                 - type: select                     # Typ Auswahlbox
                                                   title: select some types         # Beschriftung (optional)
                                                   name: my_type                    # Referenz zu Tabellenspalte
                                                   connection: connectionName       # Definition einer Datenbankverbindung (connection)
                                                   sql: 'SELECT DISTINCT key, value FROM tableName order by value' # Definition SQL, Abfrage der Werte key und value



Definition von Texten (type label)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: label      # Typ Label schreibt einen nicht bearbeitbaren Text in das Formularfenster.
                                                   title: 'Please give information about the poi.' # Definition eines nicht bearbeitbaren Textes.


Definition eines Textes (type text)
-------------------------------

Im Formular können Texte definiert werden. Hierbei kann auf Felder der Datenquelle zugegriffen werden, dazu wird JavaScript verwendet.

.. code-block:: yaml

                                                - type: text              # Typ text zur Generierung von dynamischen Texten aus der Datenbank
                                                  title:       Name       # Beschriftung (optional)
                                                  name:        name       # Referenz zu Tabellenspalte, dessen Inhalt angezeigt werden soll
                                                  css:         {width: 80%} # CSS Definition (optional)
                                                  text: data.gid + ': ' + data.name
                                                  # Text Definition in JavaScript
                                                  # data - Angabe, dass Datenbankfeld aus der Tabelle angesprochen wird.
                                                  # z.B.: data.gid --> Anzeige der ID der Geometrie im Textfeld

Definition von Textbereichen zur Eingabe (type textArea)
--------------------------------------------------------------

Ähnlich zum Textfeld über type input (siehe oben) können hier Textbereiche erzeugt werden, die bei type textArea mehrere Zeilen umfassen können.

.. code-block:: yaml

                                                 - type: textArea      # Typ textArea erzeugt einen Textbereich
                                                   rows: 4             # Anzahl der Zeilen für den Textbereich, die beim Öffnen des Formulars erscheinen. Feld kann per Maus im Formular größer gezogen werden.
                                                   name: beschreibung  # Tabellenspalte
                                                   title: Bestandsaufnahme Bemerkung # Beschriftung (optional)


Definition von Trennlinien (type breakline)
--------------------------------------------------

.. code-block:: yaml

                                                 - type: breakline      # fügt eine einfache Trennlinie ein


Definition von Checkboxen (type checkbox)
--------------------------------------------------

.. code-block:: yaml

                                                 - type:  checkbox        # Typ checkbox erzeugt eine Checkbox. Beim Aktivieren wird in die Datenbank der angegebene Value (hier 'TRUE') geschrieben.
                                                   title: Is this true?   # Beschriftung (optional)
                                                   name:  public          # Referenz zu Tabellenspalte
                                                   value: true            # angegebener Parameter beim Aktivieren der Checkbox wird in DB gespeichert (hier 'TRUE').




Definition von Pflichtfeldern
--------------------------------------------------

Die Hinweise für ein Pflichtfeld erscheinen über dem jeweiligen Feldern. Bei einer fehlenden Angabe in einem definierten Pflichtfeld wird dieses rot umrandet und (wenn vorher definiert) erscheinen Hinweise. Das Objekt kann nicht gespeichert werden, wenn Pflichtangaben fehlen.

Hinweis: Bei der Nutzung von mehreren Reitern in dem Formular kann es sein, dass der Erfasser bei einem Pflichtfeld auf einem nicht sichtbaren Reiter eine Angabe falsch setzt und das Abspeichern daher nicht funktioniert.
Hier erscheint keine Fehlermeldung außerhalb des Formulars. Der Erfasser muss die Angaben in dem Formular überprüfen (Kennzeichen: rote Umrandung/ Sprechblase mit Hinweis), bevor diese korrekt abgespeichert werden können.

.. code-block:: yaml

                                                 - type:  [Angabe zum Feldtyp]           # jedes Feld kann zum Pflichtfeld gemacht werden

                                                   mandatory: true                       # true - Das Feld muss gefüllt werden. Ansonsten kann der Datensatz nicht gespeichert werden. Bei der Definition sind auch reguläre Ausdrücke möglich.
                                                   mandatorytitle: Pflichtfeld füllen!   # Text der im Feld angezeigt wird, wenn das Feld nicht gefüllt wird oder mit einem ungültigen Wert gefüllt wird.
                                                   mandatoryText: Bitte eine Zahl eingeben! # Text der in einer Sprechblase über dem Feld angezeigt wird, wenn das Feld beim Speichern nicht gefüllt ist oder mit einem ungültigen Wert gefüllt ist.
                                                   mandatory: /^\w+$/gi                  # Es können auch reguläre Ausdrücke angegeben werden, um die Eingabe zu überprüfen (z.B. Email oder numbers) Weitere Informationen unter: http://wiki.selfhtml.org/wiki/JavaScript/Objekte/RegExp

                                                   # Prüfung, ob die Eingabe eine Zahl ist
                                                   mandatory: /^[0-9]+$/
                                                   mandatoryText: Bitte eine Zahl eingeben!


Definition eines Textfelds mit Datumsauswahl
--------------------------------------------------

.. image:: ../../../../../figures/digitizer_datepicker.png
     :scale: 80

.. code-block:: yaml

                     - type: date              # Textfeld, das eine Datumsauswahl bereitstellt
                       title: favorite Date    # Beschriftung (optional)
                       name: date_favorite     # Referenz zu Tabellenspalte
                       placeholder: Bitte geben Sie das Datum in der folgende Form an dd.mm.yy  # Platzhalter für die Datumsauswahl (optional)
                       dateFormat: dd.mm.yy     # Format für die Datumsanzeige, Standardformat dd.mm.yy (16.01.2016). Weitere Beispiele yy/mm/dd (2017/01/16) oder yy-mm-dd (2017-01-16).
                       value: 01.01.2017        # Startwert für die Datumsauswahl (optional)

Bei der Nutzung einer Spalte mit dem Tabellenformat date wird das angegebene Datum unabhängig von der Angabe dateFormat in dem Format YYYY-MM-DD in die date-Datenbankspalte geschrieben.
Fallls der Parameter dateFormat genutzt wird für eine andere Ansicht oder Abspeicherung muss ein Tabellenfeld im Textformat (z.B. date_text varchar) angelegt werden.



Definition von Hilfetexten zu den Eingabefeldern
------------------------------------------------------------------------------------------

Anders als bei Hifetexten zu den Pflichtfeldern kann der Infotext über jedem Feld erscheinen, unabhängig davon, ob dieses ein Pflichtfeld ist oder nicht. Bei der Angabe infotext: [Text] erscheint ein Info-Button über dem jeweiligen Feld.
Der Klick auf diesen Button öffnet den angegebenen Informationstext.

.. code-block:: yaml

                                                 - type:  [Angabe zum Feldtyp]           # jedes Feld kann einen Infotext nutzen

                                                   infoText: In dieses Feld dürfen nur Zahlen eingegeben werden  # Hinweistext, der angezeigt wird über i-Symbol.


Definition von Gruppierungen (type: fieldSet)
--------------------------------------------------

Elemente können in einer Zeile gruppiert werden, um logische Einheiten zu bilden oder um Platz zu sparen. Hierbei muss ein fieldSet definiert werden. Anschließend können die Elemente der Gruppe unter children angegeben werden.
Für jedes Gruppenelement kann eine Breite über CSS angegeben werden, um die Aufteilung der Zeile für die angegebenen Elemente zu kontrollieren.

.. code-block:: yaml

                     - type: fieldSet            # Gruppierung von Feldern, unabhängig vom Feldtyp
                       children:                 # Angabe der Gruppenelemente unter children
                           - type: input
                             title: Vorname
                             name: firstname
                             css: {width: 30%}   # Angabe der Breite des Gruppenelements. Zusammen sollten die Elemente 100% ergeben.
                           - type: input
                             title: Nachname
                             name: lastname
                             css: {width: 30%}
                           - type: input
                             title: E-Mail
                             name: email
                             css: {width: 40%}



Definition von Feldern für den Dateiupload
--------------------------------------------------

Über den Dateiupload können Dateien durch die Angabe in einer Datenbankspalte im Formular verknüpft werden. Dazu werden die hochgeladenen Dateien im Mapbender3 gespeichert und der Pfad in der Spalte vermerkt.
Der Speicherpfad und der Name der abgespeicherten Dateien kann bis jetzt nicht verändert werden. Der Dateiupload speichert immer in das gleiche Verzeichnis.
Pfad: http://localhost/mapbender3/uploads/featureTypes/[tabellenname]/file_reference/[dateiname].png

Für die Ansicht von eingebundenen Bildern kann das Bild-Element dazugenommen werden.

.. code-block:: yaml

                    - type: file                # Typ file für das Hochladen von Dateien
                      title: Dateiupload        # Beschriftung (optional)
                      text: Laden Sie ein Bild hoch. # Informationstext zum Feld (optional)
                      name: file_reference      # Angabe der Datenbankspalte, in die der Speicher-Pfad geschrieben wird


                      # Experimentelle Parameter:
                      #accept: image/*          # Vorauswahl von Elementen im Image-Format (Fenster für Dateiupload öffnet sich mit Einschränkungsfilter)
                                                # Speichert z.B. png und speichert nicht pdf/txt. Achtung: Es erscheint keine Fehlermeldung beim falschen Format!



Definition der Bildanzeige
-----------------------------

Für die Ansicht von einem Bilde in dem Formular kann das Bild-Element genutzt werden. Durch die Angabe einer URL in einem Datenbankfeld oder einer URL über den src-Parameter können Bilder angezeigt werden.
Bilder, die durch das Element Dateiupload in einer Tabellenspalte vermerkt sind können somit auch direkt eingebunden und angezeigt werden.
Das Bild lässt sich durch die Angabe von den beiden Parametern src und name angeben.
* **src**: Url-Pfad oder Dateipfad (kann relativer Pfad sein)
* **name**: Url-Pfad oder Dateipfad wird aus der Tabellenspalte übernommen (kann kein relativer Pfad sein)
* Anagbe von name und src zusammen: Der Inhalt der Datenbankspalte aus name wird genommen. Falls die Spalte leer ist wird die src-Angabe genutzt.


.. code-block:: yaml

                    - type: image               # Type image für das Anzeigen von Bildern
                      name: file_reference      # Referenz zur Datenbankspalte. Wenn definiert, wird der Pfad oder die URL in dem Feld ermittelt und "src" Option ersetzt
                      src: "bundles/mapbendercore/image/logo_mb3.png"  # Angabe eines Pfades oder URL zu einem Bild. Falls der relative Pfad genutzt wird muss relative: true stehen.
                      relative: true            # Optional. Standardwert ist false. Wenn true, wird der "src" Pfad ab dem "/web" Verzeichniss ermittelt.
                      enlargeImage: true        # Bild wird beim Klick auf das Vorschaubild auf Originalgröße/maximale Auflösung vergrößert. Achtung: keine Skalierung auf die Bildschirmgröße.

                      # Experimentelle Angaben zum Styling
                      imageCss:
                        width: 50%              # Image CSS Style: Skaliert das Vorschaubild in dem Formular, abweichend von der Originalgröße in Prozent.
                        height: 50%             # Angabe von width und height ist besser für die Ansicht, sonst werden Teile eventuell abgeschnitten.
                      css: {width: 25%}         # Image Container CSS Style: Skaliert bei Angabe von imagecss wieder runter, daher nicht empfohlen.

Achtung: Wenn nur name und nicht name und src angegeben wird, erscheint bei leeren Spalteneinträgen ein Bild aus dem vorherigen Dateneintrag.
Dynamische Pfade (z.B. "bundles/mapbendercore/image/[nr].png" oder 'bundles/mapbendercore/image/' + data.image_reference) können nicht angegeben werden.
Eine Möglichkeit das zu Umgehen wäre ein Trigger, der in die Datenbankspalte beim Insert den Pfad und den Inhalt eines Tabellenfeldes als Name zusammenführt.


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
* **modifyFeature** - einzelne Knotenpunkte bei Geometrien verschieben
* **moveFeature** - Geometrien verschieben
* **selectFeature** - Geometrien de-/selektieren
* **removeSelected** - die selektierten Geometrien löschen
* **removeAll** - Vorsicht: alle Geometrien aus der Tabelle löschen

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


Definition der Tabellensuche (inline Search)
------------------------------------------------------------------------

Über die Suche können Begriffe in der Tabelle gesucht werden.
Die aktivierte Sucheleiste erscheint über der Tabelle und nach der Eingabe eines Suchbegriffs werden alle Spalten dieser Tabelle durchsucht und deren Ergebnisse angezeigt.

.. code-block:: yaml

  poi:
      ...
      inlineSearch: true      # Suche in den Tabellenspalten, Standard ist true
      ...



Definition des Kontextmenüs (Context Menu)
-----------------------------------------------

Über das Kontextmenü kann ein Objekt auf der Karte näher betrachtet werden.
Nach der Aktivierung kann man über den rechten Mausklick auf einem Objekt ein Kontextmenü öffnen.

.. image:: ../../../../../figures/digitizer_contextmenu.png
     :scale: 80

Elemente des Kontextmenüs:

* **Heranzoomen:** Auf den Kartenausschnitt des Objekts zoomen.
* **Bearbeiten:** Informationen zu dem Objekt verändern. Klick öffnet die Digitalisieroberfläche.
* **Löschen:** Löscht das ausgewählte Objekt.


.. code-block:: yaml

  poi:
      ...
      useContextMenu: true
      ...


Definition des Clustering
------------------------------

Über das Clustering können die Objekte auf der Karte zusammengefasst werden.
Abhängig von der definerten Distanz und Zoomstufe werden unterschiedlich viele Objekte zusammengeführt.


.. image:: ../../../../../figures/digitizer_clustering.png
     :scale: 80

Definition der Clusterelemente:

* **scale:** Zoomstufe.
* **distance:** Distanz zwischen einzelne Features in Metern, die zusammengefügt werden.
* **disable:** Schaltet Clustering für die Zoomstufe ab.


.. code-block:: yaml

  poi:
      ...
      clustering:
          -
              scale: 10000        # Zoomstufe
              distance: 60        # Distanz zwischen einzelne Features in Metern, die zusammengefügt werden
          -
              scale: 2500
              distance: 40
          -
              scale: 1000
              distance: 20
          -
              scale: 500
              distance: 1
              disable: true       # Schaltet Clustering für die Zoomstufe ab
      ...



Definition zur Sicherung von Feldern und Speichern von Benutzerdaten
----------------------------------------------------------------------

Über die Definition der Nutzerrollen, Gruppen u.ä. können die Daten nach vordefinierten Angaben abgesichert werden. Dazu ist die Angabe eines Datenbank-Feldes mit den entsprechenden Informationen, z.B: Nutzerrollen nötig.

Es gibt mehrere Events, die genutzt werden können, um entweder Daten nur für bestimmte Personen zugänglich zu machen, oder bestimmte Benutzerdaten bei dem Editieren von Daten zu speichern:

* **onBeforeSave**: Event vor dem Speichern von neuen/ veränderten Informationen
* **onBeforeSearch**: Event vor dem Suchen in SearchField des Digitizers
* **onBeforeRemove**: Event vor dem Löschen von Daten
* **onAfterSearch**: Event nach dem Suchen in SearchField des Digitizers
* **onAfterSave**: Event nach dem Speichern von neuen/ veränderten Informationen
* **onAfterRemove**: Event nach dem Löschen von Daten

Die Events können in ähnlicher Form auch bei den Sachdaten ohne Geometrien im DataStore genutzt werden. Dazu mehr unter der Seite des Data Managers :doc:`data_manager`.

Achtung: Die Events sind eine experimentelle Entwicklung und sollten mit Vorsicht eingebunden werden.
Die korrekte Abstimmung der Events aufeinander wurde noch nicht vollständig getestet, daher kann es zu Fehlverhalten kommen.

.. code-block:: yaml

    poi:
        label: point digitizing
        inlineSearch: true
        maxResults: 500
        featureType:
            connection: search_db
            table: poi
            uniqueId: gid
            geomType: point
            geomField: geom
            srid: 4326
            events:        # Speichern des Benutzernamens, Gruppennames und des Änderungsdatums nach dem Speichern eines Objekts
              onBeforeSave: |
                $feature->setAttribute('user_name', $user->getUsername());
                $feature->setAttribute('modification_date', date('Y-m-d'));
                $feature->setAttribute('group_name', implode(',',$userRoles));


Definition der DataStore-Verbindung
--------------------------------------

Um die Sachdaten ohne Geometrien aus einem DataManager-Element in dem Digitizer anzuzeigen und zu bearbeiten kann man eine Verbindung zu einem bestehenden DataStore einrichten.
Dazu muss ein select-Feld mit Angabe der DataStore-Verbindung eingefügt werden.


.. code-block:: yaml

        - type: select
          id: interests_datastore
          name: interests_datastore
          dataStore:                    # Verbindung zum DataStore Element
            id: interests               # DataStore ID
            text: name
            uniqueId: gid
            editable: true              # true aktiviert das Editieren der Sachdaten
            popupItems:                 # Elemente im Dialog
              - { name: name, title: Name, type: input }
              - { name: sports, title: Sportart, type: input }
              - { name: healthy, title: Gesund, type: input }
              - { name: comment, title: Kommentar, type: input }

.. image:: ../../../../../figures/digitizer_datamanager.png
     :scale: 80

.. image:: ../../../../../figures/digitizer_datamanager_popup.png
     :scale: 80

**Definition der Nutzerrollen für den DataStore**


Über die Definition der Nutzerrollen können die Daten nach Benutzerrollen gesichert werden. Dazu ist im ersten Schritt die Angabe eines Datenbank-Feldes mit den Nutzerrollen nötig.

.. code-block:: yaml

        - type: select
          id: interests_datastore
          name: interests_datastore
          dataStore:
              connection: search_db           # Verbindung zum DataStore Element
              table: public.interests_datastore
              uniqueId: gid
              fields: [name, sports , healthy, comment]
            popupItems:
               - name: User_Roles              # Sicherung der Daten nach Benutzerrollen durch Angabe des DB-Feldes
                 title: 'Nutzerrollen'
                 type: select
                 service:
                     serviceName: security.context
                     method: getRolesAsArray


**Definition des DataStores für die Verbindung**

Im folgenden wird die Definition des DataStores für die korrekte Anzeige der Daten im Digitizer-Element gezeigt. Hier können die Felder und Datensätze gegen eine Gruppe oder einen User abgesichert werden.
Der Digitizer kann Benutzer (username), Gruppe und Datum (moddate) automatisch in spezifizierbare Felder schreiben. Das Abspeichern und Löschen eines Datensatzes ist nur möglich wenn der User einer bestimmten Gruppe/ Rolle angehört.

Angaben in der parameters.yml:

.. code-block:: yaml

    dataStores:
         interests:
            connection: search_db
            table: interests_datastore
            uniqueId: gid
            fields: [name, sports, healthy, comment]                                 # table fields to use for the datastore
            events:
              onBeforeSave: |
                  $item["user_name"] = $user->getUsername();                         # storing the username of the object
              onBeforeUpdate:
                  $item["user_name"] = $user->getUsername();


In sämtlichen Events steht das user-Object $user und die userRolen $userRoles zur Verfügung.
Zusätzlich steht in den remove- und save-Events noch das orignal Datenbankobject $originData zur Verfügung.


Definition der Darstellung (Styles)
--------------------------------------

Über die Angabe eines Styles kann definiert werden, wie die Objekte angezeigt werden.
*Default* definiert dabei die normale Darstellung der Objekte auf der Karte und *Select* die Darstellung der ausgewählten Objekte.

.. code-block:: yaml

  poi:
      ...
      styles:
          default:
              strokeWidth: 2
              strokeColor: '#0e6a9e'
              fillColor: '#1289CD'
              fillOpacity: 1
              fillWidth: 2
              pointRadius: 10
          select:
              strokeWidth: 3
              strokeColor: '#0e6a9e'
              fillOpacity: 0.7
              pointRadius: 10
      ...



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


