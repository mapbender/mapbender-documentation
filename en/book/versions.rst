Version history
===============

`German Version of this document. <../../de/book/versions.html>`_

You find the milestones at: https://github.com/mapbender/mapbender/milestones

Future Milestones: For details have a look at https://github.com/mapbender/mapbender/issues


Milestone 3.0.5.0
-----------------

Release Date: xx-05-2015

For details have a look at:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* **WMS reload:** WMS sources can now be reloaded if the structure has changed.

* **Digitizer:** The digitizer allows the editing of geometries and their attributes. Right now it needs access to the database where the editable tables are. The definition of the digitizer is done in YAML syntax. To provide an usable interface for the attributes, you can declare the form in your configuration file. The form supports different input fields (textboxes, checkboxes, date-pickers, and so on..), validation, tabs and it uses Bootstrap.

* **Print with legend:** The print element supports the print-out of the legend on a seperate page. This can be set with a checkbox.

* **Configurable layertree:** The layertree supports the usage of more than one layerset. You have to adjust the map element to define which layersets should be shown and the layertree element itself. The usage is documented at [13].

* **Improved FeatureInfo dialog:** You can set a) the width and height of the FeatureInfo dialog, b) if the dialog should show the original format of the WMS and c) if it should only open if a valid entry is found (otherwise a messagebox is displayed). See the documentation at [15].

* **Mobile template:** A new modern mobile template is provided.

* **SASS Compiler:** Architectual changes are made at the SASS compiler which leads to a more performant interface.

* **Vendor Specific Parameters:** A WMS layer instance supports the definition of Vendor Specific Parameters that are added to the WMS request. You can define hard coded values or the user or group information of the logged-in user. See the documentation at [14] for details.

* **Expanded functionality of HTML elements with a form-builder:** This approach is used in the Digitizer to provide the forms for attribute editing.

* **New button colletion:** The new buttons are based on a new font, the old buttons are available under the "FontAwesome" name.

* **Starting mapbender with URL parameters:** Mapbender3 can be started with URL parameters. See the documentation at [16]

* Symfony updated to 2.3.29.


**Changes in config.yml:**

* Changes in a dbal connection:
  
  * **logging: false**: This options sets, that *all* SQL statements are not logged. Further information can be found here: http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste/

  * **profiling: false**: This option handles the profiling of SQL statements. This option can be switched off in production environments.

  If possible the options should be set this way, so that they are only active in debug mode:

  .. code-block:: yaml

                  logging:               "%kernel.debug%"
                  profiling:             "%kernel.debug%" 


**Known Issues**

* After copying an application from Mapbender 3.0.4.x you have to set the layerset in the map/overview element.
 

Milestone 3.0.4.1
-----------------

Release Datum: 23-01-2015

For details have a look at:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* option 'removelayer' added into layertree menu
* parameter 'layerRemove' removed from layertree configuration
* container accordion structure changed
* import / export from applications added (without acls)
* display layer metadata
* Frontend: Sidepane Accordeon Legend is displayed without horizontal Scrollbar
* Backend: WMS Instanz configuration - contextmenu for layers shows wrong ID (only instance ID)
* Frontend: Legend - displays WMS Information although the checkbox Show
* Frontend: Layertree - contextmenu zoomlayer does not use the layer extent
* Backend: Add Source with user/password - informations is added to field originUrl not to fields user and password
* app/console mapbender:generate:element fixed errors
* bug visiblelayers fixed
* WMS with authentication saves in table mb_wms_wmssource username and password
* no metadata for applications coming from mapbender.yml definition (no entry in context menu)
* copy an application via button on application fixed
* print template resize northarrow, overview added
* improved screenshot for application handling
* https://github.com/mapbender/mapbender/milestones/3.0.4.1


Milestone 3.0.4.0
-----------------

release date: 12-09-2014

For details have a look at https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* Switched to MIT license
* Symfony Update 2.3 LTS
* OpenLayers 2.13 with additional patches
* Switch Services (BaseSourceSwitcher) with menu
* added generic HTML element
* added custom CSS editor for applications
* added accordion container for SidePane
* added screenshot management to application editing
* import/export of applications/sources
* spanish translation
 

Milestone 3.0.3
---------------

release date: 17-03-2014

For details have a look at: https://github.com/mapbender/mapbender/issues?milestone=8

* Enhancements for Search-Router für SQL-Suchen (Selectboxes, Distinct)
* WMC Editor and Loader
* WMSLoader Enhancement add WMS via link
* i18n - Internationalisation (english / german)
* Sketch to draw temporary objects
* POI - Meetingpoint
* Imageexport to generate png or jpg
* Change WMS Collection via button (BaselayerSwitcher)
* Print with overview
* Sidepane with different elements (chnage via button)
* Layertree context menue to change opacity and to zoom to layer
* Open application with parameters (f.e. position)
* ACL for elements
* Added function for validate WMS GetCapabilities documents
 

Milestone 3.0.2
---------------

release date: 27-11-2013

For details have a look at https://github.com/mapbender/mapbender/issues?milestone=6

* SearchRouter
* WMC Editor and Loader
* WMSLoader enhancement to load a WMS from a link
 

Milestone 3.0.1
---------------

release date: 06-09-2013

For details have a look at https://github.com/mapbender/mapbender/issues?milestone=5

* Kopieren einer Anwendung mit Diensten
* Popup - draggable
* PrintClient Erweiterung Druck EPSG 4326, neue Drucklayouts, Druck A4-A0
* Catch login failures to avoid  brute force login attempts
* Bug fixes
 

Milestone 3.0.0.2
-----------------

Bugfix-Release Date: 19-07-2013

For details have a look at: https://github.com/mapbender/mapbender/issues?milestone=4

 

Milestone 3.0.0.1
-----------------

Bugfix-Release Date: 07-06-2013

For details have a look at: https://github.com/mapbender/mapbender/issues?milestone=3

 

Milestone 3.0.0.0
-----------------

release date: 29-05-2013

For details have a look at https://github.com/mapbender/mapbender/issues?milestone=1

* Administration Backend for Service, Application, User/Group and security administration
* Backend-/Frontend Design   
* Security
* User/Group Administration
* WMS Administration
* Map
* Layertree
* Legend
* Overview Map
* Navigation Toolbar (Zoombar)
* Feature Info
* Coordinates Display
* Copyright
* Line/Area Ruler
* Scale Selector
* ScaleBar
* Spatial Reference System Selector
* GPS-Position
* Print
* Add WMS to application
* Documentation at http://doc.mapbender3.org
