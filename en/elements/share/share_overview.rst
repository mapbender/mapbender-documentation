.. _share_overview:

Share elements (Overview)
*************************

Mapbender offers multiple functions that simplify collaborative work within applications.

* :ref:`shareurl` enables quick sharing of self-configured map states via URL,
* :ref:`view_manager` stores custom map states,
* :ref:`applicationswitcher` enables easy cross-application switches,
* :ref:`persistent_map_view` enables the map state to be saved in the browser.

Moreover, certain map view parameters are automatically passed in every application URL. 
This allows users to share specific map views via URL.

Contained view parameters include: 

* center
* scale
* rotation
* spatial reference system

There is no extra configuration for this functionality. It is always turned on.

If a URL is opened up in a new browser tab, previously mentioned view configurations will be restored. Made changes can be undone/redone with the browser back/forward buttons.

Users will be sent back to the same part of the map if they refresh the page. They will not be sent back to the configured initial map view. In order to do so, users have to open the application again from the application list or manually delete the hash part of the application URL.

.. note:: Attributes that are not saved are the temporary layer selection and layer sorting, geometry features, source additions via the WMS loader or other runtime additions.

