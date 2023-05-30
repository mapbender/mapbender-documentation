.. _layouts:

Layouts
#######

The Layouts tab defines the regions of an application, into which elements or functions are implemented. Different templates can have different regions (also known as areas or layouts). 
An overview of all elements is available under :ref:`functions`.

Layout of the Fullscreen template:

  * Top toolbar (button region)
  * Sidepane (Area for the Layertree, Legend, Search,...)
  * Map area (with Map, Scalebar,...)
  * Footer (with Copyright, Activity Indicator,...)


Layout of the Mobile template:

  * Footer (button region)
  * Map area (with Map, navigation toolbar)
  * MobilePane (area that will overlap the map, when a dialog like Layertree or FeatureInfo is displayed)


The  ``+`` button located at the top right of each region allows adding elements. After pressing the button, a dialog box will open, which allows for the selection of an element and its subsequent configuration.

All built-in functions can be moved between regions using drag and drop.

With the exception of the Map area and the MobilePane, all regions can be individually configured using the gear icon in the top right corner. Detailed information about the templates is summarized under :ref:`mapbender_templates`.


Configuration of the Top toolbar and the Footer
***********************************************
The Top toolbar and the Footer provide the following configuration options through their gear icons:

  * Screen type (Any, Mobile, Desktop)
  * Alignment (Left, Right, Center. Default: Left)
  * Checkbox ``Generate menu for buttons``
  * ``Menu label`` input field

If a specific **Screen type** is selected, Mapbender will hide the region when using other screen types.

.. note:: You cannot choose a Screen type in the Mapbender Mobile Template.

**Alignment** adjusts the positioning of all elements in an area.

The checkbox **Generate menu for buttons** configures a dropdown menu for the elements of the area.

The dropdown menu can be labeled via the **Menu label** input field.

.. tip:: **Note**: Using the dropdown menu is especially handy on mobile devices. There's a code snippet in :ref:`CSS` that adds a scroll bar to the menu and helps to increase the user experience. 


Configuration of the sidepane
*****************************
The fullscreen template offers an adjustable sidepane.
The sidepane style can be changed via Mapbender backend (in the sidepane section of the Layouts tab).
The gear icon in the sidepane section shows the following options:

    * Type
    * Screen type
    * Width (in px)
    * Position
    * Checkbox **Initially closed**


.. image:: ../../../figures/sidepane_backend.png
     :width: 100%


The option **Type** adjusts the inserted elements:

- ``Accordion`` shows elements via tabs.

- ``Buttons`` shows elements via buttons.

- ``Unstyled`` does not contain any styling options at all and displays the elements in the configured backend order.


The option **Screen type** defines the device on which the sidepane is visible (any, mobile or desktop).

The option **Width** takes a pixel value and adjusts the sidepane width accordingly.

**Position** defines the placement of the sidepane: "Left" or "Right" can be selected.

The checkbox **Initially closed** hides the sidepane after the application is opened. It is possible to show or re-hide the sidepane while using the application.


Button area (Elements)
**********************
The button area helps configuring elements in their specific regions. The following button functions are available:

  * Toggle show/hide element
  * Show on mobile screens
  * Show on Desktop screens
  * Edit (gear icon)
  * :ref:`acl_de` element
  * Delete


Toggle show/hide element
========================
With the eye icon, it is possible to toggle an element between a shown or a hidden status. A shown element is visible in the application. A hidden one is not visible in the application itself, but can still be adjusted in the backend.

If you want to display or hide one or more elements only for a specific screen type, it is recommended to utilize the features of responsive design instead.


Responsive Design
=================
Mapbender offers a responsive design for greater usability. Every element in the toolbar and sidepane can be individually configured to appear for mobile and/or desktop resolutions.

.. image:: ../../../figures/responsive_design_overview.png
     :width: 100%

It is also possible to define templates for whole layout sections. This way, all associated elements will be automatically invisible when entering the respective view mode.


Edit
====
Opens the configuration mask for a specific element. To look up a setting for a specific function, check the element under :ref:`functions` itself.


Acl element
===========
Opens a **Secure element** window that allows configuration of the :ref:`acl` **View** right for users/groups.

With this, the visibility of an element can be set. At first, Acl configuration is inactive (gray key button), so that there are now access restrictions per element by default.


  #. Next to every element is a security key. If you click on a key, you can adjust the specific element rights of a user.

  #. Just add users who should gain access to the element with the ``+`` button in the pop-up window. A set checkmark next to the user account provides the essential rights for the respective user.

.. image:: ../../../figures/de/fom/acl_secure_element.png
     :width: 100%


After setting specific access rights, the security key turns red. If you hover over the key with the cursor, you will see the names of the users who have rights to the element.

.. image:: ../../../figures/fom/element_security_key_popup.png
     :width: 100%


You can find more security details under :ref:`security`.


Delete
======
Removes an element from both front- and backend. This process requires confirmation before it is executed.