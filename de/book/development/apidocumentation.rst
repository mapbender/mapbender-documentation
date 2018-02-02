API-Dokumentation
#################

Die Mapbender API Dokumentation findet sich unter http://api.mapbender.org/.

Die API Dokumentation wird mit Mapbender mitgeliefert und kann über den folgenden Befehl erstllt werden:

.. code-block:: yaml

                bin/composer docs

Die Dokumentation ist dann vergfügbar unter: http://localhost:8000/docs/api/ und die Mapbender-Dokumentation unter: http://localhost:8000/docs/

Bitte lesen Sie den `Contributing Guide zu den Details des eingebauten Symfony-Webservers <https://github.com/mapbender/mapbender-starter/blob/release/3.0.6/CONTRIBUTING.md#start-web-server>`_.

Für die Nutzung innerhalb von Apache oder Nginx müssen eventuell die Dateirechte im Web-Verzeichnis von Mapbender angepasst werden.



Wie wird die Mapbender API Dokumentation erstellt?
**************************************************

PHP
***

`ApiGen <http://apigen.org>`_ - wird verwendet, um die API-Dokumentation zu generieren. Sie müssen nur docblocks in den Code einfügen. Ein Beispiel für eine Klasse mit docblock-Kommentaren:

.. literalinclude:: Example.php
    :language: html+php
    :linenos:

Schauen Sie sich die Dokumentationsblöcke in der `Example.php <https://github.com/mapbender/mapbender-documentation/blob/master/de/book/development/Example.php>`_ an. 


JavaScript
**********

Bisher wurden keine zufriedenstellenden Tools gefunden.
