.. _html:

HTML Element
************

This element allows you to add generic HTML anywhere in your application.

.. image:: ../../../../../figures/html.png
     :scale: 80


Configuration
=============

For example you can add an image to your application:

.. code-block:: yaml

    <img src='http://mapbender3.org/sites/default/files/OSGeo_project.png' height='60px'>


.. image:: ../../../../../figures/html_result_application.png
     :scale: 80


YAML-Definition:

.. code-block:: yaml

    content: <p>Hello, World!</p>
    classes: my-special-css-class
   

Class, Widget & Style
============================

* Class: Mapbender\\CoreBundle\\Element\\HTMLElement
* Widget: mapbender.mbHTMLElement

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.


Examples
==================

Add an image

.. code-block:: yaml

   <img src='http://mapbender3.org/sites/default/files/OSGeo_project.png'>


Add an Link

.. code-block:: yaml

  <a href='http://mapbender3.org' target='_blank'>Go to the Mapbender3 Webside</a>

