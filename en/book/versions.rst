Version history
===============

`German Version of this document. <../../de/book/versions.html>`_

You find the milestones at: https://github.com/mapbender/mapbender/milestones

Future Milestones: For details have a look at https://github.com/mapbender/mapbender/issues


Milestone 3.0.5.3
-----------------

Release date: soon

   
**Bugfixes:**

- Performance: The CSS, JavaScript and Translation files are now held in the Symfony Cache for the `production mode <installation/configuration.html#production-and-development-environment-and-caching-app-php-and-app-dev-php>`_. This can lead to better performance on slower machines. These cache is not used by the `development-mode <installation/configuration.html#production-and-development-environment-and-caching-app-php-and-app-dev-php>`_.
- The package `eslider/sassc-binaries <https://github.com/eSlider/sassc-binaries>`_ offers now a sassc Compiler for 32-bit Linux systems. This led to a wrong display on 32-bit Linux-Systems (http://lists.osgeo.org/pipermail/mapbender_users/2015-December/004768.html)
- Redlining: The contents of the Redlining element is visible and Redlining can now be used as a Dialog or an Element in the Sidepane. See also the `documentation of the Redlining Element <../bundles/Mapbender/CoreBundle/elements/redlining.html>`_. The scroll bar for the Geometry-Types in the configuration dialog is now displayed correctly. 
- Users can be switched active or inactive by an Administrator, who has at least the ACL-user-right "operator". This can be used for users, who have self-registered but not yet activated their account. See the `documentation of user-management <../bundles/FOM/UserBundle/users.html>`_ for details.
- The text, translations and styles for the Self-Register process and the Password Reset are improved. Also the `Documentation <../bundles/FOM/UserBundle/users.html>`_ is adjusted.
- The `Print module <../bundles/Mapbender/CoreBundle/elements/printclient.html>`_ can now also be used in the Sidepane.
- Print-templates: The default print-templates have changed. The padding of the dynamic texts to their border and their justification were improved.
- Print: The Print configuration messed up mandatory (required: true) and optional fields (required: false), if they were used in combination. Optional fields were partly shown as mandatory (Github #380).
- In some cases Mapbender printed the legend of all WMS-layers, even if the layer was not set active (seen in Mapbender_Users WMS).
- Copying an application under SQLite and MySQL: There was en error that applications could not be copied if the database was SQLite or MySQL.
- Errors at the import of application as JSON on MySQL (elements lose their target) was fixed.
- WMC and thematic layertree: If a WMC is loaded and Keep Sources is set to "no", the thematic layers are now also removed from the layertree.
- WMS-URL parameter and legend: If a service was loaded with the wms_url parameter, the complete legend was shown. This behaviour is fixed. **Note:** WMS services exists, which define a legend in the root-layer element. According to the WMS-specification, this legend will be inherited by sub-layers who itself haven't defined a legend (for example if they only contain the annotations). The effect is similar in MB3 but the cause is different, so that in these cases a change in the WMS capabilities is needed (define a static legend image for these layers).
- Coordinate display: The coordinate-element display doesn't show "null" as prefix or separator anymore, although the field was defined as empty. The element has get a fixed with so that the layout in the footer region is more sable. The value can be changed (see the chapter `CSS-customizing of the element <../bundles/Mapbender/CoreBundle/elements/coordinates_display.html>`_).
- SearchRouter: The content of the result uses the whole space of the dialog and fits itself to changes of the size. In the sidebar the whole height is used. The search router can be configured `with a width and a height <../bundles/Mapbender/CoreBundle/elements/search_router.html>`_.
- ScaleSelector: The width of the element can be `customized with a CSS-Statement <../bundles/Mapbender/CoreBundle/elements/scale_selector.html>`_ and is no more set to 155 pixel.
- If all layer in a layerset-instance are set to visible=off they were not visible in the layertree and the legend. This is fixed.
- Improvements in the styling of the POI dialog if "usemailto" is set to false.
- Layertree: Titles are now shown per default with a length of 40. The default value has been changed. You can set the `parameter Titlemaxlength in the configuration dialog <../bundles/Mapbender/CoreBundle/elements/layertree.html>`_.
- Changing the Base Data, the Layout, the Layerset, the CSS and the Security of an application does not change the tab anymore and doesn't jump back to the base data tab.
- General improvements of the `Digitizer <https://github.com/mapbender/mapbender-digitizer>`_ version 1.0. Version 1.1 is compatible with Mapbender 3.0.5.3.
- Github files: Small clean up actions in the Github repository to improve the automatic build-processes.
- Transparency of services: Services with a transparency refreshed with a poor effect, caused by the "transitionEffect" in OpenLayers. The effect was removed.
- Group filter: The security configuration dialog got improvements at the selection of Groups, if the Groups had the same name but a different suffix.
- TileSize Parameter in the map configuration was not set in some cases.
- Display of dialogues under MS Edge 25 (also an error in MS Edge 20).
- mapbender.yml: At the initial import of the mapbender.yml the values of GetFeatureInfo are now set to text/html. The mapbender.yml can now customized with Redlining.


**General changes:**

- Change of the Mapbender domains: We have switched the URL www.mapbender.org to the Mapbender3 page. In future, the Mapbender3 page is also available via www.mapbender.org and www.mapbender3.org. Mapbender2 is now available at www.mapbender2.org
 
  - http://www.mapbender.org: Mapbender3,
  - http://www.mapbender3.org: Mapbender3,
  - http://www.mapbender2.org: Mapbender2.




Milestone 3.0.5.2
-----------------

Release Datum: 27.10.2015

**Bugfixes:**

- Copy applications: User-Rights and groups are copied. The user who copied the application becomes owner of the copied application.
- FOM: Changes in behaviour of wrong logins and user locking. It is only shown that the login failed, independent if the user exists or not.
- Fixed error message when creating a user with a too short password.
- Print: Fix of replace pattern.
- Print: Fix if a wrong configured WMS has special characters (%26) in the legend URL.
- Image export in Firefox.
- WMC Loader: Loading WMC and Behaviour of BaseSources.
- BaseSourceSwitcher: Tiles of a not visible service are not pre-fetched.
- BaseSourceSwitcher: If a group is defined, only one theme is switched on.
- SearchRouter: Fix of quotes for table-names.
- Copy applications: Fix of the search in the copied application.
- Simple Search: Catch the return key.
- FeatureInfo: Add WMS functionality and WMS Loader.
- Icon Polygon is visible in the toolbar of applications.
- Icons, which are not based on FontAwesome also work in the mobile application.
- Administration of the map element: The view of the configuration dialog in the backend starts on top.
- Administration data source: No form data auto-complete from the browser for username and password.
- Mobile application: Design in Firefox for Android.
- Update 3.0.4.x: FeatureInfo autoopen=true is kept.
- Doku: FOM `UserBundle translation <../bundles/FOM/UserBundle/index.html>`_ and `additional information for failed user logins <../bundles/FOM/UserBundle/users.html>`_.
- Doku: URL parameter scale in `map element <../bundles/Mapbender/CoreBundle/elements/map.html>`_.
- Doku: `WMC Loader <../bundles/Mapbender/WmcBundle/elements/wmc_loader.html>`_ and KeepSources.

**Changes in config.yml:**

* The following changes are optional parameters for the behaviour of the login (see also `the chapter in the FOM bundle for details <../bundles/FOM/UserBundle/users.html>`_):

    .. code-block:: yaml
                    
                    fom_user:

                      # Allow to create user log table on the fly if the table doesn't exits.
                      # Default: true
                      auto_create_log_table: true

                      # Time between to check login tries
                      login_check_log_time: "-5 minutes" 

                      # Login attemps before delay starts
                      login_attempts_before_delay: 3

                      # Login delay after all attemps are failed
                      login_delay_after_fail: 2 # Seconds


Milestone 3.0.5.1
-----------------

Release Datum: 26.08.2015

**New functions**: in the `Map element <../bundles/Mapbender/CoreBundle/elements/map.html>`_ and in the `Print client <../bundles/Mapbender/CoreBundle/elements/printclient.html>`_:

* Map: OpenLayers TileSize: You can set the tile-size for the map. Default: 256x256.
* Map: Delay before Tiles: For WMS-T, for example with temporal parameters (in future)
* Print: Show coordinates in PDF print
* Print: get print scale depending on map-scale
* Print: print legend_default_behaviour
* Print: add print templates with the + symbol
* Print: user-defined logo and text


**Bugfixes:**

- Layertree: loading symbol and exclamation mark symbol.
- Layertree: zoom Symbol not for layers without a BBOX information
- WMS Reload: FeatureInfo
- WMS Reload: some WMS couldn't be reloaded.
- Export/Import of application and miscellaneous bugfixes
- WMC-Editor and WMC-Load fixes.
- WMC from a Mapbender 3.0.4.1 application
- Tile buffer and BBOX buffer fixes
- FeatureInfo: Fixes in design and when shown as an Accordion Panel
- FeatureInfo: Print
- Wrong Jquery-UI link in layerset instance
- Save Layerset and Save Layout leaves you on the page
- Classic Template: SCSS corrections
- Mobile Template: Bootstrap message hides close button
- Mobile Template: close SearchRouter window
- Mobile Template: Mozilla Firefox Fixes on layout
- Backend: Layerset Filter and +-Buttons doesn't hide everything anymore
- composer.json upgrade version of Digitizer to 1.0.*
- Documentation of the JS-UI Generator (Form-Generator): https://github.com/eSlider/vis-ui.js
- Restructured `Installations-Dokumentation <installation.html>`_ and some changes (php-pear, assets-Verzeichnis, init:acl, openssl).
- Better documentation of the `Mapbender3 Templates <templates.html>`_
- Better documentation of the `Quickstart <quickstart.html>`_

**Known Issues:**

- After copying an application from Mapbender 3.0.4.x you have to set the layerset in the map/overview element. Please save the map and overview element beforehand.
- Regional Template removed


Milestone 3.0.5.0
-----------------

Release Date: 01.07.2015

For details have a look at:  https://github.com/mapbender/mapbender-starter/blob/develop/CHANGELOG.md

* **WMS reload:** WMS sources can now be reloaded if the structure has changed.

* **Digitizer:** The digitizer allows the editing of geometries and their attributes. Right now it needs access to the database where the editable tables are. The definition of the digitizer is done in YAML syntax. To provide an usable interface for the attributes, you can declare the form in your configuration file. The form supports different input fields (textboxes, checkboxes, date-pickers, and so on..), validation, tabs and it uses Bootstrap.

* **Print with legend:** The print element supports the print-out of the legend on a seperate page. This can be set with a checkbox.

* **Configurable layertree:** The layertree supports the usage of more than one layerset. You have to adjust the map element to define which layersets should be shown and the layertree element itself. The usage is documented `on the Layertree page <../bundles/Mapbender/CoreBundle/elements/layertree.html>`_.
  
* **Improved FeatureInfo dialog:** You can set a) the width and height of the FeatureInfo dialog, b) if the dialog should show the original format of the WMS and c) if it should only open if a valid entry is found (otherwise a messagebox is displayed). See the documentation of the `FeatureInfo Dialog <../bundles/Mapbender/CoreBundle/elements/feature_info.html>`_.

* **Mobile template:** A new modern mobile template is provided.

* **SASS Compiler:** Architectual changes are made at the SASS compiler which leads to a more performant interface.

* **Vendor Specific Parameters:** A WMS layer instance supports the definition of Vendor Specific Parameters that are added to the WMS request. You can define hard coded values or the user or group information of the logged-in user. See the documentation of `Vendor Specific Parameters <../book/quickstart.html#configure-your-wms>`_ for details.

* **Expanded functionality of HTML elements with a form-builder:** This approach is used in the Digitizer to provide the forms for attribute editing.

* **New button colletion:** The new buttons are based on a new font, the old buttons are available under the "FontAwesome" name.

* **Starting mapbender with URL parameters:** Mapbender3 can be started with URL parameters. See the documentation of `URL parameters <../bundles/Mapbender/CoreBundle/elements/map.html#controlling-by-url>`_.

* New translations for Portuguese and Russian.
  
* Symfony updated to 2.3.30.


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
