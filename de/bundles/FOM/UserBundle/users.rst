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

Login Fehler schließen den Account nicht dauerhaft aus. Vielmehr wird der
Account für eine bestimmte Zeit ausgeschlossen (gelockt), abhängig von der
Anzahl der fehlerhaften Login-Versuche in einem bestimmten Zeitraum. Die
Zeit, in der der Nutzer ausgeschlossen ist, wächst exponentiell mit der
Anzahl der Fehlversuche und startet bei einer Sekunde beim ersten
Fehlversuch:

    1. 1s
    2. 2s
    3. 4s
    4. 8s
    5. 16s
    6. 32s
    7. 64s
    8. 128s
    9. 256s
    10. ...


Nach dieser Zeit kann der Benutzer sich wieder anmelden.
