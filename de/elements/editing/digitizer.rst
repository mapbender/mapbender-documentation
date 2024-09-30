.. _digitizer_de:

Digitizer
=========

Der Digitizer erlaubt das Erstellen und Bearbeiten von Punkten, Linien und Flächen in der Karte.
Im Unterschied zum :ref:`Sketch-Element<sketch_de>` werden die Geometrien in einer Tabelle in einer Datenbank hinterlegt. Bisher unterstützt Mapbender PostgreSQL als Datenquelle. SpatiaLite und Oracle sind experimentell verfügbar. Die Entwicklung wurde so durchgeführt, dass die Erfassung auch auf andere Datenquellen, wie z. B. OGC WFS erweitert werden kann.

Um das Digitizer-Element nutzen zu können, muss eine YAML-Definition aufgebaut werden: 

.. toctree::
   :maxdepth: 2

   digitizer/digitizer_configuration.rst
   
   
Mehr Informationen zur Nutzung des Digitizers sind hier zu finden:   
   
.. toctree::
   :maxdepth: 2   
   
   digitizer/digitizer_functionality.rst  
