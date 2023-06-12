.. _documentation_howto:

How to write Mapbender Documentation?
#####################################

Mapbender Documentation website
*******************************

You find the Mapbender Documentation at:

https://doc.mapbender.org

The Documentation is build from the mapbender-documentation repository at Github. This repository is used to build and deploy the https://doc.mapbender.org website. The website code is generated using Sphinx, therefore the documentation source is written in Restructured Text.


Edit documentation at Git Repository mapbender-documentation
************************************************************

The documentation files are located at the git repository:

https://github.com/mapbender/mapbender-documentation/

.. code-block:: bash

   git clone git@github.com:mapbender/mapbender-documentation

Structure of the documentation
********************************************
We want to provide documentation in different languages. The language we want to support first is english. So every document should be build up in english first.

Every language (en - english, de - german) has the same file structure.

.. code-block:: yaml

  /mapbender-documentation
    index.rst          # refers to the different languages
    /figures           # images that are included in the documentation
    /de
      ...
    /en
      index.rst        # refers to TheBook, Developer's Book & the Bundle Documentation
      bundles.rst      # lists the chapters of this category - refers to rst files
      development.rst  # lists the chapters of this category - refers to rst files
      /architecture
      /development
          ....
      /functions
          /backend
          /basic
          ....


How to build the documentation via Sphinx?
******************************************
We generate the website code from the rst-files using Sphinx.

To build the website locally, you need to install Sphinx. Read more in the README.md

https://github.com/mapbender/mapbender-documentation/blob/master/README.md


How to write documentation?
***************************
We write documentation for elements, entities, services.


Images (figures)
****************
Images for the documentation are **all** located at

* mapbender-documentation/figures
* create images with size 800 x 600px (you can resize your browser window e.g. with web developer to this size)
* have a look at quickstart.rst about how to refer to an image
* for elements use elementname.png and elementname_configuration.png as name. If you provide also image for de please keep the names and create 2 more image in the de folder


Quickstart
**********

The Mapbender Quickstart is a tutorial to get to know Mapbender. It is used on OSGeoLive too http://live.osgeo.org.

If you want to add a new lesson to the Quickstart:
 * add the subject of your lesson at the beginning of the document (This Quick Start describes how to: ...)
 * add the new lesson to the document and provide a screenshot if this makes sense
 * images are stored in the ../../../figures-directory


Example for element documentation
*********************************
You have to write a new element documentation when a new element with new functionality is added to Mapbender.

In this example we assume, that you are a developer and just added a new element to Mapbender code base. We assume your element is called AddWMS and is part of the Mapbender CoreBundle.

**Now it is time to write the documentation!**

Here are the steps you have to do:

.. code-block:: bash

  # get the documentation files from github
  cd /data
  git clone git@github.com:mapbender/mapbender-documentation
  cd /mapbender-documentation/en/functions/basic

  # create a rst-file. Use the over.rst as template for element documentation!
  cp overview.rst basic/add_wms.rst

  # write the documentation. You find information how and what to write in the documentation in template_element.rst

  # keep it simple

  # build the the documentation locally to see how your documentation looks like
  cd /data/mapbender-documentation/
  rm -Rf _build
  sphinx-build . _build -A version=3.3.0

  # have a look at the documentation in your browser (example location). Is everything ok? Any changes needed?
  ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc
  http://localhost/mb-doc/

  # add, commit and push your new file to the mapbender-documentation repository
  # replace <element_name> with the element name, dont forget to remove the <, >
  git checkout -b feature/add_wms
  git add en/functions/basic/add_wms.rst
  git commit -m 'new documentation for element <element_name>'
  git push --set-upstream origin feature/add_wms

  # get the actual files from the mapbender-documentation repository
  git checkout master
  git pull



Working with reStructured Text (rst)
************************************

For more info for rst-files and reStructured Text, take a look at these documentations:

* `Wikipedia reStructured Text <https://en.wikipedia.org/wiki/ReStructuredText>`_
* `reStructured Text on docutils at SourceForge <https://docutils.sourceforge.net/rst.html>`_
* `Quick reStructuredText <https://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
