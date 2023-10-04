.. _templates:

How to create your own Template?
################################

Mapbender comes with application templates out of the box, you can find them in the Mapbender CoreBundle ``/application/mapbender/src/Mapbender/CoreBundle/Template``. But usually you want to use your own templates with your own corporate design.

To prevent overwriting your custom templates after an Mapbender upgrade you should create an extra bundle to safely store your custom files.

You can also change the style of your application with the built-in :ref:`CSS-Editor <css>`.


How to create your own template?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Steps for including your templates:**

* Create your own bundle
* Create a new namespace
* Create a template PHP-file to register your template
* Create your own Twig-file
* Create your own CSS-file(s)
* Register your bundle in src/Kernel.php
* Use your template

To help you we prepared a Workshop/DemoBundle, which can be used not only for application templates, but also for customizing the administration interface. For the following steps, you can download the files with the following links:

* https://github.com/mapbender/mapbender-workshop/tree/master



Create your own bundle
~~~~~~~~~~~~~~~~~~~~~~

User bundles are stored in the src-directory ``/application/src``.

This is how the structure can look like:


.. code-block:: bash

 src/Workshop/DemoBundle/
 
                         WorkshopDemoBundle.php
                    
                         /Resources
                                    /public
                                           demo_fullscreen.css
                                    
                                    /image
                                           workshop.ico
                                           workshop_logo.png
                                           print.png
   
                                    /views
					                      /Template
                                                   fullscreen_demo.html.twig
                         /Template
		                          DemoFullscreen.php
                                  

The following files have to be altered for design changes:

* twig-file: to change the structure (e.g. - delete a component like the sidebar)
* css-file:  to change colors, icons, fonts


Create a new namespace
~~~~~~~~~~~~~~~~~~~~~~

The file WorkshopDemoBundle.php creates the namespace for the bundle and refers to the template and to your css-files.


.. code-block:: php

    <?php

    namespace Workshop\DemoBundle;

    use Mapbender\CoreBundle\Component\MapbenderBundle;

    class WorkshopDemoBundle extends MapbenderBundle
    {
        public function getElements()
        {
            return array(
            //    'Workshop\DemoBundle\Element\MapKlick',
            );
        }
        public function getTemplates()
        {
            return array('Workshop\DemoBundle\Template\DemoFullscreen');
        }
    }
    
   

Create your own template file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our example the template file is called FullscreenDemo.php. You find it at ``src/Workshop/DemoBundle/Template/FullscreenDemo.php``.

In the template file you define the name of your template, the regions that you want to provide and refer to a twig file.


.. code-block:: php


    <?php

    namespace Workshop\DemoBundle\Template;

    use Mapbender\CoreBundle\Template\Fullscreen;

    class DemoFullscreen extends Fullscreen
    {
        protected static $title             = "Fullscreen Template Workshop";
        protected static $regions           = array('toolbar', 'sidepane', 'content', 'footer');
        protected static $regionsProperties = array(
            'sidepane' => array(
                'tabs'      => array(
                    'name'  => 'tabs',
                    'label' => 'mb.manager.template.region.tabs.label'),
                'accordion' => array(
                    'name'  => 'accordion',
                    'label' => 'mb.manager.template.region.accordion.label')
            )
        );
        protected static $css               = array(
            '@MapbenderCoreBundle/Resources/public/sass/template/fullscreen.scss',
            '@WorkshopDemoBundle/Resources/public/demo_fullscreen.scss',
        );
        protected static $js                = array(
            '@FOMCoreBundle/Resources/public/js/frontend/sidepane.js',
            '@FOMCoreBundle/Resources/public/js/frontend/tabcontainer.js',
            '@MapbenderCoreBundle/Resources/public/mapbender.container.info.js',
            '/components/jquerydialogextendjs/jquerydialogextendjs-built.js',
            "/components/vis-ui.js/vis-ui.js-built.js"
        );
        public $twigTemplate = 'WorkshopDemoBundle:Template:demo_fullscreen.html.twig';
    }
    
Create your own twig-file
~~~~~~~~~~~~~~~~~~~~~~~~~

You find the twig-files at the following path:

* ``application/mapbender/src/Mapbender/CoreBundle/Resources/views/Template``

The easiest way to create your own twig file is to copy an existing twig, save it under a new name and change the content like colors.

Use the existing template from ``mapbender/src/Mapbender/CoreBundle/Resources/views/Template/fullscreen.html.twig`` and copy it to ``fullscreen_demo.html.twig``.


Create your own css-file
~~~~~~~~~~~~~~~~~~~~~~~~

Create an empty css-file and fill it with content. You only have to define the parts that have to look different from the default style of the element.

Firebug can help you to find out the styles you want to change.

Your file could be named like this: ``src/Workshop/DemoBundle/public/demo_fullscreen.css`` and have the following definition:

.. code-block:: css

 .toolBar {
   background-color: rgba(0, 29, 122, 0.8) !important;
 }

 .toolPane {
   background-color: rgba(0, 29, 122, 0.8) !important;
 }

 .sidePane {
   overflow: visible;
   background-image: url("");
   background-color: #eff7e9;
 }

 .sidePane.opened {
     width: 350px;
 }

 .logoContainer {
   background-color: white !important;
   background-image: url("") !important;
   -webkit-box-shadow: 0px 0px 3px #0028AD !important;
   -moz-box-shadow: 0px 0px 3px #0028AD !important;
   box-shadow: 0px 0px 3px #0028AD !important;
 }

 .sidePaneTabItem {
    background-color: #0028AD;
 }

 .layer-opacity-handle {
     background-color: #0028AD;
 }

 .mb-element-overview .toggleOverview {
     background-color: #0028AD;
 }

 .button, .tabContainerAlt .tab {
     background-color: #0028AD;
 }

 .iconPrint:before {
   /*content: "\f02f"; }*/
   content:url("image/print.png");
 }

 .popup {
   background-color: #eff7e9;
   background-image: url("");
 }

 .pan{
   background-color: rgba(0, 93, 83, 0.9);
 }

The result of these few lines of css will look like this:

.. image:: ../../figures/workshop_application.png
     :scale: 80

When you open your new application a css-file will be created at:

* ``web/assets/WorkshopDemoBundle__demo_fullscreen__css.css``

If you do further edits at your css file you may have to delete the generated css file in the assets directory to see the changes. You should also clear the browser cache.

.. code-block:: bash

 sudo rm -f web/assets/WorkshopDemoBundle__demo_fullscreen__css.css


Style the administrational pages
********************************

Please change the following css-files for the backend pages:

 * login.css : Change the design of the login page
 * manager.css : Change the design of the administration pages (e.g. application overview)
 * password.css : Change the design of the password pages (e.g. Reset Password - page)

You only have to define the parts that have to look different than the default page style.

Firebug can help you to find out the styles you want to change.

Referencing the CSS-files is possible with FOMManagerBundle and FOMUserBundle. They must be filed under ``app/Resources/``. The already contained twig-files overwrite the default settings if configured correctly (Requirements from manager.html.twig file).
Alternatively, it is possible to copy a twig-file and adjust it afterwards.

 .. code-block:: bash

  cp fom/src/FOM/ManagerBundle/Resources/views/manager.html.twig app/Resources/FOMManagerBundle/views/


Register your bundle in config/bundles.php
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add write access to the ``public`` directory for your webserver user, if need be:

.. code-block:: bash

    chmod ug+w public


Update the ``public`` directory. Each bundle has its own assets - CSS files, JavaScript files, images and more - but these need to be copied into the public web folder:

.. code-block:: bash

    bin/console assets:install public


Alternatively, as a developer, you might want to use the symlink switch on that command to symlink instead of copy. This will make editing assets inside the bundle directories way easier.

.. code-block:: bash

   bin/console assets:install public --symlink --relative


Now your template should show up in the template list when you create a new application.


How to use a new template
~~~~~~~~~~~~~~~~~~~~~~~~~
There are different ways of how to use the new template:

Usage in YAML-applications
**************************

You can adjust the YAML-applications in ``config/applications`` and change the template parameter.

.. code-block:: yaml

  template:   Workshop\DemoBundle\Template\DemoFullscreen


Usage in new applications from the backend
******************************************

If you create a new application in the administration interface of Mapbender, you can choose the new template.


Usage in an existing application
********************************

For existing applications you can change the parameter in the Mapbender database in the column ``template`` of the table ``mb_core_application``.

For the *WorkshopDemoBundle* you change the entry from ``Mapbender\CoreBundle\Template\Fullscreen`` to ``Workshop\DemoBundle\WorkshopDemoBundle``.


Usecases
~~~~~~~~

How do I change the logo, the title and the language?
This and more tips can be found here: :ref:`yaml`.

How do I change the buttons?
****************************

Mapbender uses 'Font Awesome Icons' font icon collection:

.. code-block:: css

 @font-face {
   font-family: 'FontAwesome';
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?v=3.0.1");
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?#iefix&v=3.0.1") format("embedded-opentype"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.woff?v=3.0.1") format("woff"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.ttf?v=3.0.1") format("truetype");
   font-weight: normal;
   font-style: normal;
 }

In your css-file you can refer to a font images like this:

.. code-block:: css

  .iconPrint:before {
    content: "\f02f";
  }

If you want to use an image you could place the image in your bundle and refer to it like this

.. code-block:: css

  .iconPrint:before {
   content:url("image/print.png");
  }


Try this out
~~~~~~~~~~~~

* you can download the Workshop/DemoBundle at https://github.com/mapbender/mapbender-workshop
* change the color of your icons
* change the size of your icons
* change the color of the toolbar
* use an image instead of a font-icon for your button
* move the position of your overview to the left
* Have a look at the workshop files to see how it works
