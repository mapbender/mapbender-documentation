.. _examples_de:

Beispiele
=========

Benutzer mit der ID 1 zurücksetzen
----------------------------------

Der Befehl ``app/console fom:user:resetroot`` setzt den User mit der ID 1 zurück. Dieser Benutzer hat generell alle Rechte.

.. code-block:: bash
          $ app/console fom:user:resetroot
                Welcome to the Mapbender root account management command  
                Enter the username to use for the root account.
                Username [root]: root
                Enter the e-mail adress to use for the root account.
                E-Mail [root@root.de]: admin@mycompany.foo
                Enter the password to use for the root account.
                Password: secret
                Do you confirm reset [yes]? yes
                The root is now usable. Have fun!


Neue Benutzer anlegen
----------------------

Der root Benutzer (ID 1) kann neue Benutzer anlegen. Dies ist auch für andere Benutzer möglich, wenn sie im ACL "Users" als Owner eingetragen sind. Diese Ausnahmeberechtigung wurde gewählt, damit nicht jeder Nutzer seinen Benutzernamen ändern kann.


Neue Anwendungen anlegen
------------------------

Ein Benutzer, der neue Anwendungen erzeugen soll, muss im ACL "Anwendungen" das *Create* Recht besitzen. Sobald er dieses Recht hat, kann er auch Anwendungen exportieren und importieren.


Datenquellen konfigurieren
--------------------------

Um den Aufruf auf den Tab ``Datenquellen`` zu erhalten und anschließend Dienste einbinden, konfigurieren oder aktualisieren zu können, muss ein Benutzer/eine Gruppe im ACL "Datenquellen" mindestens das *Edit* Recht zugewiesen bekommen.


Anwendungen kopieren
--------------------

Ein Benutzer kann Anwendungen kopieren, wenn er im ACL ``Applications`` oder in der Anwendung selbst mindestens das *Edit* Recht hat. Dabei überschreibt das individuelle Recht der Anwendung das globale ACL Recht.

Wenn ein Benutzer eine Anwendung kopiert, dann wird er automatisch ihr Owner.


Anwendungen löschen
-------------------

Ein Benutzer kann Anwendungen löschen, wenn er im ACL ``Anwendungen`` oder er in der Anwendung selbst mindestens das *Delete* Recht hat. Dabei überschreibt das individuelle Recht der Anwendung das globale ACL Recht.
