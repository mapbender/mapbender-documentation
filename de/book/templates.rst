.. _templates:

Wie werden eigene Vorlagen (templates) erzeugt?
################################################################

Mapbender3 beinhaltet bereits erzeugte Anwendungs-Vorlagen. Häufig sollen eigene Vorlage mit Ihrem eigenen Corporate Design verwendet werden. Die bereits vorhandenen Vorlagen befinden sich zu Demonstrationszwecken im  Mapbender CoreBundle (application/mapbender/src/Mapbender/CoreBundle). Für eigene Vorlagen sollten Sie ein eigenes Bundle verwenden, um Probleme bei einem Upgrade zu vermeiden.


Wie werden eigene Vorlagen (templates) erzeugt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Folgende vier Schritte sind nötig:

* eigene twig-Datei erzeugen
* eigene css-Datei erzeugen
* eigene php-Datei erzeugen, um die Vorlage zu registrieren
* Verwenden der neuen Vorlage in der mapbender.yml oder über die Administration


Eigene twig-Datei erzeugen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Die twig-Dateien sind im folgenden Verzeichnis gespeichert:

* mapbender\\src\\Mapbender\\CoreBundle\\Resources\\views\\Template

Kopieren Sie eine existierende twig-Datei, speichern Sie diese unter einem neuen Namen und verändern Sie den Inhalt, z.B. die Farbe.

.. code-block:: bash

 cd mapbender/src/Mapbender/CoreBundle/Resources/views/Template 
 cp base.html.twig demo.html.twig


Eigene css-Datei erzeugen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Die css-Dateien befinden sich im Verzeichnis: 

* application/mapbender/src/Mapbender/CoreBundle/Resources/public/css. 

Erzeugen Sie eine eigene css-Datei und verändern Sie den Inhalt.

.. code-block:: bash

 cd fom/src/FOM/CoreBundle/Resources/public/css/frontend

 # css für den Frame (Container Position)
 cp fullscreen.css demo.css

 # css für Farben, Fonts, Icons
 cp mapbender3_theme.css mapbender3_theme_demo.css


Registrieren Sie Ihre Vorlage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Um Ihre Vorlage zu registrieren, müssen Sie eine Datei erzeugen unter: 

* mapbender/src/Mapbender/CoreBundle/Template 

.. code-block:: bash

 cd mapbender/src/Mapbender/CoreBundle/Template
 cp Fullscreen.php Demo.php

Abschließend müssen Sie den vollständigen Classnamen der neuen Vorlage in der neu erzeugten php-Datei zu den Funktionen getAssets und render hinzufügen:

.. code-block:: php

    public function getAssets($type)
    {
        parent::getAssets($type);
        $assets = array(
            'css' => array('@FOMCoreBundle/Resources/public/css/frontend/mapbender3_theme_demo.css,@FOMCoreBundle/Resources/public/css/frontend/demo.css'),
            'js' => array(),
        );

        return $assets[$type];
    }


.. code-block:: php

    public function render($format = 'html', $html = true, $css = true,
            $js = true)
    {
        $templating = $this->container->get('templating');
        return $templating
                        ->render('MapbenderCoreBundle:Template:demo.html.twig',
                                 array(
                            'html' => $html,
                            'css' => $css,
                            'js' => $js,
                            'application' => $this->application));
    }

Bearbeiten Sie Ihre twig-Datei und verweisen Sie auf die neuen css-Dateien:

.. code-block:: yaml

  <link rel="stylesheet" href="{{ asset('bundles/fomcore/css/frontend/mapbender3_theme.css') }}">
  <link rel="stylesheet" href="{{ asset('bundles/fomcore/css/frontend/fullscreen.css') }}">

verändern in
  
  .. code-block:: yaml

  <link rel="stylesheet" href="{{ asset('bundles/fomcore/css/frontend/mapbender3_theme_demo.css') }}">
  <link rel="stylesheet" href="{{ asset('bundles/fomcore/css/frontend/demo.css') }}">

Verwenden der neuen Vorlage in der mapbender.yml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Jetzt kann die Vorlage in der mapbender.yml, in der die Anwendung konfiguriert wird, verwendet werden. 

Sie finden die mapbender.yml unter:

* app/config

.. code-block:: yaml
  
  "template:  Mapbender\CoreBundle\Template\Demo"


Verwenden der neuen Vorlage in der Mapbender Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Wenn Sie eine neue Anwendung mit der Mapbender3-Administration erzeugen, können Sie eine Vorlage (Template) auswählen.

Bevor Ihre neue Vorlage angezeigt wird, muss diese registriert werden:

* mapbender/src/Mapbender/CoreBundle/MapbenderCoreBundle.php

.. code-block:: yaml

    public function getTemplates()

    {
        return array(
            'Mapbender\CoreBundle\Template\Fullscreen',
            'Mapbender\CoreBundle\Template\Demo'
            );
    }


Jetzt sollte die neue Vorlage in der Liste erscheinen.

Wie kann das Design verändert werden?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Die folgenden Dateien müssen bearbeitet werden:

* twig - verändert die Struktur (z.B. - Löschen einer Komponente wie die Sidebar)
* mapbender3_theme_demo.css - verändert die Struktur - Position und Größe des Inhalts oder des Footers
* demo.css - verändert die Farben, Icons, Schriften

Hinweis: 
In der demo.css ist der Anfang der Datei bezogen auf den Browser. Dieser Teil darf nicht editiert werden. Den Teil, den Sie bearbeiten dürfen, beginnt bei Zeile 430.


Probieren Sie es aus
~~~~~~~~~~~~~~~~~~~~~~~~
* Verändern Sie die Farbe oder ein Icon.
* Verändern Sie die Größe Ihres Icons.
* Verändern Sie die Farbe der Toobar.
* Verwenden Sie ein Bild anstatt eines Schrift-Icons für einen Button.
* Verändern Sie die Position der Übersicht.
* Schauen Sie in die Workshop-Dateien, um zu sehen wie es funktioniert.

