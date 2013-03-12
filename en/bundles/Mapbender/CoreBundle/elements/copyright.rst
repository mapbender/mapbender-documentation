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

   tooltip: "Copyright"             # text to use as tooltip
   width: 200px                     # copyright width, default '200px'
   anchor: 'inline'/'left-top'/     # copyright alignment, default 'left-bottom'
     'left-bottom'/'right-top'/     # use inline f.e. in sidebar
     'right-bottom'                 
   position: array('0px','0px')     # copyright position, default: x=0px, y=0px
   copyrigh_text: "© XXX # 2013"    # edit the text you want to display as copyright text
   dialog_link: "Terms of use"      # title for a link to "terms of use" content, default is 'Terms of use'
                                    # use '' for a link to hide "Terms of use" components
   dialog_content: "Terms of use (Content)"  # the content of the "terms of use", default is 'Terms of use (Content)'
   dialog_title: "Terms of use"     # title of the dialog, default is 'Terms of use'

HTTP Callbacks
==============

None.

JavaScript API
==============

None.

JavaScript Signals
==================

None.
