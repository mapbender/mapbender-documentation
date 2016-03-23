.. _layerset:

Layerset
========

Layersets are logical containers, that can contain one or more layerset-instances (WMS services). A typical example is the differentiation between a layerset "main" for the main map and a layerset "overview" for the overview map. You can define more layersets to show them optionally on the map or to use them in the layertree in their own folders (thematic layers).

.. image:: ../../../../../figures/mapbender3_service_edit.png
           :scale: 80

Layer-instances contain the options how a WMS is called: image-format, info-format, exception-format, scales for the different layers and many more.

.. image:: ../../../../../figures/mapbender3_wms_application_settings.png
           :scale: 80


Further information
-------------------

* You can find information about using layersets in the `Quickstart documentation <../../../../book/quickstart.html#configure-your-wms>`_.

* The relevance of layersets for the display in the layertree is described in the Thematic Layers section of the `layertree documentation <../elements/layertree.html>`_

* Likewise layersets can be switched on or off in the `Map element <../elements/map.html>`_.
