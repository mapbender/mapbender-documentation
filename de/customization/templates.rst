.. _templates_de:

Wie werden eigene Style-Vorlagen (templates) erzeugt?
#####################################################

Mapbender beinhaltet bereits erzeugte Anwendungs-Vorlagen. Häufig sollen eigene Anwendungs-Vorlagen und Administrationsoberflächen mit Ihrem eigenen Corporate Design verwendet werden.
Die bereits vorhandenen Vorlagen befinden sich zu Demonstrationszwecken im Mapbender CoreBundle `Template` Verzeichnis. Um Probleme bei einem Upgrade zu vermeiden, sollten Sie für personalisierte Oberflächen ein eigenes Bundle verwenden.

Ab der Version 3.0.4.0 kann der Stil einer einzelnen Anwendung ebenfalls über den integrierten CSS-Editor angepasst werden. Die Dokumentation zum css-Editor finden Sie unter :doc:`Wie kann der Stil einer Anwendung mit dem CSS-Editor angepasst werden? <css>`.

Wie werden eigene Vorlagen erzeugt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schritte für die Einbindung:**

* Erzeugen eines eigenen Bundles
* Template PHP-Datei zur Registrierung der eigenen Vorlage erzeugen
* Erzeugen einer eigenen Twig-Datei
* Erzeugen eigener CSS-Datei(en)
* Registrierung des Bundles in der Datei app/AppKernel.php
* Verwenden der neuen Vorlage

Die neue Anwendungs-Vorlage kann über verschiedene Wege verwendet werden:

* Eintrag in der YAML-Datei von der Anwendung (applications/app/config/applications/\*.yml)
* Auswahl über die Administration bei einer neuen Anwendung
* Anpassung bestehender Anwendungen über die Änderung des Spalteneintrags ``template`` in der Datenbank in der Tabelle ``mb_core_application``.

Für die Einbindung der eigenen Vorlage wurde ein Workshop/DemoBundle vorbereitet, dass als Template für Anwendungen und für das Anpassen der Administrationsoberflächen verwendet werden kann. Laden Sie sich für die folgenden Schritte diese Dateien bitte über dem folgenden Link herunter:

* ab Version 3.0.6 unter https://github.com/mapbender/mapbender-workshop/tree/3.0.6
* vor Version 3.0.6 unter https://github.com/mapbender/mapbender-workshop/tree/master


Erzeugen eines eigenen Bundles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anwender-Bundles werden im src-Verzeichnis abgelegt.

Die Struktur kann wie folgt aussehen:

.. code-block:: bash

 src/Workshop/DemoBundle/
                    WorkshopDemoBundle.php
                    /Resources
                                  /public
                                         demo_fullscreen.css
                                         /image
                                             workshop.ico
                                             workshop_logo.png
                                             print.png
                                             ...
                                  /views
					/Template
                                             fullscreen_demo.html.twig
                        /Template
		                DemoFullscreen.php


Die folgenden Dateien müssen für das Design bearbeitet werden:

* twig - verändert die Struktur (z.B. - Löschen einer Komponente wie die Sidebar)
* demo_fullscreen.css  - verändert die Farben, Icons, Schriften


Erzeugen eines neuen Namespaces
*******************************

Die Datei WorkshopDemoBundle.php erzeugt den Namespace für das Bundle und referenziert auf das Template und zu den eigenen CSS-Dateien.


.. code-block:: php

    <?php
    namespace Workshop\DemoBundle;
    use Mapbender\CoreBundle\Component\MapbenderBundle;
    class WorkshopDemoBundle extends MapbenderBundle
    {
        public function getTemplates()
        {
            return array('Workshop\DemoBundle\Template\DemoFullscreen');
        }
        public function getElements()
        {
            return array(
            );
        }
    }
    ?>


Anlegen der eigenen Template-Datei
**********************************

In unserem Beispiel heißt die Template-Datei FullscreenDemo.php. Sie befindet sich unter src/Workshop/DemoBundle/Template/FullscreenDemo.php.

In der Template-Datei wir der Name des Templates, die Regionen die angelegt werden sollen sowie die verwendete Twig-Datei definiert.


.. code-block:: php

 <?php

 namespace Workshop\DemoBundle;

 use Mapbender\CoreBundle\Component\MapbenderBundle;

 class DemoFullscreen extends MapbenderBundle
 {
    ...
 }

 public static function getTitle()
 {
   return 'DemoFullscreen';
 }
 ....

 public static function listAssets()
 {
        $assets = array(
            'css' => array('@MapbenderCoreBundle/Resources/public/sass/template/fullscreen.scss','@WorkshopDemoBundle/Resources/public/demo_fullscreen.css'),
            'js'    => array(
                '/components/underscore/underscore-min.js',
            ...
            ),
            'trans' => array()
        );

    return $assets;
 }

 ...
 ->render('WorkshopDemoBundle:Template:demo_fullscreen.html.twig',...


Eigene Twig-Datei erzeugen
~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Twig-Dateien sind im folgenden Verzeichnis gespeichert:

* mapbender\src\Mapbender\CoreBundle\Resources\views\Template

Kopieren Sie eine existierende Twig-Datei, speichern Sie diese unter einem neuen Namen und verändern Sie den Inhalt, z.B. die Farbe.

.. code-block:: bash

 cd mapbender/src/Workshop/DemoBundle/Resources/views/Template


Verwenden Sie mapbender/src/Mapbender/CoreBundle/Resources/views/Template/fullscreen.html.twig und kopieren Sie diese nach fullscreen_demo.html.twig


Eigene CSS-Datei erzeugen (Anwendungen)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Erzeugen Sie eine leere CSS-Datei und geben Sie in dieser nur die CSS-Definitionen für Ihre Anwendungs-Vorlage an.
Ab der Mapbender Version 3.0.3.0 muss lediglich das CSS definiert werden, das vom Standard der Elemente abweicht.

Mit Hilfe von Firebug können Sie die bestehende Definition ermitteln, in Ihre CSS-Datei kopieren und hier anpassen.

Ihre CSS-Datei könnte wie folgt heißen: src/Workshop/DemoBundle/Resources/public/demo_fullscreen.css und die folgende Definition enthalten:

.. code-block:: css

 .toolBar {
   background-color: rgba(0, 29, 122, 0.8) !important;
 }

 .toolPane {
   background-color: rgba(0, 29, 122, 0.8) !important;
 }

 .sidePane {
   overflow: visible;
   background-image: url("");
   background-color: #eff7e9;
 }

 .sidePane.opened {
     width: 350px;
 }

 .logoContainer {
   background-color: white !important;
   background-image: url("") !important;
   -webkit-box-shadow: 0px 0px 3px #0028AD;
   -moz-box-shadow: 0px 0px 3px #0028AD;
   box-shadow: 0px 0px 3px #0028AD;
 }

 .sidePaneTabItem {
    background-color: #0028AD;
 }

 .layer-opacity-handle {
     background-color: #0028AD;
 }

 .mb-element-overview .toggleOverview {
     background-color: #0028AD;
 }

 .button, .tabContainerAlt .tab {
     background-color: #0028AD;
 }

 .iconPrint:before {
   /*content: "\f02f"; }*/
   content:url("image/print.png");
 }

 .popup {
   background-color: #eff7e9;
   background-image: url("");
 }

 .pan{
   background-color: rgba(0, 93, 83, 0.9);
 }

Das Ergebnis der wenigen Zeilen CSS sieht dann so aus:

.. image:: ../../figures/workshop_application.png
     :scale: 80

Beim Laden der neuen Anwendung wird eine CSS-Datei im web/assets-Verzeichnis angelegt:

* web/assets/WorkshopDemoBundle__demo_fullscreen__css.css

Wenn Sie die CSS-Datei weiter bearbeiten müssen Sie die unter web/assets generierte Datei löschen, damit diese neu geschrieben wird und die Änderungen wirksam werden. Der Browser-Cache sollte ebenfalls geleert werden.

.. code-block:: bash

 sudo rm -f web/assets/WorkshopDemoBundle__demo_fullscreen__css.css



Styling der Administrationsseiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Passen Sie die vorhandenen CSS-Dateivorlagen für die unterschiedlichen Bereiche bitte an:

* login.css : Anpassung des Designs der Login-Oberfläche (Anmelde-Seite)
* manager.css : Anpassung des Designs der Verwaltungs/Administrations-Oberfläche (Anwendungsübersicht u.ä.)
* password.css : Anpassung des Designs der Passwort-Oberfläche (Passwort vergessen u.ä.)

Ab der Mapbender Version 3.0.3.0 muss lediglich das css definiert werden, das vom Standard der Administrationsoberfläche abweicht.

Mit Hilfe von Firebug können Sie die bestehende Definition ermitteln, in Ihre CSS-Datei kopieren und hier anpassen.

Auf die CSS-Dateien wird über das FOMManagerBundle und FOMUserBundle referenziert. Diese müssen unter app/Resources/ abgelegt werden. Die bereits enthaltenen Twig-Dateien überschreiben nach der erfolgreichen Einrichtung die Standard-Einstellungen (Vorgaben aus der manager.html.twig Datei).
Alternativ kann auch die bisherige Twig-Datei kopiert und angepasst werden.

.. code-block:: bash

 cp fom/src/FOM/ManagerBundle/Resources/views/manager.html.twig app/Resources/FOMManagerBundle/views/


Bei unveränderter Übernahme der Stylevorgaben sieht die Administration dann so aus:

.. image:: ../../figures/customization/workshop_administration.png
     :scale: 80


Registrieren Sie Ihre Vorlage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um Ihre Vorlage zu registrieren, müssen Sie eine Datei erzeugen unter:

* mapbender/src/Workshop/DemoBundle/Template/DemoFullscreen.php

.. code-block:: bash

 cd mapbender/src/Mapbender/CoreBundle/Template
 cp Fullscreen.php mapbender/src/Workshop/DemoBundle/Template/DemoFullscreen.php

Fügen Sie die neue CSS-Datei in der Funktion listAssets als letzten Eintrag ein:

.. code-block:: php


    public static function listAssets()
    {
        $assets = array(
            'css' => array('@MapbenderCoreBundle/Resources/public/sass/template/fullscreen.scss','@WorkshopDemoBundle/Resources/public/demo_fullscreen.css'),
            'js'    => array(
                '/components/underscore/underscore-min.js',
                '@FOMCoreBundle/Resources/public/js/widgets/popup.js',
                '@FOMCoreBundle/Resources/public/js/frontend/sidepane.js',
                '@FOMCoreBundle/Resources/public/js/frontend/tabcontainer.js',
                '@MapbenderCoreBundle/Resources/public/regional/vendor/notify.0.3.2.min.js',
                "/components/datatables/media/js/jquery.dataTables.min.js",
                '/components/jquerydialogextendjs/jquerydialogextendjs-built.js',
                "/components/vis-ui.js/vis-ui.js-built.js"
            ),
            'trans' => array()
        );
        return $assets;
    }


.. code-block:: php

    public function render($format = 'html', $html = true, $css = true, $js = true)
    {
        $templating = $this->container->get('templating');
        return $templating
                        ->render('WorkshopDemoBundle:Template:demo_fullscreen.html.twig',
                                 array(
                            'html' => $html,
                            'css' => $css,
                            'js' => $js,
                            'application' => $this->application));
    }



Verwenden der neuen Vorlage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bevor Ihre neue Vorlage angezeigt wird, muss diese registriert werden:

* mapbender/app/AppKernel.php

.. code-block:: php

 class AppKernel extends Kernel
 {
    public function registerBundles()
    {
        $bundles = array(
            // Standard Symfony2 bundles
            new Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
            ....

            // Extra bundles required by Mapbender/OWSProxy3
            new FOS\JsRoutingBundle\FOSJsRoutingBundle(),

            // FoM bundles
            new FOM\CoreBundle\FOMCoreBundle(),
            ...

            // Mapbender bundles
            new Mapbender\CoreBundle\MapbenderCoreBundle(),
            ...

	    new Workshop\DemoBundle\WorkshopDemoBundle(),

        );

Setzen Sie Schreibrechte für das web-Verzeichnis für Ihren Webserver-Benutzer.

.. code-block:: bash

    chmod ug+w web


Aktualisieren Sie das web-Verzeichnis. Jedes Bundle hat seine eigenen Assets - CSS Dateien, JavaScript Dateien, Bilder und mehr - diese müssen in das öffentliche web-Verzeichnis kopiert werden. Mit der Option symlink werden die Dateien nicht kopiert. Es wird stattdessen ein symbolischer Link erzeugt. Dies erleichtert das Editieren innerhalb des Bundles.

.. code-block:: bash

    app/console assets:install web
    oder
    app/console assets:install web --symlink --relative


Jetzt sollte beim Anlegen einer neuen Anwendung die neue Vorlage in der Liste erscheinen.


1. Einbindung in YAML-Anwendungen
*********************************

Jetzt kann die Vorlage in der mapbender.yml, in der die Anwendung konfiguriert wird, verwendet werden. Sie finden die mapbender.yml unter app/config/applications.

.. code-block:: yaml

  "template:   Workshop\DemoBundle\Template\DemoFullscreen"


2. Einbindung in neue Anwendungen
*********************************

Wenn Sie eine neue Anwendung mit der Mapbender-Administration erzeugen, können Sie eine Vorlage (Template) auswählen.


3. Einbindung in bestehende Anwendungen
***************************************

Für bereits existierende Anwendungen kann das Template über die Mapbender Datenbank in der Tabelle *mb_core_application* in der Spalte *template* angepasst werden.
Für das *WorkshopDemoBundle* wird hier statt des Eintrags *Mapbender\CoreBundle\Template\Fullscreen* der Eintrag *Workshop\DemoBundle\WorkshopDemoBundle* angegeben.


Anwendungsfälle
~~~~~~~~~~~~~~~

Wie kann das Logo verändert werden?
***********************************

Das Logo (Standard ist das Mapbender Logo) kann in der Datei parameters.yml angepasst werden. Diese Änderung wirkt sich global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

 server_logo:   bundles/workshopdemo/image/workshop_logo.png


Das Logo kann auch in der Twig-Datei angepasst werden:

.. code-block:: html

 <img class="logo" height="40" alt="Workshop Logo" src="{{ asset('bundles/workshopdemo/imgage/workshop_logo.png')}}" />


Wie kann der Anwendungstitel und das Favicon angepasst werden?
**************************************************************

Der Anwendungstitel und das Favicon kann auch in der Twig-Datei angepasst werden:

.. code-block:: yaml


 {% block title %}Workshop - {{ application.title }}{% endblock %}

 {% block favicon %}{{ asset('bundles/workshopdemo/imgage/workshop.ico') }}{% endblock %}



Wie können eigene Buttons eingebunden werden?
*********************************************

Mapbender verwendet Schrift-Icons auf der FontAwesome Collection:

.. code-block:: css

 @font-face {
   font-family: 'FontAwesome';
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?v=3.0.1");
   src: url("../../bundles/fomcore/images/icons/fontawesome-webfont.eot?#iefix&v=3.0.1") format("embedded-opentype"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.woff?v=3.0.1") format("woff"), url("../../bundles/fomcore/images/icons/fontawesome-webfont.ttf?v=3.0.1") format("truetype");
   font-weight: normal;
   font-style: normal;
 }


In der CSS-Datei können Sie zu den Icons der Schriftart folgendermaßen verweisen:

.. code-block:: css

  .iconPrint:before {
    content: "\f02f";
  }

Wenn Sie ein Bild nutzen möchten, legen Sie dieses am Besten in Ihrem Bundle ab und referenzieren es auf die folgende Art und Weise:

.. code-block:: css

  .iconPrint:before {
    content:url("imgage/print.png");
  }


Probieren Sie es aus
~~~~~~~~~~~~~~~~~~~~~

* Laden Sie das Workshop/DemoBundle herunter: https://github.com/mapbender/mapbender-workshop
* Ändern Sie die Farbe Ihrer Icons.
* Ändern Sie die Größe Ihrer Icons.
* Ändern Sie die Farbe der Toolbar.
* Benutzen sie ein Bild anstelle eines Font-Icons für Ihre Buttons.
* Verschieben Sie die Übersichtskarte auf die linke Seite.
* Schauen Sie in die Workshop-Dateien, um zu erfahren, wie das funktioniert.
