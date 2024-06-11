.. _ruler_de:

Linien-/Flächenmessung (Line/Area Ruler)
****************************************

Mit dem Messen-Werkzeug wird eine Geometrie gezeichnet, deren Länge oder Flächeninhalt berechnet wird. Das Element kann in der Sidepane oder mit einem :ref:`button_de` verwendet werden.
Durch die Auswahl eines Typs wird bestimmt, ob das Element Linien oder Flächen misst oder beides und so der Benutzer die Auswahl im Client treffen kann.

.. image:: ../../../figures/de/ruler.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/ruler_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird im :ref:`backend_de` in der Layouts Liste angezeigt. In der Anwendung selbst wird der Titel im Messfenster angezeigt.
* **Geometrie:** Typ des Elements, entweder 'Linie' oder 'Fläche' (definiert, ob das Element eine Strecken- oder eine Flächenmessung erstellt). Pflichtfeld.
* **Hilfetext:** Definition eines individuellen Hilfetextes. Der Standardwert mb.core.ruler.help ist in der Mapbender Übersetzungsdatei definiert und enthält auf Deutsch den Text "Doppelklicken zum Beenden". Der Text variiert je nach Anzeigesprache des Browsers.
* **Linienstärke während des Zeichnens:** Zahlenwert in Pixel, der die Strichstärke während des Zeichnens definiert.
* **Strichfarbe:** RGBA-Wert, der die Strichfarbe definiert. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden.
* **Linienstärke (Pixel):** Zahlenwert in Pixel, der die Strichstärke der gemessenen Geometrie definiert.
* **Füllfarbe:** RGBA-Wert, der die Füllfarbe einer Fläche definiert. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.
* **Schriftfarbe:** RGBA-Wert, der die Schriftfarbe des in der Geometrie angezeigten numerischen Flächeninhalts ausgibt. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.
* **Schriftgröße:** Zahlenwert, der die Schriftgröße der in der Geometrie angezeigten Fläche definiert. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.


YAML-Definition
---------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Applikation einzubinden.

.. code-block:: yaml

   title: mb.core.ruler.tag.line             # 'line', 'area' oder 'vom Nutzer auswählbar'
   class: Mapbender\CoreBundle\Element\Ruler # Element-Klasse
   target: map                               # ID des Kartenelements, z.B. 'map'
   type: line                                # Wählen Sie Typ 'line' oder 'area'
   strokeColor: 'rgba(16, 101, 93, 0.8)'     # Angabe der Strichfarbe (für Linien und Flächen)
   fillColor: 'rgba(100, 100, 100, 0.5)'     # Angabe der Füllfarbe (nur Flächenmessung)
   fontColor: 'rgba(0,0,0,1)'                # Angabe der Schriftarbe (nur Flächenmessung)
   fontSize: 14                              # Angabe der Schriftgröße (nur Flächenmessung)
   strokeWidth: 4                            # Angabe der Linienstärke, in px (für Linien und Flächen)
   strokeWidthWhileDrawing: 3                # Angabe der Linienstärke während des Zeichnens, in px (für Linien und Flächen)
