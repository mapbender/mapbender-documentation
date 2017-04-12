.. _copyright:

Copyright
*********

The copyright shows a copyright label and terms of use as a dialog.

.. image:: ../../../../../figures/copyright.png
     :scale: 80

Configuration
=============

.. image:: ../../../../../figures/copyright_configuration.png
     :scale: 80

* **Autoopen:** Enable or disable autoopening of the copyright window, when starting the application. (Default: disabled)
* **Title:** Title of the element. It will be indicated next to the button.
* **Popup width:** Width of the Popup window (default: 300).
* **Popup height:** Height of the Popup window (default: 170).
* **Tooltip:** Text used as a tooltip. It will be indacted when hovering with the mouse cursor over the button. It also used as a header in the copyright window.
* **Content:** Content of the copyright window, displayed when clicking on the button (or autoopened by starting the application, if enabled)

YAML-Definition:
----------------

.. code-block:: yaml

   class: Mapbender\CoreBundle\Element\Copyright
   title: "Copyright"              # Title of the element
   popupWidth: 300
   popupHeight: 170
   tooltip: "Copyright"            # Text to use as tooltip
   content: "Lorem ipsum"          # Edit the text you want to display as copyright text
   autoOpen: true                  # Automatically open the dialog when you start the application
   

Class, Widget & Style
============================

* **Class:** Mapbender\\CoreBundle\\Element\\Copyright
* **Widget:** mapbender.element.copyright.js
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
