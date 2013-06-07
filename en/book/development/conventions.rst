.. _conventions:

Conventions for Mapbender3
##########################

Code conventions
*****************

* variable names / way of coding 
* Code documentation
* trans convention - where to put translation


* document the x steps on the way to a new functionality

  * define the topic
  * create a ticket
  * create a workflow
  * discuss the workflow with the core team and find a final solution
  * do the programming
  * insert License
  * test
  * documentation in mapbender-documentation --> rst
  * close the ticket

 
* where to put a module/element
* naming vor files (referred to symfony convention)



Layout conventions
*******************
What to keep in mind, when you create a layout

* naming conventions
* where to put the css
* where to put the twig
* where to put the images / should be possible to easy switch an image collection an get other buttons


Translation where
************************

* conventions to put the files? Groß-Kleinschreibung/ welche Übersetzungen werden generell gepflegt? en/de weitere?
* also have a look at `Translation in Mapbender3 <../translation.rst>`


Version conventions
********************
The Mapbender3 version is defined by a four digit numbering system, seperated by dots.

3.0.10.20

* The **first** digit is constant and represents the Mapbender3 software cycle.

* The **second** digit describes all new features and major changes in Mapbender3, with
the highest difficulty level of a update process.

* The **third** digit describes new features and minor changes, which can be easily updated.

* The **fourth** digit represents only bugfixes and micro changes.

Increase a digit means always a reset for all digits before. For example - 3.0.10.20 -> 3.1.0.0

This numbering system started with Mapbender3 version 3.0.0.0

How to build a new Mapbender3 build
************************************

* update version number in parameters.yml and push

.. code-block:: bash

 git clone -b design git@github.com:mapbender/mapbender-starter mapbender-build
 cd mapbender-build
 git submodule update --init --recursive
 phing deps
 git tag -a v3.0.0.1 -m "Mapbender bugfix release Version 3.0.0.1 read changes https://github.com/mapbender/mapbender/issues?milestone=3"  
 git tag
 git push --tags
 phing tarball
 cd /data/git/mapbender-build/artefacts
 cd /data/git/mapbender-build/artefacts
 sudo tar xfz mapbender3-3.0.0build0.tar.gz 
 sudo chmod -R 777 mapbender3-3.0.0build0
 sudo mv mapbender3-3.0.0build0 mapbender3-3.0.0.1
 rm -R /data/git/mapbender-build/artefacts/mapbender3-3.0.0.1/app/config/parameters.yml
 rm -R /data/git/mapbender-build/artefacts/mapbender3-3.0.0.1/documentation/
 cp -R /data/git/mapbender-documentation/output/*  /data/git/mapbender-build/artefacts/mapbender3-3.0.0.1/documentation/
 create tar.gz with right name for example mapbender3-3.0.0.1.tar.gz
 move file to /sites/www.mapbender3.org/builds
 update Roadmap and milestones
 write release mail (mapbender-user / mapbender-dev / major releases osgeo-announce)
 twitter
 update demo.mapbender3.org
 tag version

 



Documentation conventions
**************************

* have a look at `How to write Mapbender3 Documentation? <documentation_howto>`
