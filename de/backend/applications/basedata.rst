.. _basedata_de:

Basisdaten
##########

Die Basisdaten bestimmen die grundlegenden Informationen und Einstellungen einer Anwendung. Die Basisdaten sind über eine Maske in den Anwendungseinstellungen im :ref:`backend_de` konfigurierbar. Mehr Details zu den verschiedenen Möglichkeiten der Anwendungserstellung finden Sie im :ref:`Schnellstart <quickstart_de>`.


Konfiguration
-------------

* **Titel**: Titel der Anwendung, frei ausfüllbares Textfeld.

* **URL Titel**: Titel der Anwendung als URL, frei ausfüllbares Textfeld. Keine Umlaute und Sonderzeichen erlaubt: URL Titel muss sich nach den Standards der festgelegten URL-Syntax richten.

* **Vorschaubild**: Aus dem Dateiverzeichnis hochladbare Bilddatei, die als Vorschaubild in der Anwendungsübersicht angezeigt wird. Klicken Sie auf den Button "*Datei auswählen"*.

* **Beschreibung**: Beschreibung der Anwendung, frei ausfüllbares Textfeld.

* **Kartenzustand merken**: Speichert sitzungsübergreifend den Zustand bestimmter Kartenparameter und -einstellungen. Weitere Informationen finden Sie auf der Seite zu den :ref:`Share-Elementen <persistent_map_view_de>`.

* **Ladescreen zeigen**: Zeigt ein Bild bei Anwendungsstart an, das die Ladezeit graphisch überbrückt.

  .. image:: /figures/de/mapbender_create_application.png
     :width: 80%


Konfigurieren des Ladescreens
-----------------------------

Der Ladescreen verbessert das Erscheinungsbild Ihrer Anwendung, indem er ein Logo und den Anwendungstitel anzeigt.
Um den Ladescreen zu konfigurieren, befolgen Sie die folgenden Schritte:

1. Öffnen Sie die Datei ``parameters.yaml`` in Ihrer Mapbender-Installation. Weitere Informationen zur Datei selbst finden Sie unter :ref:`yaml_de`.
2. Erstellen Sie den Schlüssel ``branding.splashscreen_image`` oder suchen Sie danach.
3. Definieren Sie den Ladescreen mithilfe einer der folgenden Methoden:

  - **Dateipfad**: Geben Sie einen einzelnen Dateipfad relativ zum Verzeichnis `application/public` in Ihrer Mapbender-Installation an.

   .. code-block:: yaml

    parameters:
      branding.splashscreen_image: path/relative/to/public/myimage.png

  - **Array**: Verwenden Sie ein Array, bei dem die Schlüssel dem Slug der Anwendung entsprechen. Dies ermöglicht eine individuelle Anpassung des Ladescreens für verschiedene Anwendungen. Verwenden Sie den Schlüssel ``default``, um ein Ersatzbild für Anwendungen bereitzustellen, die nicht explizit definiert sind.

   .. code-block:: yaml

    parameters:
      branding.splashscreen_image:
        sample_application: path/relative/to/public/sample_application.png
        another_application: path/relative/to/public/another_application.png
        default: path/relative/to/public/myimage.png


Wenn keine individuelle Bilddatei für den Ladescreen konfiguriert wurde, wird stattdessen das Logo (``branding.logo``) für alle Anwendungen verwendet.

Darüber hinaus ist das Erscheinungsbild des Ladescreens über CSS-Variablen anpassbar. Bitte wechseln Sie zu :ref:`CSS_de` für ein Beispiel.