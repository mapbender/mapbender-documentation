.. _bundle:

How to create a Bundle?
#######################

Yo can read developer contribution guide about what is a module an how to create new bundle:
https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md#bundle-creation


How to activate a Bundle?
*************************
The Bundle will be activated in the file **app/AppKernel.php**. You have to add the Bundle to the array $bundles:

.. code-block:: php

 $bundles = array(
  //...
  new Mapbender\CoreBundle\MapbenderCoreBundle(),
  new Mapbender\WmsBundle\MapbenderWmsBundle(),

  new Vendor\VendorHelloBundle()
 );


How to activate the Routings?
*****************************
The routing is a mapping of URLs (for example / or /application) to the call of a Controller from a Bundle. To do so you have to edit the file app/config/routing.yml. At the moment Mapbender3 uses the following way:

app/config/routing.yml:

.. code-block:: yaml

 _welcome:
    resource: "@MapbenderCoreBundle/Controller/WelcomeController.php"
    type: annotation


This means: Parse the mentioned file and look for Route-Annotations, which refer to funtcions.

.. code-block:: php

 <?php
 namespace Mapbender\CoreBundle\Controller;
 
 use Symfony\Bundle\FrameworkBundle\Controller\Controller;
 // annotations are imported to Symfony like classes. This is why you have to use the following call:
 use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
 use Sensio\Bundle\FrameworkExtraBundle\Configuration\Template;
 
 /**
  * Welcome controller.
  *
  * @author Christian Wygoda <arsgeografica@gmail.com>
  */
 class WelcomeController extends Controller {
	/**
	 * @Route("/", name="mapbender_welcome")
	 * @Template()
	 */
    public function indexAction() {
        //TODO: Get ORM Applications, too
        $apps = $this->getYamlApplications();
        return array(
            'apps' => $apps
        );
    }
 // ...


How to activate a new Element for the administration interface
***************************************************************
When you wrote a new functionality for Mapbender3 your new element will not show up in the administration.

You have to register it first in 

* mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php

.. code-block:: yaml

    public function getElements()
    {
        return array(
            'Mapbender\CoreBundle\Element\AboutDialog',
            'Mapbender\CoreBundle\Element\ActivityIndicator',
            'Mapbender\CoreBundle\Element\Button',
            ...
   
            'Workshop\DemoBundle\Element\SuperElement' 
            );
    }



Now your element should show up in the element list.




