.. _acl_de:


Access Control Lists (ACL)
==========================

Die Absicherung von Domain-Objekten wird in Mapbender über Access Control Lists (ACLs) implementiert. ACLs ermöglichen in Mapbender eine flexible Rechtezuweisung auf Applikationen, Dienste und die Benutzer- und Gruppenverwaltung selbst.

Mapbender bietet zur Absicherung dieser Bereiche die folgenden Rechte- und Rollenzuweisungen an:

- View       : Ein existierendes Objekt lesen
- Edit       : Ein existierendes Objekt bearbeiten
- Delete     : Ein existierendes Objekt löschen
- Operator   : Rollenbezeichnung für die Rolle "Operator", dieser hat die Rechte View, Edit und Delete.
- Master     : Rollenbezeichnung für die Rolle "Master", dieser hat Operator-Rechte und kann zusätzlich alle oberen Rechte anderen zuweisen.
- Owner      : Rollenbezeichnung für die Rolle "Owner", dieser kann sowohl Operator als auch Master-Rechte zuweisen.

