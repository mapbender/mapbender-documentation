.. _applicationswitcher:

Application Switcher
********************

The Application Switcher provides the abilitiy to switch to other Mapbender application to the same extent, other portals or websites. 

The element provides placeholder, that can be used to define links.

The element can be defined in the toolbar oder footer or the sidepane. 

In the toolbar or footer it will be shown as selectbox.

.. image:: ../../../figures/applicationswitcher_selectbox.png
     :scale: 80

When you place the element in the sidepane you can choose from cards that are devided into groups.

.. image:: ../../../figures/applicationswitcher.png
     :scale: 80

You can switch from one application to another. The map extent will be preserved.

If you refer to protected applications, these will only be made available for selection
if they are activated for the logged-in user or anonymous user.

Configuration
=============

.. image:: ../../../figures/applicationswitcher_configuration.png
     :scale: 70

* **Title:** Title of the element. The title will be shown as tooltip on mouseover on the selectbox.
* **Open in new tab:** Define whether the new application should be opened in the same window (default) or in a new tab.
* **Configuration:** Define the applications that should be offered by the applications switcher. The configuration is done in YAML syntax.

You can only refer to an application without further parameter. Or you can define additional parameters.

* **title:** Define an alternative Title. If not defined the Title of the application will be used, if you refer to an existing mapbender application of your installation. (optional)
* **url:** You can add a link and refer to a Mapbender application, a website or an alternative portal (optional)
* **imgUrl:** Link to an image, that you would like to show (optional)
* **description:** Add more Information. It wil be show as tooltip (optional)
* **group:** Define a group. Applications with the same group will be shown in a section with the group title as heading (optional)

The following placeholder are defined and provide information for the actual extent. The placeholder can be used in the url definition:

* **%scale%:** scale denominator
* **%lat%:** latitude value of the center coordinate
* **%lon%:** longitude value of the center coordinate
* **%center_x%:** x value of the center coordinate in the actual used projection 
* **%center_y%:** y value of the center coordinate in the actual used projection 
* **%rotation%:** numeric value representing the rotation of the map
* **%srs%:** EPSG code 
* **%zoom%:** zoom factor 

You can also define a configuration that will add a WMS to your
 actual application. There are additional option that you have to define in the **add_wms** section.

* **add_wms:** defines action to add a WMS
* **mb_url:** refer to the WMS getcapabilities URL
* **mb_wms_merge:** adds the WMS only once, if WMS is already part of the application it will use the WMS which is there (default: 1)
* **mb_layer_merge:** activate the layers passed mb-wms-layers and do not disable the layers which are already active (default: 1)
* **mb_wms_layers:** defines the layers to be activated, _all activates all layers, default all layers are deactivated
* **mb_add_vendor_specific:** define a vendor specific that will be added to the requests
* **mb_infoformat:** defines the GetFeatureInfo format for the WMS (default: text/html)


Example configuration

.. code-block:: yaml

    mapbender_user: # switch to another application
    mapbender_user_basic:
      title: 'Mapbender User Basic'
      url: null
      img_url: null
      group: 'Mapbender Demos'
    mapbender_user_basic_with_zoom:
      title: 'external: open with zoom'
      url: 'https://schulung.foss.academy/mapbender/application/mapbender_user?#%zoom%@%lat%/%lon%r%rotation%@EPSG:%srs%'
      description: Link to an external application with zoom and rotation.
      group: 'External'
    external_dz_nrw:
      title: 'www.dz.nrw.de with srs scale center_x and center_y'
      url: 'https://www.dz.nrw.de/?lang=de&vm=3D&srs=%srs%&cam=%center_x%,%center_y%,%scale%,360,65,55'
      img_url: null
      description: Link to Digitaler Zwilling NRW (external application).      
      group: 'External'
    external_osm:
      title: 'OSM with lon & lat'
      url: 'https://www.openstreetmap.org/?#map=19/%lon%/%lat%'
      img_url: 'https://upload.wikimedia.org/wikipedia/commons/b/b0/Openstreetmap_logo.svg'
      description: Link to OpenStreetMap (external application). 
      group: 'External'
    link_mapbender:
      title: 'Link: mapbender.org'
      url: 'https://mapbender.org'
      img_url: 'https://doc.mapbender.org/_images/mapbender_logo_font.png' #'https://mapbender.org/fileadmin/mapbender/resources/images/startseite/mapbender-stadt-markierungen.jpg'
      description: Link to the Mapbender Documentation      
      group: 'Link external Website'
    link_fossgis:
      title: 'Link: fossgis.de'
      url: 'https://fossgis.de'
      img_url: 'https://www.fossgis.de/mediawiki/images/d/d3/FOSSGIS_Logo_RGB_100x45mm_600dpi.png'
      description: Link to FOSSGIS e.V.      
      group: 'Link external Website'
    mapbender_user_wms:
      title: 'WMS Mapbender User'
      description: 'Click to load the WMS'
      img_url: 'https://wms.wheregroup.com/cgi-bin/mapbender_user.xml?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Mapbender_User&format=image/png&STYLE=default'
      group: WMS Service
      add_wms:
        mb_url: 'https://wms.wheregroup.com/cgi-bin/mapbender_user.xml'
        mb_wms_merge: 0
        mb_layer_merge: 0
        mb_wms_layers: 'Mapbender_User,Mapbender_Names'
        mb_add_vendor_specific: bplan=123
        mb_infoformat: text/html



YAML-Definition
---------------

This template can be used to insert the element into a YAML application. Please note that you have to refer to the variables with double percentage signs (%%) in the url definition.

.. code-block:: yaml

    title: Choose an Application              # Text will be displayed as tooltip
    class: Mapbender\CoreBundle\Element\ApplicationSwitcher
    open_in_new_tab: true   # false/true open application in new tab
    applications:
      mapbender_user: # switch to another application
      mapbender_user_basic:
        title: 'Mapbender User Basic'
        url: null
        img_url: null
        group: 'Mapbender Demos'
      mapbender_user_basic_with_zoom:
        title: 'external Mapbender: open with zoom'
        url: 'https://schulung.foss.academy/mapbender/application/mapbender_user?#%%zoom%%@%%lat%%/%%lon%%r%%rotation%%@EPSG:%%srs%%'
        description: Link to an external application with zoom and rotation.              
        group: 'External'
      external_dz_nrw:
        title: 'www.dz.nrw.de with srs scale center_x and center_y'
        url: 'https://www.dz.nrw.de/?lang=de&vm=3D&srs=%%srs%%&cam=%%center_x%%,%%center_y%%,%%scale%%,360,65,55'
        img_url: null
        description: Link to Digitaler Zwilling NRW (external application).         
        group: 'External'
      external_osm:
        title: 'OSM with lon & lat'
        url: 'https://www.openstreetmap.org/?#map=19/%lon%/%lat%'
        img_url: 'https://upload.wikimedia.org/wikipedia/commons/b/b0/Openstreetmap_logo.svg'
        description: Link to OpenStreetMap (external application).         
        group: 'External'
      mapbender_user_wms:
        title: 'WMS Mapbender User'
        description: 'Click to load the WMS'
        img_url: 'https://wms.wheregroup.com/cgi-bin/mapbender_user.xml?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Mapbender_User&format=image/png&STYLE=default'
        group: WMS Service
        add_wms:
          mb_url: 'https://wms.wheregroup.com/cgi-bin/mapbender_user.xml'
          mb_wms_merge: 0
          mb_layer_merge: 0
          mb_wms_layers: 'Mapbender_User,Mapbender_Names'
          mb_add_vendor_specific: bplan=123
          mb_infoformat: text/html

