.. _element_generate:

How to create your own Element?
################################
Mapbender3 offers app/console commands to create different elements. You can generate general elements, buttons, elements for map-click or map-box. The new generated element contains only a skeleton and has to be modivied after generation.


How to create your own Element?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some steps you have to follow on the way to your own element.

* create your own bundle
* create an element via app/console
* edit your new element for your needs
* add the new element to the file /mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php to make it available from the backend


Use app/console to generate a new Element?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find out more about the command with --help:

.. code-block:: bash

 app/console mapbender:generate:element --help


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

You can register an element by adding it to the function getElements() in the file /mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php 
This will make it available from the backend.

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
Note that the configuration for your generated element is done in yml syntax.


Change the action on Click event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can modify the action that is done in the JQuery widget file (mapbender/src/Mapbender/CoreBundle/Resources/public/mapbender.element.mapklick.js)

You find a _mapClickHandler that is getting the mapklick coordinates and passes the coordinates to the function _mapClickWorker

.. code-block:: bash

 _mapClickWorker: function(coordinates) {
        alert('You clicked: ' +
                coordinates.pixel.x + ' x ' + coordinates.pixel.y +
                ' (Pixel), which equals ' +
                coordinates.world.x + ' x ' + coordinates.world.y +
                ' (World).');
    }

Alternatively you could open a new window with an URL and add the coordinates as parameters. You could open OpenStreetMap and zoom to the coordinates.

http://www.openstreetmap.org/export#map=15/50.7311/7.0985

.. code-block:: bash

  
 _mapClickWorker: function(coordinates) {
        window.open('http://www.openstreetmap.org/export#map=15/' + coordinates.world.y + '/' + coordinates.world.x);
    }
