.. _digitizer:

Digitizer
==========

The digitizer element enables the creation and editing of points, lines and areas on a map. In contrast to the :ref:`sketch element<sketch>`, this element stores geometries in a database table.
Currently Mapbender supports PostgreSQL by default. SpatiaLite and Oracle are available experimentally.
Development was carried out in a way that digitizer can be extended to include other data sources (such as OGC WFS) as well.

To use the digitizer, you need to configure it first. 

.. toctree::
   :maxdepth: 2

   digitizer/digitizer_configuration.rst
   

Once you've configured the digitizer, you can start using the element's functions.   
   
.. toctree::
   :maxdepth: 2   
   
   digitizer/digitizer_functionality.rst  