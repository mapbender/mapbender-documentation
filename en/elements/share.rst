.. _share:

Share
=====

Next, we will explore :ref:`shareurl`, :ref:`view_manager`, and :ref:`applicationswitcher`, all of which fall under the category of 'Share' as they streamline collaborative work within Mapbender applications.

* :ref:`shareurl` enables quick sharing of self-configured map states via URL,
* :ref:`view_manager` stores custom map states,
* :ref:`applicationswitcher` enables cross-application switches,
* :ref:`Persistent_Map_View` simplifies the application compatibility with the web browser.

Moreover, certain map view parameters are automatically contained in every application URL. 
Thus, users can share specific map views. 

Contained view parameters include: 

* center
* scale
* rotation
* spatial reference system

There is no extra configuration for this functionality. It is always turned on.

If a URL is opened up in a new browser tab, previously mentioned view configurations will be restored. Made changes can be undone/redone with the browser back/forward buttons.

Users will be sent back to the same part of the map if they refresh the page. They will not be sent back to the configured initial map view. In order to do so, users have to open the application again from the application list or manually delete the hash part of the application URL.

.. note:: Not saved attributes are layer selection, sorting, runtime additions, geometry features or source additions via WMS loader.
