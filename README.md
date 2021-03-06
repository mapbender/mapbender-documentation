# Mapbender Documentation

This is the Mapbender documentation repository.

You find the compiled pages of [the latest released version](https://github.com/mapbender/mapbender-documentation/releases) at [https://doc.mapbender.org/](https://doc.mapbender.org/). Other versions of the documentation are also available at [https://docs.mapbender.org/](https://docs.mapbender.org/current/#other-versions-of-this-documentation).

The sources are [on Github](https://github.com/mapbender/mapbender-documentation).

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

To participate in the documentation, create a fork and submit a pull request with your changes.


Have fun!
