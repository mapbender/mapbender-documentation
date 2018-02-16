# Mapbender Documentation

This is the Mapbender documentation repository.

You find the compiled pages of [the latest released version](https://github.com/mapbender/mapbender-documentation/releases) at [https://doc.mapbender.org/](https://doc.mapbender.org/). Other versions of the documentation are also available at [https://docs.mapbender.org/](https://docs.mapbender.org/current/#other-versions-of-this-documentation).

The current working branch is [release/3.0.6](https://github.com/mapbender/mapbender-documentation/tree/release/3.0.6). The released versions are based on the [master branch](https://github.com/mapbender/mapbender-documentation/tree/master) and merged from release/3.0.6.

The website code is generated using [Sphinx](http://sphinx-doc.org/), therefore the documentation source is written in [Restructured Text](http://sphinx-doc.org/rest.html).

You find a documentation about how the documentation is structured in the documentation itself in chapter [How to write Mapbender Documentation?](http://doc.mapbender.org/en/book/development/documentation_howto.html) or directly [here in this Git-Repository](https://github.com/mapbender/mapbender-documentation/blob/master/en/book/development/documentation_howto.rst).


To build the website locally, you need to install Sphinx. Install it in Debian-based distributions via

```bash
$ apt install python-sphinx
```

You can then build the documentation by running:

```bash
$ make
```

To participate in the documentation, create a fork, work on the [release/3.0.6](https://github.com/mapbender/mapbender-documentation/tree/release/3.0.6) branch and create a [Pull-Request](https://help.github.com/articles/about-pull-requests/) with the release/3.0.6 branch as base.


Have fun!
