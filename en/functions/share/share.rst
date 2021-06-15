.. _share:

Share
*****









































































Persistent map view
===================

This feature makes certain view parameters and certain source settings "persistent". That means an application can be opened up again in the same browser without loosing certain information.

Persisted and restored settings encompass:

* view parameters (center, scale, rotation, SRS)
* per-layerset selected or deselected states
* per-source and source layer selected or deselected states
* per-source opacity

Persistence is purely based on browser local storage, which means it is private to a user's local browser. It also remains private for multi-user systems. There is no interaction whatsoever with the Mapbender login.

Behaviour is enabled on a per-application basis with a new checkbox under the "Base data" tab.

.. image:: ../../../figures/persistent_map_view.png
     :scale: 80

This feature can also be set in a Yaml-application definition, with a new *persistentView* entry on the top level. Omitting the entry is the same as setting it to false.

YAML-Definition:
----------------

.. code-block:: yaml

parameters:
    applications:
        mapbender_user:
            title: Mapbender Demo Map
            screenshot: screenshot.png
            published: true
            persistentView: true      # <== this is new
            template:  Mapbender\CoreBundle\Template\Fullscreen

This change introduces a new column in the *mb_core_application* table and as such requires a run of *app/console doctrine:schema:update --force*.

Currently not persisted and not restored are:

* Dimension parameter values
* Source additions (via WMS Loader)
* Layer / entire source removals (via Layertree context menu)
* Source / layer reordering operations via Layertree drag+drop
* States of per-layer featureinfo checkboxes


Share URL
=========

Certain view parameters are automatically contained in every application url. Thus, users can share specific map views by simply sending the complete url via email / chat or any other text-capable system. Contained view parameters include: 

* center
* scale
* rotation
* spatial reference system

There is no extra configuration for this functionality. It is always turned on.

If a url is opened up in a new browser tab, previously mentioned view configurations will be restored. Made changes can be done/redone via the browser back/forward buttons.

Users will be send back to the same part of the map if they hit F5 to reload. They will not be send back to the configured initial map view. In order to do so, users have to open the application again from the application list or manually cut off the hash of the application url.

NOTE: The following information are *not* saved by the URL: layer selection, sorting, runtime additions, geometry features or sources additions via WMS loader.


Element "Share URL"
-------------------

URL share can be further simplified by integrating a respective element in toolbar or footer.

.. image:: ../../../figures/share_url.png
     :scale: 60

After click on the button, the URL is saved to the clipboard. Standard browser interactions (e.g. open in new tab) are possible as well.

This element stores the following information:

* basic view parameters (center, scale, rotation, SRS)
* layer and layerset settings changes (selected / deselected layersets, sources and layers, layer opacity settings)

The URL does *not* transfer dynamically added sources (via WmsLoader), dynamically removed layers or sources (via Layertree context menu) or changes to source or layer order (via Layertree drag&drop)

YAML-Definition:
----------------

.. code-block:: yaml

    title: Share this map view #Optional custom title, uses default title "Share URL" if omitted (string or empty).
    tooltip: I am displayed on hover #Optional custom tooltip, same as title if omitted (string or empty).
    label: true #Enables display of title, set as FALSE will only display icon (Default: true).
    
