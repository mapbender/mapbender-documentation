.. _development_introduction_de:

Einführung
##########

Diese Dokumentation ist an Mapbender-Entwickler gerichtet und behandelt Themen, die von Mapbender-Administratoren und -Benutzern nicht benötigt werden.


Was ist zu beachten?
********************

Sie sollten einige Dinge wissen, um an der Mapbender-Entwicklung mitwirken zu können:

* Objektorientiertes PHP: Verwendet wird PHP, welches objektorientierte Programmierung ermöglicht.
* Symfony: Mapbender baut auf Symfony auf. Folgen Sie der `Symfony-Dokumentation <https://symfony.com/doc/current/index.html>`_, dort erfahren Sie mehr.
* JavaScript: jQuery wird häufig verwendet, vor allem kommt die jQuery UI Widget Factory häufig zum Einsatz. Das Verständnis davon ist essentiell, um JavaScript-Code zu schreiben.


Installation
************

Die Installation aus den Git-Quellen heraus wird unter :ref:`installation_git_de` beschrieben.


Module und Bundles
******************

Bitte beachten Sie die jeweiligen Beiträge im Entwicklungshandbuch `CONTRIBUTING.md <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md>`_, um zu erfahren, was ein `Modul <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#modules>`_ und was ein `Bundle <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#bundles>`_ ist und wie letzteres `erstellt <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#bundle-creation>`_ werden kann.


Twig
****

Mapbender nutzt den Template Ansatz, der von Symfony bereitgestellt wird. Über diesen kann Symfony beispielsweise HTML oder CSS erzeugen.
Ein Template ist eine Textdatei, die jedes textbasierte Format wie HTML oder XML generieren kann.
Sie kann verwendet werden, um ein Layout zu erstellen. Auf diese Weise kann ein Basislayout erstellt und dann beliebige Layout-Blöcke mit individuellen Templates überschrieben oder hinzugefügt werden.
Lesen Sie mehr über Templates auf der Seite :ref:`templates_de` oder im `Contributing Guide <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#generate-translations>`_. Eine Einführung in Twig gibt außerdem die `Symfony Template Dokumentation <https://symfony.com/doc/current/templates.html>`_.


Wo gibt es Hilfe?
*****************

Mailinglisten

* `Mapbender-Developer und -Anwender Mailingliste <https://mapbender.org/community/>`_

Bibliotheken und Frameworks:

* `Symfony framework <https://www.symfony.com/>`_
* `Composer documentation <https://getcomposer.org/doc/>`_
* `General GitHub documentation <https://support.github.com/>`_
* `GitHub pull request documentation <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_


Themen
******

.. toctree::
   :maxdepth: 1

   elements
   element_generate
   requestresponse
