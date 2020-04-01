.. _helpsites_de:

Wie werden eigene Hilfe-Seiten erzeugt?
#######################################

Hinzufügen neuer Hilfeseiten
****************************

Die Anpassung der bestehenden Hilfeseiten ist möglich. Dafür muss man jedoch beachten, dass Änderungen wieder unter Versionskontrolle zurückfließen müssen. Bei jeder Änderung sollte das Web-Verzeichnis neu ausgespielt und das Cache-Verzeichnis geleert werden, da die Oberflächen dort gespeichert werden.

.. code-block:: php

    #Assets installieren für das Web-Verzeichnis
    app/console assets:install web --symlink --relative

    #Cache-Verzeichnis leeren (prod und dev Ordner)
    rm -rf app/cache/*

Die Hilfeseiten werden über den folgenden Syntax aufgerufen:

.. code-block:: php

    [Mapbender-URL] + /help/
    z.B. https://my-mapbender.com/mapbender/help/

Neue Hilfeseiten können über die Datei HelpController.php eingebunden werden. Für die Einbindung einer neuen Seite an der richtigen inhaltlichen Stelle muss die Einrückung in der bestehenden Struktur korrekt sein. Neue Hilfeseiten müssen zusätzlich in dem view-Ordner angelegt werden und in der Form [dateiname].html.twig abgespeichert werden.

.. code-block:: php

    cd /application/src/Mapbender/HelpBundle/Controller/HelpController.php

    #Beispiel für den Syntax bei der Einbindung einer Seite für die Linkliste im Footer (Datei HelpController)

            'Benutzeroberfläche' => array(
                [...]
                'Fußleiste' => array(
                    'Koordinatenanzeige'        => array(),
                    'Koordinatensystemauswahl'  => array(),
                    'Linkliste'                 => array(),
                    'Maßstabsauswahl'           => array(),

    # neue Seiten anlegen
    cd application/src/Mapbender/HelpBundle/Resources/views/Pages/
    touch linkliste.html.twig

    # Über die Angabe des Titels wird die Seite in der Übersicht gefunden:

    {% set title = "Linkliste" %}

    #Assets installieren für das Web-Verzeichnis
    app/console assets:install web --symlink --relative

    #Cache-Verzeichnis leeren (prod und dev Ordner)
    rm -rf app/cache/*


Bearbeiten bestehender Hilfeseiten
**********************************
Für die Bearbeitung bestehender Hilfeseiten kann die jeweilige Datei im view-Ordner angepasst werden.

.. code-block:: php


    cd application/src/Mapbender/HelpBundle/Resources/views/Pages
    #Anpassen bestehender Datei, z.B. benutzeroberflaeche.html.twig

    #Assets installieren für das Web-Verzeichnis
    app/console assets:install web --symlink --relative

    #Cache-Verzeichnis leeren (prod und dev Ordner)
    rm -rf app/cache/*


Anpassen des Designs der Hilfeseiten
************************************
Die Designvorgaben können nach den eigenen Wünschen angepasst werden. Diese werden über css-Dateien für die Hilfeseiten vorgegeben.

.. code-block:: php

    cd application/src/Mapbender/HelpBundle/Resources/public
    # wichtige Vorgaben stehen in der Datei help.css

    #Assets installieren für das Web-Verzeichnis
    app/console assets:install web --symlink --relative

    #Cache-Verzeichnis leeren (prod und dev Ordner)
    rm -rf app/cache/*


Referenzieren von Bildern der Hilfeseiten
*****************************************
Bestehende Bilder werden fest im images-Ordner abgelegt und von den Dateien aus zugewiesen. Für den Austausch bestehender Bilder oder die Einbindung weiterer Bilder kann hier eine Anpassung erfolgen.

.. code-block:: php

    cd application/src/Mapbender/HelpBundle/Resources/public/images

    #Verweis in den Hilfeseiten, z.B. bei der Fußleiste
        <img src="{{ asset('bundles/mapbenderhelp/images/fussleiste.png') }}" alt="Fußleiste" title="Fußleiste"/>
