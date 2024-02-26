.. _element_generate_de:

Wie können eigene Elemente erzeugt werden?
##########################################

*Anmerkung*: Diese Anleitung wird gerade überarbeitet. Wir werden eine neue Dokumentation im Contributing Guide für Entwickler im Git-Repository bereitstellen:

`https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md <https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md>`_.


Mapbender bietet einen bin/console-Befehl zur Erzeugung von Elementen. 

Hierbei können vier verschiedene Typen von Elementen generiert werden:

* einfache Elemente (general)
* Schaltflächen (buttons)
* Elemente, die auf einen Kartenklick (map-click) reagieren
* Elemente, die auf das Aufziehen eines Rechtecks (map-box) reagieren 

*Achtung:* Die generierten Elemente enthalten lediglich ein Basisgerüst und müssen anschließend noch angepasst werden.

Im Folgenden soll am Beispiel eines map-klick-Elementes das Erzeugen und die Anpassung eines Elementes gezeigt werden.


Die Arbeitsschritte zum Erzeugen von eigenen Elementen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Arbeitsschritte auf dem Weg zum eigenen Element.

* Erzeugen Sie ein eigenes Bundle
* Erzeugen Sie ein Element mit Hilfe von bin/console
* Passen Sie das Element an Ihre Bedürfnisse an
* Fügen Sie das Element in die Funktion *getElements()* ein, um es über das :ref:`backend_de` verfügbar zu machen


Anlegen eines eigenen Bundles mit bin/console generate:bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Hilfe zum Befehl erhalten Sie über die Option help:

.. code-block:: bash

 bin/console generate:bundle --help

.. code-block:: bash

 bin/console generate:bundle --namespace=Workshop/DemoBundle --dir=src 


Für die Erstellung müssen noch einige Angaben gemacht werden:

.. code-block:: bash

 Bundle name [WorkshopDemoBundle]: WorkshopDemoBundle
 
 Determine the format to use for the generated configuration. 
 Configuration format (yml, xml, php, or annotation): annotation

 To help you get started faster, the command can generate some
 code snippets for you.

 Do you want to generate the whole directory structure [no]? yes
 
 Summary before generation  
 You are going to generate a "Workshop\DemoBundle\WorkshopDemoBundle" bundle
 in "src/" using the "annotation" format.
 
 Do you confirm generation [yes]? yes
 
 Confirm automatic update of your Kernel [yes]? yes
 
 Confirm automatic update of the Routing [yes]? yes
 
Nach diesen Schritten liegt das neue Bundle im Verzeichnis src vor. Außerdem wurde das Bundle in der Datei Kernel.php registriert. In der Datei routing.yaml wurde eine neue Route für das Bundle eingetragen.


Anpassung des eigenen Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anpassung des Titels und der Beschreibung
*****************************************

In der PHP-Datei finden Sie zahlreiche Funktionen. Ändern Sie den return-Wert der Funktionen *getClassTitle()* und *getClassDescription()*.

.. code-block:: php

    public static function getClassTitle() {
        return "MapKlick";
    }


.. code-block:: php

    public static function getClassDescription() {
        return "Generates an Url with the the mapklick coordinates added";
    }


Registrierung des neuen Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein Element kann registriert werden, indem es in der Funktion *getElements()* in der Datei src/Workshop/DemoBundle/WorkshopDemoBundle.php aufgeführt wird. Nach der Erstellung liegt diese Funktion vorerst nicht vor. Fügen Sie diese ein. Außerdem muss die Referenz zum MapbernderCoreBundle eingetragen werden (use Mapbender\\CoreBundle...). Sie müssen weiterhin angeben, dass die Klasse das MapbenderBundle erweitert.

Durch diesen Eintrag kann das Element im :ref:`backend_de` bei der Anwendungskonfiguration ausgewählt werden.

.. code-block:: html+php

 <?php
 
 namespace Workshop\DemoBundle; 
 
 use Symfony\Component\HttpKernel\Bundle\Bundle;
 use Mapbender\CoreBundle\Component\MapbenderBundle;
 
 class WorkshopDemoBundle extends MapbenderBundle
 {
     public function getElements()
     {
         return array(
             'Workshop\DemoBundle\Element\MapKlick'   
         );
     }
 }


Element zu einer Anwendung hinzufügen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Erstellen Sie eine Anwendung und fügen Sie das neue Element zu der Anwendung hinzu. Sie finden das Element unter dem Element-Titel in der Liste der Elemente. Beachten Sie, dass die anschließende Konfiguration des Elementes im YAML-Syntax erfolgt. Wenn Sie das Karten-Element (map) als *target* verwenden möchten, müssen Sie die ID des Kartenelements ermitteln. Dies kann beispielsweise über Firebug erfolgen.


Ändern der Aktion des Klick-Ereignisses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn Sie ein map-click-Element erzeugen, reagiert dieses auf das Klick-Ereignis mit einer Aktion. Diese Aktion kann modifiziert werden. Schauen Sie sich dazu die JQuery widget Datei an (mapbender/src/Workshop/DemoBundle/public/mapbender.element.mapklick.js). 

Hier finden Sie die Funktion *_mapClickHandler()*, die die Koordinaten des Klick-Ereignisses ermittelt und an die Funktion *_mapClickWorker()* weitergibt. Standarmäßig gibt das neu generierte Element die Pixelposition und Koordinate des Klicks in einem Dialog aus.

Sie können die Aktion der Funktion  *_mapClickWorker()* anpassen.


Standarddefinition der Funktion mapClickWorker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: js

 _mapClickWorker: function(coordinates) {
        alert('You clicked: ' +
                coordinates.pixel.x + ' x ' + coordinates.pixel.y +
                ' (Pixel), which equals ' +
                coordinates.world.x + ' x ' + coordinates.world.y +
                ' (World).');
    }


Angepassung der Funktion mapClickWorker() zum Aufruf einer URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternativ kann beispielsweise ein neues Fenster mit einer URL geöffnet und die Koordinaten als Parameter übergeben werden. So können Sie beispielsweise OpenStreetMap aufrufen und die Koordinate des Klickereignisses zentrieren.

https://www.openstreetmap.org/export#map=15/50.7311/7.0985

.. code-block:: js
  
 _mapClickWorker: function(coordinates) {
        window.open('http://www.openstreetmap.org/export#map=15/' + coordinates.world.y + '/' + coordinates.world.x);
    }
  src/Workshop/DemoBundle/WorkshopDemoBundle.php
