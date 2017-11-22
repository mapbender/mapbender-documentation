.. _html:

HTML-Element
************

Über das HTML-Element kann generisches HTML an einer beliebigen Stelle in der Anwendung definiert werden.
Im generischen HTML stehen zur Verfügung folgende Variablen: "application" (Entity Application), "entity" (Entity HTMLElement) und "configuration". Damit kann beispielsweise ein Bild in die Anwendung eingefügt werden. 

.. image:: ../../../../../figures/html_result_application.png
     :scale: 80


Configuration
=============

Einfügen eines Bildes in Ihre Anwendung:

.. code-block:: yaml

    <img src='http://mapbender.org/sites/default/files/OSGeo_project.png' height='60px'>


.. image:: ../../../../../figures/de/html.png
     :scale: 80

* **Title:** Titel des HTML-Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere HTML-Elemente voneinander zu unterscheiden. 
* **Content:** Inhalt des HTML-Elements, z.B. Bild oder Link. Content kann Variablen: "application", "entity" und "configuration" beinhalten.
* **Classes:** html-element-inline, CSS-Klasse


YAML-Definition:
----------------

.. code-block:: yaml

    content: <p>Hello, World!</p><p>Application: {{ application.title |trans }}</p> # content kann Variablen: "application", "entity" und "configuration" beinhalten.
    classes: my-special-css-class
   

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\HTMLElement
* **Widget:** mapbender.mbHTMLElement

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

   <img src='http://mapbender.org/sites/default/files/OSGeo_project.png'>


Einfügen eines Links

.. code-block:: yaml

  <a href='http://mapbender.org' target='_blank'>Go to the Mapbender Website</a>

