.. _search_digitizer:

Suche über Element Digitalisierung (Digitizer)
**********************************************
Das Digitizer-Element ermöglicht den Aufbau von Erfassungsoberflächen und enthält eine Einfeldsuche auf der Trefferliste.
In Zusammenhang mit der Digitalisierung können für die Erfassung von dazugehörigen Sachdaten sehr komplexe Formulare und eine komplexe Suche auf der Tabelle generiert werden. Mehr zu dem Element findet sich unter `Digitizer <digitizer.html>`_ .


Erweiterte Suche in Tabellen (search)
=====================================

Im Folgenden werden die einzelnen Bestandteile für die Suche über den Digitizer erklärt, die die Grundstruktur ausmachen und die in dem Formular eingebettet werden können.
<br>

Die erweiterte Suche (Parameter search) auf der Datenbanktabelle ist zusätzlich zu der simplen Suche (Parameter inlineSearch) in der Trefferliste möglich. <br>
Für eine komplexere Suche können weitere Parameter angegeben werden, die das Finden bestimmter Fachinformationen in der Tabelle erleichtern. <br>
Vorteil dieser Suche ist vor Allem, dass das Koordinatensystem während der Suche geändert werden kann. Dies ist nicht bei dem `SearchRouter <search_router.html>`_ möglich. 


.. image:: ../../../../../figures/digi_search.png
     :scale: 50 %


YAML-Definition für die Suche im Element digitizer in der Textarea unter schemes
--------------------------------------------------------------------------------

.. code-block:: yaml

  poi:
      ...
      inlineSearch: false                         # Deaktivieren der simplen Suche auf der Trefferliste
      search:
        mandatory:                  # Pflichtangabe bei der Abfrage (reguläre Ausdrücke erlaubt)
            name: .+
            type: .+      
        form:
          - type: select
            title: Type
            name: type
            value: A
            connection: search_db
                sql: |
                    SELECT
                    DISTINCT type
                    FROM public.poi
                    ORDER by type ASC
          - type: select
            name: name
            title: 'Name(n)'
            placeholder: Punktname
            multiple: true
            minimumInputLength: 1
            formatSearching: 'Der Name wird gesucht...'
            ajax: 
                delay: 100
                connection: search_db
                sql: |
                    SELECT  "name"
                    FROM    "poi"
                    WHERE   "name" LIKE '$name'
                    AND (
                        LOWER ("name") LIKE LOWER ('$name%')
                        OR LOWER ("name") LIKE LOWER ('%%$name%')
                        )
                    GROUP BY "name"
                    ORDER BY LOWER ("name") LIKE LOWER ('$name%') DESC
                    LIMIT 10
        conditions:
          - type: sql
            operator: and
            code:  |
               "type" like '$type'
          - type: sql-array
            key: name
            code:  |
               "name" LIKE '$value%' OR "name" LIKE '%%$value%'
            operator: OR
      ...

* **mandatory:** Pflichtangabe können bei der Abfrage definiert werden. Bei dem Beispiel muss z.B. erst eine Angabe der Ortsnamen und Straßennamen erfüllt sein, bevor ein Treffer in der Liste angezeigt wird. Möglich sind hier reguläre Ausdrücke, wie .+ (beide Abfragen müssen mind. eine Angabe haben, die mind. 1 oder mehr Zeichen enthält). 
* **multiple:** Auswahl mehrerer Suchbegriffe erlauben, z.B. mehrere Straßen [true/false]


.. image:: ../../../../../figures/digi_search_multiple.png
     :scale: 80

.. [funktioniert noch nicht]* **maximumSelectionSize**: Maximale Angabe von Suchbegriffen [numeric] bei der Angabe von multiple: true.
* **minimumInputLength:** Minimale Anzahl an Zeichen für den Start der Suchanfrage. [numeric]
* **delay:** Wartezeitraum, bis die Suchanfrage abgeschickt wird (in Milisekunden), erleichtert Suche bei langsamen Tippen. [true/false]
* **sql:** Angabe einer SQL-Abfrage für die Suchfelder. Eine saubere und durchdachte SQL-Abfrage bewirkt die Ausgabe der Treffer in einer sinvollen Reihenfolge, z.B. erst Treffer, die den Suchbegriff an erster Stelle haben und nicht mitten im Treffer. Nutzung von **name** im SQL möglich.
* **name:** Variable, die in der SQL-Abfrage genutzt werden kann, z.B. $post_ortsname. Dadurch ist die SQL-Abfrage gegen Angriffe von Außen besser abgesichert.
* **value:** Vorgabewert aus den Werten in der Spalte, der bei keiner aktiven Angabe eines Wertes für die Suche genutzt wird.
* **formatSearching:** Platzhalter während die Suche läuft

Suchbedingungen (conditions)
----------------------------

Bedingungen (conditions) für Abfragen können fest vergeben werden. 
* **type:** Abfragetyp für die Bedingung [sql, php]
* **operator:** SQL-Verbindungstyp von Abfragen [AND, OR]
* **code: ** Angabe von Code, der erfüllt werden muss bei einer Abfrage zu dem angegebenen Schlüsselwert (key)
* **key:** Schlüsselwert für die Abfrage, der im Codebereich referenziert wird

.. image:: ../../../../../figures/digi_search_select.png
     :scale: 80

.. code-block:: yaml

  poi:
      ...
      inlineSearch: false
      search:
        ...
        conditions:
          - type: sql
            operator: and
            code:  |
               "type" like '$type'
          - type: sql-array
            key: name
            code:  |
               "name" LIKE '$value%' OR "name" LIKE '%%$value%'
            operator: OR
      ...



YAML-Definition für das Element "digitizer" in der Sidepane in der mapbender.yml
================================================================================

Dieser Codeabschnitt zeigt, wie das Digitizer Element in eine auf einer
YAML-Datei basierende Anwendung eingebaut werden kann.

.. code-block:: yaml

                sidepane:
                    digitizer:
                        class: Mapbender\DigitizerBundle\Element\Digitizer
                        title: Digitalisation
                        target: map
                        schemes:
                            ...


Class, Widget & Style
=====================

* Class: Mapbender\\DigitizerBundle\\Element\\Digitizer
* Widget: mapbender.element.digitizer.js
* Style: sass\\element\\digitizer.scss

