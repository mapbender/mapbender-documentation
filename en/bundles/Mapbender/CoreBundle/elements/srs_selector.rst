Spatial Reference System Selector (SRS Selector)
************************************************

The spatial reference system selector changes the map's spatial reference system.

Class, Widget & Style
=====================

* Class: Mapbender\\CoreBundle\\Element\\SrsSelector
* Widget: mapbender.element.srsselector.js
* Style: mapbender.elements.css

Configuration
=============

.. code-block:: yaml

   tooltip: 'SRS Selector'  # text to use as tooltip
   label: false             #
   targets: array(map" => null,coordinatesdisplay" => null) # Array, Ids of Map element and coordinatesdisplay element


HTTP Callbacks
==============

None.

JavaScript API
==============

showHidde
---------
<>

selectSrs
----------
<>

getSelectedSrs
----------
<>

isSrsSupported
----------
<>

isSrsEnabled
----------
<>

disableSrs
----------
<>

enableSrs
----------
<>

enableOnlySrs
----------
<>

getFullSrsObj
----------
<>

enableAllSrs
----------
<>

disableAllSrs
----------
<>

getInnerJoinSrs
----------
<>

getInnerJoinArrays
----------
<>

JavaScript Signals
==================

None.
