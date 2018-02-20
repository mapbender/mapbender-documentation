.. _layertree_de:

Layertree - Table of Content (Layerbaum) 
****************************************

Funktionen
==========

**Was kann der Layerbaum?**

* Anzeige von Layern
* Anzeige von Layergruppen
* Anzeige thematischer Layergruppen (seit Version 3.0.5)
* Aktivieren und Deaktivieren von Layern
* Aktivieren und Deaktivieren der Abfrage von Layern
* Verändern der Layerreihenfolge
* Zoom zum Kartenausschnitt eines Layers
* Abfrage der Metadaten eines Layers


.. figure:: ../../../figures/layertree/layertree_example_dialog.png
           :scale: 80
           :alt: Einfacher Layertree mit einem Layerset und Layer als Dialog

           Einfacher Layertree mit einem Layerset und Layer als Dialog, über einen Button eingebunden.

.. figure:: ../../../figures/layertree/layertree_example_sidepane.png
           :scale: 80
           :alt: Komplexer Layertree mit mehreren Layersets in der Seitenleiste, unterteilt in thematischen Gruppen. 

           Komplexer Layertree mit mehreren Layersets in der Seitenleiste, unterteilt in thematischen Gruppen. 


Zur Konfiguration des Layerbaums gibt es verschiedene Verknüpfungspunkte zu anderen Elementen, die beachtet werden müssen: 

* `Layersets <../backend/layerset.html>`_
* `Kartenelement <map.html>`_
* `Datenquellen <../backend/source.html>`_


Konfiguration
=============


Allgemeine Konfiguration
------------------------

**Was muss gemacht werden?**

Um die unterschiedlichen Layersets im Layertree nutzen zu können, sind verschiedene Anpassungen notwendig. Diese betreffen die:

#. Einrichtung verschiedener Layersets
#. Einrichtung in der Karte (Map-Element) zur Anzeige der Layersets
#. Einrichtung des Layertrees selbst

Über die **Layersets** werden die gewünschten Layer in die Anwendung eingebunden. 
Die Instanzen sind die Referenzen auf die einzelnen WMS-Dienste. Über den Plus-Button **[1]** können neue Layersets erstellt. In die neuen Layersets können dann neue Layer über das Hinzufügen der bestehenden Instanzen **[2]** eingebunden werden. Das Layerset "overview" **[3]** wird – wie gehabt – für die Anzeige der Übersichtskarte verwendet. 
Eine genaue Dokumentation, wie die Dienste korrekt eingebunden werden können findet sich unter der Dokumentation des `Layersets <../backend/layerset.html>`_ und der `Datenquellen <../backend/source.html>`_. 

.. figure:: ../../../figures/layertree/layertree_configuration_layerset.png
           :scale: 80
           :alt: Einrichtung verschiedener Layersets für die Einbindung in den Layertree.

           Einrichtung verschiedener Layersets für die Einbindung in den Layertree.

Damit die neu eingebundenen Layersets auch in der Anwendung erscheinen müssen diese in dem `Kartenelement <map.html>`_ angegeben werden. 
Hier gibt man durch das Ankreuzen **[1]** der Layersets an, welche Layersets in der Kartenansicht verwendet werden sollen. Der Layerset "overview" wird beispielsweise nicht in der Hauptkarte angezeigt.  
In diesem Schritt wird auch die Reihenfolge definiert, in der die Layersets im Layertree und in der Karte erscheinen sollen. Die erstellten Layersets können in der Auflistung per Drag & Drop verschoben werden. Bitte achten Sie darauf, dass die weiter oben definierten Themen die darunter liegenden Themen überdecken können.


.. figure:: ../../../figures/layertree/layertree_configuration_map_simple.png
           :scale: 80
           :alt: Einrichtung in der Karte (Map-Element) zur Anzeige der Layersets.

           Einrichtung in der Karte (Map-Element) zur Anzeige der Layersets.


Workflow einfacher Layertree
----------------------------

Im Folgenden gehen wir eine beispielhafte Konfiguration eines Layertrees mit Basisfunktionen in drei Schritten durch: 

#. Einrichtung eines Layersets
#. Einrichtung in der Karte (Map-Element) zur Anzeige des Layersets
#. Einrichtung des Layertrees


In dem folgenden Beispiel ist ein **Layerset** mit einer Instanz definiert:

* Layerset World: 
  * Instanz `OSM Demodienst <https://osm-demo.wheregroup.com/service?&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_

Die Instanz des OSM-Demodienstes ist bei der Installation automatisch dabei. Diese muss nun nurnoch über den Reiter "Layersets" in ein bestehendes Layerset eingebunden werden. In dem folgenden Beispiel wurde das Layerset "YAML-main" in "World" umbenannt. 
Bei Schwierigkeiten mit der Einbindung kann die Dokumentation der `Layersets <../backend/layerset.html>`_ weiterhelfen. 


.. figure:: ../../../figures/layertree/layertree_configuration_layerset_simple.png
           :scale: 80
           :alt: Einrichtung eines Layersets für die Einbindung in den einfachen Layertree.

           Einrichtung eines Layersets für die Einbindung in den einfachen Layertree.

Als nächstes erfolgt die Einrichtung des `Kartenelements <map.html>`_  zur Anzeige des Layersets in der **Karte**. Dazu wechseln wir in den Reiter "Layouts" und bearbeiten das Kartenelement in dem Content-Bereich.
Wichtig ist nun, dass bei dem Bereich Layersets ein Häckchen bei dem Layerset World **[1]** gesetzt ist, damit dieses Layerset später in der Anwendung angezeigt wird. 
Bei Fragen zur weiteren Konfiguration der Karte kann die Dokumentation des `Kartenelements <map.html>`_ weiterhelfen.

.. figure:: ../../../figures/layertree/layertree_configuration_map_simple.png
           :scale: 80 
           :alt: Einrichtung in dem Kartenelement zur Anzeige des Layersets.

           Einrichtung in dem Kartenelement zur Anzeige des Layersets.


Als letzter Schritt erfolgt die Einrichtung des **Layertrees** selbst. 
Die in dem Kartenelement angegebenen Instanzen können im Layertree noch genauer definiert werden. Wenn eine vordefinierte Anwendung kopiert wurde, sollte der Layertree jetzt schon funktionieren. Bindet man das Element neu in die Anwendung ein, so kann dieses mit den Standardeinstellungen bereits genutzt werden, ohne dass weitere Anpassungen zwingend nötig sind.
Für das Verstehen der Funktionen und das eigene Erstellen eines Layertrees bearbeiten wir nun das Ebenenbaum-Element in dem Content-Bereich.

.. figure:: ../../../figures/layertree/layertree_configuration_1.png
           :scale: 80 
           :alt: Einrichtung des einfachen Layertrees im Content-Bereich.

           Einrichtung des einfachen Layertrees im Content-Bereich.

Bei der Konfiguration der Layersets ist standardisiert das Häckchen Basesource aktiviert. Dieses ist wichtig für den `Themenwechsler <basesourceswitcher.html>`_, mit dem man zwischen vordefinierten Themen wechseln kann. Über das Häckchen bei **BaseSources anzeigen** [1] werden Instanzen, die als Basesource in die Anwendung geladen wurden, auch in dem Layertree angezeigt.

Die Funktion **Header anzeigen** [2] ermöglicht das Einbinden einer Überschrift in den Themenbaum. 

.. figure:: ../../../figures/layertree/layertree_header.png
           :scale: 80 
           :alt: Überschrift in den Themenbaum.

           Überschrift in den Themenbaum.

Wenn **Automatisches Öffnen** [3] aktiv ist, ist der Layertree direkt beim Öffnen der Anwendung offen und muss nicht erst durch das Klicken auf einen Button oder das Aufklappen einer Seitenleiste aktiviert werden. Der **Titel** [4] des Elements wird in der "Layouts"-Liste angezeigt und ermöglicht, mehrere Elemente voneinander zu unterscheiden. **Target** [5] ist die ID des Kartenelements, auf das sich das Element bezieht.

.. figure:: ../../../figures/layertree/layertree_title.png
           :scale: 80
           :alt: Titel des Layertrees in dem "Layout"-Bereich

           Titel des Layertrees in dem "Layout"-Bereich.

Durch die Angabe eines **Type** [6] kann die Anzeige des Layertrees in der Anwendung definiert werden. Dabei gibt es zwei Anzeigeoptionen:  

* *Dialog*
* *Element*

.. figure:: ../../../figures/layertree/layertree_type.png
           :scale: 80
           :alt: Type-Angabe für die Anzeige des Layertrees.

           Type-Angabe für die Anzeige des Layertrees.

:Dialog: 
  Der Type *Dialog* muss gewählt werden, wenn der Layertree über einen Button eingebunden wird und sich das Konfigurations-Element in dem Content-Bereich befindet.
:Element:
  Für die Einbindung des Layertrees in dem Sidepane-Bereich muss der Type *Element* gewählt werden.

.. figure:: ../../../figures/layertree/layertree_type_map.png
           :scale: 80
           :alt: Position des Layertrees als Element und Dialog in der Anwendung.

           Position des Layertrees als Element und Dialog in der Anwendung.

Der **Displaytype** [7] bestimmt die Anzeige (*Tree*) des Layertrees. Durch die Angabe der maximalen Zeichenzahl über das Feld **Titlemaxlength** [8] kann die Anzeige des Titels der einzelnen Layer auf eine Zeichenzahl begrenzt werden. Das ist wichtig für die Begrenzung bei langen Layerbezeichnungen. Nach dem Erreichen der maximalen Zeichenzahl wird der Titel mit "..." als Zeichen abgeschnitten. 

.. figure:: ../../../figures/layertree/layertree_configuration_1.png
           :scale: 80 
           :alt: Einrichtung des einfachen Layertrees im Content-Bereich.

           Einrichtung des einfachen Layertrees im Content-Bereich.

Über das **Menu** [9] kann eine Auswahl von Buttons aktiviert werden, die dann dem Benutzer der Anwendung im Ebenenbaum zur Verfügung gestellt werden. 

* *Remove layer* (Layer aus der Anwendung entfernen)
* *Opacity* (Deckkraft der einzelnen Layer verändern)
* *Zoom to layer* (auf die BBOX des Layers zoomen)
* *Metadata* (Metadaten des Layers anzeigen)

.. figure:: ../../../figures/layertree/layertree_menu.png
           :scale: 80
           :alt: Konfiguration der Funktionen für das Kontextmenü.

           Konfiguration der Funktionen für das Kontextmenü.

Die einzelnen Funktionen können durch Klicken auf die Schaltfläche aktiviert werden. Alle aktiven Funktionen werden grün hinterlegt und in der Anwendung erscheint im Layertree rechts neben jedem Layer ein Symbol für das Kontextmenü. Durch den Klick auf den Menü-Button rechts neben dem Layernamen klappt ein Fenster auf und die einzelnen Funktionen können genutzt werden. Durch den Klick auf den x-Button rechts oben kann das Menü wieder geschlossen werden. 

.. figure:: ../../../figures/layertree/layertree_menu_map.png
           :scale: 80
           :alt: Kontextmenü der Layer im Layertree

           Kontextmenü der Layer im Layertree.

Der Slider im Layertree Menü **[1]** erscheint durch die Funktion *Opacity*. Hierüber lässt sich durch das Verschieben des grünen Kästchens die Deckkraft der einzelnen Layer bestimmen. Die prozentuale Deckkraft wird als ganze Zahl in dem Kästchen angezeigt.

Über einen Klick auf das Infoblatt im Layertree Menü **[2]** können die Metadaten des Layers angezeigt werden. Falls der Dienst Metadaten enthält, werden diese in einem neuen Dialog dargestellt.

Der Klick auf das "x" im Layertree Menü **[3]** ermöglicht das Entfernen eines Layers aus der Anwendung für die Dauer der Sitzung. 

.. figure:: ../../../figures/layertree/layertree_menu_map.png
           :scale: 80
           :alt: Layertree Menü.

           Layertree Menü.

Die Funktion **Visibility bei Ordnern ausblenden** [11] ermöglicht die Sicherung der Deckkraft. Bei aktiver Funktion wird die Deckkraft der Ebenen nicht angezeigt und kann nicht verändert werden.

.. figure:: ../../../figures/layertree/layertree_configuration_1.png
           :scale: 80 
           :alt: Einrichtung des einfachen Layertrees im Content-Bereich.

           Einrichtung des einfachen Layertrees im Content-Bereich.

Durch einen Klick auf das Ordnersymbol des Layertrees **[1]** links neben der Instanz können die eingebundenen Layer angezeigt werden. Alle Layer, die vorher bei dem Einbinden in das Layerset aktiviert wurden, erscheinen nun in der Liste. Über die Funktion **Nicht aufklappbare Ordner ausblenden** [10] können Kartenebenen, die nicht mehrere Layer enthalten ausgeblendet werden.

.. figure:: ../../../figures/layertree/layertree_buttons.png
           :scale: 80
           :alt: Layertree Buttons.

           Layertree Buttons.

Die Checkbox neben dem jeweiligem Layernamen **[2]** ermöglicht das An- und Ausschalten eines Layers. Ist das Häkchen gesetzt erscheint der Layer in der Karte. Es werden jedoch weiterhin die im Layerset definierten Regeln beachtet, wie z.B. maßstabsabhängige Anzeigen.

Das "i"-Symbol neben einem Layernamen **[3]** zeigt an, ob die Informationsabfrage aktiviert ist. Wenn das "i"-Symbol grau hinterlegt ist die Informationsabfrage nicht aktiv. Wird diese durch einen Klick aktiviert, so wird das Symbol dunkelgrau hinterlegt und bei einer Informationsabfrage erscheinen die Informationen zu dem Layer. 

Die Funktion **Info ausblenden** [12] ermöglicht das Deaktivieren der Informationsabfrage. Die Infoabfrage ist unabhängig von den Einstellungen im Layerset oder Dienst nun nicht mehr möglich. 

.. figure:: ../../../figures/layertree/layertree_configuration_1.png
           :scale: 80 
           :alt: Einrichtung des einfachen Layertrees im Content-Bereich.

           Einrichtung des einfachen Layertrees im Content-Bereich.



Workflow thematischer Layertree
-------------------------------

Im Folgenden gehen wir eine komplexe beispielhafte Konfiguration eines Layertrees mit erweiterten Funktionen, wie z.B. den thematischen Layersets, in drei Schritten durch: 

#. Einrichtung mehrerer Layersets
#. Einrichtung in der Karte (Map-Element) zur Anzeige der Layersets
#. Einrichtung des thematischen Layertrees


In dem folgenden Beispiel sind zwei **Layersets** mit jeweils zwei Instanzen definiert:

* Layerset Project NRW:
  * Instanz `DTK50 NRW <https://www.wms.nrw.de/geobasis/wms_nw_dtk50?&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_ 
  * Instanz `Wald NRW <http://www.wms.nrw.de/umwelt/waldNRW?&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_
* Layerset World: 
  * Instanz `OSM Demodienst <http://osm-demo.wheregroup.com/service?&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_ 
  * Instanz `GEBCO <https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv?&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0>`_ 


Für die Einrichtung der Layersets wurden die vier oben genannten Dienste als Instanzen hinzugefügt (detaillierte Info s.o. oder in der Doku der `Layersets <../backend/layerset.html>`_ und `Dienste <../backend/source.html>`_).

Für dieses Beispiel wurden die oben genannten Schritte durchgeführt, um das Layerset "World" **[2]** mit der Instanz "osm" hinzuzufügen. Nun fügen wir in dieses Layerset noch die Instanz "GEBCO" hinzu. 
Um die thematische Gruppierung gut nutzen zu können erstellen wir nun ein neues Layerset mit dem Namen "Project NRW" **[3]** und laden in dieses die beiden oben genannten Instanzen "DTK50 NRW" und "Wald NRW" ein. 

.. figure:: ../../../figures/layertree/layertree_configuration_layerset_komplex.png
           :scale: 80
           :alt: Konfiguration der Layersets für den thematischen Layertree

           Konfiguration der Layersets für den thematischen Layertree.


Das Layerset sollte nun drei Layersets enthalten. Die **Overview** [1] für die Übersichtskarte, das **World**-Layerset [2] mit den weltweiten/ Deutschlandweiten Daten und das **Project NRW** Layerset [3] mit den zwei regionalen Datensets aus NRW. 


Als nächstes erfolgt die Einrichtung des `Kartenelements <map.html>`_ zur Anzeige des Layersets in der Karte. Dazu wechseln wir in den Reiter "Layouts" und bearbeiten das Kartenelement in dem Content-Bereich.
Wichtig ist nun, dass bei dem Bereich Layersets ein Häckchen bei dem Layerset "World" UND dem Layerset "Project NRW" gesetzt ist **[1]**, damit diese später in der Anwendung angezeigt werden. 
Bei Fragen zur weiteren Konfiguration der Karte kann die Dokumentation des `Kartenelements <map.html>`_ weiterhelfen.

.. figure:: ../../../figures/layertree/layertree_configuration_map_komplex.png
           :scale: 80 
           :alt: Konfiguration der Layersets für den thematischen Layertree

           Konfiguration des Kartenelements für den thematischen Layertree.

Als letzter Schritt erfolgt die Einrichtung des Layertrees selbst. 
Die in dem `Kartenelement <map.html>`_ angegebenen Instanzen können im Layertree noch genauer definiert werden. Für das Verstehen der Funktionen und das eigene Erstellen eines Layertrees beachten Sie bitte die in dem Workflow für den simplen Layertree bereits erklärten Einstellungen.

.. figure:: ../../../figures/layertree/layertree_configuration_1.png
           :scale: 80 
           :alt: Einrichtung des einfachen Layertrees im Content-Bereich.

           Einrichtung des einfachen Layertrees im Content-Bereich.

Für den thematischen Layertree binden wir den Ebenenbaum in diesem Beispiel die Seitenleiste ein. Für die Einbindung in dem Sidepane-Bereich muss daher der Type *Element* **[6]** gewählt werden.

.. figure:: ../../../figures/layertree/layertree_type.png
           :scale: 80
           :alt: Einrichtung des Type Element.

           Einrichtung des Type Element.

Ist die Option **Thematische Layer** ausgeschaltet, benutzt der Layertree nicht die konfigurierten Layersets und zeigt die einzelnen Instanzen ohne thematische Strukturierung in der Hauptebene an. Nun wollen wir jedoch die Layer über unsere thematischen Layersets anzeigen, daher aktivieren wir die Funktion **Thematische Layer** [1]. 
Da wir in dem `Kartenelement <map.html>`_ beide Layersets in die Anwendung eingebunden haben, werden diese nun unter dem **Themen**-Bereich angezeigt.

.. figure:: ../../../figures/layertree/layertree_configuration_2.png
           :scale: 80 
           :alt: Einrichtung des thematischen Layertrees im Content-Bereich.

           Einrichtung des thematischen Layertrees im Content-Bereich.


Damit die **Themen** in der Anwendung wie gewünscht angezeigt werden, gibt es verschiedene Einstellungsmöglichkeiten: 

.. figure:: ../../../figures/layertree/layertree_configuration_thematic_map.png
           :scale: 80

:[1] Thema anzeigen:
  Ist diese Option gesetzt, wird der Layerset als zusätzliche Ebene angezeigt. Ist diese Option nicht gesetzt, werden die enthaltenen Layer-Instanzen in der Hauptebene angezeigt.
:[2] Thema offen oder geschlossen:
  Ist diese Option gesetzt (Symbol des geöffneten Ordners), ist das Thema im Layertree automatisch ausgeklappt.
:[3] Thema Dienste Sichtbarkeit:
  Ist diese Option gesetzt, wird im Layertree die Schaltfläche "Dienste anzeigen / ausblenden" hinzugefügt.
:[4] Thema Layer Sichtbarkeit:
  Ist diese Option gesetzt, wird im Layertree die Schaltfläche "Alle Layer anzeigen" hinzugefügt. 

Wenn wir nun bei dem Themenset "World" die Standardeinstellungen beibehalten und bei dem Themenset "Project NRW" die anderen Optionen aktivieren, sieht die Konfiguration des Elements so aus: 

.. figure:: ../../../figures/layertree/layertree_example_sidepane_config.png
           :scale: 80
           :alt: Einrichtung der thematischen Layersets im Content-Bereich.

           Einrichtung der thematischen Layersets im Content-Bereich.

Wir haben die Layersets somit als thematische Gruppen in den Ebenenbaum eingebunden. Durch die Konfiguration der thematischen Layer stellt sich der Layertree in der Anwendung nun wie folgt dar: 

.. figure:: ../../../figures/layertree/layertree_example_sidepane.png
           :scale: 80
           :alt: Aufbau des thematischen Layersets in der Seitenleiste.

           Aufbau des thematischen Layersets in der Seitenleiste.

Das Layerset "World" wird als Thema angezeigt, ist jedoch nicht geöffnet und die beiden Schaltflächen sind nicht aktiviert. Bei dem Layerset "Project NRW" wird das Thema beim Öffnen der Anwendung aufgeklappt gezeigt. Die Schaltfläche für die Anzeige/ das Ausblenden der Dienste ist vorhanden und alle Layer können über einen Button aktiviert werden.


YAML-Definition:
================

.. code-block:: yaml
                
  title: layertree             # Titel des Layerbaums
  target: ~                    # ID des Kartenelements
  type: ~                      # Typ des Layerbaums
  displaytype: tree            # In 3.0 gibt es nur den Baum (Tree), in Zukunft wird auch eine Liste angeboten.
  useAccordion: false          # akkordeonartige Anzeige. Standard ist false
  autoOpen: false              # true, wenn der Layerbaum beim Start der Anwendung geöffnet werden soll, der Standardwert ist false.
  titleMaxLength: 20           # Maximale Länge des Layertitels, Standard ist 20
  showBaseSource: true         # Anzeige des Basislayers, der Standardwert ist true
  showHeader: true             # zeigt eine Überschrift, die die Anzahl der Services zählt, der Standardwert ist true
  menu: [opacity,zoomtolayer,metadata,removelayer]  # zeigt ein Kontextmenü für den Layer an (wie Opazität, Zoom auf Layer, Anzeige des Metadatendialogs, Layer entfernen), der Standardwert ist menu: [] 


..
   .. figure:: ../../../figures/layertree/layertree_configuration_pre305.png
        :scale: 80

Optional kann ein Button für dieses Element verwendet werden, um es als Dialogfeld einzubinden. Siehe unter :doc:`button` für die Konfiguration. 
Der Layerbaum kann auch als Element definiert werden. Dann wird der Layerbaum in einem frame wie der Sidebar angezeigt.

..
   YAML-Definition:

   .. code-block:: yaml    

    title: layertree             # Titel des Layerbaums
    target: ~                    # ID des Kartenelements  
    type: ~                      # Typ des Layerbaums, element oder dialog
    autoOpen: false              # true, wenn der Layerbaum beim Start der Anwendung geöffnet werden soll, der Standardwert ist
    displaytype: tree            # In 3.0 gibt es nur den Baum (Tree), in Zukunft wird auch eine Liste angeboten.
    titlemaxlength: 20           # Maximale Länge des Layertitels, Standard ist 20  
    showBaseSource: true         # Anzeige des Basislayers, der Standardwert ist true
    showHeader: true             # zeigt eine Überschrift, die die Anzahl der Services zählt, der Standardwert ist true
    menu: [opacity,zoomtolayer,metadata,removelayer]  # zeigt ein Kontextmenü für den Layer an (wie Opazität, Zoom auf Layer, Anzeige des Metadatendialogs, Layer entfernen), der Standardwert ist menu: []
    hideInfo: null               #
    hideNotToggleable: null      #
    hideSelect: null             #
    themes: {  }                 #   

Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\Layertree
* **Widget:** mapbender.element.layertree.js
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

Keine.
