.. _gpspostion:

GPS Position
************

This element provides a button to navigate to your current position and display a symbol at that position. The scale will not be changed until you activate ``zoom to accuracy (zoom to accuracy on first position)``.

The element is built upon the `Geolocation-API <https://www.w3.org/TR/geolocation/>`_ by the W3C. To validate that your browser supports this functionality please take a look at the `Can I Use <http://caniuse.com/#feat=geolocation>`_ page. The element uses the ``High Accuracy Parameter`` that forces the positioning via GPS. If your device is shipped with a GPS-receiver and if it is activated, the positioning is more accurate. Otherwise the WIFI access points are used for positioning.

The midpoint shows the probable position of the device, the outer circle the accuracy of the positioning, that means the region where the position is probably to find.

Compatibility: Internet Explorer and MS Edge deliver without a GPS-reciever at the machine imprecise information. This behaviour is also observable with other applications.

.. image:: ../../../figures/gps_position.png
     :scale: 80

Configuration
=============

.. image:: ../../../figures/gps_position_configuration.png
     :scale: 80

* **Show label:** Switches the button label on/off (default: on).
* **Autostart:** Starts element when opening the application (default: off).
* **Title:** Title of the element.
* **Tooltip:** This text will be displayed during hovering over the element with the cursor.
* **Icon:** Icon to display on button.
* **Average:** Calculates the average of the last at parameter average defined amount of received GPS coordinates (default: 1).
* **Follow:** Refreshes the map for every received GPS position received, only use with WMS in tiled mode (default: off).
* **Center on first position:** Centers map only on first received GPS position (default: on).
* **Zoom to accuracy on first position:** Zoom map according to first received gps position accuracy (default: on).


YAML-Definition:
----------------

This template can be used to insert the element into a YAML application. The element is placed as a button into the toolbar.

.. code-block:: yaml
                
                class: Mapbender\CoreBundle\Element\GpsPosition
                label: true                         # true/false to label button (default: true)
                autoStart: false	                # true/false (default: false)
                title: GPS-Position                 # title of the button
                tooltip: GPS-Position               # text to use as tool tip
                icon: gpsposition                   # icon to display on button
                target: map                         # Id of Map element to query
                average: 1                          # calculates the average of the last at parameter average defined amount of received GPS coordinates, default 1
                refreshinterval: 5000               # refresh interval in ms, default is 5000 ms
                follow: true                        # default false, true refreshes the map for every received GPS position received, only use with WMS in tiled mode
                centerOnFirstPosition: true         # center map only on first received gps position
                zoomToAccuracy: false               # zoom map according to received gps position accuracy
                zoomToAccuracyOnFirstPosition: true # zoom map according to first received gps position accuracy

