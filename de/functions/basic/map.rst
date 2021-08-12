.. _map_de:

Map (Karte)
***********

Die Karte basiert auf OpenLayers und wird als Element im Content-Bereich integriert.

.. image:: ../../../figures/de/map.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/map_dialog.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird in der Layouts-Liste angezeigt. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Layersets:** Vorher konfiguriertes Layersets zur Anzeige der Hauptkarte (Thematische Karte, Hintergrundkarte).
* **Tile size:** Größe der Tiles bei gekachelten Diensten.
* **SRS:** Koordinatenbezugssystem beim Start der Anwendung ("Spatial Reference System"). Zwei Arten der SRS Definition werden unterstützt: EPSG: CODE oder EPSG:CODE|MEIN SRS TITEL.
* **Max. Extent:** Maximaler Kartenbereich (BBOX mit min/max x/y, die Ausschnitt definiert).
* **Start Extent:** Bereich der Karte, der beim Starten der Anwendung angezeigt wird (BBOX mit min/max x/y, die Ausschnitt definiert).
* **Feste Maßstabsstufen:** Das Zoom-Verhalten wird hierdurch konfiguriert. Feste Maßstabsstufen verbessern die visuelle Qualität von Diensten, welche nur auf bestimmten Maßstäben zwischengespeichert werden. Ist die Einstellung aktiviert, dann können nur Maßstäbe ausgewählt werden, die auch unter *scales* im Folgenden definiert sind (Standard: false).
* **Scales (csv):** Festgelegte Zoomstufen, die durch Drehen des Mausrads oder bei stufenweisem Zoomen für den Maßstab genutzt werden (werden durch Komma getrennt).
* **Other SRS:** Weitere auswählbare Projektionen unter denen die Karte angezeigt werden kann (werden durch Komma getrennt). Zwei Arten der SRS Definition werden unterstützt: EPSG:CODE oder EPSG:CODE|MEIN SRS TITEL.


Konfigurationsbeispiel
======================

Das Kartenelement (Map) muss unter Layouts im Content-Bereich integriert werden:

.. image:: ../../../figures/de/add_content.png
     :scale: 80

In der Karte können alle Instanzen angezeigt werden, welche im Layerset enthalten sind. Im vorliegenden Beispiel wird zwischen der *Hauptkarte/main* (1) und *Übersichtskarte/overview* (2) unterschieden.

.. image:: ../../../figures/de/map_example_layerset.png
     :scale: 80

Damit *Layersets* **(1)** auch in der Karte angezeigt werden, müssen diese im Kartenelement aktiviert werden. Eine Mehrfachauswahl ist hierbei auch möglich. Layersets, welche nicht ausgewählt wurden, können als Overview fungieren. Im Beispiel dient *main* als Haupt- und *overview* als Übersichtskarte.

Das Feld *SRS* **(2)** definiert das Koordinatenreferenzsystem. Im Beispiel ist dies EPSG 25832 bzw. ETRS89/UTM Zone 32N. Wenn andere Referenzsysteme zur Auswahl stehen sollen, werden diese unter *Other SRS* **(7)** angegeben. Im Beispiel umfasst dies: 25833 (ETRS89/UTM Zone 33N), 31466 (DHDN/3-degree Gauss-Krüger Zone 2), 31467 (DHDN/3-degree Gauss-Krüger Zone 3), 3857 (WGS 84/Pseudo-Mercator) und 4326 (WGS 84).

Weiterhin kann das Feld *Max. Extent* **(3)** definiert werden. Dieses gibt den maximalen sichtbaren Kartenbereich an. Alles was außerhalb dieser Angabe liegt, wird vom Anwender nicht gesehen. Das Feld *Start Extent* **(4)** wiederum definiert den Startbereich, welcher beim Öffnen der Anwendung zu sehen ist. Im Beispiel wird das Stadtgebiet von Bonn angezeigt. Zudem definiert *Scales* **(6)** die unterschiedlichen Zoomstufen in der Anwendung. Zwischen diesen kann mithilfe von dem :ref:`scale_selector_de`oder der :ref:`zoom_bar_de` navigiert werden. Feste Maßstabsstufen **(5)** wurden dabei im Beispiel deaktiviert. Das heißt, es ist auch eine Auswahl anderer Maßstäbe über das Mausrad möglich.

.. image:: ../../../figures/de/map_example_dialog.png
     :scale: 80


YAML-Definition:
----------------

.. code-block:: yaml

   layerset: null             # verweist auf ein Layerset, definiert zuerst das layerset und verweist darauf
   dpi: 72                    # Auflösung, Standard ist 72
   srs: "EPSG:4326"           # Koordinatenbezugssystem. Zwei Arten der SRS Definition werden unterstützt:
                                - "EPSG:CODE" oder
                                - "EPSG:CODE|MEIN SRS TITEL"
   units: "degrees"           # Einheiten in Grad oder Meter, Standard ist "degrees" (Grad)
   extents:
       max: [0, 40, 20, 60]
       start: [5, 45, 15, 55] # Kartenbereich (extent)
   scales: "25000000,10000000,5000000,1000000,500000" # eine CSV-Liste für den Maßstab
   otherSrs:
       - EPSG:31466
       - EPSG:31467
       - EPSG:25832          # andere Koordinatenbezugssystem. Zwei Arten der SRS Definition werden unterstützt:
                                - ["EPSG:CODE","EPSG:CODE"] or
                                - ["EPSG:CODE|MEIN SRS TITEL","EPSG:CODE|MEIN SRS TITEL"]
   tileSize: 256             # Kachelgröße



Kontrolle über URL-Parameter
============================

Ebenen sichtbar machen
----------------------

Sie können die ID der Ebene mit der ID <layerid> und des Dienstes <serviceid> in der URL als parameter übergeben, um einen Layer in der Startansicht zu aktivieren.

.. code-block:: php

  ?visiblelayers=<serviceid>/<layerid>


Es können mehrere Layer kommasepariert übergeben werden.

Die Werte für layerid und serviceid sind spezifisch für eine
Anwendung. Daher bekommen die Werte für layerid und serviceid in der
jeweiligen Anwendung und zwar im Layerset und dort in einem Layer. Jeder
Layer besitzt ein Icon mit drei Punkten auf der rechten Seite. Klicken Sie
auf die drei Punkte des Layers und ein Popupfenster erscheint.

.. image:: ../../../figures/wms_instance_layer_id.png
     :scale: 80

Der erste Wert nennt die interne SourceID und SourceLayerId (31-591). Der
zweite Wert listet die InstanceID und InstanceLayerId, die wir im weiteren
nutzen wollen (73-836).

Nutzen Sie diese Werte für den "visibleLayers" Parameter in der URL und
trennen Sie beide Werte mit einem Schrägstrich.

Zum Beispiel: http://localhost/mapbender/application/myapp?visiblelayers=73/836

Wenn Sie zwei per Voreinstellung nicht sichtbare Layer haben, fügen Sie
beide Werte von layerid und serviceid in die URL und trennen diese mit einem Komma.

Zum Beispiel: http://localhost/mapbender/application/myapp?visiblelayers=73/836,73/840



Punkte übergeben
----------------

Sie können einen oder mehrere Punkte in der URL übergeben. Jeder Punkt verfügt dabei über die folgenden Parameter:

- Punkt (point): Koordinatenpaar, die Werte werden mit Komma getrennt (zwingend)
- Beschriftung (label): Beschriftung, die angezeigt werden soll (optional)
- Maßstab (scale): Maßstab, in dem der Punkt angezeigt werden soll (optional. Die Angabe ist nur bei der Anzeige eines Punktes sinnvoll)

Wenn Sie mehr als einen Punkt im Aufruf übergeben, zoomt die Karte auf 150 % der Gesamt-Boundingbox.

Format für die Übergabe eines Punktes:

.. code-block:: php

   ?poi[point]=363374,5621936&poi[label]=Label&poi[scale]=5000


Für die Übergabe vieler Punkte wird das folgende Format verwendet:

.. code-block:: php

   ?poi[0][point]=363374,5621936&poi[0][label]=Label%201&poi[1][point]=366761,5623022&poi[1][label]=Label%202


Rechteck (BBOX) übergeben
-------------------------

Es kann ein Rechteck (BBOX) beim Start übergeben werden. Es wird dann auf dieses Rechteck gezoomt. Der Aufruf sieht wie folgt aus:

.. code-block:: php

   ?bbox=364286,5622263,365979,5622806


Maßstab übergeben
-----------------

Es kann der gewünschte Maßstab aus der Liste der verfügbaren Maßstäbe übergeben werden.

.. code-block:: php

   ?scale=1000



SRS (Projektion) übergeben
--------------------------

Es kann eine gewünschte Projektion für den Start der Anwendung übergeben werden.

.. code-block:: php

   ?srs=EPSG:4326



Center - Zentrieren der Anwendung
---------------------------------

Es kann eine Koordinate beim Start übergeben werden, die in der Anwendung zentriert werden soll. Sie benötigen zusätzlich die Angabe der Projektion.

.. code-block:: php

   ?center=364286,5622263


Weitere Startparameter
----------------------

Die Elemente WMS Loader und WMC Loader stellen ebenfalls Parameter zur Verfügung, die beim Start einer Anwendung übergeben werden können. Schauen Sie sich für nähere Informationen die Dokumentation dieser Elemente an.

