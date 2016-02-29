.. _simplesearch:

SimpleSearch
************

SimpleSearch bietet eine einstufige Lösung für Geodatenabfragen an, betrieben wird diese z.B. von Solr. Es wird ein Eingabefeld verwendet, welches direkt in die Toolbar eingebunden werden kann. Es sendet den eingegebenen Suchbegriff an eine konfigurierbare URL. Diese empfängt JSON-formatierte Daten, welche eine Beschriftung und Geometrieattribute für jeden Eintrag beinhaltet.

Die Geometriedaten können in WKT oder in GeoJSON-Format codiert werden.

.. image:: ../../../../../figures/simplesearch.png
     :scale: 80


Konfiguration
=============

.. image:: ../../../../../figures/de/simplesearch_configuration_a.png
     :scale: 80

.. image:: ../../../../../figures/de/simplesearch_configuration_b.png
     :scale: 80
             
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Query URL:** Solr URL, an die der eingegebene Suchbegriff gesendet wird (z.B. ``http://localhost:8080/solr/core0/select?wt=json&indent=true``).
* **Query URL key:** Der Suchparameterschlüssel, der angehängt wird (z.B. ``q``).
* **Query Whitespace replacement pattern:** Pattern zum Austausch von Leerzeichen.
* **Query key format:** Einfaches Suchformat (z.B. ``%s``).
* **Token search/ replace (JavaScript regex):** Tokenizer spaltet/ sucht/ ersetzt regexp.

  * Token, z.B.: ``[^a-zA-Z0-9äöüÄÖÜß]``
  * Token search, z.B.: ``([a-zA-ZäöüÄÖÜß]{3,})``
  * Token replace, z.B.: ``$1*``
    
* **Collection path:** Dies kann ein Attributspfad sein, der vom Abfrageergebnis extrahiert wird (z.B. ``response.docs``).
* **Label attribut:** Attrubutname der zur Beschriftung genutzt wird (z.B. ``label``).
* **Geom attribut:** Name der Attribute der Geometriedaten (z.B. ``geom``).
* **Geom format:** Geodatenformat, kann WKT oder GeoJSON sein (z.B. ``WKT``).
* **Delay:** Automatische Vervollständigungs-Verzögerung (z.B. ``300``).
* **Result buffer:** Puffert das Objekt (in Karteneinheiten) vor dem Zoomen (z.B. ``10``).
* **Result minscale/ maxscale:** Maßstabsbegrenzung beim Zoomen (z.B. ``1000`` und ``5000``). ~ wenn keine Begrenzung gewünscht wird.
* **Result icon url:** Symbol, das zur Trefferanzeige verwendet werden soll (z.B. ``http://demo.mapbender3.org/bundles/mapbendercore/image/pin_red.png``).
* **Result icon offset:** Abstand x und y des Symbols (z.B. ``-6,-38`` für das Stecknadel-Icon).



YAML-Definition:
----------------

.. code-block:: yaml

   query_url: http://example.com/solr/core/0/select?wt=json&indent=true&rows=8   # Solr URL (z.B. ``http://localhost:8080/solr/core0/select?wt=json&indent=true``).
   query_key: q                                                                  # Der Suchparameterschlüssel, der angehängt wird
   query_ws_replace:                                                             # Pattern zum Austausch von Leerzeichen.
   query_format: '%s'                                                            # Einfaches Suchformat.
   token_regex: [^a-zA-Z0-9äöüÄÖÜß]                                              # Tokenizer split regexp.
   token_regex_in: ([a-zA-ZäöüÄÖÜß]{3,})                                         # Tokenizer search regexp.
   token_regex_out: '$1*'                                                        # Tokenizer replace regexp.
   collection_path: response.docs                                                # Es kann ein Attributspfad sein, der vom Abfrageergebnis extrahiert wird.
   label_attribute: label                                                        # Attributname, der für die Trefferausgabe genutzt wird 
   geom_attribute: geom                                                          # Name des Attributs der Geometriedaten 
   geom_format: WKT                                                              # Geodatenformat, kann WKT oder GeoJSON sein
   delay: 300                                                                    # Automatische Vervollständigungs-Verzögerung. 0   result_buffer: 50                                                             # Buffert die Geometrieergebnise (Karteneinheiten) vor dem Zoomen
   result_minscale: 1000                                                         # Maßstabsbegrenzung beim Zoomen, ~ für keine Begrenzung
   result_maxscale: 5000
   result_icon_url: http://demo.mapbender3.org/bundles/mapbendercore/image/pin_red.png # Marker, der zur Trefferanzeige verwendet werden soll
   result_icon_offset: -6,-38                                                    # Offset x und y des Symbols
   

Class, Widget & Style
=========================

* **Class:** Mapbender\\CoreBundle\\Element\\SimpleSearch
* **Widget:** mapbender.element.simplesearch.js

HTTP Callbacks
==============

- /search: Proxy-Element, welches die konfigurierbare URL abfragt. Im Entwicklungsmodus wird die endgültige Abfrage-URL zum einfachen Debugging als ein x-mapbender-simplesearch-url Header zurückgegeben.

JavaScript API
==============

Keine.

JavaScript Signals
==================

Keine.

So richten Sie Solr ein:
========================

Installation
------------

Laden Sie Apache Solr herunter und entpacken Sie es in einen beliebigen Ordner. Nach dem erfolgreichen Entpacken der Datei kann Solr durch den Aufruf von solr/bin/install_solr_service.sh als Service in einem Linux-System installiert werden.
* **Download**: http://lucene.apache.org/solr/
* **Dokumentation**: http://lucene.apache.org/solr/resources.html#documentation 

**Installation** von Apache Solr über das Terminal im data-Verzeichnis: 

.. code-block:: yaml
    cd /data
    wget http://apache.lauf-forum.at/lucene/solr/5.4.1/solr-5.4.1.tgz
    tar -zxvf solr-5.4.1.tgz
    cd solr-5.4.1/


Start und Stopp
---------------

Sie können durch die folgende Befehle Solr über das Terminal starten und stoppen:

* **Start Solr:**
** /sites/solr-5.4.1/bin/solr start -s /sites/solr_data
* **Solr Stop:**  
** /sites/solr-5.4.1/bin/solr stop -all


Solr-Core
---------

Der Solr-Home Ordner ist der Bereich, in dem sich die verschiedenen Solr-Kerne für die Suche befinden. Die Minimalkonfiguration wird in folgender Datei vorgenommen:

Datei: /opt/solr-home/solr.xml

Tragen Sie den folgenden XML-Block in die Datei ein:

.. code-block:: yaml
    <?xml version="1.0" encoding="UTF-8" ?>
    <solr></solr>

Für die Anlage der Kerne erstellen Sie einen Ordner unter data/solr_data. Jeder Core besteht aus den drei Konfigurationsdateien: 
* **core.properties**
* **solrconfig.xml** 
* **schema.xml**

Durch die core.properties wird der Core von Solr als Kern erkannt. Die solrconfig.xml beschreibt den Funktionsumfang den dieser Kern mit sich bringt. Und die schema.xml beschreibt den Aufbau des Index.

Eventuelle Anpassung der Konfigurationsdateien unter /data/solr_data/places(/conf): 
* core.properties
* solrconfig.xml
* schema.xml

Solr example
------------

Das Verzeichnis /solr-5.4.1/example enthählt Beispiele für Solr. Jedes Beispiel ist in einem seperaten Verzeichnis abegelegt. Um ein bestimmtes Beispiel auszuführen, geben Sie den folgenden Befehl im Terminal ein:

  bin/solr -e <EXAMPLE> where <EXAMPLE> is one of:
  
    cloud        : SolrCloud Beispiel
    dih          : Datenimport Handler (rdbms, mail, rss, tika)
    schemaless   : Schemaloses Beispiel (Schema wird durch die Daten währen dem Indizieren abgeleitet)
    techproducts : Beispiele für umfassende Funktionen von Solr


PostgreSQL-Datenverbindung
--------------------------

Eventuelle Anpassung der Datenverbindung in den Konfigurationsdateien unter data/solr_data/places/config:
* solrconfig.xml
* data-config.xml

* passenden PostgreSQL-Treiber downloaden: 
** https://jdbc.postgresql.org/download.html

.. code-block:: yaml
    cd /sites/solr_data/places/
    wget https://jdbc.postgresql.org/download/postgresql-9.1-903.jdbc4.jar


Solr-Schema
-----------

Ein Solr-Schema besteht aus des folgenden Teilen:
* **Feldern** (field)
* **Feldtypen** (fieldType)
* **Angabe eines ID-Feldes** per uniqueKey 




Jetty absichern
---------------

Freigabe bestimmter IP Adressen für den Zugriff in der Jetti-Konfiguration unter solr/etc/jetty.xml

.. code-block:: yaml
    <Set name="host"><SystemProperty name="jetty.host" /></Set>
    <Set name="port"><SystemProperty name="jetty.port" default="8983"/></Set>

