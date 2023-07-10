# Mapbender Documentation

This is the Mapbender documentation repository.

You can find the compiled pages of [the latest released version](https://github.com/mapbender/mapbender-documentation/releases) at [https://doc.mapbender.org/](https://doc.mapbender.org/). Other versions of the documentation are also available at [https://docs.mapbender.org/](https://docs.mapbender.org/current/#other-versions-of-this-documentation).

The sources are [on Github](https://github.com/mapbender/mapbender-documentation).

The website code is generated using [Sphinx](http://sphinx-doc.org/), therefore the documentation source is written in [Restructured Text](http://sphinx-doc.org/rest.html).

To build the website locally, you need to install Sphinx. Install it in Debian-based distributions via

```bash
sudo apt-get install sphinx-common python3-sphinx
sudo apt-get install pip3
sudo pip3 install sphinxcontrib-phpdomain
sudo pip3 install sphinx-rtd-theme
sudo pip install sphinx-notfound-page
```

You can then build the documentation by running:

```bash
$ make
```

Example

```bash

cd /data
git clone git@github.com:mapbender/mapbender-documentation
cd mapbender-documentation
git checkout master

sphinx-build . _build -A version=3.3

ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc

http://localhost/mb-doc/

If you want rebuild the documentation delete the old version before
rm -rf _build
```

To participate in the documentation, create a fork and submit a pull request with your changes.


Have fun!
