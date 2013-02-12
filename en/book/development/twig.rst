.. _twig:

Twig
#####
Symfony follows the template approach and we use this in Mapbender3. Symfony uses a templating engine to generate HTML, CSS or other content. 

Twig is a templating engine that is packaged in Symfony2 and offers an easy and powerfull way to generate templates. 

A template is a text file that can generate any text based format like HTML, XML. It is used to express presentation and not programm logic.

You can use templates to create a layout. You can create a base layout and the overwrite or append any of your layout blocks with individual templates.

Read more about Templates in Mapbender3 at :doc:`How to create your own Template? <../templates>`.


Documentation
*************
Read more about Twig in Twig documentation the http://twig.sensiolabs.org/.

You find a good introduction in the Symfony2 TheBook **Creating and using Templates** http://symfony.com/doc/current/book/index.html

 
Twig Syntax
***********

.. code-block:: yaml

   {# define a comment like this #}
   
   {{ mb_user }}      {# echo a variable #}
   
   {%    %}           {# do something if, for #}
   
   {{ mb_user|upper }}   {# use filter #}

   {{title|trans }}   {# translates the variable title #}
   {% trans %}title{% endtrans %} 


Twig Template caching
*********************
Twig is fast and the twig template is compiled to a native PHP class at runtime.

You find the compiled classes at

 app/cache/dev/twig   # when running in the development mode 

 or 

 app/cache/prod/twig   # when running in the productive mode 

**Notice:** The files are cached in the productive mode. In the debug mode, the Twig template will be automatically recompiled.

Template Location
****************************
Templates can be located at 

* app/Resources/views/
* <path bundle>/Resources/views/

Template Name
*************
The name of your template should follows the syntax **bundle:controller:template**.

In Mapbender3 we use for example the following twig templates:
 
* app/base.html.twig
* application/mapbender/src/Mapbender/CoreBundle/Resources/views/frontend.html.twig
* application/mapbender/src/Mapbender/CoreBundle/Resources/views/Template/fullscreen.html.twig


Check the syntax of your Twig template
**************************************
You can check for syntax errors in Twig templates using the twig:lint console command:

.. code-block:: yaml

 app/console twig:lint mapbender/src/Mapbender/CoreBundle/Resources/views/Template/fullscreen.html.twig

The example checks by filename, but you could also check by directory or bundle name.

.. ToDO
 assets  
 ****** 
 app-Variable
 ************
 example
 ******



