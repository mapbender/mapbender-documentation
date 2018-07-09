.. _cookieconsent_de:

Cookie-Banner
=============

(seit 3.0.7.0)

Anwendungen unterstützen die Anzeige eines Cookie-Banners, welches über die Mapbender Konfigurationsdatei eingerichtet werden kann. Wir nutzen den Code von `Cookie Consent <https://cookieconsent.insites.com/>`_, ohne dass dabei ein Aufruf ins Internet gestartet wird.

Das Banner erscheint in einer beliebigen Anwendung beim ersten Aufruf.

.. image:: ../../../figures/cookiebanner.png
           :scale: 80

Sobald die Mitteilung akzeptiert wurde, taucht das Banner so lange nicht auf, bis die Cookies im Webbrowser gelöscht worden sind. Mapbender ist abhängig von Cookies und dort wird die PHP-Session hinterlegt.


Konfiguration
-------------

Die Konfiguration findet in der ``app/config/config.yml`` Datei statt und gilt für die gesamte Mapbender Instanz. Innerhalb der Abschnitte ``twig`` und ``globals`` wird ein Eintrag ``cookieconsent`` hinzugefügt. Ist dieser Abschnitt nicht vorhanden, wird das Banner nicht angezeigt.

.. tip:: Nach dem Ändern der Parameter müssen sie die Inhalte des Cache-Verzeichnisses (``app/cache/\*``) löschen.

.. code-block:: yaml

   # Twig Configuration
   twig:
       [...]
       globals:
       [...]
        cookieconsent:
            backgroundColor: "#000000"
            backgroundTextColor: "#ffffff"
            buttonColor: "#f1d600"
            buttonTextColor: "#000000"
            message: "This website uses cookies to ensure you get the best experience on our website."
            dismissText: "OK"
            linkText: "Learn more"
            linkUrl: "http://www.myurl.loc/privacy-policy"
            theme: "classic"
            position: "bottom-right"
       [...]


Die Parameter orientieren sich dabei an den Parametern der Cookie Consent Vorlage.

- **backgroundColor:** Hintergrundfarbe des Banners in HEX-Code.
- **backgroundTextColor:** Farbe des Textes auf dem Banner in HEX-Code.
- **buttonColor:** Farbe der Schaltfläche in HEX-Code.
- **buttonTextColor:** Farbe des Textes auf der Schaltfläche in HEX-Code.
- **message:** Die Cookie-Meldung als Text in doppelten Anführungszeichen.
- **dismissText:** Der Schaltflächentext in doppelten Anführungszeichen.
- **linkText:** Der Text des Links. Geschrieben in doppelten Anführungszeichen.
- **linkUrl:** Die URL des Links, gewöhnlicherweise zu den Privacy Terms. Geschrieben in doppelten Anführungszeichen. 
- **theme:** Das Thema des Banners. Siehe die Cookie Consent Webseite.
- **position:** Die Position des Banners.  Siehe die Cookie Consent Webseite.
