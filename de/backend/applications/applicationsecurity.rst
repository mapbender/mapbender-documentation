.. _applicationsecurity_de:

Sicherheit
##########
Jede Anwendung verfügt über individuelle Sicherheitseinstellungen: Hier können Sie unterschiedliche Berechtigungen explizit pro Anwendung zuweisen.


Anwendungszuweisungen
*********************

Standardmäßig stehen Benutzern/Gruppen alle Anwendungen zur Verfügung, die mit ausreichenden Berechtigungen Zugriff auf das :ref:`backend_de` haben. Für einzelne Anwendungen kann der Zugriff noch genauer definiert werden, so dass diese nur bestimmten Benutzern/Gruppen zur Verfügung stehen.

#. Bearbeiten Sie Ihre **Anwendung**.

#. Wählen Sie **Sicherheit**.

#. Machen Sie ihre Anwendung öffentlich zugänglich über die Auswahl **Öffentlicher Zugriff** (oder alternativ über den **Anwendung publizieren/verbergen**-Button in der Anwendungsübersicht).

#. Fügen Sie für individuelle Einstellungen alternativ Benutzer oder Gruppen über den ``+``-Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Rechtetabelle. So weisen Sie eine Anwendung einem oder mehreren Benutzer(n)/Gruppe(n) zu.

#. Melden Sie sich erneut unter der ausgewählten Benutzerbezeichnung an, um die Rechtevergabe zu testen.

  .. image:: ../../../figures/de/mapbender_security.png
     :width: 100%


Elementzuweisungen
******************

Standardmäßig stehen alle Elemente den Benutzern/Gruppen zur Verfügung, die Zugriff auf eine Anwendung haben. Für einzelne Elemente kann der Zugriff noch genauer definiert werden, so dass diese nur bestimmten Benutzern/Gruppen zur Verfügung stehen.

#. Bearbeiten Sie Ihre **Anwendung**.

#. Wählen Sie **Layouts**.

#. Jedes Element verfügt über einen eigenen ``AcL-Element``-Button (Schlüssel). Wählen Sie den Button zu dem Element, das nur ausgewählten Benutzern/Gruppen zur Verfügung stehen soll.

#. Fügen Sie Benutzer oder Gruppen über den ``+``-Button hinzu. Setzen Sie anschließend die view-Berechtigung. Das Element wird so innerhalb der Anwendung abgesichert und nur den gewählten Benutzer(n)/Gruppe(n) zugänglich.

#. Testen Sie die Konfiguration, indem Sie die Anwendung mit Benutzern aufrufen, die (keine) Berechtigungen zum Element erhalten haben.

  .. image:: ../../../figures/fom/element_security_key_popup.png
     :width: 100%
