.. _digitizer:

Digitizer
==========

The digitizer element allows the creation and editing of points, lines and areas on a map. In contrast to the :ref:`sketch element<sketch>`, this element stores geometries in a database table. Currently Mapbender supports PostgreSQL by default. SpatiaLite and Oracle are available experimentally. Development was carried out in a way that digitizer can be extended to include other data sources such as OGC WFS as well.  

More information on the functionality of the digitizer can be found here:   
   
.. toctree::
   :maxdepth: 2   
   
   digitizer/digitizer_functionality.rst  

In order to use the digitizer, one has to define a specific yaml definition: 

.. toctree::
   :maxdepth: 2

   digitizer/digitizer_configuration.rst
   
