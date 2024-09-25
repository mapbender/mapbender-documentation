.. _css_de:

CSS-Editor
##########

Mapbender verfügt über einen CSS-Editor zur Anpassung des Stils (Farben, Größen, Icons, ...) einer Anwendung. Es ist möglich, zusätzliche CSS-Klassen zu definieren, die den Standardstil überschreiben. Sie können außerdem SCSS im Editor verwenden und auf eine SCSS-Datei in Ihrem Bundle verweisen.

.. image:: ../../../figures/de/css_editor.png
     :width: 100%

.. tip:: Mithilfe von Browser-Entwicklerwerkzeugen ist es möglich, Elemente zu identifizieren, ihre Klassen in den CSS-Editor zu kopieren und dort anzupassen.


Anwendungsbeispiel
==================

Bildlaufleiste zu Menü hinzufügen
---------------------------------
Wenn Sie das Schaltflächenmenü in der oberen Werkzeugleiste verwenden, können Sie festlegen, bei welcher Bildschirmgröße die Höhe reduziert und eine Bildlaufleiste angezeigt werden soll. Dies verbessert die Benutzerfreundlichkeit der Anwendung auf mobilen Geräten.

.. code-block:: css

  // Scrollbar in Toolbox
  .dropdown-menu {
    overflow-y: auto;
    max-height: calc(100vh - 100px);
  }


Die Menü-Funktion kann im **Layouts**-Tab des Backends gefunden werden: Klicken Sie auf den Zahnrad-Button und aktivieren anschließend das Kontrollkästchen **Menü für Schaltflächen generieren**.


Den Ladescreen individuell anpassen
-----------------------------------

Sofern der Ladescreen einer Anwendung über :ref:`basedata_de` aktiviert ist, ist es möglich, diesen weiter über CSS anzupassen.

.. code-block:: CSS

    :root {
        --primary: #079ee0;                                 /* Farbe des Ladeindikators */
        --splashscreen-border: none;                        /* Rand um den Startbildschirm-Dialog, der z.B. mit https://html-css-js.com/css/generator/border-outline/ generiert werden kann */
        --splashscreen-border-radius: 25px;                 /* Radius der abgerundeten Ecken um den Dialog */
        --splashscreen-background: rgba(255,255,255,0.8);   /* Hintergrundfarbe des Ladescreens */
        --splashscreen-fade-out-duration: 200ms;            /* Animationsdauer beim Ausblenden des Ladescreens */
    }