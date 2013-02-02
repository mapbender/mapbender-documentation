Mapbender3 Documentation
========================

This is the Mapbender3 documentation repository. This repository is used to
build and deploy the [doc.mapbender3.org](http://doc.mapbender3.org) website
on a nightly base.

The website code is generated using [Sphinx](http://sphinx-doc.org/), therefore
the documentation source is written in
[Restructured Text](http://sphinx-doc.org/rest.html).

You find a documentation about how to document at:

http://doc.mapbender3.org/en/book/development/documentation_howto.html

or

https://github.com/mapbender/mapbender-documentation/blob/master/en/book/development/documentation_howto.rst


To build the website locally, you need to install Sphinx, in Debian-based
distributions a

    apt-get install sphinx-common

should usually suffice.

Additionally, a Sphinx extension for Symfony2 is used as a submodule, so a

    git submodule update --init --recursive

is also required.

You can then build the documentation by running

    sphinx-build . output

or by using the supplied generate.sh shell script.

Have fun!

