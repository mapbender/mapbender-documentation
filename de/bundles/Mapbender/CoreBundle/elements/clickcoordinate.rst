.. _clickcoordinate:

Klick-Koordinate 
******************

Das Element *Klick-Koordinate* ermöglicht die Ausgabe von einer oder mehreren Koordinatenpunkten. Dazu werden die Koordinaten des Punktes automatisch in das Feld des Werkzeugs eingetragen, nachdem dieser über einen Mausklick an der gewünschten Stelle der Karte gewählt wurde. Dabei können die aufgenommenen Koordinaten direkt in das gewünschte System transformiert werden. Das jeweilige System wird im Fenster ausgewählt und kann mit den entsprechenden Zugriffsrechten im Mapbender-Backend angepasst werden.

Zusätzlich besteht bei dem Element die Möglichkeit, die Koordinaten in die Zwischenablage zu kopieren. Diese Funktionalität ist über das Kopier-Symbol rechts der angezeigten Koordinaten zu erreichen.

Die Klick-Koordinate kann im Backend über einen Button als Dialog oder direkt in der Seitenleiste als Element eingebunden werden.  


.. image:: ../../../../../figures/mapcoordinate_klickkoordinate.png
     :scale: 80     


Das Element ermöglicht die Aufnahme von mehreren Koordinatenpunkten. Durch das gedrückt halten von "Strg" können mehrere Koordinatenpunkte übernommen werden, die auch in der Karte angezeigt werden. Diese werden dann kommasepariert aufgelistet, z.B. 365205.40 5621464.56,365772.41 5621758.56.  


Konfiguration
=============


**Element Klick-Koordinate**


.. image:: ../../../../../figures/mapcoordinate_configuration_klickkoordinate.png
     :scale: 80



* **Title**: Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Target**: ID des Kartenelements, auf das sich das Element bezieht.
* **Type**: Anzeige als Dialog- oder Blockelement.
* **Srs list**: Eingabe von weiteren EPSG Codes, die nicht im Map-Element aufgelistet sind, für die Transformation der Koordinaten. Muster für Eingabe: EPSG:25832,EPSG:25833
* **Map's Srs hinzufügen**: EPSG-Codes, die im Kartenelement definiert wurden, werden in der Liste für die Transformation angezeigt.  
* **Koordinatenausgabe aufklappbar**:  Falls aktiv, erscheint oben rechts ein Button zum Einklappen des oberen Menüs *Koordinatensystem der Ausgabe von Koordinaten* für die Transformation.


.. image:: ../../../../../figures/mapcoordinate_klickkoordinate_aufklappbar.png
     :scale: 80


* **Koordinatenausgabe geöffnet**:  Falls aktiv, ist die Koordinatenausgabe beim Start des Elements geöffnet.



YAML-Definition:
================

.. code-block:: yaml

   title: 'Klick-Koordinate'            # Titel, wie Klick-Koordinate
   type: 'element'                      # Auswahl Positionierung des Elements ( Sidepane(element) oder Popup(dialog))
   target: ~                            # ID/Name des Elements Karte (map)


Für dieses Element wird ein Button benötigt. Siehe unter `Button <../elements/button.html>`_ für die Konfiguration. 
Die Klick-Koordinate kann auch als Element definiert werden. Dann wird die Ein-/Ausgabe von Koordinaten über einem frame wie der Sidebar angezeigt.


Class, Widget & Style
===========================

Element *Klick-Koordinate*

* Class: Mapbender\MapToolBundle\Element\ClickCoordinate
* Widget: mapbender.mbClickCoordinate
* Style: mapbender.element.mapclickcoordinate.scss


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
