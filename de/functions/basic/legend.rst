.. _legend_de:

Legende
*******

Dieses Element zeigt eine Legende der Layer an, die in der Karte dargestellt werden. Dabei wird jeder einzelne Layer mit seinen Punkten, Flächen und Linien aufgelistet.

.. image:: ../../../figures/legend.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/legend_configuration.png
     :scale: 80


* **Automatisches Öffnen:** true, wenn die Legende beim Start der Anwendung geöffnet werden soll, der Standardwert ist false.
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt. Der Titel wird außerdem neben dem Button angezeigt, wenn "Beschriftung anzeigen" aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Element type:** Anzeige als Dialog- oder Blockelement, Standard ist Dialog.
* **Display type:** akkordeonartige Anzeige oder Liste. Standard ist Liste.
* **Target:** ID des Kartenelements, auf das sich das Element bezieht.
* **Titel der Datenquelle anzeigen:** zeigt den WMS Titel, der Standardwert ist true.
* **Titel der Ebene anzeigen:** zeigt den Layertitel, der Standardwert ist true.
* **Titel der gruppierten Ebenen anzeigen:** zeigt den Gruppenlayertitel für gruppierte Layer, der Standardwert ist true.

Für das Element wird ein Button oder die Sidepane verwendet. Zu der Konfiguration des Buttons besuchen sie die Dokumentationsseite unter `Button <../misc/button.html>`_.


Konfigurationsbeispiele
=======================

Legende in der Sidepane
-----------------------
Die Legende in der Sidepane wird über das ``+`` -Zeichen in der Anwendung unter Layouts, Sidepane eingebunden.

.. image:: ../../../figures/de/add_sidepane.png
     :scale: 80

Im Dialogfeld wird das Element "Legende" ausgewählt. Anschließend öffnet sich der Konfigurationsdialog "Element hinzufügen – Legende".

.. image:: ../../../figures/de/legend_example_sidepane_dialog.png
     :scale: 80

Das hier konfigurierte Element hat den Titel "Legende". Es entspricht dem *Element type* "blockelement", da es in der Sidepane fest eingebunden ist. Der *Display type* ist "list" und das *Target* die "Hauptkarte". Die Legende öffnet sich automatisch (Häkchen bei *Automatisches Öffnen*). Der Titel der Ebenen wird angezeigt sowie der Titel der gruppierten Ebenen (Häkchen bei *Titel der Ebene anzeigen* und *Titel der gruppierten Ebene anzeigen*).

Diese Konfiguration ergibt folgendes Ergebnis in der Anwendung:

.. image:: ../../../figures/legend_example_sidepane.png
     :scale: 80

Es wird empfohlen, dass die Legende immer als "blockelement" eingebunden wird, wenn diese in der Sidepane angezeigt werden soll. Wird sie als *Element type* "dialog" eingebunden, öffnet sich ein Dialogfeld und die Legende wird nicht in der Sidepane angezeigt. Lediglich die Überschrift "Legende" ist zu sehen. Sofern dieser Dialog geschlossen wurde, ist dieser nicht mehr aufrufbar. Falls die Legende in der Toolbar eingebunden werden soll, empfiehlt es sich diese über einen Button zu konfigurieren und nicht über das Element Legende.

Legende in der Toolbar
-----------------------
Die Legende kann auch als Button in der Toolbar eingebunden werden. Hierfür muss zuerst das Element Legende in der Anwendung unter dem Reiter Layouts im Content integriert werden.

.. image:: ../../../figures/de/add_content.png
     :scale: 80

Für das Konfigurationsbeispiel wurden folgende Einstellungen gewählt:

.. image:: ../../../figures/de/legend_example_toolbar_dialog.png
     :scale: 80

Wichtig ist hier, den *Element type* auf "dialog" einzustellen. Für das Konfigurationsbeispiel wurde das Häkchen bei *Automatisches Öffnen* entfernt, sodass sich die Legende nur bei aktivem Klicken auf den Button öffnet.
Sobald dieses Element im Content eingebunden wurde, muss ein Button in der Toolbar eingefügt werden. Die Konfiguration von Buttons wird in der Mapbender-Dokumentation unter `Button <../misc/button.html>`_ beschrieben.

Die Konfiguration eines Buttons für die Legende kann wie folgt aussehen:

.. image:: ../../../figures/de/legend_example_button.png
     :scale: 80

Mit diesen Einstellungen sieht das Ergebnis in der Anwendung wie folgt aus:

.. image:: ../../../figures/de/legend_example_toolbar.png
     :scale: 80

In der Toolbar ist der Button für das Legenden-Element zu sehen. Sobald auf den Button geklickt wird, öffnet sich das Dialogfeld und zeigt die Legende an.

Inwiefern sich die Aktivierung bzw. Deaktivierung einzelner Haken auf die Legende auswirkt, ist hier zu sehen:

.. image:: ../../../figures/de/legend_example_toolbar_checkboxes.png
     :scale: 80