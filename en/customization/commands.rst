.. _commands:

app/console commands
====================

Mapbender provides commands that can be executed via the command line. Some of the commands are provided by the Symfony components, others belong to Mapbender. 

Some useful commands are described in the following document.

Make sure you are in the correct directory (above the app directory)

* mapbender/application (installation via GitHub)

* mapbender (installation via package)

    
Help command
------------

.. code-block:: yaml

    app/console  


The parameter --help displays the help message for every command for example:   

.. code-block:: yaml

    app/console mapbender:user:create --help
   

.. _app_command_export_import_clone:

Application Export, Import & Cloning
------------------------------------

app/console mapbender:application:export 
****************************************

You can export an application as JSON- or YAML-file. In the command you have to add the Url title (slug) of the application and define the export file.

.. code-block:: yaml

   app/console mapbender:application:export mapbender_user_db --format=json > export.json


app/console mapbender:application:import
****************************************

You can import an application from a JSON or YAML-file. Mapbender will automatically choose a new name if the name already excists.  

.. code-block:: yaml
   
   app/console mapbender:application:import export.json
    
    Imported 1 applications
    * mapbender_user_db_imp2


app/console mapbender:application:clone
***************************************

You can clone an existing application in the Application backend. This will create a new application with a *_imp* suffix as application name.
In the example below, the name of the new application becomes `mapbender_user_yml_imp1`.

.. code-block:: bash

	app/console mapbender:application:clone mapbender_user_yml


User administration
--------------------

app/console mapbender:user:create 
*********************************

Command to create a new user on the command line. 
User name, email and password are mandatory. User name and email have to be unique.
 

.. code-block:: yaml

    app/console mapbender:user:create --help
    app/console mapbender:user:create --password <password> --email <email> <name>
    app/console mapbender:user:create --password mypassword123 --email max.mustermann@mapbender.org 'Max Mustermann' 
   
   
**Update user settings**

Information for a user can be updated.

Following information can be updated:

* email
* password

The user name cannot be changed.

.. code-block:: yaml
   
    app/console mapbender:user:create --update --password <password> --email <email> <name>

    app/console mapbender:user:create --update --password mypassword8910 --email max.mustermann@mapbender.org 'Max Mustermann'
    

app/console fom:user:resetroot
******************************

Command to create or update the root account. User name, email and password must be assigned for creation.

During the update, the unique assignment is made via the already existing ID, therefore all three parameters mentioned above can be changed.  


.. code-block:: yaml

	app/console fom:user:resetroot


.. code-block:: yaml

	app/console fom:user:resetroot --username="root" --password="root" --email="root@example.com"



app/console mapbender:user:list
*******************************

Command to list all existing users with their ID and user name and the time of creation.


.. code-block:: yaml

	app/console mapbender:user:list
        
	User #3 name: max_mustermann since 2019-10-14 12:10:44
    
    
Database
---------
    
app/console mapbender:database:upgrade 
**************************************

Command to update the Mapbender database. 


.. code-block:: yaml

	app/console mapbender:database:upgrade 
	
	Updating map element configs
	Found 28 map elements
	28/28 [============================] 100%
	Updated 28 Map elements
	Exiting now



app/console doctrine:database:create 
************************************

The command is used only once during installation and creates the administration database for Mapbender. The database connection can be found in the parameters.yml file. 


.. code-block:: yaml

	app/console doctrine:database:create



app/console doctrine:schema:create 
**********************************

The command is used only once during installation and creates the database schema, which means that the tables required by Mapbender are created.


.. code-block:: yaml

	app/console doctrine:schema:create
	
	
app/console doctrine:schema:validate
************************************

Validate whether that the database is up-to-date.


.. code-block:: yaml	

	app/console doctrine:schema:validate
	[Mapping]  OK - The mapping files are correct.


Print
-----

app/console mapbender:print:queue:next
**************************************

The queued print is disabled by default because it requires some external integration setup. To run print jobs via the command line, the following parameter must be added to the parameters.yml file and set to TRUE to enable queued printing.

.. code-block:: yaml

	mapbender.print.queueable: true

Read more about the general characteristics of queued print at :ref:`queued_print`. Also `here <https://github.com/mapbender/mapbender/pull/1070>`_


The print assistant is then updated in the backend of Mapbender and two new lines appear: mode and queue. 
Mode is set to "queue" and queue is set to "global", if the print jobs are expected to be accessible to all colleagues. 
The new tab "Recent jobs" (which shows your scheduled print jobs) appears in the print client pop-up window. 

To run the jobs the following commands can be used.


.. code-block:: yaml		

	app/console mapbender:print:queue:next
	
The command mapbender:print:queue:next executes the next print job in the queue. For a potentially infinite process, the following options can be set to 0.


.. code-block:: yaml

	app/console mapbender:print:queue:next --max-jobs=0 --max-time=0

Optionally you can set a limit for the number of jobs to process and the maximum time for a job.  

* --max-jobs=MAX-JOBS
* --max-time=MAX-TIME  


app/console mapbender:print:queue:rerun 
***************************************

This command reruns a print queue job. The ID for the job must be set. 

.. code-block:: yaml

	app/console mapbender:print:queue:rerun 1
	
	Starting processing of queued job #1
	PDF for queued job #1 rendered to /data/mapbender/application/app/../web/prints/mapbender_20191104103745.pdf

	
	
app/console mapbender:print:queue:dumpjob 
*****************************************

This command dumps the queued print job from the database to JSON or YAML. The ID of the print job is required. This ID can be determined from the open print queue in the Mapbender application.

.. code-block:: yaml

	app/console mapbender:print:queue:dumpjob [options] [--] <id>
    
    app/console mapbender:print:queue:dumpjob 2 > print_configuration.json
	
	app/console mapbender:print:queue:dumpjob 2 
    {
        "template": "a4portrait",
        "quality": "288",
        "scale_select": "25000",
        "rotation": "-20",
        "extra": {
            "title": "My Title"
        },
        "layers": {
            "0": {
                "type": "wms",
                "sourceId": "8",
                "url": "https:\/\/osm-demo.wheregroup.com\/service?_SIGNATURE=31%3AIHZNT0zPZhFG95dN3QOzsizaDwA&TRANSPARENT=TRUE&FORMAT=image%2Fpng&VERSION=1.3.0&EXCEPTIONS=INIMAGE&SERVICE=WMS&REQUEST=GetMap&STYLES=&LAYERS=osm&_OLSALT=0.3940783483836241&CRS=EPSG%3A25832&BBOX=363375.30907721,5626747.0157598,368124.31589362,5620823.2546257&WIDTH=512&HEIGHT=512",
                "minResolution": null,
                "maxResolution": null,
                "order": 0,
                "opacity": 1,
                "changeAxis": false
            },
            "1": {
                "type": "wms",
                "sourceId": "7",
                "url": "https:\/\/wms.wheregroup.com\/cgi-bin\/mapbender_user.xml?_SIGNATURE=26%3Atq6ae-UqhnZLMjiQlLrj-wCHiOI&TRANSPARENT=TRUE&FORMAT=image%2Fpng&VERSION=1.3.0&EXCEPTIONS=INIMAGE&SERVICE=WMS&REQUEST=GetMap&STYLES=&LAYERS=Mapbender_User&_OLSALT=0.6831931928241708&CRS=EPSG%3A25832&BBOX=363375.30907721,5626747.0157598,368124.31589362,5620823.2546257&WIDTH=2400&HEIGHT=1141",
                "minResolution": null,
                "maxResolution": null,
                "order": 0,
                "opacity": 0.85,
                "changeAxis": false
            },
            "2": {
                "type": "wms",
                "sourceId": "7",
                "url": "https:\/\/wms.wheregroup.com\/cgi-bin\/mapbender_user.xml?_SIGNATURE=26%3Atq6ae-UqhnZLMjiQlLrj-wCHiOI&TRANSPARENT=TRUE&FORMAT=image%2Fpng&VERSION=1.3.0&EXCEPTIONS=INIMAGE&SERVICE=WMS&REQUEST=GetMap&STYLES=&LAYERS=Mapbender_Names&_OLSALT=0.6831931928241708&CRS=EPSG%3A25832&BBOX=363375.30907721,5626747.0157598,368124.31589362,5620823.2546257&WIDTH=2400&HEIGHT=1141",
                "minResolution": null,
                "maxResolution": null,
                "order": 1,
                "opacity": 0.85,
                "changeAxis": false
            }
        },
        "width": 1920,
        "height": 913,
        "center": {
            "x": 365749.81248542,
            "y": 5623785.1351928
        },
        "extent": {
            "width": 4749.006816409994,
            "height": 5923.761134099215
        },
        "overview": {
            "layers": {
                "0": "https:\/\/osm-demo.wheregroup.com\/service?_signature=31%3AIHZNT0zPZhFG95dN3QOzsizaDwA&TRANSPARENT=TRUE&FORMAT=image%2Fpng&VERSION=1.3.0&EXCEPTIONS=INIMAGE&SERVICE=WMS&REQUEST=GetMap&STYLES=&LAYERS=osm&CRS=EPSG%3A25832&BBOX=350757.32820012,5616536.5348653,377637.46662208,5629318.6006879&WIDTH=250&HEIGHT=125"
            },
            "center": {
                "x": 364197.3974111,
                "y": 5622927.5677766
            },
            "height": 78125,
            "changeAxis": false
        },
        "mapDpi": 90.714,
        "extent_feature": {
            "0": {
                "x": 362505.8322437394,
                "y": 5625755.14826519
            },
            "1": {
                "x": 366968.4389051802,
                "y": 5627379.404257199
            },
            "2": {
                "x": 368994.48453732743,
                "y": 5621812.889632087
            },
            "3": {
                "x": 364531.877875887,
                "y": 5620188.63364008
            },
            "4": {
                "x": 362505.8322437394,
                "y": 5625755.14826519
            }
        },
        "userId": null,
        "userName": null,
        "legendpage_image": {
            "type": "resource",
            "path": "images\/legendpage_image.png"
        }
    }

app/console mapbender:print:runJob
**********************************

Command to run a print job from a saved job definition. The JSON file created with the previously described command (app/console mapbender:print:dumpjob) will create a pdf print output.
		

.. code-block:: yaml	

	app/console mapbender:print:runJob print_configuration.json /tmp/print.pdf
	

app/console mapbender:print:queue:repair 
****************************************

If a print job in the queue has crashed, e.g. a WMS service is not accessible, printing cannot be performed. 
The command resets the status of the print jobs so that they can be executed again.  
	

.. code-block:: yaml		

	app/console mapbender:print:queue:repair 
	
	
app/console mapbender:print:queue:clean
***************************************

This command purges old jobs from the print queue (database and files). This includes created PDFs as well as corresponding database entries for the print jobs which are listed in the table called "mb_print_queue". With the command the expiring age can be set, for example, 20 can be used to delete all jobs older than 20 days.

.. code-block:: yaml	
	
	app/console mapbender:print:queue:clean 20
	
	Print queue clean process started.
	Deleted 0 print queue item(s)



app/console mapbender:print:queue:gcfiles 
*****************************************

gcfiles means "garbage collection files". This command deletes unreferenced files from print queue storage path. This can happen, for example, if a job is deleted from the database or the file path to the PDFs is no longer up-to-date.

.. code-block:: yaml

	app/console mapbender:print:queue:gcfiles
	
	No unreferenced local files found


Mailer
------

app/console debug:framework.mailer
**********************************

Command displays the configured mailer(s)

.. code-block:: yaml

	app/console debug:framework.mailer 

   
Server
------
 
app/console server:run
**********************

This command runs the PHP's built-in web server. The terminal displays that the server is running on the given local address (http://127.0.0.1:8000). 
In this mode you can work locally with Mapbender.

Quit the server with CONTROL-C. 



.. code-block:: yaml

	app/console server:run
	
	[OK] Server running on http://127.0.0.1:8000                                                                           
    	// Quit the server with CONTROL-C. 
    


app/console server:start
************************

The command starts the PHP's built-in web server in the background. 

In the terminal appears a message saying that the web server is listening on the displayed address (http://127.0.0.1:8000)


.. code-block:: yaml

	app/console server:start
	
	[OK] Web server listening on http://127.0.0.1:8000        


app/console server:stop
***********************

The command stops the PHP's built-in web server. A message appears in the terminal that the server with this specified address was stopped (http://127.0.0.1:8000).


.. code-block:: yaml

	app/console server:stop
	
	

app/console server:status
*************************

Outputs the status of the built-in web server for the given address.


.. code-block:: yaml

	app/console server:status
    
 
Clear cache 

app/console cache:clear
***********************

The command clear the cache directory.
 
Dev:



.. code-block:: yaml

		app/console cache:clear --env=dev
        
		
Prod:


.. code-block:: yaml	

		app/console cache:clear --env=prod --no-debug
        
    
WMS Services
------------

app/console mapbender:wms:add
***********************************

Adds a new WMS Source to your Mapbender Service repository.

.. code-block:: yaml

    app/console mapbender:wms:add https://osm-demo.wheregroup.com/service?VERSION=1.3.0&Service=WMS&request=getCapabilities
    
    * <empty name> OpenStreetMap (WhereGroup)
    * * osm OpenStreetMap
    * * osm-grey OpenStreetMap (grey scale)
    Saved new source #76


app/console mapbender:wms:parse:url
***********************************

Command to parse a GetCapabilities document by url. The command can be used to validate a WMS Url.

.. code-block:: yaml

    app/console mapbender:wms:parse:url --validate https://osm-demo.wheregroup.com/service?VERSION=1.3.0&Service=WMS&request=getCapabilities


app/console mapbender:wms:reload:file
*************************************

Command to reload (update) a WMS source from given file.

.. code-block:: yaml

   app/console mapbender:wms:reload:url 76 /var/www/html/service.xml


The following additional options are possible:

* --deactivate-new-layers  If set, newly added layers will be deactivated in existing instances. Deactivated layers are not visible in the frontend.
* --deselect-new-layers    If set, newly added layers will be deselected in existing instances. Deselected layers are not visible on the map by default, but appear in the layer tree and can be selected by users.


app/console mapbender:wms:reload:url
************************************

Command to reload (update) a WMS source from given url.

.. code-block:: yaml

   app/console mapbender:wms:reload:url 76 https://osm-demo.wheregroup.com/service?VERSION=1.3.0&Service=WMS&request=getCapabilities


The following additional options are possible:

* --user=USER              Username (basicauth) [default: ""]
* --password=PASSWORD      Password (basic auth) [default: ""]
* --deactivate-new-layers  If set, newly added layers will be deactivated in existing instances. Deactivated layers are not visible in the frontend.
* --deselect-new-layers    If set, newly added layers will be deselected in existing instances. Deselected layers are not visible on the map by default, but appear in the layer tree and can be selected by users.


app/console mapbender:wms:show
******************************

Command to displays layer information of a persisted WMS source. You have to parse the ID of the WMS Source to get the information.

.. code-block:: yaml

   app/console mapbender:wms:show 76
   
     Source describes 3 layers:
     * <empty name> OpenStreetMap (WhereGroup)
     * * osm OpenStreetMap
     * * osm-grey OpenStreetMap (grey scale)



app/console mapbender:wms:validate:url 
**************************************

Command to check the accessibility of the WMS data source. The available layers are listed, if the service is accessible. 

.. code-block:: yaml

    app/console mapbender:wms:validate:url "https://osm-demo.wheregroup.com/service?VERSION=1.3.0"
    
	WMS source loaded and validated
	Source describes 3 layers:
	* OpenStreetMap (WhereGroup)
	* OpenStreetMap
	* OpenStreetMap (grey scale)
    
    
Other
-----

app/console mapbender:source:rewrite:host 
*****************************************

Command to update the host name in the source URLs. Like this it is not necessary to reload Service capabilities.

.. code-block:: yaml

    app/console mapbender:source:rewrite:host "https://osm-demo.wheregroup.com" "http://osm-demo.wheregroup.com" 
    
	3 modified urls in WMS source #5 / OpenStreetMap (OSM) Demo WhereGroup
	Summary:
	1 sources changed
	3 urls changed
	4 sources unchanged
	14 urls unchanged
    

.. _mapbender_config_check:

app/console mapbender:config:check 
**********************************

Command to check the system configuration and mapbender requirements. Useful command to determine whether dependencies are compliant and database access works.

.. code-block:: yaml

	app/console mapbender:config:check 


.. hint:: Please note that config:check will use the php-cli version. The settings may be different from your webserver PHP settings. Please use php -r 'phpinfo();' to show your PHP webserver settings.


The following requirements are checked and displayed:

* Databse connections
* PHP Version 
* System requirements 
* Asset Folders
* FastCGI
* Apache modus (rewrite)
* PHP ini
* loaded PHP extensions
* Directory permissions

app/console mapbender:version
*****************************

The command outputs the current version of Mapbender.

.. code-block:: yaml

	app/console mapbender:version
	 
	Mapbender 3.3.4
 
	
app/console debug:config
************************

Command lists all registered bundles (packages) and, if available, their aliases.
 
.. code-block:: yaml		

	app/console debug:config	
