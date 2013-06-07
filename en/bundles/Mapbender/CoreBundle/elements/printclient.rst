PrintClient
***********************

PrintClient is still under construction. For now WGS84 is not supported.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\PrintClient
* Widget: mapbender.element.printClient.js
* Style: mapbender.element.printClient.css

Configuration
=============

Also see :doc:`button` for inherited configuration options.

.. code-block:: yaml

    target: map                                 # id of a "map" element (if yml configuration - string 'map', if database configuration - id of a "map" element)
    autoOpen: false				# true/false open when application is started, default: false
    print_directly: true                	# true/false must be true for now
    templates:
        a4portrait:                             # template name, tamplate file name without file extension 
            label: "A4 Portrait"                # template label at dialog
            format: a4                          # format
        a4landscape:                            # template name, tamplate file name without file extension 
            label: "A4 Landscape"               # template label at dialog
            format: a4                          # format
    scales: [5000, 10000, 25000]        	# define scales to choose from selectbox or if empty free scale can be defined in a textfield
    quality_levels:                             # define quality levels in dpi
        72: draft                               # 72 - dpi value, draft - label
        288: high quality                       # 288 - dpi value, draft - label
    rotatable: true                             # true/false use true for rotation
    optional_fields:            		# define optional fields - not yet implemented

HTTP Callbacks
==============

/direct
--------------------------------

Not Yet Implemented

JavaScript API
==============

open
----------

Opens the print client dialog.

close
-----
Closes the print client dialog.

JavaScript Signals
==================

None.
