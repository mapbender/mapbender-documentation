.. _ruler_de:

Linien-/Flächenmessung (Line/Area Ruler)
****************************************

Mit dem Lineal wird eine Linie oder eine Fläche gezeichnet, deren Länge oder Flächeninhalt berechnet wird. Für das Element wird ein Button verwendet. Die Konfiguration findet sich unter :ref:`button_de`.
Durch die Auswahl eines Typs wird bestimmt, ob das Element Linien oder Flächen misst. Jedes eingebundene Element kann nur entweder Linien oder Flächen messen. Für die Nutzung von beiden Funktionen (Flächen- und Linienmessung) in einer Anwendung werden zwei Buttons benötigt, die in einer gemeinsamen Gruppe sind.

.. image:: ../../../figures/de/ruler.png
     :scale: 80

Konfiguration
=============

.. image:: ../../../figures/de/ruler_configuration.png
     :scale: 80

* **Title:** Titel des Elements. Dieser wird im Backend in der Layouts Liste angezeigt. In der Anwendung selbst wird der Titel im Messfenster angezeigt.
* **Geometrie:** Typ des Elements, entweder 'line' oder 'area' (misst nur einzelne Linien oder addiert diese zu einer Fläche). Pflichtfeld.
* **Hilfetext:** Gibt einen Hilfetext aus: Der Standardwert mb.core.ruler.help bedeutet "Doppelklicken zum Beenden" (je nach Anzeigesprache des Browsers).
* **Linienstärke während des Zeichnens:** Zahlenwert in Pixel, der die Strichstärke während des Zeichnens definiert.
* **Strichfarbe:** RGBA-Wert, der die Strichfarbe definiert. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden.
* **Linienstärke (Pixel):** Zahlenwert in Pixel, der die Strichstärke der gemessenen Geometrie definiert.
* **Füllfarbe:** RGBA-Wert, der die Füllfarbe einer Fläche definiert. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.
* **Schriftfarbe:** RGBA-Wert, der die Schriftfarbe des in der Geometrie angezeigten numerischen Flächeninhalts ausgibt. Kann nach einem Klick in die Eingabemaske über einen Farbwähler geändert werden. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.
* **Schriftgröße:** Zahlenwert, der die Schriftgröße der in der Geometrie angezeigten Fläche definiert. Wird als Geometrie *Linie* gewählt, bleibt die Option ohne Effekt.


YAML-Definition:
----------------

Diese Vorlage kann genutzt werden, um das Element in einer YAML-Applikation einzubinden.

.. code-block:: yaml

   title: mb.core.ruler.tag.line             # 'line', 'area' oder beliebigen Titel wählen
   class: Mapbender\CoreBundle\Element\Ruler # Element-Klasse
   target: map                               # ID des Kartenelements, z.B. 'map'
   type: line                                # Wählen Sie Typ 'line' oder 'area'

