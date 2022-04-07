.. _applicationswitcher:

ApplicationSwitcher
*******************

The ApplicationSwitcher element provides a selectbox that refers to other Mapbender applications. You can switch from one application to another. The map extent will be preserved.

.. image:: ../../../figures/applicationswitcher.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/applicationswitcher_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be shown as tooltip on mouseover on the selectbox.
* **Applications:** Choose the applications that should be offered in the selectbox.
* **Open in new tab:** Define whether the new application should be opened in the same window (default) or in a new tab.


ApplicationSwitcher Configuration
---------------------------------

First, you have to select the link element by clicking on the ``+`` - symbol in the Toolbar section in the Layouts tab.

.. image:: ../../../figures/de/add_toolbar.png
     :scale: 80

After the selection of the ApplicationSwitcher element, the "Add element - ApplicationSwitcher" dialog box opens, where you can configure the element.

You can define a the field *Title*. This title will be displayed as tooltip on mouseover on the selectbox.

With the checkbox *Open in new tab:*, you can define whether the new application should be opened in the same window (default) or in a new tab.


YAML-Definition:
----------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

    title: Choose an Application              # Text will be displayed as tooltip
    class: Mapbender\CoreBundle\Element\ApplicationSwitcher
    applications: ["mapbender_user","mapbender_user_basic"]     # Define the applications for the ApplicationSwitcher as array 
    open_in_new_tab: true   # false/true open application in new tab

