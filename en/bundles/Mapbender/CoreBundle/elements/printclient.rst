PrintClient
***********************

under construction

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\PrintClient
* Widget: mapbender.element.printClient.js
* Style: mapbender.element.printClient.css

Configuration
=============

Also see :doc:`button` for inherited configuration options.

.. code-block:: yaml

   target: map
	autoOpen: false				# true/false open when application is started
        printer:
	    service:				# printer server url f.e. http://localhost/mbPrinterService.php
	formats:				# define the formats
	    a4:					# block concerning format a4
		label:  A4			# label for format selectbox
		orientations:			# define portrait and/or landscape 
		    portrait:			# define portrait options
		        label: Portrait		# label for orientation selectbox
		        height: 21		# print frame height
		        width: 17		# print frame width
		    landscape:		
		        label: Landscape
		        height: 17
		        width: 21
		scales: [5000, 10000, 25000]	# define scales to choose from selectbox or if empty free scale can be defined in a textfield
		quality_levels: 		# define quality levels in dpi, default is ?
		    72: draft
		    288: high quality
		title_block_selector: true	# show/hide title block
		rotatable: true			# textfield to define rotation
		free_extent: true		# if true a checkbox will show up to print full map extent
		optional_fields: 		# define optional fields
		    editor:			# name of optional field
                	type: text		# type (can be text/checkbox/selectbox)
                	options:		# define options (can be required/label ...)
                  	    required: false
        	    approved:
                 	type: checkbox
                	options:
                	    label: approved		

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
