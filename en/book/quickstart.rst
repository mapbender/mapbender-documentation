:Author: OSGeo-Live
:Author: Astrid Emde
:Version: osgeo-live7.0
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)
:Thanks: mapbender-user list

.. image:: ../../../../_static/mapbender3_logo.png
  :scale: 100 %
  :alt: project logo
  :align: right

########################
Mapbender Quickstart 
########################

Mapbender is a web based geoportal framework to publish, register, view, navigate, monitor and grant secure access to spatial data infrastructure services. 

Management interfaces empower administrators who need to maintain and categorize map and feature services and grant access to individuals, groups and other services. 

Mapbender3 is the next version in the Mapbender series. It is rewritten from the ground up, using modern web technologies. The foundation is laid by Symfony 2, the brand-new version of the successful Symfony PHP web application framework.

On the client-side expect to find OpenLayers and jQuery (UI) nicely glued together by MapQuery.

With this new code base we will continue the Mapbender idea of being a Geoportal Framework:
  * Applications can be setup and configured right from within the browser
  * Services like WMS can be managed inside a service repository and linked to applications
  * Rights management are easy to maintain, for individual users and groups, whether you store them inside the database or in an LDAP. 

You will need nothing but a standard web browser for this quickstart.

This Quick Start describes how to:

  * start Mapbender
  * create an application 
  * load a Web Map Service (OGC WMS)
  * configure WMS
  * create an individual application
  * create a user and a group and assign applications to them

Start Mapbender
================================================================================

#. Choose  :menuselection:`Mapbender` from the start menu or visit http://localhost/mapbender3/app.php


#. The application will take a few moments to start up

If you have any difficulties running Mapbender, please check whether your Apache web server and your PostgreSQL database are running.


Start Mapbender in the developer mode app_dev.php
=================================================
Symfony offers a developer mode with lot of information about your application (logging, exceptions, database queries, memory usage, time and more). This mode is only available from localhost.

  .. image:: figures/mapbender3_app_dev.png
     :scale: 80

#. Start the developer mode: http://localhost/mapbender3/app_dev.php

#. Have a look at the information that is offered in the developer mode.

  .. image:: figures/mapbender3_app_dev_controller.png
     :scale: 80


Welcome page
================================================================================

#. The Welcome page lists applications that are public and can be used by all users. The applications are listed with a litte screenshot, a title and a description.

#. You can open an application by click on the title or the start button.

#. Before you can administrate with Mapbender you have to login to get access to the administration.

#. Click on the Mapbender logo at the left to open the login page.

#. You can login with the user that was generated on installation. It can be :guilabel:`root` and password :guilabel:`root` (This is the default user and password that you get after installation of Mapbender on OSGeo-Live. Please change the root password if you want to run a productive environment. Please don't delete the user :guilabel:`root`.).
  
  .. image:: figures/mapbender3_welcome.png
     :scale: 80

After successful login you are directed to the :guilabel:`Mapbender administration`.



Application overview
================================================================================
After the login you are directed to the :guilabel:`Application overview` with a list of applications you are allowed to access.

The Application overview provides the following functionality:

 * title and description
 * link to the application
 * icon to publish/unpublish the application
 * Button to edit the application 
 * Button to delete the application 
 * Button to create a new application 

  .. NOT IMPLEMENTED YET: In Mapbender you have template applications, that you can use to set up your own applications.

  .. image:: figures/mapbender3_application_overview.png
     :scale: 80


Create an individual application
================================================================================

Create a new application by providing basic information about your application. After that you use the edit mode to add elements, layers and security.

#. choose :menuselection:`Applications --> Button Create new application`

#. define a Title and description for your application

#. define an URL title which will be used in the URL to open te application. It can be the same as the title

#. choose a template from the list of templates. This will define the style of your application

#. choose the button **Create** to create the application

#. go to the link :menuselection:`Application Management --> Edit application elements` and select the new application

#. your application is set up. Now you need a WMS to be displayed in your application. This will be described in the section **WMS Management**.

  .. image:: figures/mapbender3_create_application.png
     :scale: 80

..
  NOT IMPLEMENTED YET
  Copy or rename an application
  ================================================================================
 You also can create a new application by copying an existing application. Go t  o :menuselection:`Application Management --> Rename/copy application`, choose the application you want to copy and define a name for the new application. This functionality not only copies the application, it also copies the services of the application and the user/groups (optional). That means that the new application already has map services and the user and groups which have access to the copied application will have access to the new application too.

Delete an application
================================================================================
You can delete an application from the :menuselection:`Applications` with the Button Delete. Only the application is deleted, not the services which were part of the application. 
You are not allowed to delete applications which also belong to other users.

..
  NOT IMPLEMENTED YET
  Export an application
  ================================================================================
  You can export an application as SQL with :menuselection:`Application Management --> Export  application (SQL)`. The SQL contains all the definitions of the application elements and can be imported in another Mapbender installation. 

  .. tip:: The export of an application does not contain the service information and the informations about user and group access.



Management of Data Sources
=================================
Mapbender can handle different Services like OGC WMS or OGC WMTS or OGC WFS. Every Service has to be handled differently. The administration provides an administration interface for every source (at the moment only WMS). 

Service Repository overview
=============================

#. Go to :guilabel:`Services` and have a look at the Service repository.

#. You get an overview on the Sources that are loaded in your Mapbender.

#. Type (f.e WMS, WMTS), Title, Description offer first information about the services.

#. On click on the button :menuselection:`View` you get further information about the source.

#. With the button :menuselection:`Delete` you can delete the source from your repository.


Loading Web Map Services
================================================================================
You can load OGC Web Map Services (WMS) to your application.

A WMS returns an XML-file when the getCapabilities document is requested. This information is parsed by Mapbender and Mapbender gets all the necessary information about the service from this XML

.. tip:: You should first check the Capabilities document in your browser before you try to load it with Mapbender

#. Choose :menuselection:`Services --> Button Add`. Link to the WMS getCapabilities URL in the text field :menuselection:`Originurl` 

#. Enter username and password if your service needs authentication.

#. Hit **Load** to load the Service to the repository.

#. After successfull registration of the service Mapbender will display an overview on the information that was provides by the service.

  .. image:: figures/mapbender3_load_wms.png
     :scale: 80


Here are some example WMS:

Germany demo 

http://wms.wheregroup.com/cgi-bin/germany.xml?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS 

WhereGroup OSM WMS (see also http://www.wheregroup.com/de/osmwms)

http://osm.wheregroup.com/cgi-bin/osm_basic.xml?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.1.1

Omniscale OSM WMS (see also http://osm.omniscale.de/)
http://osm.omniscale.net/proxy/service?
 

.. NOT YET IMPLEMENTED
  .. tip:: Create a container application and upload every WMS just once to this container application. You can transfer the WMS from this container to other aplications. When you update the WMS the possible changes will appear in all applications that contain this WMS. You easily can copy a WMS from one to another application with the menu entry *Link WMS to application*.


Add Service to Application
==========================
After the successfull upload of a WMS you want to add your WMS to an application.

#. Choose :menuselection:`Applications --> Layers--> Button Add Source`. 

#. Select a Source and add it to your application.

#. You can change the order of the Services in your application by drag & drop.
	
  .. image:: figures/mapbender3_add_source_to_application.png
     :scale: 80

Configure your WMS
================================================================================
You can configure the WMS for your specific application. Maybe you don't want to provide all layers or you want to change the order or titles of the layer or disable the feature info or change the maxscale for a layer.

#. Choose :menuselection:`Applications --> Layers--> Button Edit Source Instance` to configure a the Instance.

#. You see a table with the layers of the Service. 

#. You can change the order of the layers via drag & drop

.. image:: figures/mapbender3_wms_application_settings.png
  :scale: 80

Service configuration

* format - choose the format for getMap-Requests
* infoformat - choose the format for getFeatureInfo-Requests
* exceptionformat - choose the format for exceptions
* opacity - choose opacity in percent
* tiled - you can request a WMS in tiles, default is not tiled


Layer configuration

* on/off - enable/disable a layer for this individual application
* sel - selectable in geodata explorer
* sel_default - layer is active when the application starts
* info / info default - layer provides feature info requests, info default activates the feature info functionality
* minscale / maxscale - the scale range in which the layer should be displayed, 0 means no scale limitation
* style - if a WMS provides more than one style you can choose a different style than the default style
* prio - defines the order in which the layer are drawn


Add Elements to your application
================================
Mapbender offers a set of elements. You can add the elements to your application. You have different regions (top, content, footer) to which you can add elements.

  .. image:: figures/mapbender3_add_element.png
     :scale: 80

#. Choose : menuselection:`Applications --> Elements--> Button +` to get an overview over the elements Mapbender3 provides.

#. Choose an element from the list.

#. Notice that you have different areas in your application. Make sure to add the element to a regio that makes sense.

#. Have a look at your application. Open your application from :menuselection:`Applications --> Applications Overview`

Now you should get an idea how easy it is to change a Mapbender application without changes in the code. 

  .. image:: figures/mapbender3_application_elements.png
     :scale: 80

.. NOT IMPLEMENTED YET 
 When you select an element for example **map** you see that the element has a set of attributes. These attributes are HTML attributes. By defining a Mapbender element you define an HTML element. On start of your application Mapbender will create an HTML page from all defined elements.

Examples for elements Mapbender3 offers:

* About Dialog
* Activity Indicator
* Button
* Coordinates Display
* Copyright
* Feature Info
* Legend
* Map
* Ruler Line/Area
* Scale Selector
* SRS Selector
* Table of Content
* Navigation Bar

You find detailed information on every elements at the http://doc.mapbender3.org/en/bundles/Mapbender/CoreBundle/index.html.

.. Link does not work like this: doc:`Mapbender3 element documentation <bundles/Mapbender/WmsBundle/index>`.


Try it yourself
================================================================================

* add a map to the content of your application
* add a table of content to the content of your application
* add a button that opens the table of content to the top of your application
* add the navigation to the content
* add a copyright and change the copyright text
* add a SRS Selector to the footer


User and group management
=========================
An access to Mapbender requires authentication. Only public applications can be used by everyone. 

A user has permissions to access one or a set of applications and services.

.. NOT IMPLEMENTED YET
  There is no inherent difference between roles like :guilabel:`guest`, :guilabel:`operator` or :guilabel:`administrator`. The :guilabel:`role` of a user depends on the functionality and services the user has access through his applications.


Create a user
================================================================================

#. To create a user go to :guilabel:`Users -> Button Create new user`.

#. Choose a name and a password for your user. 

#. Provide an email address for the user.

#. Save your new user.

.. image:: figures/mapbender3_create_user.png
     :scale: 80 


Create a group
================================================================================
#. Create a group by :menuselection:`Users --> Groups --> Button Create new group`. 

#. Define a name and a description for your group.

#. Save your new group.


Assign applications to user/group
================================================================================

#. Assign a user to a group by :menuselection:`Users --> Group --> Edit your Group`. 

#. Choose one or more users you want to add to the group at :menuselection:`Users`.

#. Assign a user by :menuselection:`Users --> Users --> Edit --> Groups` to a group. 

  .. image:: figures/mapbender3_assign_user_to_group.png
     :scale: 80
 

Roles
=====
Mapbender3 provides different roles you can assign to a group.

* Can administrate everything (super admin) 
* Can administrate users & groups 
* Can administrate applications 

#. Assign roles to a group by :menuselection:`Users --> Group --> Edit your Group --> Roles`.

  .. image:: figures/mapbender3_roles.png
     :scale: 80 


Assign an Application to a User/Group
======================================
#. Edit your application by :menuselection:`Applications --> Edit`

#. Choose :menuselection:`Security`

#. Publish/unpublish your application

#. Set permission like View Edit Delete Undelete Operator Master Owner 

#. Assign an application to a user/group

#. Test your configuration!

#. Logout from Mapbender by :menuselection:`Logout`.

#. Login as the new user

  .. image:: figures/mapbender3_security.png
     :scale: 80


Things to try
================================================================================

Here are some additional challenges for you to try:

#. Try to load some WMS in your application. Try to configure your WMS.

#. Try to create an individual application.


What Next?
================================================================================

This is only the first step on the road to using Mapbender3. There is a lot more functionality you can try.

Mapbender Project home
htp://mapbender.org

Mapbender3 Webside

  http://mapbender3.org/

You find tutorials at

  http://doc.mapbender3.org
  http://api.mapbender3.org


Get to know Mapbender on 
	
	http://projects.mapbender.osgeo.org

Get involved in the project

	http://www.mapbender.org/Community
