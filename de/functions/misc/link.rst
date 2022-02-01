.. _link_de:

Link
****

Dieses Element stellt ein Button-Modul bereit, über das eine Webseite oder ein Skript verlinkt werden kann. 

Konfiguration
=============

.. image:: ../../../figures/de/link_configuration.png
     :scale: 80

* **Beschriftung anzeigen:** Schaltet die Beschriftung des Buttons an/aus (Standard: an).
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Target:** Zielelement (Titel), das bei Anklicken des Buttons ausgelöst wird.
* **Group:** Hiermit kann das Element einer Gruppe hinzugefügt werden. Aus dieser Gruppe können nicht mehrere Buttons gleichzeitig aktiviert sein. Wird ein anderer Button aus der Gruppe ausgewählt, wird der vorher ausgewählte automatisch deaktiviert.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Icon:** Symbol des Buttons, basierend auf einer CSS-Klasse.


Icons
-----

Für einige Symbole können zwei verschiedene Icon-Typen ausgewählt werden.

* Ein Symbol basierend auf einer Grafik (z.B. "About"),
* Ein Symbol basierend auf einer Schrift (z.B. "About (Font Awesome)").

Letztere basieren auf einem `IconSet <https://github.com/mapbender/icons>`_, das mit dem Mapbender als Modul ausgeliefert wird. Wir empfehlen die Verwendung der Symbole aus dieser Bibliothek.


Mehr Informationen dazu unter:

* https://github.com/mapbender/icons
* http://rawgit.com/mapbender/icons/master/demo.html

Konfigurationsbeispiele:
=========================
Je nach Ziel der Anwendung werden unterschiedliche Buttons benötigt, die verschiedene Funktionen bieten. Diese können nach Bedarf und Wunsch integriert werden. 
Buttons können für Features eingebunden werden, die vorher im Content konfiguriert wurden. Beispielsweise können die Legende oder die Linien- und/oder Flächenmessung über Buttons angesprochen werden:

Link zur Mapbender-Webseite
---------------------------

Zuerst muss über das ``+`` - Zeichen in der Anwendung unter dem Reiter Layouts im Toolbar Bereich das Element Button ausgewählt werden.

.. image:: ../../../figures/de/add_toolbar.png
     :scale: 80
     
Nach Auswahl des Elements Link öffnet sich der Dialog "Element hinzufügen – Link". Hier werden die Einstellungen zur Konfiguration des Elements vorgenommen.

Im Feld *Title* definieren Sie den Text, der rechts neben dem Button angezeigt werden soll. 
Hierzu muss *Beschriftung anzeigen* aktiviert sein. Sie können im Feld "Tooltip" einen Text definieren, der erscheinen soll, wenn die Maus über den Button fährt. 
Unter *Icon* können Sie über die Auswahl einen der möglichen Button-Symbole ausgewählen.

... image:: ../../../figures/de/link_configuration.png
     :scale: 80


YAML-Definition:
----------------

.. code-block:: yaml

    title: Link                              # Titel
    class: Mapbender\CoreBundle\Element\Button
    tooltip: Besuchen Sie diese Webseite     # Text des Tooltips
    icon: iconInfoActive                     # Symbol verwendete CSS Klasse
    label: true                              # false/true, um den Button zu beschriften. Der Standardwert ist true.
    click: https://mapbender.org             # bezieht sich auf eine Webseite oder ein Skript, z.B.: http://mapbender.org
