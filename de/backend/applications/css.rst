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