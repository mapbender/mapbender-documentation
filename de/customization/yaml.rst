.. _yaml_de:

YAML Konfiguration (Konfigurations- und Anwendungsdateien)
==========================================================

Die folgenden Konfigurationsdateien liegen unter `config/` und dessen Unterverzeichnissen:


doctrine.yaml
-------------

Diese Datei enthält grundlegende Architektur-Vorgaben von Mapbender. Gleichzeitig sind hier die Parameter für die `parameters.yaml` als Platzhalter definiert. Des Weiteren legt die Datei fest, welche Konfigurationen für den produktiven Modus und den Entwicklungsmodus verwendet werden sollen.

* **fom_user.selfregistration**: Um die Selbstregistrierung zu de/aktivieren, passen Sie diesen Parameter an. Sie müssen unter self_registration_groups eine/mehrere Gruppen angeben, so dass selbstregistriere Anwender automatisch (bei der Registrierung) diesen Gruppen zugewiesen werden. Über die Gruppe bekommen Sie dann entsprechend Rechte zugewiesen.
* **fom_user.reset_password**: Über diesen Parameter kann die Möglichkeit de/aktiviert werden, das Passwort neu zu setzen.
* **framework.session.cookie_httponly**: Stellen Sie für HTTP-only session cookies sicher, dass der Parameter framework.session.cookie_httponly auf true steht.


Datenbank-Konfiguration
***********************

Zur Konfiguration der Datenbankverbindung erfolgt in den Dateien ``.env.local`` und ``doctrine.yaml``. In der ``.env.local`` wird die Datenbankverbindung definiert in einer Variable. Die Variablen werden in der ``doctrine.yaml`` angegeben.


.. note:: Jede Datenbank, die in der `.env` definiert wird, kann in der `doctrine.yaml` unter url zu einer Verbindung angegeben werden:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default                     # gibt die Datenbankverbindung an, die standardmäßig von Mapbender verwendet werden soll (``default_connection: default``).
            connections:
                default:
                url: '%env(resolve:MAPBENDER_DATABASE_URL)%'# Platzhalter, der auf die definierte Umgebungsvariable in der parameters.yaml verweist. 
                persistent: true                            # Parameter, ob die Verbindung zur Datenbank dauerhaft hergestellt werden soll.
                charset:    UTF8                            # Die Kodierung, die die Datenbank verwendet.
                logging:   "%kernel.debug%"                 # Die Option sorgt dafür, das alle SQLs nicht mehr geloggt werden (Standard: %kernel.debug%). `Mehr Informationen <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
                profiling: "%kernel.debug%"                 # Profiling von SQL Anfragen. Diese Option kann in der Produktion ausgeschaltet werden. (Standard: %kernel.debug%)
                #server_version: '15'                       # Wichtig: Sie MÜSSEN die Serverversion konfigurieren, entweder hier oder in der DATABASE_URL Umgebungsvariable (siehe .env-Datei).


**Verwendung mehrerer Datenbanken**

Es folgt ein Beispiel mit zwei Datenbankverbindungen in der `doctrine.yaml`:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # Datenbankverbindung default
                default:
                    url: '%env(resolve:MAPBENDER_DATABASE_URL)%'
                    charset:    UTF8
                    #server_version: '15'
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"
                # Datenbankverbindung geodata_db
                geodata_db:
                    url: '%env(resolve:GEOBASIS_DATABASE_URL)%'
                    persistent: true
                    charset:  UTF8
                    logging: '%kernel.debug%'
                    profiling: '%kernel.debug%'
                    # IMPORTANT: You MUST configure your server version,
                    # either here or in the DATABASE_URL env var (see .env file)
                    #server_version: '15'


.env bzw. .env.local
--------------------
In dieser Datei werden zentrale Umgebungsvariablen zusammengeführt:


Datenbank
*********
Zur Konfiguration der Datenbankverbindung werden die Dateien `.env` und `doctrine.yaml` verwendet. In der `.env` wird die Umgebungsvariable für die Datenbankverbindung definiert. `.env` wird von `.env.local` überschrieben.
Diese wird in der `doctrine.yaml` ausgelesen. In der `doctrine.yaml` können auch mehrere Datenbankverbindungen definiert werden. Zu jeder Datenbankverbindung wird ein Alias vergeben.

Beispiel:
Die Datenbankkonfiguration in der `.env` sieht standardmäßig folgendermaßen aus, sofern die mitinstallierte SQLite-Datenbank verwendet wird:

.. code-block:: bash

    MAPBENDER_DATABASE_URL="sqlite:///%kernel.project_dir%/var/db/demo.sqlite"

Beispiel:
Die Datenbankkonfiguration in der `.env.local` sieht wie folgt aus, wenn eine Suchdatenbank via PostgreSQL referenziert wird:

.. code-block:: bash

    SEARCH_DB_DATABASE_URL="postgresql://dbuser:dbpassword@localhost:5432/dbname?serverVersion=14&charset=utf8"


Verwendung mehrerer Datenbanken
*******************************
Mit Mapbender können Sie auch mehrere Datenbanken verwenden. Dies wird bei der Einbindung von Geodaten empfohlen. Diese sollten getrennt von der Mapbender-Datenbank liegen.
Eine zweite Datenbank benötigen Sie ebenfalls für die Geodatensuche (über den :ref:`search_router_de`) und die Datenerfassung (:ref:`digitizer_de`).
Die Standard-Datenbankverbindung (``default_connection: default``) wird von Mapbender verwendet.

Wenn Sie eine weitere Datenbank verwenden möchten, müssen Sie eine zweite Datenbankverbindung mit einem anderen Namen in der `.env.local`-Datei definieren.
In den Elementen :ref:`search_router_de` und :ref:`digitizer_de` kann nun auf die Datenbankverbindung (connection) mit dem Namen *search_db* verwiesen werden.

Weitere Information über diese Konfigurationsmöglichkeit gibt es in der `Symfony Dokumentation <https://symfony.com/doc/current/best_practices.html#use-parameters-for-application-configuration>`_.
Mapbender verwendet Doctrine. Doctrine ist eine Sammlung von PHP-Bibliotheken und bietet einen objektrelationalen Mapper und eine Datenbankabstraktionsschicht (`Doctrine Projektseite <https://www.doctrine-project.org/>`_).


Mailer
******
Die Angabe zum Mailer wird in der `.env.local` Datei über die Variable ``MAILER_DSN`` definiert.

.. code-block:: bash

    #MAILER_DSN=smtp://user:pass@smtp.example.com:25
    MAILER_DSN=null://null

Der Mailer-Einstellugnen selbst werden in `fom.yaml` konfiguriert.

.. code-block:: yaml

    fom_user:
        selfregister: false
        reset_password: true
        max_reset_time: 1
        mail_from_address: info@mapbender.org
        mail_from_name: Mapbender Team
           
.. hint:: Ein Mailer wird für die Funktionen 'Registrierung' und 'Passwort zurücksetzen' benötigt. Weitere Informationen im Kapitel :ref:`users_de`.


parameters.yaml
---------------
Hier werden weitere grundlegende Parameter von Mapbender bestimmt.


Disclaimer
**********

.. image:: ../../figures/disclaimer.png

Es kann ein Disclaimer mittels Sitelinks hinzugefügt werden. Dafür muss Folgendes in der `parameters.yaml` ergänzt werden:

.. code-block:: yaml

    mapbender.sitelinks:
      - link: https://mapbender.org/impressum           			# Link URL
        text: Impressum & Kontakt									# Link Text
      - link: https://mapbender.org/datenschutz
        text: Datenschutz
      - link: https://doc.mapbender.org/
        text: Dokumentation

Die Sitelinks werden mittels "|" voneinander getrennt.

Elemente deaktivieren
*********************
Die Deaktivierung von einzelnen Elementen kann über den nachfolgenden Parameter konfiguriert werden:

.. code-block:: yaml

    mapbender.disabled_elements:



Icons anpassen
**************
Mithilfe des Setzens folgender Parameter wird die spezifische Anpassung von Icons ermöglicht:

1. ``mapbender.icons.disable_default`` (Standardwert: false).

   - Wenn auf `true` gesetzt, werden die mitgelieferten Icons des Mapbender-Namespace im Button-Bearbeitungsformular deaktiviert. Dazu gehören die Icons About, Area Ruler, Feature Info, Image Export, Layer tree, Legend, Line ruler und Polygon. Diese werden z.B. für die ähnlich bezeichneten Elemente :ref:`about_dialog_de`, :ref:`ruler_de`, :ref:`feature_info_de`, :ref:`imageexport_de`, :ref:`layertree_de`, :ref:`legend_de`, :ref:`digitizer_de` und :ref:`sketch_de` verwendet.

2. ``mapbender.icons.disable_default_fa`` (Standardwert: false).

   - Wenn auf `true` gesetzt, werden die mitgelieferten Font Awesome-Icons im Button-Bearbeitungsformular deaktiviert. Dies betrifft alle anderen verfügbaren Icons, die nicht im Mapbender-Namespace enthalten sind.

3. ``mapbender.icons.custom`` (Standardwert: ~).

   - Ermöglicht das Hinzufügen weiterer Icons aus FontAwesome (eine Liste frei verfügbarer Icons finden Sie auf der `Font Awesome-Homepage <https://fontawesome.com/search?o=r&m=free>`_.
   - Der Parameter ist ein Array von Objekten, die drei Schlüssel enthalten:

     - `name`: Bezeichnung für dieses Icon, z.B. zur Verwendung in yaml-definierten Anwendungen.

     - `title`: Beschreibung des Icons, wie es im Auswahlfeld im Bearbeitungsformular für Schaltflächen angezeigt wird.

     - `class`: Vollständiger Klassenname (einschließlich "fa") des Icons. Kopieren Sie ihn aus dem unteren Teil des Popups, wenn Sie auf das Icon auf der Font Awesome-Homepage klicken.

Mit diesen Konfigurationsoptionen können Sie die Icons in Mapbender an Ihre Anforderungen anpassen. Anbei ein Beispiel:

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



Logo und Login-Bild
*******************
In der `parameters.yaml` kann auf das eigene Logo und auf ein alternatives Bild für den Login verwiesen werden. Diese Änderung wirkt sich global auf die gesamte Mapbender-Installation aus.

Mithilfe der Branding-Parameter kann ein eigener Projektname, eine eigene Versionsnummer, ein Logo, eine eigene Favoriten-Symbolgrafik und ein alternatives Bild für den Login verwendet werden. Diese Änderung wirkt sich global auf die gesamte Mapbender-Installation aus.

.. code-block:: yaml

    branding.project_name: Geoportal powered by Mapbender
    branding.project_version: 1.0
    branding.logo: ./bundles/mapbendercore/image/OSGeo_project.png
    branding.favicon: ./application/public/brand-favicon.ico
    branding.login_backdrop: ./bundles/mapbendercore/image/login-backdrop.jpg

Die Dateien müssen unter ``application/public`` verfügbar sein.



Projektname
***********
Der Projektname (Standard: Mapbender) kann in der Datei `parameters.yaml` angepasst werden. Diese Änderung wirkt sich global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.project_name: Geoportal


.. warning:: In der `parameters.yaml` dürfen **keine Tabulatoren für Einrückungen** verwendet werden. Nutzen Sie stattdessen Leerzeichen.


Proxy-Einstellungen
*******************
Wenn ein Proxy verwendet wird, muss dieser in der Datei `parameters.yaml` im Bereich OWSProxy Configuration angegeben werden.

Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml

    # OWSProxy Configuration
        ows_proxy3_logging: false             # Protokollierung von Anfragen, Standard ist false, true protokolliert in Tabelle owsproxy_log 
        ows_proxy3_obfuscate_client_ip: true  # Verbergen der Client IP, Standard ist true, true verbirgt das letzte Byte der IP-Adresse des Clients
        ows_proxy3_host: myproxy              # Proxy-Definition für die Verbindung über einen Proxy-Server. Hostname des Proxyservers
        ows_proxy3_port: 8080                 # Proxy-Definition für die Verbindung über einen Proxy-Server. Port des Proxyservers
        ows_proxy3_connecttimeout: 60
        ows_proxy3_timeout: 90
        ows_proxy3_user: ~                    # Benutzername für Proxyserver (bei Bedarf Benutzer für Proxyserver festlegen)
        ows_proxy3_password: ~                # Passwort für den Proxy-Server (setzen Sie das Passwort für den Proxy-Server, falls definiert)
        ows_proxy3_noproxy:                   # Liste der Hosts, bei denen die Verbindungen nicht über den Proxyserver erfolgen soll
            - 192.168.1.123


Spracheinstellung
*****************
Mapbender verwendet automatisch die ausgewählte Sprache der Browsereinstellungen.
Es ist jedoch möglich, eine bevorzugte Sprache (`fallback_locale`) zu definieren, die Mapbender bei unvollständigen Übersetzungen anstelle der Browsersprache nutzt.

Die Sprache kann nur für die gesamte Mapbender Installation angepasst werden (nicht für einzelne Anwendungen).

Folgende Sprachcodes sind verfügbar:

* en für Englisch (Standard)
* de für Deutsch
* es für Spanisch
* fr für französisch,
* it für Italienisch
* nl für Niederländisch
* pt für Portugiesisch
* ru für Russisch
* tr für Türkisch
* uk für Ukrainisch

Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml

    fallback_locale:   en
    locale:            de    
    secret:            ThisTokenIsNotSoSecretChangeIt


Mapbender kann auch explizit eine Sprache verwenden. Dazu muss der Parameter ``mapbender.automatic_locale: false`` gesetzt werden. Anschließend nutzt Mapbender die unter locale definierte Spracheinstellung.

.. code-block:: yaml

    mapbender.automatic_locale: false
    fallback_locale:   en
    locale:            es
    secret:            ThisTokenIsNotSoSecretChangeIt


Weitere Informationen unter :ref:`translation`.


SSL Zertifikat
**************
Für Produktivumgebungen ist die Installation eines SSL-Zertifikats wichtig. Anschließend muss die Variable ``parameters.cookie_secure`` in Ihrer `parameters.yaml` auf ``true`` gesetzt werden. Dadurch wird sichergestellt, dass das Login-Cookie nur über sichere Verbindungen übertragen wird.


Überschreiben von JavaScript- und CSS/Sass-Ressourcen
*****************************************************
Um genannte Ressourcen manuell zu überschreiben, können Sie als Alternative :ref:`zum Überschreiben im Bundle selbst<de/development/introduction:Überschreiben von JavaScript- und CSS/Sass-Ressourcen>` in Ihrer ``paramaters.yaml``-Datei Folgendes hinzufügen:

.. code-block:: yaml

    mapbender.asset_overrides:
        "@MapbenderCoreBundle/Resources/public/sass/element/featureinfo.scss": "@@MyBundle/Resources/public/sass/element/custom_featureinfo.scss"


.. note:: Beachten Sie, dass das `@`-Zeichen im Ersetzungsschlüssel durch ein weiteres `@@`-Zeichen maskiert werden muss.


YAML Anwendungsdateien
----------------------

Als YAML definierte Anwendungen werden im Verzeichnis `/applications/` abgelegt. Dort liegen nach jeder Installation bereits drei Beispielanwendungen als YAML Dateien:

- Mapbender Demo (*mapbender_user*)
- Mapbender Demo Basic (*mapbender_user_basic*)
- Mapbender Mobile Demo (*mapbender_mobile*)

Falls eine Beispielanwendung nicht im Mapbender sichtbar sein soll, kann sie mit einem Texteditor geöffnet und die Variable ``published`` wie folgt angepasst werden:

.. code-block:: yaml

	parameters:
		applications:
			mapbender_mobile:
				[...]
				published: false


Löschen Sie anschließend den :ref:`Mapbender-Cache<de/customization/commands:Cache löschen>` und Ihren Browser-Cache. Danach ist die Anwendung für Benutzer nicht mehr sichtbar.

.. hint:: Der Root-Benutzer sieht immer alle unveröffentlichten Anwendungen.


Sie können außerdem die Anwendungsdateien aus dem Verzeichnis ``applications`` entfernen, um Sie aus der Mapbender-Instanz zu entfernen. Wiederholen Sie anschließend das Löschen der Caches.

Auf die gleiche Weise können auch neue YAML-basierte Anwendungen in dieses Verzeichnis abgelegt werden, um sie der Mapbender-Instanz hinzuzufügen.


Mapbender Demo Map
------------------

Dies ist die Demo-Anwendung, die für eine Desktop-Anwendung standardmäßig verwendet werden sollte.

Detaillierte Beschreibungen zu den enthaltenen Elementen finden Sie unter :ref:`elements_de`.


Mapbender Demo Map basic
------------------------

Die zweite Demo-Anwendung, welche folgende Unterschiede zur ersten Demo-Anwendung aufweist:

Werkzeugleiste
    Enthält Elemente aus dem Seitenbereich der ersten Demo-Anwendung.

Seitenbereich
    Enthält keine im Voraus konfigurierten Elemente.

Kartenbereich
    Verwendet eine kompaktere :ref:`navigation_toolbar_de` ohne den Zoom-Schieberegler.
    Beinhaltet die :ref:`simplesearch_de`.

Detaillierte Beschreibungen der Elemente finden Sie unter :ref:`elements_de`.


Mapbender mobile
----------------

Diese Anwendung dient als mobile Vorlage für Smartphones und Tablets.


Export/Import von YAML Anwendungsdateien über die Benutzeroberfläche
--------------------------------------------------------------------

**Export**

Sie können eine Anwendung unter **Anwendungen** → **Exportieren** als JSON-Datei exportieren.

Nutzen Sie dazu den Exportieren-Button, der sich in der Anwendungsübersicht im Button-Menü einer Anwendung befindet.

.. image:: ../../figures/application_export_button.png


**Import**

Unter **Anwendungen** → **Importieren** kann eine Exportdatei in eine Mapbender-Installation importiert werden.

Wählen Sie dazu zunächst den Button ``+ Anwendung anlegen``. Anschließend klicken Sie auf den Importieren-Button.

.. image:: ../../figures/de/application_import_button.png

Nutzen Sie danach die abgebildete Maske, um eine Importdatei als Anwendung zu laden.

.. image:: ../../figures/de/import_dialog.png


Export/Import/Klonen von YAML Anwendungsdateien über die Konsole
----------------------------------------------------------------

Bitte gehen Sie zu :ref:`de/customization/commands:Anwendungs-Export, Import und Klonen`, um entsprechende Konsolenbefehle einzusehen. Nachfolgend finden Sie einige einführende Worte darüber, was mit Anwendungen über die Konsole möglich ist.

**Export über die Konsole**

Anwendungen können als .json oder .yaml - Datei über die Konsole exportiert werden.
Jedoch kann eine YAML-Datei, die über die Konsole exportiert wurde, nicht unter `/applications/` abgelegt und somit als Anwendung in Mapbender eingefügt werden.
Das YAML-Format einer Datei, die über die Konsole exportiert wurde, unterscheidet sich von dem YAML-Format der Dateien unter `/applications/`.

**Import über die Konsole**

YAML-Dateien, die zuvor über die Benutzeroberfläche oder die Konsole exportiert wurden, können über die Konsole via bin/console importiert werden.


**Anwendung über die Konsole klonen**

Klont/Kopiert eine existierende Anwendung.

