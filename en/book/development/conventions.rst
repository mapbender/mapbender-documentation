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


Git branch conventions
**********************

We follow the Git Flow branching model (Read more about it in the
`original document <http://nvie.com/posts/a-successful-git-branching-model/>`_
describing it). Basically that boils down to having at least two branches:

* develop - for the daily work, always has the latest merged commits, and is
  equal to or ahead of the latest release
* master - only changes on new releases (right now and until the 3.0.1 release,
  some of our repositories don't have a master branch but will get one then
  again)

Furthermore there might be more branches, which must always be namespaced:

* feature/<name> - Used for developing new features (feature/printservice)
* hotfix/<name> - Used for making hot fixes for releases (hotfix/bug_123)
* release/<name> - Used for preparing releases, very short-lived (release/3.0.1)

Some Linux distributions have a package called git-flow which will provide easy
git command shortcuts to use the merge/branch model of Git Flow without having
to do everything by yourself (which is still possible and you should always know
how Git Flow uses plain git to achieve things).


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


Issue conventions
********************
Issues (bugs and features) are administrated in the **mapbender**-repository at:

* https://github.com/mapbender/mapbender/issues

We create a milestone for every version of Mapbender3:

*  https://github.com/mapbender/mapbender/issues/milestones

There are some rules you should keep in mind:

* **write understandable tickets!!**

* **write your title** so that the issue is already described in the title: 

  * Browser - Backend/Frontend - element - issue 
  * like: Firefox - Frontend - layertree - option visible is not handled in frontend
  * see ticket https://github.com/mapbender/mapbender/issues/48
* write **comments** with all necessary information: 
  * for bugs: describe step by step how the error can be reproduced
  * for features: describe feature and functionality
* when you create a new ticket do not assign it to a milestone or developer, if you are not sure

* **add labels** to your ticket 
  * bug - describes a bug that orrurs in a special version of Mapbender3 (add info about the version)
  * feature - new feature
  * enhancement - stands for feature enhancement
  * wip - work in progress

* when you work on a ticket or close it please **assign a user and milestone**

* **when you close a ticket**, please:

  * add a comment in the ticket and **refer to the commit**,
  * refer to the documentation at http://doc.mapbender3.org or a demo if possibile.




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

Release
********

* check whether all tickets are done
* build a build - check documentation -> How to build a new Mapbender3 build 
* update Roadmap and milestones
* update demo.mapbender3.org
* write release mail (mapbender-user / mapbender-dev / major releases osgeo-announce)
* twitter




How to build a new Mapbender3 build
************************************

* update version number in parameters.yml and push

.. code-block:: bash

 # clone the source-code from the release branch
 git clone -b release/3.0.5 git@github.com:mapbender/mapbender-starter mapbender-build

 # change to the directory
 cd mapbender-build
 git submodule update --init --recursive
 phing deps

 # tagging
 cd application/mapbender
 git tag -a v3.0.5.0 -m "Mapbender release Version 3.0.5.0 read changes https://github.com/mapbender/mapbender/milestones/3.0.5.0"  
 git push --tags
 
 # tag submodules
 cd ../../application/fom
 git tag -a v3.0.5.0 -m "Mapbender release Version 3.0.5.0 read changes https://github.com/mapbender/mapbender/milestones/3.0.5.0"  
 git push --tags
 
 # tag owsproxy3
 cd ../../application/owsproxy3
 git tag -a v3.0.5.0 -m "Mapbender release Version 3.0.5.0 read changes https://github.com/mapbender/mapbender/milestones/3.0.5.0"  
 git push --tags
 
 # tag mapbender-starter
 cd ../../
 git tag -a v3.0.5.0 -m "Mapbender release Version 3.0.5.0 read changes https://github.com/mapbender/mapbender/milestones/3.0.5.0"  
 git tag
 git push --tags (will be shown at https://github.com/mapbender/mapbender-starter/releases)

 # use phing to create the tarball
 phing tarball

 # change to the artefacts directory, where phing created the tarball
 cd artefacts/

 # untar the archive to change some files
 tar -xvf mapbender3-3.0.5build1.tar.gz 

 # that step should not be neccessary: sudo chmod -R 777 mapbender3-3.0.5build1

 # change the name of the directory
 mv mapbender3-3.0.5build1 mapbender3-3.0.5.0

 # remove some files in that directory
 rm -R mapbender3-3.0.5.0/app/config/parameters.yml
 rm -Rf mapbender3-3.0.5.0/documentation/*

 # tag the documentation
 cd /data/git/mapbender-documentation/
 git tag -a v3.0.5.0 -m "Mapbender release Version 3.0.5.0 read changes https://github.com/mapbender/mapbender/milestones/3.0.5.0"  
 
 # copy the actual documentation output
 cp -R /data/git/mapbender-documentation/output/*  mapbender3-3.0.5.0/documentation/
 
 # create tar.gz with right name for example mapbender3-3.0.5.0.tar.gz
 tar -czvf mapbender3-3.0.5.0.tar.gz mapbender3-3.0.5.0/
  
* move file to /sites/www.mapbender3.org/builds
* update Roadmap: milestones, features, date on http://mapbender3.org/roadmap
* write release mail to mapbender-user and mapbender-dev 
* only for major releases write release mail to news_item@osgeo.org (see also http://www.osgeo.org/content/news/submit_news.html)
* twitter on https://twitter.com/mapbender
* update http://demo.mapbender3.org and http://sandbox.mapbender3.org

 



Documentation conventions
**************************

* have a look at `How to write Mapbender3 Documentation? <documentation_howto>`_
