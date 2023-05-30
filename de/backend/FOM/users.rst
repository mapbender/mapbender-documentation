.. _users_de:

Benutzer
========

Benutzer werden als FOM\\UserBundle\\Entity\\User implementiert und im Datenbank Repository gespeichert. Die Entität hält nur die notwendigen Informationen über einen Nutzer vor.

Das Bundle enthält Möglichkeiten für folgende Optionen:

* Benutzerverwaltung durch einen Administrator
* Registierung eines Benutzers
* Zurücksetzung des eigenen Passworts

Der Benutzer mit der ID 1 (root) ist besonders, da dieser Benutzer bei der Installation erstellt wird und immer alle Rechte hat. Falls alle Stricke reißen, können Sie mit diesem Benutzer alles verwalten. Und falls Sie gar die Anmeldedaten vergessen haben sollten, können Sie über ein app/console Kommando den Benutzer zurücksetzen: *fom:user:resetroot*.


Passwort vergessen
------------------

Falls ein Benutzer sein Passwort vergessen hat, kann er in der Login-Maske über den Link "Passwort vergessen" ein neues Passwort anfordern. Dazu gibt er dann seinen Benutzernamen oder seine E-Mail Adresse an.

.. image:: ../../../../figures/de/fom/user_forgot_password.png

Danach bekommt der Benutzer eine E-Mail mit einem Link zur Zurücksetzung des Passworts. Der Link ist nach der Nutzung nicht mehr gültig. Der Text der Mail kann in der Datei /FOM/UserBundle/Resources/translations/messages.de.xlf angepasst werden.

Die Funktionalität kann in der config.yml ausgeschaltet werden.

.. code-block:: yaml

                fom_user:
                    reset_password: true # true/false


Registrierung
-------------

Benutzer können sich in Mapbender selbst registrieren. Vorher muss in der config.yml die Einstellung *fom_user:selfregister* auf true gestellt werden.

.. code-block:: yaml

                fom_user:
                    selfregister: false # true/false

Im Login-Dialog erscheint der "Register" Link. Der Benutzer wird zu einer Maske geführt, in der er Name, Passwort und E-Mail Adresse angeben kann.

.. image:: ../../../../figures/de/fom/user_self_register.png

Danach erhält er eine Bestätigungsmail, mit der er seine Anmeldung abschließen kann. Bis zu diesem Zeitpunkt ist er als inaktiver Nutzer in Mapbender hinterlegt.

Die Texte der Bestätigungsmail können unter /FOM/UserBundle/Resources/translations/messages.de.xlf angepasst werden.


Aktivieren von Nutzern
----------------------

Benutzer können von Administratoren mit der ACL-Rolle *edit* aktiviert oder deaktiviert werden. Ein Benutzer mit Administrationsrechten kann sich selbst nicht aktivieren oder deaktivieren.

.. image:: ../../../../figures/de/fom/edit_user_activated.png

Ein Benutzer, der deaktiviert ist, kann sich so lange nicht mehr im Mapbender anmelden, bis er wieder aktiviert wird.

Benutzer, die sich selbst registriert haben, aber die Freischaltungsmail noch nicht bestätigt haben, können so von einem Administrator per Hand freigeschaltet werden.


Login Fehler
------------

Fehlerhafte Logins werden mit der Meldung "Login fehlerhaft" kommentiert. Loginfehler schließen den Account nicht dauerhaft aus. Vielmehr wird der Account für eine bestimmte Zeit ausgeschlossen (gelockt).

Die config.yml ermöglicht die Anpassung dieses Verhaltens:

.. code-block:: yaml

   fom_user:

       # Allow to create user log table on the fly if the table doesn't exits.
       # Default: true
       auto_create_log_table: true

       # Time between to check login tries
       login_check_log_time: "-5 minutes"

       # Login attemps before delay starts
       login_attempts_before_delay: 3

       # Login delay after all attemps are failed
       login_delay_after_fail: 2 # Seconds


* **auto_create_log_table:** Angabe zur Rückwärtskompatibilität (Standard: true).
* **login_check_log_time:** Angabe zur Bereinigung der Login-Failure Tabelle (Standard: -5 minutes)
* **login_attempts_before_delay:** Anzahl der Login Versuche, bevor das Login-Delay greift (Standard: 3)
* **login_delay_after_fail:** Länge des Login-Delays in Sekunden (Standard: 2).
