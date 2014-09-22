.. _wmc_loader:

WMC Loader (WMC laden)
***********************

Mapbender kann Konfigurationen speichern (siehe WMC Editor). Diese Konfigurationen  mit dem Element WMC-Lader geladen werden. 

Sie können den WMC-Lader ihrer Applikation als Selektbox oder als Button, der einen Dialog öffnet, hinzufügen.

Wenn Sie eine Konfiguration auswählen, werden die Dienste der Konfiguration in Ihrer vorhandenen Applikation zusammengefügt.



Konfiguration
=============

.. image:: ../../../../../figures/wmc_loader_configuration.png
     :scale: 80

     
Das Element kann als Selektbox oder als Dialog konfiguriert werden. Wenn das Element als Dialog verwendet wird, wird ein Button benötigt. Siehe unter :ref:`button_de` für die Konfiguration.
     

YAML-Definition:

.. code-block:: yaml

   title: WMC Loader
   tooltip: 'Load configuration'        # Text des Tooltips
   target: map                          # Name des Kartenelements 
   components:  ['idloader', 'listloader', 'wmcloader'] # Komponenten:
                                        # idloader (läd die Konfiguration per ID beim Start der Applikation), 
                                        # listloader (läd die Konfiguration von einer Liste), 
                                        # wmcloader (läd die Konfiguration von einer Datei
   keepSources: false                   # behält die Dienste, die bereits geladen sind, in der Applikation.
                                        # Standard ist false
   keepExtent: false                    # behält den aktuellen Extent, Standard ist false 
                                        # (erscheint im Extent der Konfiguration)


Class, Widget & Style
==============

* Class: Mapbender\\WmcBundle\\Element\\WmcLoader
* Widget: <Put Widget name here>
* Style: <Put name of css file here>


HTTP Callbacks
==============


<action>
--------------------------------



JavaScript API
==============


<function>
----------


JavaScript Signals
==================

<signal>
--------


Controlling by URL
==================

WMC per ID laden
------------------

Im Element WMC Loader muss die Option *Id Loader* aktiviert sein, um das Laden eines WMCs über die URL zu erlauben.

Beim Aufruf der Anwendung wird die <wmcid> über den Parameter *wmcid* der URL angefügt:


.. codeblock
  ?wmcid=<wmcid>



