.. _feature_info_de:

Feature Info (Information)
**************************

Dieses Element stellt eine Informationsabfrage bereit, die per WMS funktioniert.

.. image:: ../../../figures/de/feature_info.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/feature_info_configuration.png
     :scale: 80


* **Automatisches Öffnen (Autoopen):** Schaltet ein/aus, ob das Informationsfenster beim Start der Anwendung automatisch geöffnet werden soll (Standard: ausgeschaltet).
* **Print Result:** Anzeige eines Links, über den die abgefragten Daten ausgedruckt werden können. Standardwert ist false.
* **Beim Schließen deaktivieren:** Steuert, ob das FeatureInfo beim Schließen des Ergebnisfensters deaktiviert wird oder nicht, der Standardwert ist true.
* **Title:** Titel des Elements. Dieser wird in der Layouts Liste angezeigt und ermöglicht, mehrere Button-Elemente voneinander zu unterscheiden. Der Titel wird außerdem neben dem Button angezeigt, wenn “Beschriftung anzeigen” aktiviert ist.
* **Tooltip:** Text, der angezeigt wird, wenn der Mauszeiger eine längere Zeit über dem Element verweilt.
* **Target:** ID des Kartenelements, auf das sich das Element bezieht.
* **Type:** Auswahl, ob die Info als Element oder Dialog angezeigt werden soll. Default und mandatory: Dialog.
* **Display type:** Anzeige der Information als Tabs oder in Accordionform.
* **Max count:** Maximale Anzahl an Treffern/Ergebnissen, die angezeigt werden soll.
* **Width/ Height:** Größe des Dialogfeldes (Breite und Höhe in Pixel).
* **Original Zeigen:** Original css-Stil des Ergebnisses wird angezeigt. Standardwert ist false.
* **nur valide zeigen:** Dieser Parameter hängt sehr vom Format des GetFeatureInfo Responses ab. Beispiel UMN: Solange ein Template korrekte HTML Head und Body Elemente definiert (z.B. über die Angabe einer Headers und Footers Datei), interpretiert Mapbender das Resultat als valide. Fehlen diese Head und Body Angaben, so gilt dies für Mapbender als nicht valide.

  * Bitte stellen Sie sicher, dass die GetFeatureInfo Antworten valides HTML zurückgeben.
  * Wenn Sie ``text/plain`` als Ausgabeformat definieren, darf der Schalter ``only valid`` nicht aktiviert sein, da ``text/plain`` kein valides HTML zurückgibt.

**Hinweis:** Über das Ergebnisfenster des FeatureInfo Dialogs können der Anwendung dynamisch WMS Dienste hinzugefügt werden. Hierfür wird der WMS Loader genutzt. Konkret muss dafür das jeweilige HTML-Template, für die Darstellung des FeatureInfo Responses, mit dem Link zu dem gewünschten WMS Dienst ergänzt werden. Für nähere Informationen siehe das Kapitel `Hinzufügen eines WMS über einen definierten Link <../misc/wms_loader.html#hinzufugen-eines-wms-uber-einen-definierten-link>`_.
Ein Beispiel für die Nutzung dieser Funktionalität liefert das `Geoportal der Stadt Gütersloh <http://www.geodaten.guetersloh.de/Bebauungsplaene>`_.

.. image:: ../../../figures/feature_info_guetersloh.png
     :scale: 80

In dem Beispiel ist dargestellt, wie über das Ergebnisfenster des FeatureInfo der entsprechende WMS zu einem bestimmten Bebauungsplan in die Anwendung geladen wurde.

Anzeige als Original und gestyled
---------------------------------

Mit der Option "Original zeigen" wird die Original-Darstellung des FeatureInfo Responses genutzt. Ist die Option deaktiviert, wird versucht eine einheitliche Darstellung in Mapbender zu erreichen.

Beispiel Original:

.. image:: ../../../figures/de/feature_info_original.png
     :scale: 80

Beispiel gestyled:

.. image:: ../../../figures/de/feature_info_not_original.png
     :scale: 80



Anzeige als Tabs und Accordion
------------------------------

Mit dem Schalter "Type" können die Responses mehrerer Dienste in unterschiedlichen Tabs oder als Accordion angezeigt werden.

Beispiel Tabs:

.. image:: ../../../figures/de/feature_info_tabs.png
     :scale: 80

Beispiel Accordion:

.. image:: ../../../figures/de/feature_info_accordion.png
     :scale: 80



Ausdruck der Resultate
----------------------

Mit dem Schalter "print Result" kann die Information des FeatureInfo ausgedruckt werden. Eine Druckschaltfläche ist dann in dem Feature-Dialog sichtbar. Das Drucken geschieht über den Druckdialog des Webbrowsers.

Um alle Bilder und Hintergrundfarben im Ausdruck zu erhalten, sollten Sie die Druckeinstellungen des Webbrowsers beachten: In Firefox kann man die Option "Hintergrund drucken" im Druckoptionendialog anschalten, in Chrome-basierten Browsern nennt sich die Option "Hintergrundgrafiken". Die übermittelten Schriften können bei einem Ausdruck in PDF je nach Viewer unterschiedlich gut funktionieren. Des Weiteren modifizieren die meisten Browser Webseiten etwas vor dem Druck, damit nicht so viel Tinte/Toner verbraucht wird.



Button-Konfiguration
--------------------

Für das Element wird ein Button verwendet. Siehe das Kapitel `Button <../misc/button.html>`_ für die generelle Konfiguration. Der folgende Screenshot zeigt ein Beispiel für einen FeatureInfo Button, der so lange aktiviert ist, bis er vom Benutzer wieder deaktiviert wird. Eine weitere Möglichkeit, ihn zu deaktivieren, wäre, den FeatureInfo Dialog zu schließen, wenn bei diesem die Option "Beim Schließen deaktivieren" angeschaltet ist.

* **Group:** featureinfo
* **Deactivate:** deactivate

.. image:: ../../../figures/de/feature_info_button.png
     :scale: 80



YAML-Definition:
----------------

.. code-block:: yaml

   title: FeatureInfo      # Titel des Elements
   tooltip: Feature Info   # Text des Tooltips
   type: dialog            # Default und mandatory: dialog.
   target: map             # ID des Kartenelements
   autoActivate: false     # true, wenn die Infoabfrage beim Start der Anwendung geöffnet wird, der Standardwert ist false.
   deactivateOnClose: true # true/false um die Funktion nach dem Schließen des Ergebnisfensters zu deaktivieren, der Standardwert ist true
   onlyValid: false        # Korrekte HTML Ausgabe erfordern. Standardwert ist false.
   printResult: false      # Anzeige eines Links, über den die Infoabfrage ausgedruckt werden kann. Standardwert ist false.
   showOriginal: false     # Der Original css-Stil des Ergebnisses wird angezeigt. Standardwert ist false.
   displayType: tabs       # tabs/accordion Default: tabs
   width: 700              # Breite des Dialogs in Pixel, Standardwert: 700
   height: 500             # Höhe des Dialog in Pixel, Standardwert: 500



Class, Widget & Style
=====================

* **Class:** Mapbender\\CoreBundle\\Element\\FeatureInfo
* **Widget:** mapbender.element.featureInfo.js
* **Style:** mapbender.elements.css

HTTP Callbacks
==============

Keine.
