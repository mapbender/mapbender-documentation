Benutzer
========

Benutzer werden als FOM\\UserBundle\\Entity\\User implementiert und im
Datenbank Repository gespeichert. Die Entität hält nur die notwendigen
Informationen über einen Nutzer vor, komplexere Benutzerdaten sollten in
Benutzerprofilen hinterlegt werden (TBD).

Das Bundle enthält alle Mittel um Benutzer durch einen Administrator zu
verwalten als auch das eigene Registrieren eines Nutzes sowie das
Zurücksetzen des eigenen Passwortes.

Der Benutzer mit der ID 1 ist besonders, da dieser Benutzer bei der
Installation erstellt wird und immer alle Rechte hat. Falls alle Stricke
reißen, können Sie mit diesem Benutzer alles verwalten. Und falls Sie gar
die Anmeldedaten vergessen haben sollten, können Sie über ein app/console
Kommando den Benutzer zurücksetzen: fom:user:resetroot.


Login Fehler
------------

Fehlerhafte Logins werden mit der Meldung "Login fehlerhaft"
kommentiert. Aus Sicherheitsgründen wird nicht genannt, ob es am falschen
Loginnamen oder falschen Passwort liegt. Login Fehler schließen den Account
nicht dauerhaft aus. Vielmehr wird der Account für eine bestimmte Zeit
ausgeschlossen (gelockt).

Die config.yml ermöglicht die Anpassung des Verhaltens:

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
   

* **auto_create_log_table:** Angabe zur Rückwärtskompatibilität (Default: true).
* **login_check_log_time:** Angabe zur Bereinigung der Login-Failure Tabelle (Default: -5 minutes)
* **login_attempts_before_delay:** Anzahl der Login Versuche, bevor das Login-Delay greift (Default: 3)
* **login_delay_after_fail:** Länge des Login-Delays in Sekunden (Default: 2).
