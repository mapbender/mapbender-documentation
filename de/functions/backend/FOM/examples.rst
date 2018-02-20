.. _fom_examples_de:

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


Neuen Benutzer anlegen
----------------------

Der root Benutzer (ID 1) kann neue Benutzer anlegen. Ein Benutzer kann dann neue Benutzer anlegen, wenn er im ACL "Users" als Owner eingetragen ist. Wir haben diese Ausnahme der Berechtigungen gewählt, damit nicht jeder Nutzer seinen Benutzernamen ändern kann.


Neue Anwendungen anlegen
------------------------

Ein Benutzer, der neue Anwendungen erzeugen soll, muss im ACL "Applications" das Create Recht besitzen. Sobald er dieses Recht hat, kann er auch Anwendungen exportieren und importieren.

Um Layerset Instances einzubauen, muss er im ACL "Service Source" das Edit Recht besitzen.



Anwendungen kopieren
--------------------

Ein Benutzer kann Anwendungen kopieren, wenn:

* er im ACL "Applications" mindestens das Edit Recht hat.
* oder er in der Anwendung mindestens das Edit Recht hat. Dabei überschreibt das Recht der Anwendung das globale ACL Recht.

Dabei wird der Benutzer automatisch Owner seiner kopierten Anwendung.


Anwendungen löschen
-------------------

Ein Benutzer kann Anwendungen löschen, wenn:

* er im ACL "Applications" mindestens das Delete Recht hat
* oder er in der Anwendung mindestens das Delete Recht hat. Dabei überschreibt das Recht der Anwendung das globale ACL Recht.
