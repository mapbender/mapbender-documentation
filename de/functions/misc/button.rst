.. _button_de:

Button
******

Dieses Element stellt ein Button-Modul bereit. Einige Elemente wie die `Legende <../elements/legend.html>`_, `Layertree (Layerbaum) <layertree.html>`_, `FeatureInfo (Infoabfrage) <../elements/feature_info.html>`_, `Linien- und Flächenberechnung <../elements/ruler.html>`_ und der `Druck <../elements/printclient.html>`_ benötigen einen Button, um einen Dialog anzuzeigen oder um aktiviert zu werden, wenn das Element nicht in einem Frame definiert wurde.

Buttons können optional gruppiert werden, so dass nur ein Button in der Gruppe aktiviert ist. Dieses wird im Gruppen-Parameter eingestellt.
Es kann außerdem ein Button definiert werden, der sich auf eine Webseite oder ein Script bezieht und bei Aktivierung zu diesem weiterleitet. Bei dem Parameter *Target* stehen nur Funktionen zur Auswahl, die vorher in der Anwendung unter dem Reiter *Layouts* entweder in den Content oder den Footer eingebunden wurden.

Konfiguration
=============

.. image:: ../../../figures/de/button_configuration.png
     :scale: 80

* **Beschriftung anzeigen (Show button label):** Schaltet die Beschriftung des Buttons an/aus.
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Icon:** Symbol des Buttons, basierend auf einer CSS Klasse.
* **Target:** Zielelement (Titel(ID)) des Buttons, das bei Anklicken des Buttons ausgelöst wird. (Bswp.: Drucken; hier wird eine Dropdown-Liste aller Features angezeigt, welche vorher in Content, Sidepane oder Footer konfiguriert wurden)
* **Click:** Bezieht sich auf eine Webseite oder ein Skript (z.B.: http://mapbender3.org). Bei Klick auf den Button öffnet sich die angegebene Webseite.
* **Group:** Hiermit kann das Element einer Gruppe hinzugefügt werden. Aus dieser Gruppe können nicht mehrere Buttons gleichzeitig aktiviert sein. Wird ein anderer Button aus der Gruppe ausgewählt, wird der vorher ausgewählte automatisch deaktiviert.
* **Action:** Methode, die aufgerufen wird, wenn der Button aktiviert wird (z.B. activate oder open). 
* **Deactivate:** Methode, die aufgerufen wird, wenn der Button deaktiviert wird (z.B. deactivate).



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
Buttons können für Features eingebunden werden, die vorher im Content konfiguriert wurden. Beispielsweise die Legende, die Informationsabfrage oder die Linien- und/oder Flächenmessung können über Buttons angesprochen werden.

Button für die Legende
-----------------------

Für Karten sind Legenden sehr hilfreich, da sich so die Betrachter der Karte über den Inhalt informieren können. Die Legende ist in diesem Anwendungsbeispiel im Content als Element type "dialog" eingebunden. Wie eine Legende konfiguriert wird, wird in der Dokumentation unter `Legende <../elements/legend.html>`_ beschrieben.
Der Button für eine Legende wird wie folgt eingebunden:

Zuerst muss über das ``+`` - Zeichen in der Anwendung unter dem Reiter Layouts im Toolbar Bereich das Element Button ausgewählt werden.

.. image:: ../../../figures/de/add_toolbar.png
     :scale: 80
     
Nach Auswahl des Elements Button öffnet sich der Dialog "Element hinzufügen – Button". Hier werden die Einstellungen zur Konfiguration des Buttons vorgenommen.
Die Bezeichnung des Buttons zum Öffnen der Legende wird im Feld *Title* eingetragen und lautet hier "Legende". Sobald die Maus über den Button geführt wird, erscheint der Text "Legende öffnen", da dies im Feld *Tooltip* angegeben wurde. Als Icon können nun eine Vielzahl an Möglichkeiten ausgewählt werden. In diesem Falle, wird die Option "Legend" gewählt.

.. image:: ../../../figures/de/button_legend_dialog_icon.png
     :scale: 80
     
Nun wird im Feld *Target* gewählt, welche vorher definierte Funktion mit dem Button angesprochen werden soll. Die Liste, die dort als Dropdown-Menü erscheint, beinhaltet alle Funktionen, die vorher im Content, in der Sidepane oder im Footer konfiguriert wurden. Da hier der Button für die Legende konfiguriert wird, wird ebenfalls die Option "Legend" gewählt.

.. image:: ../../../figures/de/button_legend_dialog_target.png
     :scale: 80
     
Die restlichen Felder (*Click, Group, Action* und *Deactivate*) werden für diesen Fall leer gelassen. Per default ist hier für die Methode, die aufgerufen wird, wenn der Button aktiviert wird (*Action*), "open" konfiguriert. Das bedeutet die Legende wird bei klicken auf den Button in einem Dialogfeld geöffnet. Der Button sieht in der Mapbender-Anwendung wie folgt aus:

.. image:: ../../../figures/de/button_legend_text.png
     :scale: 80
     
Da im Konfigurationsdialog zum Button Element bei *Beschriftung anzeigen* ein Haken gesetzt war, wird die Beschriftung neben dem Icon angezeigt. Ist dieser Haken nicht aktiviert, sieht der Button wie folgt aus:

.. image:: ../../../figures/de/button_legend_symbol.png
     :scale: 80
     
Wäre hier im Feld *Icon* statt "Legend", "Legend (Font Awesome)" ausgewählt und die Beschriftung aktiviert worden, sehe der Button wie folgt aus:

.. image:: ../../../figures/de/button_legend_font_awesome_text.png
     :scale: 80
     
Nun öffnet sich bei klicken auf den Button die Legende in einem Dialogfeld. Der Aufruf der Legende über den Button funktioniert lediglich nur dann, wenn das Element Legende als *Element type* "dialog" konfiguriert wurde. Der *Element type* "blockelement" sollte lediglich dann verwendet werden, wenn die Legende als festes, direkt sichtbares Element beispielsweise in die Sidepane integriert werden soll.


Button für Linien- und Flächenmessung
--------------------------------------

Auch die Funktionen der Linien- und Flächenmessung können über Buttons in eine Anwendung eingebunden werden. Auch in diesem Fall ist es notwendig, dass diese Funktionen schon in Content, Sidepane oder Footer konfiguriert sind.
In diesem Konfigurationsbeispiel sollen beide Buttons einer Gruppe zugeordnet werden, so dass entweder Linien oder Flächen gemessen werden können, jedoch nicht beides gleichzeitig.
Der Button wird, wie schon der Legendenbutton, über das ``+`` - Zeichen in der Anwendung unter dem Reiter *Layouts* im Toolbar Bereich eingebunden. Es erscheint der Dialog "Element hinzufügen – Button", der für die Konfiguration des Buttons für die Linienmessung wie folgt aussehen kann:

.. image:: ../../../figures/de/button_distance_dialog.png
     :scale: 80
     
Im Anwendungsbeispiel ist die Bezeichnung (*Title*) des Buttons "Linienmessung". Der Text "Linien messen" wird beim Platzieren der Maus auf dem Button angezeigt. Als *Icon* wird "Line ruler" gewählt und als *Target* das vorher im Content erstellte Element "Distance". Das Element "Distance" wurde mithilfe der Funktion Linien-/Flächenmessung erstellt und als Linienmessung konfiguriert. Wie das Element Linien-/Flächenmessung konfiguriert wird, wird in der Dokumentation unter `Linien-/Flächenmessung <../elements/ruler.html>`_ beschrieben.

Um die Gruppierung mit der Flächenmessung möglich zu machen, wird im Feld *Group* ein Gruppenname vergeben. Hier lautet die Bezeichnung der Gruppe "messen". Dieser Gruppenname wird analog auch bei dem Button für die Flächenmessung eingetragen. Im Feld *Deactivate* wurde "deactivate" eingetragen. So wird die Funktion der Flächenmessung bei erneutem klicken auf den Button beendet.
Der Button für die Flächenmessung wird analog eingebunden. Der Dialog der Konfiguration des Buttons sieht im Konfigurationsbeispiel wie folgt aus:

.. image:: ../../../figures/de/button_area_dialog.png
     :scale: 80

Zu beachten ist besonders das Feld *Group* mit dem Namen der Gruppe, der mit dem Eintrag im Feld *Group* des Buttons Linienmessung übereinstimmen muss. Beide Buttons können in der Anwendung wie folgt aussehen:

.. image:: ../../../figures/de/button_measure.png
     :scale: 80

Ist der Button Linienmessung aktiv, sieht er wie folgt aus:

.. image:: ../../../figures/de/button_measure_activated.png
     :scale: 80

Sobald nun auf den Button Flächenmessung geklickt wird, wird die Funktion Linienmessung beendet und die Funktion Flächenmessung aktiviert.


YAML-Definition:
----------------

.. code-block:: yaml

    title:        # Titel
    tooltip:      # Text des Tooltips
    icon: ~       # Symbol verwendete CSS Klasse
    label: true   # false/true, um den Button zu beschriften. Der Standardwert ist true.
    target: ~     # Titel (Id) des Zielelements
    click:        # bezieht sich auf eine Webseite oder ein Skript, z.B.: http://mapbender.org
    group: ~      # Gruppe, in die der Button eingefügt werden soll. Nur ein Button pro Gruppe kann aktiviert sein.
    action: ~     # Methode, die aufgerufen wird, wenn der Button aktiviert wird. 
    deactivate: ~ # Methode, die aufgerufen wird, wenn der Button deaktiviert wird

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\Button
* **Widget:** mapbender.mbButton (mapbender.element.button.js)
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

Keine.

JavaScript API
==============

activate
--------

Aktiviert den Button. Wird über einen Klick aufgerufen, wenn der Button deaktiviert ist.

deactivate
----------

Deaktiviert den Button. Wird über einen Klick aufgerufen, wenn der Button aktiviert ist oder wenn ein anderer Button der gleichen Gruppe aktiviert ist.

JavaScript Signals
==================

Keine.

