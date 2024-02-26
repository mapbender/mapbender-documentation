.. _css:

CSS editor
##########

Mapbender offers an CSS editor for every application which easily allows you to change its style (colors, sizes, icons, ...). It is possible to define additional CSS classes that will overwrite the default style. You can use scss in the editor. And you can refer to an scss-file in your bundle. 

.. image:: ../../../figures/css_editor.png
     :width: 100%

.. tip:: A browser inspect tool can help you to find out the CSS classes you want to change.


Examples
========

Add scrollbar to the top toolbar
--------------------------------
When you use the menu option in the top toolbar you can define at what size of the screen the height should be reduced and a scrollbar should appear. This enhances the usability of the application on mobile devices.

.. code-block:: css

  // Scrollbar in Toolbox
  .dropdown-menu {
    overflow-y: auto;
    max-height: calc(100vh - 100px);
  }


The function itself can be found in the :ref:`layouts` tab: Click the gear button and activate the checkbox ``Generate menu for buttons``.


Adjust the splashscreen
-----------------------

If your Mapbender application has its splashscreen active via :ref:`basedata`, it is possible to customize it further via CSS:

.. code-block:: CSS

    :root {
        --primary: #079ee0;                                 /* application-wide primary color, will be used as the loading indicator's color */
        --splashscreen-border: none;                        /* border around the splashscreen dialog, generate using e.g. https://html-css-js.com/css/generator/border-outline/ */
        --splashscreen-border-radius: 25px;                 /* determines the radius of rounded corners around the dialog */
        --splashscreen-background: rgba(255,255,255,0.8);   /* background color of the splashscreen */
        --splashscreen-fade-out-duration: 200ms;            /* animation duration of the fade out */
    }