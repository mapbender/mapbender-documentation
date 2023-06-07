.. _datamanager_de:

Data Manager
************

Der Data Manager ähnelt in seiner Funktionalität dem `Digitizer <digitizer.html>`_. Der Data Manager speichert allerdings nur Sachdaten und keine Geodaten.

Der Data Manager kann zur Pflege von Referenztabllen verwendet werden, beispielsweise einer Tabelle mit Kontaktinformationen.


Setup
-----

Der Data Manager benötigt einen Zugriff auf die Datenbank, in der die zu editierenden Tabellen liegen. Sie müssen dazu einen Datenbankzugriff konfigurieren.
Mehr zu diesem Thema finden Sie unter `Konfiguration der Datenbank <../../customization/yaml.html>`_.

Konfigurationsbeispiel
----------------------

Die Definition des Data Managers erfolgt im YAML-Syntax. 
Hier definieren Sie die Datenbankverbindung, die editierbaren Felder, den Formularaufbau.


.. hint:: Bei fehlerhaften Angaben zur Datenbank, Feldern und Formularfehler erscheinen Fehlermeldungen. Über den normalen Aufruf und app.php kommt eine allgemeine Fehlermeldung. Falls Sie die detaillierte Fehlermeldung sehen möchten, sollten Sie die Seite über app_dev.php aufrufen. Hier tauchen ausführliche Fehlermeldungen zum Fehlerverhalten auf.


Der Data Manager kann beispielsweise genutzt werden, um Kontaktinformationen zu speichern.

.. image:: ../../../figures/de/data_manager.png
     :scale: 80

In dem dargestellten Konfigurationsbeispiel öffnet sich eine Eingabevorlage nach Klick auf das ``+``-Zeichen.

.. image:: ../../../figures/data_manager_form.png
     :scale: 80

SQL for the contact table
--------------------------

The following SQL commands must be executed in your database to create the contact table for the example.

.. code-block:: postgres

   CREATE TABLE public.contacts (
        gid serial PRIMARY KEY,
        firstname varchar,
        lastname varchar,
        street varchar,
        housenumber varchar,
        postcode integer,
        location varchar,
        phone varchar,
        email varchar,
        notes varchar,
        public boolean,
        date_of_creation date DEFAULT date(now()),
        user_of_last_edit varchar,
        date_favorite date,
	color_favorite varchar
    );


Element-Konfiguration
---------------------

Das Element kann danach in die Seitenleiste eingebettet werden.

.. image:: ../../../figures/de/data_manager_configuration.png
     :scale: 80

YAML-Definition
---------------

Im Folgenden ist der YAML-Code des oben dargestellten Konfigurationsbeispiels hinterlegt:

.. code-block:: yaml

    contacts:
      dataStore:
        connection: geodata_db
        table: contacts
        uniqueId: gid
        events:
          onBeforeSave: '$feature->setAttribute(''user_of_last_edit'', $user ); '    
      allowEdit: true
      allowCreate: true
      allowDelete: true
      allowRefresh: false
      popup:
        title: contacts
        width: 550px
      formItems:
        -
          type: form
          children:
            -
              type: label
              title: 'Example for element Data Manager'        
            -
              type: fieldSet
              children:
                -
                  type: input
                  title: last name
                  attr:
                      placeholder: 'Please enter your last name.'
                  name: lastname
                  css:
                    width: 50%
                -
                  type: input
                  title: 'first name'
                  name: firstname
                  css:
                    width: 50%
            -
              type: breakLine
            -
              type: fieldSet
              children:
                -
                  type: input
                  title: street
                  name: street
                  css:
                    width: 30%
                -
                  type: input
                  title: 'house number'
                  name: housenumber
                  css:
                    width: 20%
                -
                  type: input
                  title: postcode
                  name: postcode
                  css:
                    width: 20%
                -
                  type: input
                  title: location
                  name: location
                  css:
                    width: 30%

            -
              type: fieldSet
              children:
                -
                  type: date
                  title: date_favorite
                  name: date_favorite
                  css:
                    width: 50%
                -
                  type: colorPicker
                  title: color favorite
                  name: color_favorite
                  attr:
                    placeholder: '#ff0000'
                  css:
                    width: 50%
            #-
            #  type: breakLine
            -
              type: fieldSet
              children:
                -
                  type: input
                  title: phone number
                  name: phone
                  mandatory: true
                  mandatoryText: 'Please add your phone number.'
                  infoText: 'Help: Please add your phone number.'
                  copyClipboard: true              
                  css:
                    width: 50%              
                -
                  type: input
                  title: email
                  infoText: 'Help: Please add your e-mail.'
                  copyClipboard: true              
                  placeholder: 'Please enter your e-mail.'
                  name: email
                  css:
                    width: 50%
            -
              type: breakLine
            -
              type: textArea
              title: notes
              placeholder: 'You can leave notes here.'
              name: notes
              value: 'Guter Tester'
            -
              type: checkbox
              name: public
              value: true
              title: 'publish contact'          
            -
              type: text
              title: 'Information'
              text: "'user: ' + data.user_of_last_edit + ' Datum:' + data.date_of_creation\n"           
            - type: radioGroup
              title: Choose one
              name: choice_column_1
              options:
                - label: Option 1
                  value: v1
                - label: Option 2
                  value: v2
                - label: Option 3
                  value: v3                          
              value: v2   # Pre-select second option by default for new items
            - type: select
              title: Select at least one (multiple choice)
              attr:
                required: required
                multiple: multiple
              name: choice_column_2
              options:
                - label: Option 1
                  value: v1
                - label: Option 2 (disabled)
                  value: v2
                  attr:
                    disabled: disabled
                - label: Option 3
                  value: v3
                - label: Option 4
                  value: v4                            
              value: v1,v3   # use comma-separated values for default multi-select value          
      table:
        autoWidth: false
        columns:
          -
            data: lastname
            title: last name
          -
            data: firstname
            title: first name
        info: true
        lenghtChange: false
        ordering: true
        pageLength: 10
        paging: true
        processing: true
        searching: true


