.. _poi:

POI
***

Generate POI-URLs (aka meeting points) suitable for e-mail. The generated point is projected and displayed in the coordinate system of the map.


.. image:: ../../../figures/poi.png
     :scale: 70


Configuration
=============

.. image:: ../../../figures/poi_configuration.png
     :scale: 70
     
* **Use Mailto:** Sends POI by email.
* **Title:** Title of the element. The title will be listed in :ref:`layouts` and allows to distinguish between different buttons. It will be indicated if "Show label" is activated.
* **Body:** Defines text to display. 
* **GPS:** Defines GPS Position in the map.

YAML-Definition
---------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml

    target: map                             # only map-element is possible
    body: 'Please take a look at this POI'  # define a text to display

