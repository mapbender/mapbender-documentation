How to write Mapbender3 Documentation?
######################################

Mapbender3 Documentation webside
********************************

You find the Mapbender3 Documentation at:

http://doc.mapbender3.org

The Documentation is build from the mapbender-docmentation repository at Github. This repository is used to build and deploy the http://doc.mapbender3.org website on a nightly base. The website code is generated using Sphinx, therefore the documentation source is written in Restructured Text.

Mapbender3 also provides an API Documentation at:

http://api.mapbender3.org

This API Documentation is generated from the Mapbender3 code. You find information about how to write the Mapbender3 API documentation at :doc:`API documentation <apidocumentation>`.

This HowTo concentrates on the build of the documentation at http://doc.mapbender3.org.


Edit documentation at Git Repository mapbender-documentation
************************************************************

The documentation files are located at the git repository:

https://github.com/mapbender/mapbender-documentation/


Developers granted secure access to the code must use the SSH-URL of the
repository to get the files and be able to push: 

    :command:`git clone git@github.com:mapbender/mapbender-documentation`

Structure of the documentation
********************************************
We want to provide documentation in different languages. The language we want to support first is english. So every document should be build up in english first. 

Every language (en - english, de - german) has the same file structure.

.. code-block:: yaml

  /mapbender-documentation
    index.rst          # refers to the different languages
    /de 
      ...
    /en
      index.rst        # refers to TheBook, Developer's Book & the Bundle Documentation
      bundles.rst      # lists the chapters of this category - refers to rst files
      development.rst  # lists the chapters of this category - refers to rst files
      thebook.rst      # lists the chapters of this category - refers to rst files
      /book
        ....
        /development
          ....  
      /bundles
          /Mapbender
            /CoreBundle
              index.rst             # refers to the elements, entitiy & service documentation
              template_element.rst  # template to use for new element documentation
              /elements
                legend.rst
                ...
              /services    
                ...
            /WmsBundle
              ...
          /FOM
            ...


How to build the documentation via Sphinx?
********************************************
We generate the webside code from the rst-files using Sphinx. 

To build the website locally, you need to install Sphinx. In Debian-based distributions this is done via:

  apt-get install sphinx-common

Additionally, a Sphinx extension for Symfony2 is used as a submodule, so a

  git submodule update --init --recursive

is also required.

You can then build the documentation by running

 sphinx-build . output

or by using the supplied generate.sh shell script.


How to write documentation? 
***************************
We write documentation for elements, entities, services.

Quickstart
**********
The Mapbender3 Quickstart is a tutorial to get to know Mapbender. It is used on OSGeo-Live too http://live.osgeo.org.

If you want to add a new lesson to the Quickstart:
 * add the subject of you lesson at the beginning of the document (This Quick Start describes how to: ...)
 * add the new lesson to the document and provide a screenshot if this makes sense
 * images are stored in the figures-directory


Example for element documentation
*********************************
You have to write a new element documentation when a new element with new functionality is added to Mapbender.

In this example we assume, that you are a developer and just added a new element to Mapbender3 code base. We assume your element is called AddWMS and is part of the Mapbender CoreBundle. 

**Now it is time to write the documentation!**

Here are the steps you have to do:

.. code-block:: yaml

  # get the documentation files from github
  cd /data
  git clone git@github.com:mapbender/mapbender-documentation
  cd /mapbender-documentation/en/bundles/Mapbender/CoreBundle

  # create a rst-file. Use the template for element documentation! 
  cp template_element.rst elements/add_wms.rst
 
  # write the documentation. You find information how and what to write in the documentation in template_element.rst

  # build the the documentation locally to see how your documentation looks like
  cd /data/mapbender-documentation/
  sphinx-build . output
  
  # have a look at the documentation in your browser (example location). Is everything ok? Any changes needed?
  file:///data/mapbender-documentation/documentation/output/index.html

  # add, commit and push your new file to the mapbender-documentation repository
  git add en/bundles/Mapbender/CoreBundle/elements/add_wms.rst
  git commit -m 'new documentation for element AddWms' en/bundles/Mapbender/CoreBundle/elements/add_wms.rst
  git push

  # get the actual files from the mapbender-documentation repository
  git pull
