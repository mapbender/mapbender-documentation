.. _development_introduction:

Introduction
############

This book is targeted at Mapbender developers and will cover useful topics not needed by administrators or users of Mapbender installations.


Things to consider
******************

There are a couple of things you should be familiar with in order to contribute to Mapbender:

* Object-Orientated PHP: We're using PHP > 5.6 which offers full object orientation.
* Symfony: This is what we build upon. So read `The Book
  <https://symfony.com/doc/current/index.html>`_ to learn more about Symfony.
* Docblock annotations: We use ApiGen to generate code documentation.
* JavaScript: We use jQuery a lot and especially the jQuery UI widget factory. These are essential to understand to write maintainable JavaScript code.


Installation
************

The installation procedure from Git is described under :ref:`installation_git`.


Modules and bundles
*******************

Please refer to the respective sections in the `CONTRIBUTING.md` guide to understand what `modules <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#modules>`_ and what `bundles <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#bundles>`_ are, and how the latter can be `created <https://github.com/mapbender/mapbender-starter/blob/master/CONTRIBUTING.md#bundle-creation>`_.


Getting Help
************

Malinglists:

* `Mapbender-Developer and -User mailinglist <https://mapbender.org/?q=en/community>`_

Libraries and frameworks:

* `Symfony framework <https://www.symfony.com/>`_
* `PHPUnit documentation <https://phpunit.de/>`_
* `Composer documentation <https://getcomposer.org/doc/>`_
* `General GitHub documentation <https://help.github.com/>`_
* `GitHub pull request documentation <https://help.github.com/send-pull-requests/>`_


Topics
******

.. toctree::
   :maxdepth: 1

   controllers
   conventions
   elements
   element_generate
   frontend_architecture
   requestresponse
   twig
