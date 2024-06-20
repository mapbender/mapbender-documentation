Data Upload
***********

**Data Upload** allows you to upload geodata as points, lines, polygons and multipolygons. Supported geodata file formats are GeoJSON, KML, GML, and GPX.
Simply drag and drop the files into the element or choose them from within a file manager window.
You can either choose a fitting CRS or use the feature *Determine projection automatically*.

.. hint:: File size is limited. A maximum file size can be defined in the element configuration.

.. image:: ../../../figures/dataupload.png
     :scale: 70


Configuration
-------------

.. image:: ../../../figures/dataupload_configuration.png
     :scale: 70


* **Title**: Title of the element, appears in the header of the element.
* **Max. filesize (MB)**: Maximum permitted file size in megabytes. Default: 10 MB.
* **Help text**: Define a help text that is displayed above the upload field of the element.

After **Data Upload** has been added to the backend, it is displayed at the corresponding position in Mapbender.
After an object is uploaded, it will be shown in the map and the element list.
There, you can toggle its visibility, zoom to it, or delete it again.


YAML Definition
---------------

This template can be used to insert the element into a YAML application.

.. code-block:: yaml
     
 dataupload:
    class: Mapbender\CoreBundle\Element\DataUpload     # Element class name
    target: map                                        # Element target
    maxFileSize: 10                                    # Maximum file size (Megabyte)
    helpText: mb.core.dataupload.admin.helpText        # Text that appears as help dialog