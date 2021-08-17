.. _security_de:

Sicherheitskonzepte
===================

Sicherheit wird im FOM User Bundle bereitgestellt und basiert auf diesen Konzepten:

- :doc:`Benutzer <users>`
- :doc:`Rollen und Gruppen <roles_groups>`
- :doc:`Access Control Lists (ACL) <acl>`


Rechte
========

Mapbender bietet verschiedene Rechte an, die Sie vergeben können. Sie basieren auf :doc:`Access Control Lists (ACL) <acl>`.

* view - anzeigen
* edit - editieren
* delete - löschen
* operator - kann anzeigen, editieren und löschen
* master - kann anzeigen, editieren, löschen und diese Rechte außerdem weitergeben
* owner - Besitzer, darf alles (inkl. Vergabe von master und owner Recht)

Weisen Sie einem Benutzer über ``Benutzer --> Benutzer bearbeiten --> Sicherheit`` die gewünschten Rechte zu.

  .. image:: /figures/mapbender_roles.png
     :scale: 80


Zuweisen einer Anwendung zu einem Benutzer/einer Gruppe
=======================================================

#. Bearbeiten Sie Ihre Anwendung über ``Anwendungen --> Bearbeiten``.

#. Wählen Sie ``Sicherheit``.

#. Veröffentlichen oder verbergen Sie Ihre Anwendung für alle über die Auswahl **Öffentlicher Zugriff** unter ``Sicherheit`` (oder alternativ über den **Anwendung publizieren/verbergen**-Button in der Anwendungsübersicht).

#. Fügen Sie für individuelle Einstellungen alternativ Benutzer oder Gruppen über den Plus-Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Rechtetabelle. So weisen Sie eine Anwendung einem oder mehreren Benutzer(n)/Gruppe(n) zu.

#. Melden Sie sich erneut unter der ausgewählten Benutzerbezeichnung an, um die Rechtevergabe zu testen.

#. Alternativ können Sie auch unter ``Sicherheit --> Globale Zugriffssteuerungsliste (ACL) --> Anwendungen`` schnell Berechtigungen von Benutzern/Gruppen für alle Anwendungen festlegen.


Zuweisen einzelner Elemente zu Benutzern/Gruppen
================================================

Standardmäßig stehen alle Elemente den Benutzern/Gruppen zur Verfügung, die Zugriff auf eine Anwendung haben. Für einzelne Elemente kann der Zugriff noch genauer definiert werden, so dass diese nur bestimmten Benutzern/Gruppen zur Verfügung stehen.

#. Bearbeiten Sie Ihre Anwendung über ``Anwendungen --> Bearbeiten``.

#. Wählen Sie ``Layouts``.

#. Jedes Element verfügt über einen eigenen ``AcL-Element``-Button (Schlüssel). Wählen Sie den Button zu dem Element, das nur ausgewählten Benutzern/Gruppen zur Verfügung stehen soll.

#. Fügen Sie Benutzer oder Gruppen über den Plus-Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Rechtetabelle. Das Element wird so innerhalb der Anwendung abgesichert und nur bestimmten Benutzer(n)/Gruppe(n) zugänglich.

#. Testen Sie die Konfiguration, indem Sie die Anwendung mit Benutzern aufrufen, die (keine) Berechtigungen zum Element erhalten haben.


Zuweisen von Benutzern zu einem Benutzer/einer Gruppe
=====================================================

#. Bearbeiten Sie Ihre Benutzer über ``Sicherheit --> Benutzer``.

#. Wählen Sie ``Sicherheit``.

#. Weisen Sie Benutzern/Gruppen individuelle Berechtigungen auf den individuellen Benutzer zu. Fügen Sie Benutzer oder Gruppen über den Plus-Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Rechtetabelle. So weisen Sie Benutzer(n)/Gruppe(n) einen Benutzer zu.

#. Melden Sie sich unter dem Benutzer bzw. der Gruppe mit neuen Rechten an, um die Rechtevergabe zu testen. Je nach Konfiguration ist es so z.B. möglich, dass alle Teilnehmer einer Gruppe Berechtigungen über einen bestimmten Benutzer haben und dessen Account bearbeiten oder löschen können.
