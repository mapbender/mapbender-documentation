.. _digitizer_functionality:

Functionalities
***************

The Digitizer-Element offers complex editing functionality:

* move objects
* add vertices (lines, polygons)
* generation of enclaves, exclaves, circles and ellipses

In connection with the digitization, very complex forms can be generated for the acquisition of data.
    

.. image:: ../../../figures/digitizer.png
     :scale: 80

The following option for the construction of the forms are available:

* Define more then one feature types for digitization. You can switch from one feature type to the other with a select box
* Use a table as source. You can also define a filter to get a subset of the table
* Textfields
* Selectboxes, Multiselectboxes
* Radiobuttons, Checkboxes
* Textareas
* Datepicker
* File upload and Image Display
* Definition of tabs
* Definition breakLines
* Definition of Text 
* Mandatory fields, regular expressions to valid the content are possible
* Definition of help texts
* Duplicate features
* Refresh after save
* Possibility to copy entered information from a form into the clipboard


.. image:: ../../../figures/digitizer_with_tabs.png
     :scale: 80


Usage
=====

General
-------

The Digitizer allows the editing of FeatureTypes. These are based on points, lines and polygon-geometries and their attribute-data. The attribute-data is displayed in the formular of the Digitizer. The geometry-editing is done via the map.


Create geometries
-----------------

Every FeatureType can unlock several `Toolsets <#definition-of-the-available-toolsets-toolset-type>`_ that can be used in the button-bar of the Digitizer.


For example in the FeatureType "poi" the toolset "drawPoint" unlocks the button to create a new point, the toolset "modifyFeature" unlocks the move-button.


.. image:: ../../../figures/digitizer_buttons_poi.png
     :scale: 80



Save, Delete, Cancel
--------------------

Three buttons are available in the attribute-dialog: Save, Delete and Cancel.

*Saving* changes only happens, if the "Save" button in the attribute-dialog is pressed. A move of the geometry alone doesn't save the feature directly (to avoid unnecessary stores into the database). It is mandatory to open the attribute-dialog and to click Save.

.. image:: ../../../figures/digitizer_save_delete_cancel.png
     :scale: 80

* **Save:** Saves the geometry and the attribute-data into the database.
* **Delet:** Deletes the data.
* **Cancel:** Doesn't save and delete the data, but keeps the geometry for further editing in the internal storage. The geometry is still present in the map and can be adjusted (for example with polygons). Attribute data is not stored.

Several options exit in the `basic definitions <#feature-basic-definition>`_, to customize the behaviour.

* allowEditData: Show the Save button.
* allowDelete: Show the Delete button.
* allowCancelButton: Show the Cancel button.
* allowDeleteByCancelNewGeometry: Behaviour of the Cancel button.

The *Delete* of a feature can be done with the dialog and from the table.


Vertices
--------

Editing polygons allows you to edit, move and delete vertices. The "edit vertices" button expects you to select a polygon. It will then be shown with its vertices.

.. image:: ../../../figures/digitizer_edit_vertices.png
           :scale: 80

The existing vertices are displayed opaque, possible new vertices are always in the middle of an edge, are light transparent and can be added by clicking on them.

Existing vertices can be deleted with the Delete-Key of the keyboard. To do this, move your mouse-pointer over a vertex and press the Del-key. *Note:* If the deletion of a vertex doesn't work in the first place, a click with the right mouse-button on the map may help. Especially with activated context-menu some events can currently get stuck.



