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
                                        # idloader - lädt die Konfiguration per ID beim Start der Applikation z.B. ?wmcid=<wmcid>
                                        # listloader - lädt die Konfiguration aus einer Liste
                                        # wmcloader - lädt die Konfiguration aus einer Datei
   keepSources: false                   # definiert, was mit den Diensten in der Applikation geschehen soll
                                        # Standard ist false (no)
                                        # BaseSources - behält nur die als BaseSource markierten Dienste in der Anwendung
                                        # AllSources - behält die Dienste, die bereits geladen sind, in der Anwendung
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


Kontrolle über den Aufruf
=====================================

WMC per ID laden
------------------

Im Element WMC Loader muss die Option *Id Loader* aktiviert sein, um das Laden eines WMCs über die URL zu erlauben.

Beim Aufruf der Anwendung wird die <wmcid> über den Parameter *wmcid* der URL angefügt:


.. code-block:: php

  ?wmcid=<wmcid>



