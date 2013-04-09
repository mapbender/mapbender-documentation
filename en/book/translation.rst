.. _translation:

Translation in Mapbender3
######################################

Mapbender3 uses the translator service (`Translator <http://api.symfony.com/2.1/Symfony/Component/Translation/Translator.html>`_) which is a Symfony component. 

In the code you use the function **trans** to translate a text into another language.

Example how the function **trans** can be used in a Twig template:

.. code-block:: yaml

 {% block title %}{{ application.title | trans }}{% endblock %}

or 

.. code-block:: yaml

 {% trans %}{{ application.title }}{% endtrans %}


Example for PHP:

.. code-block:: yaml

 echo $translator->trans('Hello World');


XLIFF-files for translations
****************************
The translations can be stored in different formats. We use XLIFF-format for Mapbender3. Symfony will take the XLIFF-loader to load and parse the file.

This is how a translation file messages.de.xliff for german translation could look like.

.. code-block:: yaml

 <?xml version="1.0" encoding="utf-8"?>
 <xliff xmlns="urn:oasis:names:tc:xliff:document:1.2" version="1.2">
  <file source-language="en" datatype="plaintext" original="file.ext">
    <body>
      <trans-unit id="1">
        <source>FeatureInfo</source>
        <target>Sachinformation</target>
      </trans-unit>
      <trans-unit id="2">
        <source>Services</source>
        <target>Dienste</target>
      </trans-unit>
      <trans-unit id="3">
        <source>X coordinate</source>
        <target>X-Koordinate</target>
      </trans-unit>
      .....        

**Notice:** Each time you create a new translation resource you have to clear your cache.

.. code-block:: php

 app/console cache:clear


How can you activate translation?
*********************************
Activate translator in the configuration file **app/config/config.yml**

.. code-block:: yaml

 framework:
    translator:      { fallback: %locale% }

Activate your default locale in the configuration file **app/config/parameters.yml**

.. code-block:: yaml

    locale:            de


Check whether translations (xliff-files) for your language exist 

* mapbender/src/Mapbender/CoreBundle/Resources/translations
* mapbender/src/Mapbender/ManagerBundle/Resources/translations
* mapbender/src/Mapbender/WmsBundle/Resources/translations
* mapbender/src/Mapbender/WmcBundle/Resources/translations
* ...


Create xliff-files for your language
*************************************
If your language is not translated yet, it is easy to add a new language.

* Check the translation directories and create a new file by copying an existing locale
* translate the source-tags into the target-tags
* clear your cache


Naming conventions and locations
********************************** 
Symfony looks for translation files in the following directories in the following order:

* the <kernel root directory>/Resources/translations
* the <kernel root directory>/Resources/<bundle name>/translations
* Resources/translations/ directory of the bundle.

Bundle translations can overwrite translations of the other directories.

Naming
~~~~~~~
The naming convention is **domain.locale.loader**.

* domain    - we use the default domain messages
* locale    - locale that the translations is made for (e.g. de, de_DE);
* loader    - defines the loader to load and parse the file. Symfony offers XLIFF, PHP, YAML


Share your translations with the Mapbender3 community!
******************************************************
Supporting more and more language would be great for Mapbender3. The Mapbender project would be happy if you could share your translations with the community.

This is what you have to do:

* send the new xliff-files for your language to the Mapbender developer (mapbender@osgeo.org) or create a patch at github


