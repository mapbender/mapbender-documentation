.. _mapcoordinate:

Karte zentrieren 
******************

Über das Element *Karte zentrieren* lässt sich ein gewünschter Kartenausschnitt mithilfe des zugehörigen eingegebenen Koordinatenpunkts zentrieren. Zusätzlich ist eine dynamische Koordinatentransformation mit dem Werkzeug möglich, sodass auch Punkte anderer Koordinatensysteme eingegeben werden können.   

Zusätzlich besteht bei dem Element die Möglichkeit, die Koordinaten in die Zwischenablage zu kopieren.

Das Element wird im Mapbender-Backend über einen Button als Dialog oder direkt in der Seitenleiste als Element eingebunden. 



.. image:: ../../../../../figures/mapcoordinate_kartezentrieren.png
     :scale: 80


Konfiguration
=============

**Element Karte zentrieren**


.. image:: ../../../../../figures/mapcoordinate_configuration_kartezentrieren.png
     :scale: 80



* **Title**: Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Target**: ID des Kartenelements, auf das sich das Element bezieht.
* **Type**: Anzeige als Dialog- oder Blockelement.



YAML-Definition:
================

.. code-block:: yaml

   title: 'Karte zentrieren'            # Titel, wie Karte zentrieren
   type: 'element'                      # Auswahl Positionierung des Elements ( Sidepane(element) oder Popup(dialog))
   target: ~                            # ID/Name des Elements Karte (map)


Für dieses Element wird ein Button benötigt. Siehe unter `Button <../elements/button.html>`_ für die Konfiguration. 
Die Funktion *Karte zentrieren* kann auch als Element definiert werden. Dann wird die Ein-/Ausgabe von Koordinaten über einem frame wie der Sidebar angezeigt.


Class, Widget & Style
===========================

Element *Karte zentrieren*

* Class: Mapbender\MapToolBundle\Element\SearchCoordinate
* Widget: mapbender.mbSearchCoordinate
* Style: mapbender.element.searchcoordinate.scss



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
