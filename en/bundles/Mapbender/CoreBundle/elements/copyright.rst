.. _copyright:

Copyright
************

The copyright shows a copyright label and terms of use as a dialog.

Class, Widget & Style
==============

* Class: Mapbender\\CoreBundle\\Element\\Copyright
* Widget: mapbender.element.copyright.js
* Style: mapbender.elements.css

Configuration
=============

.. code-block:: yaml

   tooltip: "Copyright"           # text to use as tooltip
   width: 200px                   # copyright width, default '200px'
   anchor: array('inline',
     'left-top','left-bottom',
     'right-top','right-bottom')  # copyright alignment
   position: array('0px','0px')   # copyright position, default: x=0px, y=0px
   copyrigh_text: "© XXX # 2013"  # edit the text you want to display as copyright text
   dialog_link: "Terms of use"    # 
   dialog_content: "Terms of use (Content)" #
   dialog_title: "Terms of use"   #

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
