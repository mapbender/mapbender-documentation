.. _yaml:

YAML Configuration (Configuration and Application files)
========================================================

The following configuration files are under `application/config` and its subfolders.


doctrine.yaml
-------------

* **fom_user.selfregistration**: To enable or disable self-registration of users, change this parameter. You have to define self_registration_groups, so that self-registered users are added to these groups automatically, when they register. They will get the rights that are assigned to these groups.
* **fom_user.reset_password**: In the same way the possibility to reset passwords can be enabled or disabled.
* **framework.session.cookie_httponly**: For HTTP-only session cookies, make sure the framework.session.cookie_httponly parameter is set to true.


Database configuration
**********************

The files ``.env.local`` and ``doctrine.yaml`` are needed to configure databases in Mapbender. In ``.env.local``, (multiple) variables and definitions for database connection(s) can be defined. These variables are being processed in ``doctrine.yaml``. 

.. note:: Every database defined in `.env` needs to have a placeholder in `doctrine.yaml`:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default                     # Database connection, used as standard in Mapbender (``default_connection: default``).
            connections:
                default:
                url: '%env(resolve:MAPBENDER_DATABASE_URL)%'# Placeholder which resolves the environment variable in parameters.yaml. 
                persistent: true                            # Parameter specifying if the database connection should be established continuously.
                charset:    UTF8                            # Coding of the database.
                #server_version: '15'                       # Important: You MUST configure your server version, either here or in the DATABASE_URL env var (see .env file).
                logging:   "%kernel.debug%"                 # Option, SQLs won't be logged (standard: %kernel.debug%). `More information: <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
                profiling: "%kernel.debug%"                 # Profiling SQL requests. This option can be turned of in production. (standard: %kernel.debug%)


**Use of several databases**

Example with two database connections in `doctrine.yaml`:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # database connection default
                default:
                    url: '%env(resolve:MAPBENDER_DATABASE_URL)%'
                    charset:    UTF8
                    #server_version: '15' 
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"
                # database connection geodata_db
                geodata_db:
                    url: '%env(resolve:GEOBASIS_DATABASE_URL)%'
                    persistent: true
                    charset:  UTF8
                    logging: '%kernel.debug%'
                    profiling: '%kernel.debug%'
                    # IMPORTANT: You MUST configure your server version,
                    # either here or in the DATABASE_URL env var (see .env file)
                    #server_version: '15'


.env or .env.local file
-----------------------
This file handles necessary environmental variables:


Database
********
The files `.env` and `doctrine.yaml` are used to configure database connections in Mapbender. In `.env`, (multiple) variables for database connection(s) can be defined. The `.env` is overwritten by `.env.local`.
This is read by `doctrine.yaml`. Several database connections can also be defined in `doctrine.yaml`. An alias is assigned to each database connection.

Example:
Database configuration in `.env.local` with the default database variable, if the pre-installed SQLite database is used:

.. code-block:: bash

    MAPBENDER_DATABASE_URL="sqlite:///%kernel.project_dir%/var/db/demo.sqlite"

When using PostgreSQL (e.g. for the use with :ref:`search_router`), use the following configuration instead:

.. code-block:: bash

    SEARCH_DB_DATABASE_URL="postgresql://dbuser:dbpassword@localhost:5432/dbname?serverVersion=14&charset=utf8"


Use of several databases
************************
Mapbender also allows you to use several databases. This is recommended when integrating geodata. These should be stored separately from the Mapbender database.
You need a second database for geo data search (with SearchRouter) and data collection (Digitizer).
The default database connection (``default_connection: default``) is used by Mapbender.

If you want to use another database, you just have to define a database connection with a different name in your `.env.local` file.
Now, you can refer to the database *search_db* in the elements SearchRouter and Digitizer.

To learn more about this structure, visit the `Symfony documentation <https://symfony.com/doc/current/best_practices.html#use-parameters-for-application-configuration>`_.
Mapbender uses Doctrine. Doctrine is a collection of PHP libaries (`Doctrine project <http://www.doctrine-project.org/>`_).


Mailer
*******
The mailer information is defined in the `.env.local` file via the ``MAILER_DSN`` variable.

.. code-block:: bash

    #MAILER_DSN=smtp://user:pass@smtp.example.com:25
    MAILER_DSN=null://null


The configuration will be called via the `fom.yaml` file:

.. code-block:: yaml

    fom_user:
        selfregister: false
        reset_password: true
        max_reset_time: 1
        mail_from_address: info@mapbender.org
        mail_from_name: Mapbender Team

.. hint:: The functions 'Self-Registration' and 'Reset password' need a mailer. More information in chapter :ref:`users`.


parameters.yaml
---------------
The following fundamental Mapbender parameters are specified here.


Disclaimer
**********

.. image:: ../../figures/disclaimer.png

A disclaimer can be added through the use of site links.

.. code-block:: yaml

    mapbender.sitelinks:
      - link: https://mapbender.org/en/legal-notice/				# Link URL
        text: Imprint & Contact									    # Link text
      - link: https://mapbender.org/en/privacy-policy/
        text: Privacy Policy
      - link: https://doc.mapbender.org/
        text: Documentation


Disabling Elements
******************
Disabling individual elements can be configured using the following parameter:

.. code-block:: yaml

    mapbender.disabled_elements:


Customizing icons
*****************
By setting the following parameters, you can enable specific customization of icons:

1. ``mapbender.icons.disable_default`` (default: false).

   - When set to `true`, the default icons from the Mapbender namespace are disabled in the button edit form. These include the icons About, Area Ruler, Feature Info, Image Export, Layer tree, Legend, Line ruler, and Polygon. These are used, for example, for the similarly named elements: :ref:`about_dialog`, :ref:`ruler`, :ref:`feature_info`, :ref:`imageexport`, :ref:`layertree`, :ref:`legend`, :ref:`digitizer`, and :ref:`sketch`.

2. ``mapbender.icons.disable_default_fa`` (default: false).

   - When set to `true`, the default Font Awesome icons are disabled in the button edit form. This applies to all other available icons that are not in the Mapbender namespace.

3. ``mapbender.icons.custom`` (default: ~).

   - Allows adding more icons from FontAwesome (a list of freely available icons can be found on the `Font Awesome homepage <https://fontawesome.com/search?o=r&m=free>`_).
   - The parameter is an array of objects containing three keys:

     - `name`: Identifier for this icon, e.g., for usage in yaml-defined applications.

     - `title`: Description of the icon as shown in the selection menu in the button edit form.

     - `class`: Full class name (including "fa") of the icon. Copy it from the lower part of the popup when you click on the icon on the Font Awesome homepage.

With these configuration options, you can customize the icons in Mapbender to suit your requirements. Here's an example:

.. code-block:: yaml

    mapbender.icons.disable_default: true
    mapbender.icons.disable_default_fa: true
    mapbender.icons.custom:
        - name: iconSnowflake
          title: Snowflake
          class: fa-solid fa-snowflake
        - name: iconHeartbeat
          title: Heartbeat
          class: fa-solid fa-heart-pulse


Language settings
*****************
Mapbender is automatically adjusted to your browser's language.
Yet it is also possible to set your preferred language via the `fallback_locale` parameter. If a translation of your browser's language is missing in Mapbender, it will take the defined language.

The locale can only be set for the entire Mapbender installation (not for single applications).

Available language codes are:

* en for English (default)
* de for German
* es for Spanish
* fr for French
* it for Italian
* nl for Dutch
* pt for Portugese
* ru for Russian
* tr for Turkish
* uk for Ukrainian     

Configuration example:

.. code-block:: yaml

    fallback_locale:   en
    locale:            en    
    secret:            ThisTokenIsNotSoSecretChangeIt


You also can force Mapbender to use the language defined for the parameter locale to be used. To do this, add ``mapbender.automatic_locale: false``.

.. code-block:: yaml

    mapbender.automatic_locale: false
    fallback_locale:   en
    locale:            es
    secret:            ThisTokenIsNotSoSecretChangeIt


More information in :ref:`translation`.


Logo and branding
*****************
In `parameters.yaml`, you can refer to your own logo and to an alternative image for the login page. This change has a global impact on the whole Mapbender installation.


.. code-block:: yaml

    branding.project_name: Geoportal powered by Mapbender
    branding.project_version: 1.0
    branding.logo: ./bundles/mapbendercore/image/OSGeo_project.png
    branding.favicon: ./application/public/brand-favicon.ico
    branding.login_backdrop: ./bundles/mapbendercore/image/login-backdrop.jpg


The files must be accessible under ``application/public``.


Project name
************
The name of the project (default: Mapbender) can be changed in `parameters.yaml`. The change has a global impact on the whole Mapbender installation.

.. code-block:: yaml

    branding.project_name: Geoportal


.. important:: In `parameters.yaml`, **tabulators may not be used for indentation**. Instead, you need to use the space bar.


Proxy settings
**************
If you use a proxy, you need to change `parameters.yaml`.

.. hint:: OWSProxy3 is a transparent Buzz-based proxy that uses cURL for connection to web resources via/without a proxy server.

Configuration example:

.. code-block:: yaml

    # OWSProxy Configuration
        ows_proxy3_logging: false             # logging of requests, default is false, true logs in table owsproxy_log 
        ows_proxy3_obfuscate_client_ip: true  # obfuscats a client ip, default is true, true will hide the last byte of the client's ip address
        ows_proxy3_host: myproxy              # proxy definition for connnection via a proxy server. Host name of the proxy server
        ows_proxy3_port: 8080                 # proxy definition for connnection via a proxy server. Port name of the proxy server
        ows_proxy3_connecttimeout: 60
        ows_proxy3_timeout: 90
        ows_proxy3_user: ~                    # user name for proxy server (set user for proxy server if needed)
        ows_proxy3_password: ~                # password for proxy server (set password for proxy server if defined)
        ows_proxy3_noproxy:                   # list of hosts for connnections without proxy server
            - 192.168.1.123


SSL certificate
***************
For productive environments, it is important to install a SSL certificate. After that, set the ``parameters.cookie_secure`` variable in your `parameters.yaml` to ``true``. This ensures that the Login cookie is only transmitted over secure connections.


Overriding JavaScript and CSS/Sass Resources
********************************************
To manually override JavaScript and CSS/Sass resources, and as an alternative to :ref:`overriding in the bundle <en/development/introduction:Overriding JavaScript and CSS/Sass Resources>`, you can add the following to your ``paramaters.yaml`` file:

.. code-block:: yaml
    
    mapbender.asset_overrides:
        "@MapbenderCoreBundle/Resources/public/sass/element/featureinfo.scss": "@@MyBundle/Resources/public/sass/element/custom_featureinfo.scss"


.. note:: Please note that the @ sign in the replacement key must be escaped with an additional @@ sign.


YAML Application files
-----------------------

YAML application files are stored under ``application/config/applications``. There are three files pre-implemented as example applications:

- Mapbender Demo (*mapbender_user*)
- Mapbender Demo Basic (*mapbender_user_basic*)
- Mapbender Mobile Demo (*mapbender_mobile*)

If you do not want the three example applications to be visible, you can adjust the ``published`` variable as follows.

.. code-block:: yaml

	parameters:
		applications:
			mapbender_mobile:
				[...]
				published: false


Then, clear the :ref:`Mapbender cache<en/customization/commands:Clear cache>` and your browser cache. After that, the applications will not be visible for users.

.. hint:: The root user can always see unpublished applications.


It is also possible to remove the applications from the ``applications`` folder. Repeat the cache clearing process afterwards.

In the same way, new YAML applications can be placed in the folder and will be automatically recognized by Mapbender.


Mapbender Demo Map
------------------

This is the main Demo application. Should be used for a desktop based application.

Detailed descriptions of the elements at :ref:`elements`.


Mapbender Demo Map basic
------------------------

Differences to the main Demo Map:

Toolbar
    Contains elements from the sidepane of the first demo application.

Sidepane
    Has no elements pre-implemented.

Map area
    Uses a compact :ref:`navigation_toolbar` without the zoom slider. Includes the :ref:`simplesearch`.

Detailed descriptions of the elements at :ref:`elements`.


Mapbender mobile
----------------

For a mobile template on smartphones and tablets.


Export/import YAML application files with the backend
-----------------------------------------------------

**Export**

You can export applications as JSON files under **Applications** → **Export**.

You can locate the export button within the application overview page. Find it in the application's button menu.

.. image:: ../../figures/application_export_button.png


**Import**

Under **Applications** → **Import**, an export file can be imported into a Mapbender installation.

To do this, first select the ``Create Application`` button. Then click on the Import button:

.. image:: ../../figures/import_button.png

Then, use the Import mask to load an import file as an application.

.. image:: ../../figures/import_mask.png


Export/import/clone YAML application files over the console
-----------------------------------------------------------

Please go to :ref:`en/customization/commands:Application Export, Import & Cloning` to see the console commands. Find a few introductional words about exporting and importing applications over the console below.

**Export**

Applications can be exported as .json or .yaml file over the console.

A YAML file that has been exported over the console cannot be placed under application/config/application to be imported in a Mapbender installation.
The YAML format that is produced by exporting over the console is different from the YAML format of the files under application/config/application.


**Import**

YAML files that have been exported over the user interface or console can be imported over the console.


**Clone**

Clone/Copy an existing application.

