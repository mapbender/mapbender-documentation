.. _security_de:

Sicherheitskonzepte
###################

Sicherheit wird im FOM User Bundle bereitgestellt und basiert auf diesen Konzepten:

- :doc:`Benutzer <users>`
- :doc:`Rollen und Gruppen <roles_groups>`
- :doc:`Access Control Lists (ACL) <acl>`


Rechte
******

Mapbender bietet verschiedene Rechte an, die Sie vergeben können. Sie basieren auf :doc:`Access Control Lists (ACL) <acl>`.

* view - anzeigen
* edit - editieren
* delete - löschen
* operator - kann anzeigen, editieren und löschen
* master - kann anzeigen, editieren, löschen und diese Rechte außerdem weitergeben
* owner - Besitzer, darf alles (inkl. Vergabe von master und owner Recht)

Weisen Sie einem Benutzer über **Benutzer** → **Benutzer bearbeiten** → **Sicherheit** die gewünschten Rechte zu.

  .. image:: /figures/mapbender_roles.png
     :width: 100%


Zuweisen von Benutzern zu einem Benutzer/einer Gruppe
*****************************************************

#. Bearbeiten Sie Ihre Benutzer über **Sicherheit** → **Benutzer**.

#. Wählen Sie **Sicherheit**.

#. Weisen Sie Benutzern/Gruppen individuelle Berechtigungen auf den individuellen Benutzer zu. Fügen Sie Benutzer oder Gruppen über den ``+``-Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Rechtetabelle. So weisen Sie Benutzer(n)/Gruppe(n) einen Benutzer zu.

#. Melden Sie sich unter dem Benutzer bzw. der Gruppe mit neuen Rechten an, um die Rechtevergabe zu testen. Je nach Konfiguration ist es so z.B. möglich, dass alle Teilnehmer einer Gruppe Berechtigungen über einen bestimmten Benutzer haben und dessen Account bearbeiten oder löschen können.
