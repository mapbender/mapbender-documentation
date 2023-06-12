.. _layouts_de:

 .. |mapbender-button-add| image:: ../../../figures/mapbender_button_add.png

 .. |mapbender-button-edit| image:: ../../../figures/mapbender_button_edit.png

 .. |mapbender-button-key| image:: ../../../figures/mapbender_button_key.png
  
Layouts
#######

In Layouts werden die Regionen einer Anwendung und die in ihnen enthaltenen Elemente aufgelistet.
Eine Übersicht über alle Elemente gibt es unter :ref:`functions_de`.

.. note:: Unterschiedliche Templates können durch unterschiedliche Regionen strukturiert sein.


Layout des Fullscreen Templates:

  * Obere Werkzeugleiste (Region für die Platzierung von Buttons, Links, HTML, ...)
  * Sidepane (Seitenleisten-Region für den Ebenenbaum, die Legende, die Suche, den Druck, HTML, ...)
  * Kartenbereich (Region für die Karte, die Maßstabsleiste, ...)
  * Fußzeile (Region für das Impressum, die Aktivitätsanzeige, die Maßstabsauswahl, ...)


Layout des Mobilen Templates:

  * Fußzeile (Region für das Copyright, die Aktivitätsanzeige, die Maßstabsauswahl, ...)
  * Kartenbereich (Region für die Karte, die Maßstabsleiste, ...)
  * MobilePane (Region für Dialoge wie den Ebenenbaum, die Legende, den Hintergrundwechsler, die Infoabfrage, ...)


Der |mapbender-button-add| Button rechts oberhalb des Bereichs ermöglicht das Hinzufügen von Elementen. Nach dem Klick auf den Button öffnet sich eine Dialogmaske, die die Auswahl eines Elements und dessen anschließende Konfiguration ermöglicht.

Alle eingebauten Funktionen lassen sich per Drag & Drop zwischen den Regionen verschieben.

Die Regionen können über den |mapbender-button-edit| Button in der oberen rechten Ecke individuell konfiguriert werden.

Die unterschiedlichen Regionen bieten folgende Konfigurationsmöglichkeiten:


Konfigurationsmöglichkeiten der Oberen Werkzeugleiste und Fußzeile
******************************************************************
Die Regionen der Oberen Werkzeugleiste und der Fußzeile bieten folgende Konfigurationsmöglichkeiten über den |mapbender-button-edit| Button an:

  * **Bildschirmtyp** (Alle, Mobil, Desktop. Standard: Alle) Bei dieser Option wird der Bereich für die nicht ausgewählte Geräteart ausgeblendet. *Alle* zeigt die Region auf allen Geräten an.
  * **Ausrichtung** (Links, Rechts, Zentriert. Standard: Rechts.): Die Ausrichtung definiert die Positionierung der Elemente innerhalb der Bereiche.
  * **Checkbox Schaltflächen zu Menü zusammenfassen**: Konfiguriert ein Ausklappmenü, welches die in den Bereich eingebundenen Elemente umfasst.
  * **Menütitel-Textfeld**: Mit dieser Textbox lässt sich dem Ausklappmenü eine Beschriftung zuweisen.

.. tip:: **Hinweis**: Das Ausklappmenü ist besonders sinnvoll, wenn die Anwendung für mobile Endgeräte ausgerichtet sein soll. Unter :ref:`CSS_de` findet sich ein Codebaustein, der die Bedienbarkeit bei Anwendungen mit vielen Elementen erhöht. 


Sidepane-Konfigurationsmöglichkeiten
************************************
Die Ansichtsoptionen für die Sidepane können im Sidepane-Bereich im Mapbender-Backend ausgewählt werden. Dazu genügt ein Klick auf den |mapbender-button-edit| Button:

.. image:: ../../../figures/de/sidepane_backend.png
    :alt: Mapbender Sidepane Konfiguration


* **Typ**: Siehe Funktionsbeschreibung unten.
* **Bildschirmtyp** (Alle, Mobil, Desktop. Standard: Alle) Bei dieser Option wird der Bereich für die nicht ausgewählte Geräteart ausgeblendet. *Alle* zeigt die Region auf allen Geräten an.
* **Breite** (in Pixeln, Standard: 350 px) Definiert über einen Pixelwert die Breite der Sidepane in der Anwendung.
* **Position** (Links, Rechts. Standard: Links) gibt an, ob die Sidepane am linken oder rechten Bildschirmrand angezeigt wird.
* **Geschlossen starten** (Standard: deaktiviert) hält nach Aktivierung die Sidepane bei Anwendungsstart eingeklappt. Sie ist über einen Button in der Anwendung nachträglich aus- & wieder einklappbar.

Die Option **Typ** zeigt die Sidepane-Elemente in unterschiedlichen Ansichten an:

  - ``Akkordeon`` zeigt alle hinzugefügten Elemente in Reitern.

  - ``Buttons`` zeigt alle hinzugefügten Elemente über Buttons.

  - ``Unformatiert`` verzichtet auf Styling-Optionen und zeigt die Elemente direkt und in der im Backend gewählten Reihenfolge untereinander an.


Element-Buttonleiste
********************
Jedem Element kann ein konfigurierter Button zugewiesen werden. Die Buttonleiste dient der Konfiguration dieser Buttons.
Dabei verfügen die Buttons über folgende Optionen:

.. image:: ../../../figures/mapbender_layouts_button_area.png
    :alt: Buttonleiste der Elemente


* **aktiv/inaktiv**: Ein aktives Element ist in der Anwendung freigeschaltet. Ein inaktives Element kann zwar bearbeitet werden, ist aber in der Anwendung ausgeblendet.
* **Auf Mobilgeräten anzeigen**: Zeigt Elemente nur auf mobilen Geräten an.
* **Auf großen Bildschrimen anzeigen**: Zeigt Elemente nur auf Desktop-Geräten an.
* **Bearbeiten**: Erlaubt die Anpassung des Elements.
* **ACL Element**: Erlaubt die Konfiguration von Element-Sichtbarkeiten bei bestimmten Berechtigungen.
* **Löschen**: Entfernt ein Element vom Back- und Frontend.


Bearbeiten
==========
Öffnet über den |mapbender-button-edit| Button die individuelle Konfigurationsmaske eines Elements. Diese finden Sie in der Dokumentation des jeweiligen Elements unter :ref:`functions_de`.


Acl Element
===========
Öffnet über den |mapbender-button-key| Button einen **Element sichern**-Dialog, der ein explizites Konfigurieren der :ref:`acl_de` Regel **View** für Benutzer und Gruppen ermöglicht.

Ist dies nicht konfiguriert, hat das Element keine expliziten Zugangsbeschränkungen und sollte allen Benutzern und Gruppen zur Verfügung stehen.

Sofern die **View**-Regel für bestimmte Benutzer oder Gruppen gesetzt ist, können ausschließlich dort Eingetragene auf das Element zugreifen.

Beschränken Sie den Zugriff, indem Sie Benutzer über den |mapbender-button-add| Button hinzufügen. Eine gesetzte Checkbox zeigt an, dass die benötigten Berechtigungen zur Verfügung stehen.

.. image:: ../../../figures/de/fom/acl_secure_element.png
     :width: 100%


Der Schlüssel wird nach erfolgreicher Rechtevergabe rot. Wenn Sie nun den Cursor über den Schlüssel halten, sehen Sie die Namen der berechtigten Nutzer in einem Pop-Up Fenster.

.. image:: ../../../figures/fom/element_security_key_popup.png
     :width: 100%


Detaillierte Informationen zu den Sicherheitseinstellungen finden sich unter :ref:`security_de`.


Löschen
==========
Löscht das Element mitsamt der konfigurierten Einstellung aus Front- und Backend.