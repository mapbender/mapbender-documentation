.. _translation:

Translation in Mapbender3
######################################

Mapbender3 uses the translator service which is a Symfony component. You get more information at the `Symfony Translation Documentation <http://symfony.com/doc/2.8/book/translation.html>`_ and `Translator Class Documentation <http://api.symfony.com/2.8/Symfony/Component/Translation.html>`_ . 

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


yml-files for translations
****************************
The translations can be stored in different formats. We use yml-format for Mapbender3. 

We use place holder for every text f.e. **mb.core.featureinfo.popup.btn.ok**. Like this you can define different tranlsation for the same word which accurs in different modules.

We translate the place holder to different languages. English is the default language that we provide. It is also defined as the fallback language in the parameters.yml file. The fallback language will be used if you define a language in parameters.yml that does not exist.

This is how a translation file messages.de.yml for german translation could look like.

.. code-block:: yaml

    mb:
      core:
        featureinfo:
          error:
            nolayer: 'Informationsebene existiert nicht.'
            unknownoption: 'Unbekannte Option %key% für %namespace%.%widgetname%.'
            noresult: 'kein Ergebnis'
          popup:
            btn:
              ok: Schließen
          class:
            title: Information
            description: Information
          tag:
            featureinfo: Information
            feature: Objekt
            info: Info
            dialog: Dialog
        aboutdialog:
          content:
            versionprefix: Version
            learnmore: 'Lernen Sie Mapbender3 kennen '
            linktitle: 'Besuchen Sie die offizielle Mapbender3 Webseite.'
            website: '- zur Webseite'
            .....        

**Notice:** Each time you create a new translation resource you have to clear your cache.

.. code-block:: php

 app/console cache:clear


How can you activate translation?
*********************************

Activate your default locale in the configuration file **app/config/parameters.yml**

.. code-block:: yaml
    
    fallback_locale:   en
    locale:            de


Check whether translations (yml-files) for your language exist 

* mapbender/src/Mapbender/CoreBundle/Resources/translations/
* mapbender/src/Mapbender/ManagerBundle/Resources/translations/
* mapbender/src/Mapbender/PrintBundle/Resources/translations/
* mapbender/src/Mapbender/WmcBundle/Resources/translations/
* mapbender/src/Mapbender/WmsBundle/Resources/translations/
* fom/src/FOM/CoreBundle/Resources/translations/
* fom/src/FOM/ManagerBundle/Resources/translations/
* fom/src/FOM/UserBundle/Resources/translations/
* ...


Create yml-files for your language
*************************************
If your language is not translated yet, it is easy to add a new language.

* Check the translation directories and create a new file by copying the english locale
* translate
* set locale in your parameters.yml to the new language
* clear your cache
* if everything is fine with your new language give the files to the Mapbender3 commnity - best would be a pull request or send the files to mapbender@osgeo.org


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
* loader    - defines the loader to load and parse the file. We use YAML


Share your translations with the Mapbender3 community!
******************************************************
Supporting more and more language would be great for Mapbender3. The Mapbender project would be happy if you could share your translations with the community.

This is what you have to do:

* Option 1: send the new yml-files for your language to the Mapbender developer (mapbender@osgeo.org) or 

* Option 2: create a pull request on github

We prefer option 2.


How to translate and make a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Repositories 

* https://github.com/mapbender/mapbender/
* https://github.com/mapbender/mapbender-digitizer/
* https://github.com/mapbender/fom
* https://github.com/mapbender/data-manager/
https://github.com/mapbender/data-source
https://github.com/mapbender/map-tools/


Since Git is a distributed versioning system, it is very convenient for each developer/contributor to have a personal public copy of the "official" repository (also known as fork). 

Web hosting services like GitLab or GitHub provide this option if you visit the main code repository and press the button "Fork". This way the developer can make changes to a personal isolated repository. Then one can ask the rest of the developers to review the code and merge accordingly through a "pull request".

After forking the official repositories, your working repositories are: https://github.com/your_id/mapbender and https://github.com/your_id/mapbender


Github - editing on GitHub
=========================================

* you can edit files directly on GitHub.
* navigate to the file f.e https://github.com/mapbender/mapbender/blob/release/3.0.6/src/Mapbender/CoreBundle/Resources/translations/messages.de.yml
* edit the file
* save changes and create a new branch for this commit and start a pull request


git - working on the command line
=========================================

On Linux systems get the source code locally using:

.. code-block:: yaml
    
    git clone https://github.com/your_id/mapbender

In order to be able to get and send changes to your public repository, you need to link your local copy to your public copy. This is done automatically for you when you "git clone". The repository that you cloned from has the alias "origin".

In order to be able to get changes that others do to the main repository, you need to manually link to that using:

git remote add upstream https://github.com/mapbender/mapbender

On MS Windows systems, install TortoiseGit, which extends Windows Explorer to include git commands.

1. The first thing you should do when you install Git is to set your user name and e-mail address.

.. code-block:: yaml
    
    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com

.. code-block:: yaml
    
    cd mapbender

2. Pull any updates from upstream project (master is the equivalent of subversion trunk)

.. code-block:: yaml
    
    git pull upstream master

optionally check to see what has changed.

.. code-block:: yaml
    
    git diff messages.de.yml

3. add the changes into stage area

.. code-block:: yaml
    
    git add messages.de.yml

4. commit changes locally

.. code-block:: yaml
    
    git commit -m "changed translation"

5. send the changes to your public repository 

.. code-block:: yaml
    
    git push origin master

At this point you can let others know that you have some changes that you want to merge, so you can use the button "Pull Request" on GitLab or GitHub. Or you can continue until you feel ready to share your changes :)


6. Last step: pull request

In order to merge your work with the main repository, you have to make a pull request.

You can do it by logging on your github account and go to the branch you changed. Click on the New pull request green button. The changes you made previously while appear.

You can review and comment your request before submitting. To submit, click on the Create pull request green button. Then, you're done ! Good job !

More information about Github pull request here: https://help.github.com/articles/using-pull-requests/ 

Working with files:

to add a file

.. code-block:: yaml
    
    cd <dir>

create a file

.. code-block:: yaml
    
    git add <file>
    git commit -m "commit message"
    git push origin master


