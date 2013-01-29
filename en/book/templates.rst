How to create your own Template?
################################

Mapbender3 comes with application templates you can use. But usually you want to use your own template with your own corporate design. 

How to create your own template?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 4 steps you have to follow on the way to your own template.

* create your own twig-file
* create your own css-file
* create a template php-file to register your template
* use your template in yml-configuration or choose it through the administration

Create your own twig-file
~~~~~~~~~~~~~~~~~~~~~~~~~
You find the twig-files at the following path:

* \\src\\Mapbender\\CoreBundle\\Ressourcen\\views\\Template

The easiest way to create your own twig file is to copy an existing twig, save it under a new name and change the content like colors.

.. code-block:: yaml

 cd application/src/Mapbender/CoreBundle/Ressourcen/views/Template 
 cp base.html.twig demo.html.twig


Create your own css-file
~~~~~~~~~~~~~~~~~~~~~~~~~
The css-files are located in application/src/Mapbender/CoreBundle/Ressourcen/public/css. Create your own css file and edit the content.

.. code-block:: yaml

 cd application/src/Mapbender/CoreBundle/Ressourcen/public/css
 cp mapbender.template.base.css mapbender.template.demo.css


Register your template
~~~~~~~~~~~~~~~~~~~~~~
To register your template you have to create a file at 

* application/src/Mapbender/CoreBundle/Template 

.. code-block:: yaml

 cd application/src/Mapbender/CoreBundle/Template
 cp Fullscreen.php Demo.php


Use your new template in mapbender.yml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now you can use the template in mapbender.yml where you can configure applications.

You find the mapbender.yml at:

* application/app/config

.. code-block:: yaml
  
  "template:  Mapbender\CoreBundle\Template\Demo"


Use your new template in the Mapbender administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When you create a new application through the Mapbender3 administration you have to choose a template you want to use. Your new template should show up in the list.


