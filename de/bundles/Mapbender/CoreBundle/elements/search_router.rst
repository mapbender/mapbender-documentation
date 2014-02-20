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
        connection: search_db
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

   target: map  # für die Ergebnisanzeige
   asDialog: true  # true, false im Dialog rendern
   timeoutFactor:  2  # timeout Faktor (multipliziert mit automatischem Verschiebungfaktor), um die automatische Vervollständigung direkt nach dem Start der Suche zu verhindern
   routes:      # Sammlung von Suchrouten
       demo_a:  # maschinenlesbarer Name
           title: Demo A  # von Menschen lesbarer Name
           class: Mapbender\CoreBundle\Component\SQLSearchEngine  # aktuelle Suchmaschine
           class_options:  # die class-options werden zur Suchmaschine weitergeleitet
               connection: ~  # verwendeter DBAL Verbindungsname, verwenden Sie ~ für den Standardnamen
               relation: test.demo_a  # ausgewählte Relation, Sie können Unterabfragen verwenden
               attributes: [id, name]  #  Array von Spalten, die ausgewählt werden können, Ausdrücke (expressions) sind möglich
               geometry_attribute: geom  # Name der Geometriespalte für die Suchanfrage
           form:  # Suchformularkonfiguration
               the_name:  # Feldname, verwenden Sie Relationsspaltennamen für die Abfrage oder anderes für geteilte Felder (siehe unten)
                   type: text  # Feldtyp, normalerweise Text oder Integer
                   options:  # Feld Optionen
                       required: true  # für HTML5 erforderliche Attribute, Standard ist true
                       label: Custom Label  #  Fügen Sie eine benutzerdefinierte Beschriftung ein, ansonsten wird der Feldname als Beschriftung verwendet     
                       attr:  # HTML Attribute
                           data-autocomplete: on  # automatische Datenvervollständigung, Standard ist on (eingeschaltet)
                   split: [name, zusatz]  # optionales Feld, kann geteilt werden
                   autocomplete-key: id  # Spaltenname, der als automatisch vervollständigter Schlüssel zurückgegeben wird (statt eines Spaltenwertes)
                   compare: ~  # Siehe unten Vergleichsmodus
           results:
               view: table  # aktuelle Ergebnisansicht
               headers:  #    Hash des Tabellen-Headers und die entsprechenden Ergebnisspalten
                   id: ID  # Spaltenname -> Header Beschriftung
                   name: # Name
               callback:  #  Was soll beim Klick/Mousover passieren
                   event: click  # Ereignis, auf das gehört werden soll (Klick oder Mouseover)
                   options:
                       buffer: 10  # Wert des Puffers für die Geometrie des Ergebnisses, bevor gezoomt wird
                       minScale: ~  # Maßstabsbeschränkung für das Zoomen
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
