.. _roles_groups_de:

Gruppen und Rollen
==================

Gruppen
*******
Gruppen sind selbst erstellte Datenbank-Entitäten. Benutzer können ihnen individuell zugewiesen werden.
Gemeinsame Gruppenmitglieder besitzen die gleichen Rechte, sofern diese global für die Gruppe konfiguriert wurden.
Gruppen werden, die entsprechende Berechtigung vorausgesetzt, über ``Sicherheit`` → ``Gruppen`` → ``Neue Gruppe hinzufügen`` angelegt und konfiguriert.
Dort bietet Mapbender ebenfalls eine Übersicht über alle Gruppen an:

  .. image:: /figures/de/mapbender_security_group_overview.png
   :scale: 70

Rollen
******
Rollen sind Zugehörigkeiten zu systemeigenen Standard-Gruppen.
Die folgenden Rollen sind für eine übergreifende Rechtevergabe auf bestimmte Domänen-Objekte verfügbar:

* **Alle angemeldeten Nutzer**: Rechtevergabe betrifft alle Benutzer mit einem Account. 
* **Öffentlicher Zugriff**: Rechtevergabe betrifft alle unangemeldeten Besucher von Mapbender-URLs.

Rollen können je nach Kontext in der ``Anwendungssicherheit`` oder im Bereich ``Globale Berechtigungen`` Berechtigungen zugewiesen werden.
Eine individuelle Anwendung könnte dann beispielsweise wie folgt abgesichert sein:

  .. image:: /figures/de/mapbender_roles_application_overview.png
   :scale: 70