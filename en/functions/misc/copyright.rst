.. _copyright:

Copyright
*********

The copyright shows a copyright label and terms of use as a dialog.

.. image:: ../../../figures/copyright.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/copyright_configuration.png
     :scale: 80

* **Autoopen:** Enable or disable autoopening of the copyright window, when starting the application (default: off).
* **Title:** Title of the element. It will be indicated next to the button.
* **Tooltip:** Text used as a tooltip. It will be displayed when hovering with the cursor over the button. It also used as a header in the copyright window.
* **Popup width:** Width of the Popup window (default: 300).
* **Popup height:** Height of the Popup window (default: 170).
* **Content:** Content of the copyright window, displayed when clicking on the button (or autoopened by starting the application, if enabled).

YAML-Definition:
----------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

   class: Mapbender\CoreBundle\Element\Copyright
   title: "Copyright"              # Title of the element
   popupWidth: 300
   popupHeight: 170
   tooltip: "Copyright"            # Text to use as tooltip
   content: "Lorem ipsum"          # Edit the text you want to display as copyright text
   autoOpen: true                  # Automatically open the dialog when you start the application
   
