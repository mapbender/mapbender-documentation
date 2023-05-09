.. _element_generate:

How to create your own Element?
###############################

.. note:: This guide is under complete restructuring. We will provide a new documentation in the Contributing Guite in our Git-Repository:

`https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md>`_.


Mapbender offers an app/console command to create different elements:

* general elements
* buttons
* elements for map-click events
* elements for map-box events

.. hint:: The new generated element contains only a skeleton and has to be modified after generation.

The following example show the generation and modification of a map-click element.


The steps to create your own Element?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some steps you have to follow on the way to your own element.

* create your own bundle
* create an element via app/console
* edit your new element for your needs
* add the new element to the function *getElements()* to make it available from the backend


Use app/console to generate your own bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find out more about the command with help:

.. code-block:: bash

 app/console generate:bundle --help

.. code-block:: bash

 app/console generate:bundle --namespace=Workshop/DemoBundle --dir=src 


You have to answer some questions before the element will be created:

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
 
After this steps you new bundle is available at src. The bundle is already registered in the File AppKernel.php. In the file routing.yml you will find a new entry for the bundle.


Use app/console to generate a new element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find out more about the command with help:

.. code-block:: bash

 app/console mapbender:generate:element --help


Generate a new element with the following command:

.. code-block:: bash

 app/console mapbender:generate:element --type "map-click" "Workshop\DemoBundle" MapKlick src


You will get a summary of actions
 
.. code-block:: bash

 Summary of actions
 - Your element WorkshopDemoBundle\Element\MapKlick has been created.
 - The following files have been created:
  - PHP class (src/Workshop/DemoBundle/Element/MapKlick.php)
  - jQuery widget (src/Workshop/DemoBundle/Resources/public/mapbender.element.mapklick.js)


Edit your new element for your needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change the title and description in the php file
************************************************

You will find several functions in the php file. Change the return value of the functions *getClassTitle()* and *getClassDescription()*.

.. code-block:: php

    public static function getClassTitle() {
        return "MapKlick";
    }


.. code-block:: php

    public static function getClassDescription() {
        return "Generates an Url with the the mapklick coordinates added";
    }


Register the new Element
~~~~~~~~~~~~~~~~~~~~~~~~

You can register an element by adding it to the function *getElements()* in the file src/Workshop/DemoBundle/WorkshopDemoBundle.php. After creation of the bundle this function does not exist. You also have to refer to the MapbenderBundle and define that your  extends the MapbenderBundle.

This will make the element available in the backend when you configure your application.

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


Add the new element to an application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new application and add your element to the new application.
Note that the configuration for your generated element is done in YAML syntax. If you want to use the map-element as target you have to find out the id of the map-element (e.g. via inspector tool).


Change the action on Click event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you generated a map-click element you get an event on click and an action. The action can be modified. Have a look in the JQuery widget file (mapbender/src/Workshop/DemoBundle/Resources/public/mapbender.element.mapklick.js). 

You will find the function *_mapClickHandler()* that determines the coordinates from the click event and passes them to the function *_mapClickWorker()*. The new generated element will show the coordinates of the click event in an alert box.

You can modify the action of the function *_mapClickWorker()*.


Default definition of _mapClickWorker()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: js

 _mapClickWorker: function(coordinates) {
        alert('You clicked: ' +
                coordinates.pixel.x + ' x ' + coordinates.pixel.y +
                ' (Pixel), which equals ' +
                coordinates.world.x + ' x ' + coordinates.world.y +
                ' (World).');
    }


modified _mapClickWorker() opens OpenStreetMap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alternatively you could open a new window with an URL and add the coordinates as parameters. You can open OpenStreetMap and center to the coordinates of the click event.

https://www.openstreetmap.org/export#map=15/50.7311/7.0985

.. code-block:: js
  
 _mapClickWorker: function(coordinates) {
        window.open('https://www.openstreetmap.org/export#map=15/' + coordinates.world.y + '/' + coordinates.world.x);
    }

