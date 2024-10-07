.. _digitizer_de:

Digitizer
=========

Der Digitizer erlaubt das Erstellen und Bearbeiten von Punkten, Linien und Flächen in der Karte. Im Unterschied zum :ref:`Sketch-Element<sketch_de>` werden die Geometrien in einer Tabelle in einer Datenbank hinterlegt.
Bisher unterstützt Mapbender vollumfänglich PostgreSQL als Datenquelle. SpatiaLite und Oracle sind experimentell verfügbar.
Der Digitizer wurde so entwickelt, dass die Datenerfassung auch auf andere Datenquellen, z. B. OGC WFS, erweitert werden kann.

Um das Digitizer-Element nutzen zu können, muss es zunächst konfiguriert werden.

.. toctree::
   :maxdepth: 2

   digitizer/digitizer_configuration.rst
   
   
Im Anschluss an die Konfiguration können verschiedene Digitizer-Funktionen genutzt werden.
   
.. toctree::
   :maxdepth: 2   
   
   digitizer/digitizer_functionality.rst  
