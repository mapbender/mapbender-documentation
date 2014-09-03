.. _html:

HTML-Element
************

Über das HTML-Element kann generisches HTML an einer beliebigen Stelle in der Anwendung definiert werden.

.. image:: ../../../../../figures/html.png
     :scale: 80


Configuration
=============

Fügen Sie beispielsweise ein Bild in Ihre Anwendung ein:

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


Beispiele
==================

Einfügen eines Bildes

.. code-block:: yaml

   <img src='http://mapbender3.org/sites/default/files/OSGeo_project.png'>


Einfügen eines Links

.. code-block:: yaml

  <a href='http://mapbender3.org' target='_blank'>Go to the Mapbender3 Webside</a>

