# Mapbender Documentation

This is the repository of the Mapbender documentation.

You can find compiled pages of the latest [tagged releases](https://github.com/mapbender/mapbender-documentation/releases) on the [official documentation landing page](https://doc.mapbender.org/). Other versions of the documentation are also available on the same page under [Older Versions](https://doc.mapbender.org/#older-versions).

The website code is generated using [Sphinx](https://sphinx-doc.org/), the documentation is written in [Restructured Text](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).

The documentation source code is available on [Github](https://github.com/mapbender/mapbender-documentation).

## Prerequisites

To build the website locally, you need to install Sphinx first. Install it and the required extensions in Debian-based distributions with:

```bash
sudo apt install sphinx-common python3-sphinx
sudo apt install python3-sphinxcontrib.phpdomain
sudo apt install python3-sphinx-rtd-theme
sudo apt install python3-sphinx-notfound-page
sudo apt install python3-sphinx-copybutton
```

You will then be able to build the documentation by running:

```bash
make
```

## How to build

Alternatively, clone the repository from GitHub to any directory:

```bash
cd /data
git clone git@github.com:mapbender/mapbender-documentation
cd mapbender-documentation
git checkout master
```

Then, build a tagged version with:

```bash
sphinx-build . _build -A version=4.0
```

Now, create a symlink from your build folder to the Apache Webserver:

```bash
ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc
```

Finally, you can open the documentation in a web browser using:

<http://localhost/mb-doc/>

If you want to rebuild the documentation, delete the old build first:

```bash
rm -rf _build
```

## How to participate

To contribute to the documentation, first create a fork of this repository, then implement your changes in it and finally test the changes on your local machine.

```bash
  cd /mapbender-documentation/en/elements/basic # In your forked repo, let's assume that you want to create a docs page that is part of the Mapbender CoreBundle. Switch to the folder where you want to put your file.
  cp overview.rst basic/add_wms.rst  # Create an .rst file. In this example, we copy the overview.rst as a template for the new documentation file.
  # Write the documentation. Keep it short and simple. Use the structure of the document and check the documentation rules below.
  sphinx-build . _build -A version=4.0 # Build the documentation locally to see what your documentation looks like. Adjust the version number (optional).
  ln -s /data/mapbender-documentation/_build/ /var/www/html/mb-doc # Create a symlink from your Sphinx build folder to your Apache web server to test the documentation locally.
```

Now, take a look at the documentation in your browser. Is everything OK? Are any changes needed? If not, you can create a pull request to add your reviewed changes to the documentation.

## How to write

Here are some basic conventions for writing documentation.

### Formatting syntax

We implement the basic .rst formatting syntax in the Mapbender documentation. It is documented in detail on the [Sphinx page](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer).

For inline markup, the aim is to comply with the following syntax:

* One asterisk for file names (*README.md*),
* two asterisks for text quoted directly from Mapbender, e.g. feature names or button labels (**Save**),
* backquotes for (file) paths (`figures/sketch.png`),
* double backquotes for inline code (``bin/console mapbender:security:migrate-from-acl``),

For several lines of code, we use code blocks.

```rst
.. code-block::
```

Moreover, we use formatting blocks to add important information to the documentation.

```rst
.. hint::
    This is a small hint.

.. note::
    This is an important note.

.. tip::
    This is a handy tip.

.. warning::
    This is a warning.
```

## Referencing syntax

Here are some basic conventions for referencing images and headings.

### Referencing images

Images for the documentation are available in `mapbender-documentation/figures`.

* Create optimized web images in .png file format that are approximately 1 MB (or smaller) in size.
* For elements, use *elementname.png* and *elementname_configuration.png* as names.
* If you also provide German image files, please keep the names and create two more images in the `de` folder.
* See the [Quickstart](en/quickstart.rst) file to see image referencing methods in action.

### Referencing text

Each .rst file has its own tag that you can refer to. Use `:ref:` and the tag in the first line of the corresponding file to refer to another page in the documentation, e.g.:

```bash
    :ref:`overview_de` points to the German page of the overview map.
```

For referencing specific documentation sections, we use the [Sphinx Autosectionlabel extension](https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html). It allows to reference sections using its title. The syntax is a combination of the file path name, a colon and the section title name.

For example, you can add a link to the *Install Mapbender* section of the Quickstart document like this:

```bash
    The following class refers to the :ref:`en/quickstart:Install Mapbender` text section.
```

### Languages

The two fully supported languages (i.e.: en - English, de - German) should have the same file structure:

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
      /elements
          /backend
          /basic
          ....
```

Have fun!
