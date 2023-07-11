# Mapbender Documentation

This is the Mapbender documentation repository.

You can find the compiled pages of [the latest released version](https://github.com/mapbender/mapbender-documentation/releases) at [https://doc.mapbender.org/](https://doc.mapbender.org/). Other versions of the documentation are also available at [https://docs.mapbender.org/](https://docs.mapbender.org/current/##older-versions).

The sources are [on Github](https://github.com/mapbender/mapbender-documentation).

The website code is generated using [Sphinx](http://sphinx-doc.org/), therefore the documentation source is written in [Restructured Text](http://sphinx-doc.org/rest.html).

To build the website locally, you need to install Sphinx first. Install it in Debian-based distributions via

```bash
sudo apt-get install sphinx-common python3-sphinx
sudo apt-get install pip3
sudo pip3 install sphinxcontrib-phpdomain
sudo pip3 install sphinx-rtd-theme
sudo pip install sphinx-notfound-page
```

You can then build the documentation by running:

```bash
make
```

## How to build the documentation

```bash
cd /data
git clone git@github.com:mapbender/mapbender-documentation
cd mapbender-documentation
git checkout master

sphinx-build . _build -A version=3.3

ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc

http://localhost/mb-doc/

If you want rebuild the documentation, delete the old version before
rm -rf _build
```

## How to participate in the documentation

To participate in the documentation, create a fork and submit a pull request with your changes. In your fork, write new content, e.g.:

```bash
  cd /mapbender-documentation/en/functions/basic # Let's assume that you want to create a docs page that is part of the Mapbender CoreBundle. Switch to the folder where your file should be located.
  cp overview.rst basic/add_wms.rst  # Create a rst-file. E.g., copy the overview.rst as template for your add_wms.rst documentation file.
  # Write the documentation: keep it short and simple. Use the structure of the document.
  sphinx-build . _build -A version=3.3.0 # Build the documentation locally to see how your documentation looks like. Adjust the version number (if necessary).
  ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc # Create a symlink from your Sphinx build folder to your Apache web server to test the documentation locally.
```

Now, take a look at the documentation page in your browser. Is everything ok? Are any changes needed? If not, you can create a pull request to add your reviewed changes into the documentation.

## Rules

Below you'll find some basic conventions about documentation writing.

### Images (figures)

Images for the documentation are located at mapbender-documentation/figures

* Create images with size 800 x 600px
* Have a look at quickstart.rst to learn about image referring
* For elements, use elementname.png and elementname_configuration.png as name. If you also provide german image files, please keep the names and create two more images in the de folder.

### Languages

The two fully supported languages (i.e.: en - english, de - german) should have the same file structure, that is:

```bash
  /mapbender-documentation
    index.rst          # refers to the different languages
    /figures           # images that are included in the documentation
    /de                # German file locations
      ...
    /en                # English file locations
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
```

Have fun!
