.. _applicationsecurity_de:

 .. |mapbender-button-add| image:: ../../../figures/mapbender_button_add.png
 .. |mapbender-button-edit| image:: ../../../figures/mapbender_button_edit.png
 .. |mapbender-button-key| image:: ../../../figures/mapbender_button_key.png
 .. |mapbender-button-publish| image:: ../../../figures/mapbender_button_publish.png

Sicherheit (Anwendungsreiter)
#############################

Jede Anwendung besitzt einen Reiter für individuelle Sicherheitseinstellungen. In diesen können Sie unterschiedliche Berechtigungen explizit für die individuelle Anwendung zuweisen.

.. note:: Eine globale gesetzte Berechtigung überschreibt eine über diese Seite gesetzte individuelle Berechtigung.


Anwendungszuweisungen
*********************

Standardmäßig stehen alle Anwendungen den :ref:`Benutzern<users_de>` und :ref:`Gruppen<roles_groups_de>` zur Verfügung, die mit ausreichenden Berechtigungen Zugriff auf das :ref:`backend_de` haben. Für einzelne Anwendungen kann der Zugriff noch genauer definiert werden, so dass diese nur bestimmten Accounts zur Verfügung stehen.

#. Bearbeiten Sie Ihre **Anwendung** |mapbender-button-edit|.

#. Wählen Sie den Reiter **Sicherheit**.

#. Machen Sie ihre Anwendung öffentlich zugänglich über die Auswahl **Öffentlicher Zugriff** (oder alternativ über den **Anwendung publizieren/verbergen** |mapbender-button-publish| in der Anwendungsübersicht).

#. Fügen Sie für individuelle Einstellungen alternativ Benutzer oder Gruppen über den |mapbender-button-add| Button hinzu. Setzen Sie anschließend individuelle Berechtigungen über die Berechtigungstabelle. So weisen Sie eine Anwendung einem oder mehreren Benutzern oder Gruppen zu.

#. Melden Sie sich erneut unter der ausgewählten Benutzerbezeichnung an, um die Rechtevergabe zu testen.

  .. image:: ../../../figures/de/mapbender_security.png
     :width: 100%


Elementzuweisungen
******************

Standardmäßig stehen alle Elemente einer Anwendung den :ref:`Benutzern<users_de>` und :ref:`Gruppen<roles_groups_de>` zur Verfügung, die Zugriff auf sie haben. Für einzelne Elemente kann der Zugriff noch genauer definiert werden, so dass diese nur bestimmten Accounts zur Verfügung stehen.

#. Bearbeiten Sie Ihre **Anwendung** |mapbender-button-edit|.

#. Wählen Sie den Reiter **Layouts**.

#. Jedes Element verfügt über einen eigenen |mapbender-button-key| Button. Wählen Sie den Button zu dem Element, das nur ausgewählten Benutzern oder Gruppen zur Verfügung stehen soll.

#. Fügen Sie Benutzer oder Gruppen über den |mapbender-button-add| Button hinzu. Setzen Sie anschließend die *view*-Berechtigung. Das Element wird so innerhalb der Anwendung abgesichert und nur den gewählten Benutzern oder Gruppen zugänglich.

#. Testen Sie die Konfiguration, indem Sie die Anwendung mit Benutzern aufrufen, die (keine) Berechtigungen zum Element erhalten haben.

  .. image:: ../../../figures/de/fom/element_security_key_popup.png
     :width: 100%
