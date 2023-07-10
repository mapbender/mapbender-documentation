.. _documentation_howto:

How to write Mapbender Documentation?
#####################################
This documentation is build and deployed from the mapbender-documentation repository on Github.

Please take a look at the documentation files in this repository:

https://github.com/mapbender/mapbender-documentation/

.. code-block:: bash

   git clone git@github.com:mapbender/mapbender-documentation


How to build the documentation via Sphinx?
******************************************
We generate the website code from the rst-files using Sphinx.

To build the website locally, you need to install Sphinx first. Read more in the README.md of the repository:

https://github.com/mapbender/mapbender-documentation/blob/master/README.md


Example for element documentation
*********************************
Let's assume that you are a developer and just added a new element to Mapbender code base. In this example, your element is called AddWMS and is part of the Mapbender CoreBundle.

**Now it is time to write the documentation!**

Here are the steps you have to do:

.. code-block:: bash

  # get the documentation files from github
  cd /data
  git clone git@github.com:mapbender/mapbender-documentation
  cd /mapbender-documentation/en/functions/basic

  # create a rst-file. Use the overview.rst as template for element documentation!
  cp overview.rst basic/add_wms.rst

  # write the documentation. You find information how and what to write in the documentation in template_element.rst

  # keep it short and simple

  # build the documentation locally to see how your documentation looks like
  cd /data/mapbender-documentation/
  rm -Rf _build
  sphinx-build . _build -A version=3.3.0

  # have a look at the documentation in your browser (example location). Is everything ok? Are any changes needed?
  ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc
  http://localhost/mb-doc/

  # Next, add, commit and push your new file to the mapbender-documentation repository
  git checkout -b feature/add_wms
  git add en/functions/basic/add_wms.rst
  git commit -m 'new documentation for element <element_name>'
  git push --set-upstream origin feature/add_wms

  # get the actual files from the mapbender-documentation repository
  git checkout master
  git pull


Images (figures)
****************
Images for the documentation are located at:

* mapbender-documentation/figures
* create images with size 800 x 600px (you can resize your browser window, e.g. with web developer to this size)
* have a look at quickstart.rst about how to refer to an image
* for elements, use elementname.png and elementname_configuration.png as name. If you also provide german image files, please keep the names and create two more images in the de folder.


Languages
*********
All fully supported languages (i.e.: en - english, de - german) should have the same file structure.

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
