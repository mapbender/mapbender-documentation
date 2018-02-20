.. _roles_groups_de:

Rollen und Gruppen
==================

Rollen sind definiert über Instanzen von
FOM\\ManagerBundle\\Component\\Bundle und nutzen die getRoles Methode.

Die Benennung der Rollen folgt dem Standard Symfony Role Naming Schema, in
dem Rollen mit dem Präfix "ROLE\_" benannt werden.

Rollen können für globale Rechteüberprüfungen benutzt werden, wenn kein
Domänen-Objekt involviert ist und können als Sicherheits-Identitäten von ACE
in ACL genutzt werden.

Gruppen sind Datenbank-Entitäten, die zu Benutzern auf einer individuellen
Basis zugewiesen werden können. Sie können auch mehreren Rollen zugewiesen
werden. Daher liegt ihr Nutzen in der Sammlung von Rollen, die jedem Nutzer
einer Gruppe zugeordnet werden sollen.

.. image:: users.png



Zukunft
-------

Später ist es möglich, individuelle Rollen direkt einem Nutzer zuzuordnen.

Symfony bietet zusätzlich eine API für hierarchische Rollen an, die bisher
noch nicht Teil des FOMUserBundles ist.
