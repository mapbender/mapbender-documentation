.. _element_generate:

How to create your own Element?
################################
Mapbender3 offers an app/console command to create different elements. You can generate general elements, buttons, elements for map-click or map-box events. 

*Please note:* The new generated element contains only a skeleton and has to be modivied after generation.

The following example show the generation and modification of a map-click element.


The steps to create your own Element?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some steps you have to follow on the way to your own element.

* create your own bundle
* create an element via app/console
* edit your new element for your needs
* add the new element to the function *getElements()* to make it available from the backend


Use app/console to generate a new Element?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find out more about the command with --help:

.. code-block:: bash

 app/console mapbender:generate:element --help


Generate a new element with the following command:

.. code-block:: bash

 app/console mapbender:generate:element --type "map-click" "Mapbender\CoreBundle" MapKlick mapbender/src


You will get a summary of actions
 
.. code-block:: bash

 - Your element MapbenderCoreBundle\Element\MapKlick has been created.
 - The following files have been created:
  - PHP class (mapbender/src/Mapbender/CoreBundle/Element/MapKlick.php)
  - jQuery widget (mapbender/src/Mapbender/CoreBundle/Resources/public/mapbender.element.mapklick.js)


Edit your new element for your needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change the title and description in the php file
******************************************************

You will find several functions in the php file. Change the return value of the functions *getClassTitle()* and *getClassDescription()*.

.. code-block:: bash

    public static function getClassTitle() {
        return "MapKlick";
    }


.. code-block:: bash

    public static function getClassDescription() {
        return "Generates an Url with the the mapklick coordinates added";
    }


Register the new Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can register an element by adding it to the function *getElements()* in the file /mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php 

This will make the element available in the backend when you configure your application.

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


Add the new element to an application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new application and add your element to the new application.
Note that the configuration for your generated element is done in YAML syntax. If you want to use the map-element as target you have to find out the id of the map-element (f.e. via firebug inspect).


Change the action on Click event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you generated a map-click element you get an event on click and an action. The action can be modified. Have a look in the JQuery widget file (mapbender/src/Mapbender/CoreBundle/Resources/public/mapbender.element.mapklick.js). 

You will find the function *_mapClickHandler()* that determines the coordinates from the click event and passes them to the function *_mapClickWorker()*. The new generated element will show the coordinates of the click event in an alert box.

You can modify the action of the function *_mapClickWorker()*.

Default definition of *_mapClickWorker()*
------------------------------------------

.. code-block:: bash

 _mapClickWorker: function(coordinates) {
        alert('You clicked: ' +
                coordinates.pixel.x + ' x ' + coordinates.pixel.y +
                ' (Pixel), which equals ' +
                coordinates.world.x + ' x ' + coordinates.world.y +
                ' (World).');
    }


modified *_mapClickWorker()* opens OpenStreetMap
------------------------------------------------
Alternatively you could open a new window with an URL and add the coordinates as parameters. You can open OpenStreetMap and center to the coordinates of the click event.

http://www.openstreetmap.org/export#map=15/50.7311/7.0985

.. code-block:: bash
  
 _mapClickWorker: function(coordinates) {
        window.open('http://www.openstreetmap.org/export#map=15/' + coordinates.world.y + '/' + coordinates.world.x);
    }

