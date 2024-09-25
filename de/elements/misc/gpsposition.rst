.. _gpspostion_de:

GPS-Position
************

Dieses Elememt stellt einen Button bereit, der zur aktuellen Position auf der Karte navigiert und ein markierendes Symbol anzeigt. Der Maßstab wird dabei nicht verändert, außer durch Aktivierung der Einstellung ``zoom to accuracy (zoom to accuracy on first position)``.

Die Funktion baut auf der `Geolocation-API <https://www.w3.org/TR/geolocation/>`_  des W3C auf. Ob Ihr Browser diese Funktionalität unterstützt, erfahren Sie auf der `Can I Use <https://caniuse.com/#feat=geolocation>`_ Seite. Die Funktion nutzt den ``High Accuracy Parameter``, der die Standortbestimmung über GPS forciert. Falls das Gerät einen GPS-Empfänger hat und dieser aktiviert ist, ist die Positionsbestimmung also genauer. Ansonsten werden die WLAN Access-Points zur Positionsbestimmung herangezogen.

Der Mittelpunkt zeigt die wahrscheinliche Position des Gerätes an, der äußere Kreis die Genauigkeit der Positionsbestimmung, d.h. in welchem Bereich sich die ermittelte Position wahrscheinlich befindet.

Kompatibilität: Internet Explorer und MS Edge geben ohne GPS-Gerät am Rechner teilweise sehr ungenaue Informationen heraus. Das Verhalten ist auch mit anderen Anwendungen zu beobachten.

.. image:: ../../../figures/gps_position.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/gps_position_configuration.png
     :scale: 70

* **Beschriftung anzeigen:** Schaltet die Beschriftung des Buttons an/aus (Standard: an).
* **Autostart** Startet Element beim Öffnen der Anwendung (Standard: aus).
* **Titel:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Symbol:** Symbol des Buttons, basierend auf einer CSS Klasse.
* **Durchschnitt:** Berechnet den Mittelwert der unter Average angegebenen letzten empfangenen GPS Koordinaten (Standard: 1).
* **Folge:** Positioniert die Karte bei jeder empfangenen GPS Koordinate neu (Standard: false).
* **Zentriere auf die erste Position:** Zentriert die Karte auf die erstermittelte Position (Standard: true).
* **Zoom auf Genauigkeit der ersten Position:** Zoomt auf die ermittelte Koordinate nach Messgenauigkeit bei erster ermittelten Position (Standard: true).


YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Anwendung einzubinden.

.. code-block:: yaml

                class: Mapbender\CoreBundle\Element\GpsPosition
                label: true                         # false/true, um den Button zu beschriften (Standard: true)
                autoStart: false                    # true, wenn diese Funktion beim Start der Anwendung geöffnet werden soll (Standard: false).
                title: GPS-Position                 # Titel des Buttons
                tooltip: GPS-Position               # Text des Tooltips
                icon: iconGpsTarget                 # Symbol für den Button
                target: map                         # ID des Kartenelements
                average: 1                          # berechnet den Mittelwert der unter average angegebenen letzten empfangenen GPS Koordinaten (Standard: 1).           
                refreshinterval: 5000               # Aktualisierungsintervall in ms (Standard: 5000 ms).
                follow: true                        # True positioniert die Karte bei jeder empfangenen GPS Koordinate neu (Standard: false). Sollte nur mit WMS Diensten im gekachelten Modus verwendet werden, da sonst bei jeder Neupositionierung ein neuer Kartenrequest geschickt wird
                centerOnFirstPosition: true         # Zentriert die Karte auf die erstermittelte Position
                zoomToAccuracy: false               # Zoomt auf die ermittelte Koordinate nach Messgenauigkeit
                zoomToAccuracyOnFirstPosition: true # Zoomt auf die ermittelte Koordinate nach Messgenauigkeit bei erster ermittelten Position

