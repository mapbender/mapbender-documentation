.. _share:

Share
=====

Share offers a variety of possibilities that simplify the joint work with Mapbender applications:
*Share URL* enables quick sharing of self-configured map states via URL, *View Manager* stores custom map states, *Application Switcher* enables cross-application switches and *Persistent Map View* simplifies the application compatibility with the web browser.

Certain view parameters are automatically contained in every application URL. 
Thus, users can share specific map views. 

Contained view parameters include: 

* center
* scale
* rotation
* spatial reference system

There is no extra configuration for this functionality. It is always turned on.

If a URL is opened up in a new browser tab, previously mentioned view configurations will be restored. Made changes can be undone/redone with the browser back/forward buttons.

Users will be sent back to the same part of the map if they refresh the page. They will not be sent back to the configured initial map view. In order to do so, users have to open the application again from the application list or manually delete the hash part of the application URL.

.. note:: The following information is not saved by the URL: layer selection, sorting, runtime additions, geometry features or source additions via WMS loader.

.. toctree::
   :maxdepth: 1

   share/shareurl.rst
   share/view_manager.rst
   share/persistant_map_view.rst

