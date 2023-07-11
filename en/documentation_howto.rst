.. _documentation_howto:

How to write Mapbender Documentation?
#####################################
This documentation is built and deployed from the mapbender-documentation repository on Github.

Please take a look at the documentation files in this repository:

https://github.com/mapbender/mapbender-documentation/


How to build the documentation via Sphinx?
******************************************
We generate the website code from the rst-files using Sphinx.

To build the website locally, you need to install Sphinx first. Find more information in the README.md file:

https://github.com/mapbender/mapbender-documentation/blob/master/README.md


Example for element documentation
*********************************
Let's assume that you are a developer and just added a new element to the Mapbender code base. In this example, your element is called AddWMS and is part of the Mapbender CoreBundle.

**Now it is time to write the documentation!**

Here are the steps you have to do:

.. code-block:: bash

  # Get the documentation files from GitHub:
  cd /data
  git clone git@github.com:mapbender/mapbender-documentation
  cd /mapbender-documentation/en/functions/basic

  # Create a rst-file. E.g., use the overview.rst as template for element documentation:
  cp overview.rst basic/add_wms.rst

  # Write the documentation: keep it short and simple.

  # Build the documentation locally to see how your documentation looks like. Adjust the version number (if necessary).
  cd /data/mapbender-documentation/
  rm -Rf _build
  sphinx-build . _build -A version=3.3.0

  # Have a look at the documentation in your browser (example location). Is everything ok? Are any changes needed?
  ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc
  http://localhost/mb-doc/

  # Next, add, commit and push your new file to the mapbender-documentation repository:
  git checkout -b feature/add_wms
  git add en/functions/basic/add_wms.rst
  git commit -m 'new documentation for element <element_name>'
  git push --set-upstream origin feature/add_wms

  # To get the actual files from the mapbender-documentation repository, run
  git checkout master
  git pull


Images (figures)
****************
Images for the documentation are located at:

* mapbender-documentation/figures
* create images with size 800 x 600px (you can resize your browser window, e.g. with web developer to this size)
* have a look at quickstart.rst to learn about image referring
* for elements, use elementname.png and elementname_configuration.png as name. If you also provide german image files, please keep the names and create two more images in the de folder.


Languages
*********
At last, all fully supported languages (i.e.: en - english, de - german) should have the same file structure.

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
