.. _css:

CSS editor
##########

Mapbender offers an CSS editor for every application which easily allows you to change its style (colors, sizes, icons, ...). In the editor it is possible to define additional CSS classes that will overwrite the default style. 

The CSS editor is located in the "CSS" tab of every application.

.. image:: ../../figures/css_editor.png
     :width: 100%

.. tip:: A browser inspect tool can help you to find out the CSS classes you want to change.


Example
=======

The CSS editor can be useful for extending Mapbender's functionality: In the example below, the provided code block creates a scrollbar for applications with an expandable side menu, enhancing the application's usability on mobile devices.

.. code-block:: css

  // Scrollbar in Toolbox
  .dropdown-menu {
    overflow-y: auto;
    max-height: calc(100vh - 100px);
  }


The function itself can be found in the ``Layout`` tab of the backend: Click the gear icon and activate the checkbox ``Generate menu for buttons``.