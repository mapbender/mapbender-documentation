.. _about_dialog:

About Dialog
************

This element renders a button which shows a simple about dialog, listing Mapbender's version.
(Future: Licenses, Custom information page)

.. image:: ../../../../../figures/about_dialog.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/about_dialog_configuration.png
     :scale: 80

YAML-Definition:

.. code-block:: yaml

   tooltip: 'About Mapbender3' # text to use as tooltip
   label: true # false/true to label the scale selector
   icon: 'abouticon' # icon to display on button

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\AboutDialog
* Widget: mapbender.mbAboutDialog
* Style: mapbender.elements.css

HTTP Callbacks
==============

about
-----

Retrieves dialog contents.

JavaScript API
==============

None.

JavaScript Signals
==================

None.

