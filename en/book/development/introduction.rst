Introduction
############

This book is targeted at Mapbender3 developers and will cover useful topics
not needed by administrators or users of Mapbender3 installations.

Things you should now
*********************

There are a couple of things you should be familiar with in order to contribute
to Mapbender3:

* Object-Orientated PHP: We're using PHP 5.3 which offers full object
  orientation. No simple scripts anymore.
* Symfony2: This is what we build upon. So read `The Book
  <http://symfony.com/doc/current/index.html>`_ and learn about controllers,
  templating and the other cool things.
* Docblock annotations: We use ApiGen to generate code documentation.
  :doc:`More on this <apidocumentation>`.
* JavaScript: We use jQuery a lot and especially the jQuery UI widget factory.
  These are essential to understand to write maintainable JavaScript code.

  
Installation
************

The installation procedure from Git is described in the chapter `Git-based installation <../installation/installation_git.html>`_.


Getting Help
************

Malinglists:

* `Mapbender3-Developer and -User mailinglist <http://mapbender3.org/?q=en/community>`_


Libraries and frameworks:

* `Symfony framework <http://www.symfony.com/>`_
* `PHPUnit documentation <https://phpunit.de/>`_
* `Composer documentation <https://getcomposer.org/doc/>`_
* `General GitHub documentation <https://help.github.com/>`_
* `GitHub pull request documentation <https://help.github.com/send-pull-requests/>`_




Topics
******

.. toctree::
   :maxdepth: 1

   git
   github
   apidocumentation
   requestresponse
   code_convention
   translations
   elements
   administrations

