app/console Befehle
======================

Mapbender bietet Befehle, die über die Kommandozeile aufgerufen werden können. Einige der Befehle werden von den Symfony-Komponenten bereitgestellt, andere gehören zu Mapbender. 

Im Folgenden werden einige dieser Befehle vorgestellt. 

Achten Sie beim Ausführen der Befehle darauf, dass Sie sich im richtigen Verzeichnis befinden (oberhalb vom app-Verzeichnis)

* mapbender/application (bei Installation über GitHub)

* mapbender (bei der Paketinstallation)

    
Übersicht der Befehle
---------------------

  .. code-block:: yaml

    app/console  


Die Hilfe für jeden Befehl kann mit [Befehl] --help aufgerufen werden, z.B.:  

.. code-block:: yaml

    app/console mapbender:user:create --help
    

    

app/console mapbender:user:create 
-------------------------------------

Befehl zum Anlegen eines Benutzers über die Kommandozeile. 
Dabei sind die Angabe von Benutzername, Email und Passwort erforderlich. Der Benutzername und die Email müssen eindeutig sein.

.. code-block:: yaml

    app/console mapbender:user:create --help
    app/console mapbender:user:create --password <password> --email <email> <name>
    app/console mapbender:user:create --password mypassword123 --email max.mustermann@mapbender.org 'Max Mustermann' 
   
   
**Aktualisierung eines Benutzers**

Die Angaben zu einem Benutzer können aktualisiert werden.

Folgende Angaben können aktualisiert werden:

* E-Mail
* Passwort

Der Benutzername kann nicht verändert werden.

.. code-block:: yaml
   
    app/console mapbender:user:create --update --password <password> --email <email> <name>

    app/console mapbender:user:create --update --password mypassword8910 --email max.mustermann@mapbender.org 'Max Mustermann'
    

    
app/console mapbender:wms:validate:url 
-------------------------------------   

Befehl zur Prüfung der Erreichbarkeit der WMS-Datenquelle. Ist der Dienst erreichbar, werden die verfügbaren Layer aufgelistet. 

.. code-block:: yaml

    app/console mapbender:wms:validate:url "https://osm-demo.wheregroup.com/service?VERSION=1.3.0"
    
	WMS source loaded and validated
	Source describes 3 layers:
	* OpenStreetMap (WhereGroup)
	* OpenStreetMap
	* OpenStreetMap (grey scale)



app/console mapbender:source:rewrite:host 
------------------------------------------ 

Aktualisiert den Hostnamen in den Quell-URLs, ohne die Funktionen/Capabilities neu laden zu müssen. 

.. code-block:: yaml

    app/console mapbender:source:rewrite:host "https://osm-demo.wheregroup.com" "http://osm-demo.wheregroup.com" 
    
	3 modified urls in WMS source #5 / OpenStreetMap (OSM) Demo WhereGroup
	Summary:
	1 sources changed
	3 urls changed
	4 sources unchanged
	14 urls unchanged
    

app/console mapbender:config:check 
-----------------------------------

Der Befehl prüft die Konfiguration und gibt zur Information die Systemkonfiguration aus. Dadurch kann ermittelt werden, ob Abhängigkeiten nicht erfüllt werden.

.. code-block:: yaml

	app/console mapbender:config:check 


Es werden folgende Anforderungen überprüft und angezeigt:

* Datenbankverbindungen
* PHP-Version 
* Systemanforderungen 
* Asset-Ordner
* FastCGI
* Apache Modus (rewrite)
* PHP ini
* geladene PHP-Erweiterungen
* Zugriffserlaubnis auf Verzeichnisse


app/console cache:clear
------------------------

Der Befehl löscht das Cache-Verzeichnis für eine bestimmte Umgebung. 
Wird keine bestimmte Option angegeben, wird der Cache der dev-Umgebung geleert. 

Eventuell muss der Befehl mit root-Rechten (sudo) ausgeführt werden.
 
Dev-Umgebung:



.. code-block:: yaml

		app/console cache:clear --env=dev
        
		
Prod-Umgebung:


.. code-block:: yaml	

		app/console cache:clear --env=prod --no-debug
		



app/console server:run
------------------------

Der Befehl führt den von PHP eingebauten Webserver aus. Im Terminal erscheint eine Meldung, dass der Server läuft und zeigt die lokale Adresse an (http://127.0.0.1:8000). 
In diesem Modus kann lokal mit Mapbender gearbeitet werden.

Mit Control -C kann der Server wieder gestoppt werden. 



.. code-block:: yaml

	app/console server:run
	
	[OK] Server running on http://127.0.0.1:8000                                                                           
    // Quit the server with CONTROL-C. 
    


app/console server:start
------------------------

Der Befehl startet den von PHP eingebauten Webserver im Hintergrund. 

Im Terminal erscheint eine Meldung, dass der Server auf die angegebene Adresse hört (http://127.0.0.1:8000)


.. code-block:: yaml

	app/console server:start
	
	[OK] Web server listening on http://127.0.0.1:8000        


app/console server:stop
------------------------

Der Befehl stoppt den von PHP eingebauten Webserver im Hintergrund. Im Terminal erscheint eine Meldung, dass der Server mit angegebener Adresse gestoppt wurde (http://127.0.0.1:8000)


.. code-block:: yaml

	app/console server:stop
	
	

app/console server:status
-------------------------

Dieser Befehl gibt den Status des lokalen Webservers aus.


.. code-block:: yaml

	app/console server:status



app/console mapbender:database:upgrade 
--------------------------------------

Aktualisiert die Kartenelementkonfigurationen, falls neue vorhanden sind. 


.. code-block:: yaml

	app/console mapbender:database:upgrade 
	
	Updating map element configs
	Found 28 map elements
	28/28 [============================] 100%
	Updated 28 Map elements
	Exiting now



app/console doctrine:database:create 
-------------------------------------

Der Befehl wird einmalig bei der Installation verwendet und legt die Administrationsdatenbank für Mapbender an. Die Angabe zur Datenbankverbindung befindet sich in der parameters.yml-Datei.


.. code-block:: yaml

	app/console doctrine:database:create



app/console doctrine:schema:create 
-----------------------------------

Mit dem Befehl wird bei der Installation das Datenbankschema angelegt, d.h. es werden die von Mapbender benötigten Tabellen erstellt.


.. code-block:: yaml

	app/console doctrine:schema:create
	
	
app/console doctrine:schema:validate
---------------------------------------

Der Befehl wird einmalig bei der Installation verwendet. Dieser Befehl überprüft, ob der Aufbau der Datenbank korrekt und aktuell ist.


.. code-block:: yaml	

	app/console doctrine:schema:validate
	[Mapping]  OK - The mapping files are correct.


app/console fom:user:resetroot
-------------------------------

Mit diesem Befehl lässt sich der root-Account erstellen oder aktualisieren. Für die Erstellung müssen ein Benutzername, eine E-Mail und ein Passwort vergeben werden.

Bei der Aktualisierung erfolgt die eindeutige Zuordnung über die bereits vorhandene ID, deshalb können alle drei o.g. Parameter verändert werden. 


.. code-block:: yaml

	app/console fom:user:resetroot



app/console mapbender:user:list
-------------------------------

Dieser Befehl zeigt im Terminal alle vorhandenen Benutzer mit ihrer ID und ihrem Benutzernamen an sowie Datum und Uhrzeit ihrer Erstellung.


.. code-block:: yaml

	app/console mapbender:user:list
        
	User #3 name: al_bauer since 2019-10-14 12:10:44


app/console mapbender:version
-------------------------------

Der Befehl gibt die aktuelle Mapbender-Version aus.

.. code-block:: yaml

	app/console mapbender:version 
        
	Mapbender 3.0.8.4
 
	
app/console debug:config
------------------------

Mit diesem Befehl werden alle registrierten Bundles (Pakete) aufgelistet und, falls vorhanden, der Alias dazu genannt.

.. code-block:: yaml	

	app/console debug:config	



app/console debug:swiftmailer
-----------------------------

zeigt die/den konfigurierten Mailer an

.. code-block:: yaml

	app/console debug:swiftmailer 


app/console mapbender:print:queue:next
--------------------------------------

Der Druck in der Warteschlange ist standardmäßig deaktiviert, da er eine externe Integration erfordert. Druckaufträge können danach über die Kommandozeile gesteuert werden. Dafür muss in der parameters.yml-Datei folgender Parameter hinzugefügt und auf TRUE gesetzt werden:

.. code-block:: yaml

	mapbender.print.queueable

Weitere Informationen unter: https://github.com/mapbender/mapbender/pull/1070

Anschließend wird im Backend des Mapbenders der Druckassistent aktualisiert und es erscheinen zwei neue Zeilen, Modus und Warteschleife.

Modus wird auf "Warteschleife" gesetzt und Warteschleife auf "global", wenn davon auszugehen ist, dass die Druckaufträge für alle Anwender zugänglich sind. 

Im Backend erscheint dadurch der neue Reiter/Tab "Druckaufträge". Diese können durch folgende Befehle über die Kommandozeile gesteuert werden. 

.. code-block:: yaml

	app/console mapbender:print:queue:next
	
Es wird der nächste Druckauftrag ausgeführt, der in der Warteschleife steht. Für einen potenziell unendlich laufenden Prozess können folgende Optionen auf 0 gesetzt werden. 


.. code-block:: yaml

	app/console mapbender:print:queue:next --max-jobs=0 --max-time=0

Optional kann die Anzahl der Prozesse und die maximale Ausführungszeit limitiert werden.

* --max-jobs=MAX-JOBS
* --max-time=MAX-TIME  


app/console mapbender:print:queue:rerun 
---------------------------------------

 Dieser Befehl führt einen Druckwarteschlangenauftrag erneut aus. Die Angabe der ID ist dabei erforderlich.
 
.. code-block:: yaml

	app/console mapbender:print:queue:rerun 1
	
	Starting processing of queued job #1
	PDF for queued job #1 rendered to /data/mapbender/application/app/../web/prints/mapbender_20191104103745.pdf

	
	
app/console mapbender:print:queue:dumpjob 
------------------------------------------

Dieser Befehl gibt Druckaufträge in ein angegebenes Format (JSON oder yml) aus. Die ID des jeweiligen Druckauftrages ist für den Befehl erforderlich. Diese ID kann über die geöffnete Druckwarteschlange in der Mapbender-Anwendung ermittelt werden.

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
			"title": "Egal!"
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
----------------------------------

Mit diesem Befehl kann ein Druckauftrag aus einer Druck-Konfiguration heraus ausgeführt werden. Diese Konfiguration kann über app/console mapbender:print:dumpjob erstellt werden.


.. code-block:: yaml	

	app/console mapbender:print:runJob print_configuration.json /tmp/print.pdf
	

app/console mapbender:print:queue:repair 
-------------------------------------------

Wenn ein Druckauftrag in der Warteschlange einen Fehler aufweist oder abgestürzt ist, beispielsweise ein WMS-Dienst nicht erreichbar ist, kann der Druck nicht ausgeführt werden. 

Mit dem Befehl mapbender:print:repair wird der Status der Druckaufträge zurückgesetzt. Anschließend werden die Aufträge automatisch erneut ausgeführt.

.. code-block:: yaml

	app/console	app/console mapbender:print:repair 
	
	
	
app/console mapbender:print:queue:clean
---------------------------------------

Dieser Befehl löscht erfolgreich abgearbeitete Druckaufträge. Dazu zählen einerseits erstellte PDFs als auch dazugehörige Datenbankeinträge zu den Druckaufträgen. Beim Aufruf des Befehls kann die Angabe des Alters hinzugefügt werden, mit der Angabe 20 werden beispielsweise alle Aufträge gelöscht werden, die älter als 20 Tage sind.

.. code-block:: yaml	
	
	mapbender:print:queue:clean 20
	
	Print queue clean process started.
	Deleted 0 print queue item(s)



app/console mapbender:print:queue:gcfiles 
-----------------------------------------

gc steht für "garbage collection". gcfiles löscht entsprechend alle Druckaufträge, bei denen der Datenbankeintrag keine Referenz mehr zum Dateisystem hat. 
Dies geschieht zum Beispiel, wenn ein Auftrag in der Datenbank gelöscht oder der Dateipfad zum PDF nicht mehr aktuell ist. 

.. code-block:: yaml

	app/console mapbender:print:queue:gcfiles
	
	No unreferenced local files found


