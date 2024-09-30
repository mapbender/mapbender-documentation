.. _digitizer:

Digitizer
==========

The digitizer element allows the creation and editing of points, lines and areas on a map. In contrast to sketch, this element saves geometries in a table in a database. Currently Mapbender supports PostgreSQL. SpatiaLite and Oracle are available experimentally. Development was carried out in a way that digitizer can be extended to include other data sources such as OGC WFS as well.  

More information about the functionality of the digitizer can be found here:   
   
.. toctree::
   :maxdepth: 2   
   
   digitizer/digitizer_functionality.rst  

In order to use the digitizer, one has to define a specific yaml-definition: 

.. toctree::
   :maxdepth: 2

   digitizer/digitizer_configuration.rst
   
