Data Upload
***********

**Data Upload** allows you to upload geodata as points, lines, polygons and multipolygons. Supported geodata file formats are GeoJSON, KML, GML, and GPX.
Simply drag and drop the files into the element or select them from the file system manually.
You can either choose a fitting CRS or use the feature *Determine projection automatically*.

.. hint:: File size is limited. A maximum file size can be defined in the element configuration.

.. image:: ../../../figures/dataupload.png
     :width: 100%


Configuration
-------------

.. image:: ../../../figures/dataupload_configuration.png
     :width: 100%


* **Show label**: Shows a label which incorporates the title and appears next to the coordinates.
* **Title**: Title of the element. It will appear next to the coordinates if 'Show label' is activated.
* **Target**: Id of the Map element to query.
* **Group**: Optional group name.
* **Tooltip**: Hint text entered as a tooltip will be indicated by hovering over the element with the cursor.
* **Icon**: Choose an icon that will be displayed as the button of the element in the map.

After the element has been added to the backend, it is displayed at the corresponding position in Mapbender.
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