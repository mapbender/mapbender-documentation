.. _copyright:

Copyright
*********

The copyright element can be used to show simple text or HTML in a window dialog. It can be opened automatically on application start. It is also possible to integrate links and images into the window (see :ref:`html`).

The "Don't show again" option can be activated. Then the dialog will only be displayed again when the text changes.

.. image:: ../../../figures/copyright.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/copyright_configuration.png
     :scale: 70

* **Open automatically:** Enable or disable autoopening of the copyright window while starting the application (default: off).
* **Title:** Title of the element. It will be indicated next to the button.
* **Dialog width:** Width of the Popup window (default: 300).
* **Dialog height:** Height of the Popup window (default: 170).
* **Content:** Content of the copyright window, displayed when clicking on the button (or autoopened by starting the application, if enabled).
* **"Don't show again"-Option** Checkbox. Defines whether the checkbox "Don't show again" show be shown in the dialog (default: false).
* **"Don't show again"-Text** Text to show at the "Don't show again" checkbox.

Refer to a twig file
--------------------

You can refer to a twig file in the Content area. Please note that the twig file has to contain valid HTML.

.. code-block:: yaml

   {% include 'WorkshopDemoBundle::news.html.twig %}'


YAML-Definition
---------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

   class: Mapbender\CoreBundle\Element\Copyright
   title: "Copyright"              # Title of the element
   popupWidth: 300
   popupHeight: 170
   content: "You are using Mapbender.We hope you enjoy the software."    # Define the text that you show up. HTML and reference to a twig file is possible.
   autoOpen: true                  # Automatically open the dialog when you start the application
   dontShowAgain: true             # default false
   dontShowAgainLabel: mb.core.copyright.admin.dontShowAgainDefaultLabel # an individual text for the checkbox can be definied
