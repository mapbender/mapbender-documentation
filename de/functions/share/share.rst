.. _share_de:

Share
*****

Anwendung wechseln
==================

Nutzer können mit diesem Element von ihrer aktuellen Anwendung in eine andere wechseln. Dabei werden die Parameter Zentrierung, Maßstab, Referenzsystem und Rotation beibehalten.

Das Element kann in Toolbar oder Footer implementiert werden. Der Nutzer definiert selbst, zu welchen Anwendungen ein Wechsel möglich ist. (Bestehen keine Zugriffsrechte für bestimmte Anwendungen, dann werden diese auch nicht angezeigt.) Es existiert außerdem die Möglichkeit, ausgewählte Anwendungen in einem neuen Browser-Tab zu öffnen.

.. image:: ../../../figures/de/application_switcher.png
     :scale: 80


YAML-Definition:
----------------

.. code-block:: yaml

  applications: ['mapbender_user', 'mapbender_mobile', 'mapbender_user_basic']   #Definition der auswählbaren Anwendungen
  open_in_new_tab: false                                                         #Öffnet ausgewählte Anwendungen in neuem Tab (Standard=false). 

