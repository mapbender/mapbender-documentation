.. _element_generate:

Wie können eigene Elemente erzeugt werden?
#################################################

Mapbender3 bietet einen app/console-Befehl zur Erzeugung von Elementen. Hierbei können vier verschiedene Typen von Elementen generiert werden. Es können einfache Elemente (general), Schaltflächen (buttons), Elemente, die auf einen Kartenklick (map-click) oder das Aufziehen eines Rechtecks (map-box) reagieren, erzeugt werden. 

*Achtung:* Die generierten Elemente enthalten lediglich ein Basisgerüst und müssen anschließend noch angepasst werden.

Im Folgenden soll am Beispiel eines map-klick-Elementes das Erzeugen und die Anpassung eines Elementes gezeigt werden.


Die Arbeitsschritte - wie werden eigene Elemente erzeugt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Arbeitsschritte auf dem Weg zum eigenen Element.

* Erzeugen Sie ein eigenes Bundle
* Erzeugen Sie ein Element mit Hilfe von app/console
* Passen Sie das Element an Ihre Bedürfnisse an
* Fügen Sie das Element in die Funktion +getElements()* ein, um es über das Backend verfügbar zu machen


Eigene Elemente über app/console generieren?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Hilfe zum Befehl erhalten Sie über die Option --help:

.. code-block:: bash

 app/console mapbender:generate:element --help


Erzeugen Sie ein Element über den folgende Befehl:

.. code-block:: bash

 app/console mapbender:generate:element --type "map-click" "Mapbender\CoreBundle" MapKlick mapbender/src


Es wird eine Übersicht über die erfolgte Aktion ausgegeben. Es wurde eine PHP-Datei und eine js-Datei erzeugt.

.. code-block:: bash

 - Your element MapbenderCoreBundle\Element\MapKlick has been created.
 - The following files have been created:
  - PHP class (mapbender/src/Mapbender/CoreBundle/Element/MapKlick.php)
  - jQuery widget (mapbender/src/Mapbender/CoreBundle/Resources/public/mapbender.element.mapklick.js)


Anpassung des eigenen Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anpassung des Titels und der Beschreibung
******************************************************

In der PHP-Datei finden Sie zahlreiche Funktionen. Ändern Sie den return-Wert der Funktionen *getClassTitle()* und *getClassDescription()*.

.. code-block:: bash

    public static function getClassTitle() {
        return "MapKlick";
    }


.. code-block:: bash

    public static function getClassDescription() {
        return "Generates an Url with the the mapklick coordinates added";
    }


Registrierung des neuen Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein Element kann registriert werden, indem es in der Funktion *getElements()* in der Datei /mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php aufgeführt wird. 

Hierdurch kann das Element im Backend bei der Anwendungskonfiguration ausgewählt werden.

.. code-block:: bash

    public function getElements()
    {
        return array(
            'Mapbender\CoreBundle\Element\AboutDialog',
            'Mapbender\CoreBundle\Element\ActivityIndicator',
            'Mapbender\CoreBundle\Element\BaseSourceSwitcher',
            'Mapbender\CoreBundle\Element\Button',
            ....
            'Mapbender\CoreBundle\Element\MapKlick'
        );
    }


Element zu einer Anwendung hinzufügen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Erstellen Sie eine Anwendung und fügen Sie das neue Element zu der Anwendung hinzu. Sie finden das Element unter dem Element-Titel in der Liste der Elemente. Beachten Sie, dass die anschließende Konfiguration des Elementes im YAML-Syntax erfolgt. Wenn Sie das Karten-Element (map) als *target* verwenden möchten, müssen Sie die id des Kartenelements ermitteln. Dies kann beispielsweise über Firebug erfolgen.


Ändern der Aktion des Klick-Ereignisses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn Sie ein map-click-Element erzeugen reagiert dieses auf das Klick-Ereignis mit einer Aktion. Diese Aktion kann modifiziert werden. Schauen Sie sich dazu die JQuery widget Datei an (mapbender/src/Mapbender/CoreBundle/Resources/public/mapbender.element.mapklick.js). 

Hier finden Sie die Funktion *_mapClickHandler()*, die die Koordinaten des Klick-Ereignisses ermittelt und an die Funktion *_mapClickWorker()* weitergibt. Standarmäßig gibt das neu generierte Element die Pixelposition und Koordinate des Klicks in einem Dialog aus.

Sie können die Aktion der Funktion  *_mapClickWorker()* anpassen.

Standarddefinition der Funktion *_mapClickWorker*
------------------------------------------------------

.. code-block:: bash

 _mapClickWorker: function(coordinates) {
        alert('You clicked: ' +
                coordinates.pixel.x + ' x ' + coordinates.pixel.y +
                ' (Pixel), which equals ' +
                coordinates.world.x + ' x ' + coordinates.world.y +
                ' (World).');
    }


Angepassung der Funktion *_mapClickWorker()* zum Aufruf einer URL
----------------------------------------------------------------------------------

Alternativ kann beispielsweise ein neues Fenster mit einer URL geöffnet und die Koordinaten als Parameter übergeben werden. So können Sie beispielsweise OpenStreetMap aufrufen und die Koordinate des Klickereignisses zentrieren.

http://www.openstreetmap.org/export#map=15/50.7311/7.0985

.. code-block:: bash
  
 _mapClickWorker: function(coordinates) {
        window.open('http://www.openstreetmap.org/export#map=15/' + coordinates.world.y + '/' + coordinates.world.x);
    }

