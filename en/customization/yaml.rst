.. _yaml:

YAML Configuration (Configuration and Application files)
========================================================

The following Configuration files are under application/config.


parameters.yaml
---------------
The following fundamental Mapbender parameters are specified here.


Database
********
The files ``parameters.yaml`` and ``doctrine.yaml`` are needed to configure databases in Mapbender. In ``parameters.yaml``, (multiple) variables for database connection(s) can be defined. These variables are being processed in ``doctrine.yaml``. An alias is assigned to each database connection.

* **database_driver**: Database driver. Possible values are:
    * pdo_sqlite - SQLite PDO driver
    * pdo_mysql - MySQL PDO driver
    * pdo_pgsql - PostgreSQL PDO driver
    * oci8 - Oracle OCI8 driver
    * pdo_oci - Oracle PDO driver

  Please note: Necessary PHP drivers need to be installed and activated.

Example:
Database configuration in ``parameters.yaml``, when PostgreSQL is used:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: secret


Use of several databases
************************
Mapbender can handle several databases. This is recommended if you want to keep your data seperated from Mapbender data. Or if you want to use code that doesn't belong to a Mapbender bundle.

You need a second database for *geo data search* (with SearchRouter)  and data collection (Digitizer).

The default database connection (``default_connection: default``) is used by Mapbender.

If you want to use another database, you have to define a database connection with a different name.

.. code-block:: yaml

    parameters:
        # database connection "default"
        database_driver:   pdo_pgsql
        database_host:     localhost
        database_port:     5432
        database_name:     mapbender
        database_path:     ~
        database_user:     postgres
        database_password: postgres

        # database connection "search_db"
        database2_driver:   pdo_pgsql
        database2_host:     localhost
        database2_port:     5432
        database2_name:     search_db
        database2_path:     ~
        database2_user:     postgres
        database2_password: postgres


Now, you can refer to the database **search_db** in the elements SearchRouter and Digitizer.

To learn more about this structure, visit the `Symfony documentation <https://symfony.com/doc/current/best_practices.html#use-parameters-for-application-configuration>`_.

Mapbender uses Doctrine. Doctrine is a collection of PHP libaries (`Doctrine project <http://www.doctrine-project.org/>`_).


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

Site links will be seperated by "|".


.. _custom-icons:

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
Mapbender is automatically adjusted to your browser's language. Yet it is possible to set a language option in the configuration file **application/config/parameters.yaml**.
If a translation of your browser's set language is missing in Mapbender, it will then take a fallback language.

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


You also can force Mapbender to use the language defined for the parameter locale to be used. to do this add mapbender.automatic_locale: false.

.. code-block:: yaml

    mapbender.automatic_locale: false
    fallback_locale:   en
    locale:            es
    secret:            ThisTokenIsNotSoSecretChangeIt


More information in :ref:`translation`.


Logo
****
In parameters.yaml, you can refer to your own logo and to an alternative image for the login page. This change has a global impact on the whole Mapbender installation.

.. code-block:: yaml

    branding.logo: ./bundles/mapbendercore/image/logo_mb.png
    branding.login_backdrop: ./bundles/mapbendercore/image/body.png


 The files must be accessible under application/public.


Mailer
*******
Mailer information are inserted in ``parameters.yaml`` via the `mailer_dsn` parameter (e.g. smtp or sendmail).

Configuration example:

.. code-block:: yaml

    mailer_dsn: smtp://user:pass@smtp.example.com:25

The functions 'Self-Registration' and 'reset password' need a mailer.

More information in chapter :ref:`users`.


Project name
************
The name of the project (default: Mapbender) can be changed in ``parameters.yaml``. The change has a global impact on the whole Mapbender installation.

.. code-block:: yaml

    branding.project_name: Geoportal


**Important note:** In ``parameters.yaml`` **tabulators may not be used for indentation** instead you need to use space.


Proxy settings
**************
If you use a proxy, you need to change ``parameters.yaml``.

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
For productive environments, it is important to install a SSL certificate. After that, set the ``parameters.cookie_secure`` variable in your ``parameters.yaml`` to ``true``. This ensures that the Login cookie is only transmitted over secure connections.


doctrine.yaml
-------------

* **fom_user.selfregistration**: To enable or disable self-registration of users, change the fom_user.selfregistration parameter. You have to define self_registration_groups, so that self-registered users are added to these groups automatically, when they register. They will get the rights that are assigned to these groups.
* **fom_user.reset_password**: In the same way the possibility to reset passwords can be enabled or disabled.
* **framework.session.cookie_httponly**: For HTTP-only session cookies, make sure the framework.session.cookie_httponly parameter is set to true.


Database
********
Important: Every database defined in parameters.yaml needs to have a placeholder in ``doctrine.yaml`` as well:

.. code-block:: yaml

    doctrine:                                               # Values, surrounded by %-marks, are variables
        dbal:
            default_connection: default                     # Database connection, used as standard in Mapbender (``default_connection: default``).
            connections:
                default:
                driver:    "%database_driver%"              # More information below the code
                host:      "%database_host%"                # Database host on which the database runs. Either name of the host (e.g. localhost) or IP address (e.g. 127.0.0.1).
                port:      "%database_port%"                # Port, the database listens to (e.g. 5432 for PostgreSQL).
                dbname:    "%database_name%"                # Name of the database (e.g. mapbender). Create a database with the command ``doctrine:database:create`` bzw. ``doctrine:schema:create``.
                path:      "%database_path%"                # %database_path%, path to the file of the SQLite database. If you don't use a SQ-lite database, write (~) or ``null``.
                user:      "%database_user%"                # User name for database connection.
                password:  "%database_password%"            # Password.
                persistent: true                            # Parameter specifying if the database connection should be established continuously.
                charset:    UTF8                            # Coding of the database.
                #server_version: '15'                       # Important: You MUST configure your server version, either here or in the DATABASE_URL env var (see .env file).
                logging:   "%kernel.debug%"                 # Option, SQLs won't be logged (standard: %kernel.debug%). `More information: <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
                profiling: "%kernel.debug%"                 # Profiling SQL requests. This option can be turned of in production. (standard: %kernel.debug%)


Use of several databases
************************
Example with two database connections in ``doctrine.yaml``:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # database connection default
                default:
                    driver:    "%database_driver%"
                    host:      "%database_host%"
                    port:      "%database_port%"
                    dbname:    "%database_name%"
                    path:      "%database_path%"
                    user:      "%database_user%"
                    password:  "%database_password%"
                    charset:    UTF8
                    #server_version: '15' 
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"
                # database connection search_db
                search_db:
                    driver:    "%database2_driver%"
                    host:      "%database2_host%"
                    port:      "%database2_port%"
                    dbname:    "%database2_name%"
                    path:      "%database2_path%"
                    user:      "%database2_user%"
                    password:  "%database2_password%"
                    charset:    UTF8
                    #server_version: '15' 
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"

More information under ``parameters.yaml``.


YAML Application files
-----------------------

YAML application files are stored under **application/config/applications**.
“**Mapbender mobile**”, “**Mapbender Demo Map**” and “**Mapbender Demo Map basic**” are pre-implemented as example applications.

If you do not want the three example applications to be visible, you can change the variable 'published' to 'false'.

.. code-block:: yaml

	parameters:
		applications:
			mapbender_mobile:
				[...]
				published: false

Now the applications will not be visible for users (except for root user).

New YAML applications can be placed in the folder and will be automatically recognized by Mapbender.


Mapbender Demo Map
------------------

This is the main Demo application. Should be used for a desktop based application.

Detailed descriptions of the elements at :ref:`elements`.


Mapbender Demo Map basic
------------------------

Differences to the main Demo Map:

Toolbar
    Uses :ref:`coordinate_utility` instead of :ref:`POI`.

Sidepane
    Has no elements pre-implemented.

Map area
    Uses :ref:`coordinate_utility` instead of :ref:`scaledisplay` and :ref:`POI`.

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

Please go to :ref:`app_command_export_import_clone` to see the console commands. Find a few introductional words about exporting and importing applications over the console below.

**Export**

Applications can be exported as .json or .yaml file over the console.

A YAML file that has been exported over the console cannot be placed under application/config/application to be imported in a Mapbender installation.
The YAML format that is produced by exporting over the console is different from the YAML format of the files under application/config/application.


**Import**

YAML files that have been exported over the user interface or console can be imported over the console.


**Clone**

Clone/Copy an existing application.

