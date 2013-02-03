How to create a Bundle?
#######################

A Bundle is created by the command

   :command:`app/console init:bundle '<Namespace>' <directory normally below src>`

Example:
    :command:`app/console init:bundle 'Vendor' HelloBundle`

A new directory was created at:
    mapbender3/application/src/Vendor/HelloBundle


Autoloading
***********
When you activate a Bundle you have to tell the system, in which directory(s) the classes of the Bundles are stored. 

This is done by the **app/autoload.php**.

The function **registerNamespaces** the array is enlarged by the registered directories.

.. code-block:: javascript

 $loader->registerNamespaces(array(
    //...
     'Mapbender'        => __DIR__.'/../mapbender/src'
 ));

The row means that the system will look for the namespace **Mapbender** at first in the directory **Mapbender** below mapbender/src.

In this case the class Mapbender\\CoreBundle\\Component\\Element should be loaded. 

Also the namespace-component (devided by \) will be interpreted as a directory name and the closing classname (Element) will be interpreted as a file. So in this case **Element.php** will be expected.


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

