.. _development_introduction_de:

Einführung
##########

Diese Dokumentation ist an Mapbender-Entwickler gerichtet und behandelt Themen, 
die von Mapbender-Administratoren und -Benutzern nicht benötigt werden.

Dinge, die es zu beachten gilt
******************************

Sie sollten einige Dinge wissen, um an der Mapbender-Entwicklung mitwirken zu können:

* Objektorientiertes PHP: Verwendet wird PHP > 5.6, welches objektorientierte Programmierung ermöglicht.
* Symfony: Mapbender baut auf Symfony auf. Folgen Sie der `Symfony-Dokumentation
  <https://symfony.com/doc/current/index.html>`_, dort erfahren Sie mehr.
* Docblock-Anmerkungen: Es wird ApiGen zu Erstellung der Dokumentation verwendet.
* JavaScript: jQuery wird häufig verwendet, vor allem kommt die jQuery UI Widget Factory häufig zum Einsatz. Das Verständnis davon ist essentiell, um JavaScript-Code zu schreiben.

Installation
************

Die Installation aus den Git-Quellen heraus wird unter :ref:`installation_git_de` beschrieben.

Wo gibt es Hilfe?
*****************

Mailinglisten

* `Mapbender-Developer und -Anwender Mailingliste <https://mapbender.org/community/>`_

Bibliotheken und Frameworks:

* `Symfony framework <https://www.symfony.com/>`_
* `PHPUnit documentation <https://phpunit.de/>`_
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
