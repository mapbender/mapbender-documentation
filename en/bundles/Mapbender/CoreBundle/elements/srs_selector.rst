.. _srs_selector:

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
   label: false             # true/false to label  the srs selector
   target: ~                # Id of Map element to query


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
