.. _imageexport:

ImageExport
***********

ImageExport allows you to export your current map view. You can choose png or jpeg format.

.. image:: ../../../figures/image_export.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/image_export_configuration.png
     :scale: 80

* **Title:** Title of the element. The title will be listed in "Layouts" and allows to distinguish between different buttons. The title will be displayed besides the button if "Show label" is activated.

YAML-Definition:
----------------

.. code-block:: yaml

   target: ~                        # Id of Map element to query (e.g. map)

You need a button to show this element. See :ref:`button` for inherited configuration options.
