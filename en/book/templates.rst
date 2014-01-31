.. _templates:

How to create your own Template?
################################

Mapbender3 comes with application templates you can use. But usually you want to use your own template with your own corporate design. 
This document will show you how to create a Workshop DemoBundle for demonstration purposes.

How to create your own template?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 4 steps you have to follow on the way to your own template.

* create your own bundle
* create a template php-file to register your template
* create your own twig-file
* create your own css-files
* register your bundle in app/AppKernel.php
* use your template in yml-configuration or choose it through the administration

Notice: We already prepared a Workshop/DemoBundle that you can use as a template. You can download it here:

* Workshop/DemoBundle at https://github.com/mapbender/mapbender-workshop 


Create your own bundle
~~~~~~~~~~~~~~~~~~~~~~~~~

User bundles are stored in the src-directory. 

This is how the structure can look like:

.. code-block:: bash

 src/Workshop/DemoBundle
                        /Resources
                                  /public
                                         demo_fullscreen.css
                                         demo_theme.css   
                                         /imgage
                                             workshop.ico
                                             workshop_logo.png
                                             print.png
                                             ...
                                  /views
					/Template								
                                             fullscreen_demo.html.twig
                        /Template
		                DemoFullscreen.php


Create a new namespace 
**************************

The file WorkshopDemoBundle.php creates the namespace for the bundle and refers to the template.

.. code-block:: bash

 <?php

 namespace Workshop\DemoBundle;

 use Mapbender\CoreBundle\Component\MapbenderBundle;

 class DemoFullscreen extends MapbenderBundle
 {
    ...
 }

 public static function getTitle()
 {
   return 'DemoFullscreen';
 }

 ...
 ->render('WorkshopDemoBundle:Template:demo_fullscreen.html.twig',




Create your own template file
*************************************************

In our example the template file is called FullscreenDemo.php. You find it at src/Workshop/DemoBundle/Template/FullscreenDemo.php.

In the template file you define the name of your template, the regions that you want to provide and refer to a twig file.


Create your own twig-file
~~~~~~~~~~~~~~~~~~~~~~~~~

You find the twig-files at the following path:

* mapbender\\src\\Workshop\\DemoBundle\\Resources\\views\\Template

The easiest way to create your own twig file is to copy an existing twig, save it under a new name and change the content like colors.

.. code-block:: bash

 cd mapbender/src/Workshop/DemoBundle/Resources/views/Template 
 use an existing template and copy it to fullscreen_demo.html.twig


Create your own css-file
~~~~~~~~~~~~~~~~~~~~~~~~~

The css-files are located in application/mapbender/src/Mapbender/CoreBundle/Resources/public/css. Create your own css file and edit the content.

.. code-block:: bash

 cd fom/src/FOM/CoreBundle/Resources/public/css/frontend

 # css for frame (container position)
 copy the file fullscreen.css to  src/Workshop/DemoBundle/Resources/public/demo_fullscreen.css

 # css for colors, fonts, icons
 copy the file mapbender3_theme.css to src/Workshop/DemoBundle/Resources/public/demo_theme.css


Register your template
~~~~~~~~~~~~~~~~~~~~~~

To register your template you have to create a file at 

* mapbender/src/Workshop/DemoBundle/Template/DemoFullscreen.php 

.. code-block:: bash

 cd mapbender/src/Mapbender/CoreBundle/Template
 cp Fullscreen.php mapbender/src/Workshop/DemoBundle/Template/DemoFullscreen.php


Add the fully qualified Template class name to your Bundles setup class getTemplates function:

.. code-block:: php

    public function getAssets($type)
    {
        parent::getAssets($type);
        $assets = array(
            'css' => array('@WorkshopDemoBundle/Resources/public/css/demo_theme_demo.css,@WorkshopDemo/Resources/public/css/demo_fullscreen.css'),
            'js' => array(),
        );

        return $assets[$type];
    }


.. code-block:: php

    public function render($format = 'html', $html = true, $css = true,
            $js = true)
    {
        $templating = $this->container->get('templating');
        return $templating
                        ->render('WorkshopDemoBundle:Template:demo_fullscreen.html.twig',
                                 array(
                            'html' => $html,
                            'css' => $css,
                            'js' => $js,
                            'application' => $this->application));
    }

Edit your twig-file and refer to the new css-files

.. code-block:: yaml

  <link rel="stylesheet" href="{{ asset('bundles/workshopdemo/css/demo_theme.css') }}">
  <link rel="stylesheet" href="{{ asset('bundles/workshopdemo/css/demo_fullscreen.css') }}">


Use your new template in mapbender.yml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can use the template in mapbender.yml where you can configure applications.

You find the mapbender.yml at:

* app/config

.. code-block:: yaml
  
  "template:   Workshop\DemoBundle\Template\DemoFullscreen"


Register your bundle in app/AppKernel.php
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When you create a new application through the Mapbender3 administration you have to choose a template you want to use. 

Before your new template will show up you have to register your bundle in the file app/AppKernel.php

* mapbender/app/AppKernel.php

.. code-block:: yaml

 class AppKernel extends Kernel
 {
    public function registerBundles()
    {
        $bundles = array(
            // Standard Symfony2 bundles
            new Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
            ....

            // Extra bundles required by Mapbender3/OWSProxy3
            new FOS\JsRoutingBundle\FOSJsRoutingBundle(),

            // FoM bundles
            new FOM\CoreBundle\FOMCoreBundle(),
            ...
    
            // Mapbender3 bundles
            new Mapbender\CoreBundle\MapbenderCoreBundle(),
            ...

	    new Workshop\DemoBundle\WorkshopDemoBundle(),

        );

Update the web-directory. Each bundle has it's own assets - CSS files, JavaScript files, images and more -
but these need to be copied into the public web folder:

.. code-block:: yaml

    app/console assets:install web


Alternatively, as a developer, you might want to use the symlink switch on that command to
symlink instead of copy. This will make editing assets inside the bundle
directories way easier.

.. code-block:: yaml

   app/console assets:install web --symlink --relative


Now your template should show up in the list.


How to change your design?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have to edit the following files, if want to change the design

* twig - changes in the structure (like - delete a component like sidebar), refer to a logo
* demo_theme.css - changes in the structure - position and size of content or footer
* demo_fullscreen.css - changes of color, icons, fonts

Notice: 
In demo_fullscreen.css the beginning of the file is concerned for browser specific css. Do not edit this part. The part you can edit starts at row 430.


How to change the logo?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The logo (default is the Mapbender3 logo) can be changed in the parameters.yml. Which causes a global change. 

.. code-block:: yaml

 server_logo:   bundles/workshopdemo/image/workshop_logo.png


Or in the twig file:

.. code-block:: yaml

 <img class="logo" height="40" alt="Workshop Logo" src="{{ asset('bundles/workshopdemo/imgage/workshop_logo.png')}}" />	


How to change the title and favicon?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml


 {% block title %}Workshop - {{ application.title }}{% endblock %}

 {% block favicon %}{{ asset('bundles/workshopdemo/imgage/workshop.ico') }}{% endblock %}



How to change the buttons?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mapbender3 uses Fonts from the FontAwesome collection have a look at your demo_theme.css (or mapbender3_theme.css)

.. code-block:: yaml

 @font-face {
   font-family: 'FontAwesome';
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?v=3.0.1");
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?#iefix&v=3.0.1") format("embedded-opentype"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.woff?v=3.0.1") format("woff"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.ttf?v=3.0.1") format("truetype");
   font-weight: normal;
   font-style: normal; }


In the file demo_theme.css the font images are refered like this:

.. code-block:: yaml

  .iconPrint:before {
    content: "\f02f";

If you want to use an image you could place the image in your bundle and refer to it like this

.. code-block:: yaml

  .iconPrint:before {
   content:url("imgage/print.png");}


Try this out
~~~~~~~~~~~~
* you can download the Workshop/DemoBundle at https://github.com/mapbender/mapbender-workshop 
* change the color of your icons
* change the size of your icons
* change the color of the toobar
* use an image instead of a font-icon for your button
* move the position of your overview to the left

* Have a look at the workshop files to see how it works

