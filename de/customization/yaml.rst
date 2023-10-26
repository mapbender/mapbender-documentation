.. _yaml_de:

YAML Konfiguration (Konfigurations- und Anwendungsdateien)
==========================================================

Die folgenden Konfigurationsdateien sind zu finden unter application/config.


parameters.yaml
---------------
Hier werden grundlegende Parameter von Mapbender bestimmt.


Datenbank
*********
Zur Konfiguration der Datenbankverbindung werden die Dateien ``parameters.yaml`` und ``doctrine.yaml`` verwendet. In der ``parameters.yaml`` werden Variablen für die Datenbankverbindung definiert. Es können mehrere Datenbankverbindungen definiert werden. Die Variablen werden in der ``doctrine.yaml`` verarbeitet. Zu jeder Datenbankverbindung wird ein Alias vergeben.

* **database_driver**: Der Datenbanktreiber. Mögliche Werte sind:
    * pdo_sqlite - SQLite PDO driver
    * pdo_mysql - MySQL PDO driver
    * pdo_pgsql - PostgreSQL PDO driver
    * oci8 - Oracle OCI8 driver
    * pdo_oci - Oracle PDO driver

  Beachten Sie, dass Sie den entsprechenden PHP-Treiber installiert bzw. aktiviert haben.

Beispiel:
Die Datenbankkonfiguration in der ``parameters.yaml`` sieht folgendermaßen aus, wenn PostgreSQL verwendet wird:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:     ~
    database_user:     postgres
    database_password: geheim


Verwendung mehrerer Datenbanken
*******************************
Mit Mapbender können Sie auch mehrere Datenbanken verwenden. Dies wird empfohlen, wenn Sie Ihre eigenen Daten von den Mapbender-Daten trennen möchten. Das kann nützlich sein, wenn Sie eigenen Code verwenden, der nicht zu einem Mapbender-Bundle gehört.

Eine zweite Datenbank benötigen Sie ebenfalls für die *Geodatensuche* (über den SearchRouter) und die Datenerfassung (Digitizer). Die Geodaten sollten grundsätzlich in einer anderen Datenbank als der Mapbender Datenbank gesichert werden.

Die Standard-Datenbankverbindung (``default_connection: default``) wird von Mapbender verwendet.

Wenn Sie eine weitere Datenbank verwenden möchten, müssen Sie eine zweite Datenbankverbindung mit einem anderen Namen definieren.

.. code-block:: yaml

    parameters:
        # Datenbankverbindung "default"
        database_driver:   pdo_pgsql
        database_host:     localhost
        database_port:     5432
        database_name:     mapbender
        database_path:     ~
        database_user:     postgres
        database_password: postgres

        # Datenbankverbindung "search_db"
        database2_driver:   pdo_pgsql
        database2_host:     localhost
        database2_port:     5432
        database2_name:     search_db
        database2_path:     ~
        database2_user:     postgres
        database2_password: postgres


In den Elementen SearchRouter und Digitizer kann nun auf die Datenbankverbindung (connection) mit dem Namen **search_db** verwiesen werden.

Weitere Information über diese Konfigurationsmöglichkeit gibt es in der `Symfony Dokumentation <https://symfony.com/doc/current/best_practices.html#use-parameters-for-application-configuration>`_.

Mapbender verwendet Doctrine. Doctrine ist eine Sammlung von PHP-Bibliotheken und bietet einen objektrelationalen Mapper und eine Datenbankabstraktionsschicht (`Doctrine Projektseite <https://www.doctrine-project.org/>`_).


Disclaimer
**********

.. image:: ../../figures/disclaimer.png

Es kann ein Disclaimer mittels Sitelinks hinzugefügt werden. Dafür muss Folgendes in der ``parameters.yaml`` ergänzt werden:

.. code-block:: yaml

    mapbender.sitelinks:
      - link: https://mapbender.org/impressum           			# Link URL
        text: Impressum & Kontakt									# Link Text
      - link: https://mapbender.org/datenschutz
        text: Datenschutz

Die Sitelinks werden mittels "|" voneinander getrennt.


Logo und Login-Bild
*******************
In der ``parameters.yaml`` kann auf das eigene Logo und auf ein alternatives Bild für den Login verwiesen werden. Diese Änderung wirkt sich global auf die gesamte Mapbender-Installation aus.

.. code-block:: yaml

    branding.logo: ./bundles/mapbendercore/image/logo_mb.png
    branding.login_backdrop: ./bundles/mapbendercore/image/body.png


Die Dateien müssen unter application/web verfügbar sein.


Mailer
******
Die Mailerangaben werden in der ``parameters.yaml`` über `mailer_dsn` eingetragen.
Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml

    mailer_dsn: smtp://user:pass@smtp.example.com:25


Ein Mailer wird für die Funktionen 'Self-Registration' und 'Passwort zurücksetzen' benötigt.

Weitere Informationen im Kapitel :ref:`users_de`.


Projektname
***********
Der Projektname (Standard: Mapbender) kann in der Datei ``parameters.yaml`` angepasst werden. Diese Änderung wirkt sich global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.project_name: Geoportal


**Wichtiger Hinweis:** In der ``parameters.yaml`` dürfen **keine Tabulatoren für Einrückungen** verwendet werden.


Proxy-Einstellungen
*******************
Wenn ein Proxy verwendet wird, muss dieser in der Datei ``parameters.yaml`` im Bereich OWSProxy Configuration angegeben werden.

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
Es ist jedoch möglich, eine bevorzugte Sprache (fallback) zu definieren, die Mapbender bei unvollständigen Übersetzungen anstelle der Browsersprache nutzt. Es werden Englisch und/oder Deutsch aufgrund ihres hohen Übersetzungsanteils empfohlen.
Dies kann nur für die gesamte Mapbender Installation angepasst werden (nicht für einzelne Anwendungen).

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

    # locale en, de, es, fr, it, nl, pt, ru, tr, uk are available
    fallback_locale:   en
    locale:            de    
    secret:            ThisTokenIsNotSoSecretChangeIt

Weitere Informationen unter :ref:`translation`.


SSL Zertifikat
**************
Für Produktivumgebungen ist die Installation eines SSL-Zertifikats wichtig. Anschließend muss die Variable ``parameters.cookie_secure`` in Ihrer ``parameters.yaml`` auf ``true`` gesetzt werden. Dadurch wird sichergestellt, dass das Login-Cookie nur über sichere Verbindungen übertragen wird.

doctrine.yaml
-------------

Diese Datei enthält grundlegende Architektur-Vorgaben von Mapbender. Gleichzeitig sind hier die Parameter für die ``parameters.yaml`` als Platzhalter definiert. Des Weiteren legt die Datei fest, welche Konfigurationen für den produktiven Modus und den Entwicklungsmodus verwendet werden sollen.

* **fom_user.selfregistration**: Um die Selbstregistrierung zu de/aktivieren, passen Sie den fom_user.selfregistration Parameter an.   Sie müssen unter self_registration_groups eine/mehrere Gruppen angeben, so dass selbstregistriere Anwender automatisch (bei der Registrierung) diesen Gruppen zugewiesen werden. Über die Gruppe bekommen Sie dann entsprechend Rechte zugewiesen.
* **fom_user.reset_password**: Über diesen Parameter kann die Möglichkeit de/aktiviert werden, das Passwort neu zu setzen.
* **framework.session.cookie_httponly**: Stellen Sie für HTTP-only session cookies sicher, dass der Parameter framework.session.cookie_httponly auf true steht.

Datenbank
*********
Wichtig: Jede Datenbank, die in der ``parameters.yaml`` definiert wird, muss auch als Platzhalter in der ``doctrine.yaml`` stehen:

.. code-block:: yaml

    doctrine:                                               # Bei Werten, die von dem %-Zeichen umschlossen werden,handelt es sich um Variablen
        dbal:
            default_connection: default                     # gibt die Datenbankverbindung an, die standardmäßig von Mapbender verwendet werden soll (``default_connection: default``).
            connections:
                default:
                driver:    "%database_driver%"              # Mehr Information unterhalb des Codes
                host:      "%database_host%"                # Der Host, auf dem die Datenbank läuft. Entweder der Name (z.B. localhost) oder die IP-Adresse (z.B. 127.0.0.1).
                port:      "%database_port%"                # Der Port, auf dem die Datenbank lauscht (z.B. 5432 für PostgreSQL).
                dbname:    "%database_name%"                # Der Name der Datenbank (z.B. mapbender). Erstellen Sie die Datenbank mit dem Befehl ``doctrine:database:create`` bzw. ``doctrine:schema:create``.
                path:      "%database_path%"                # Der %database_path% ist der Pfad zur Datei der SQLite-Datenbank. Wenn Sie keine SQLite-Datenbank verwenden, schreiben Sie als Wert entweder eine Tilde (~) oder ``null``.
                user:      "%database_user%"                # Benutzername für die Verbindung zur Datenbank.
                password:  "%database_password%"            # Das Passwort des Datenbankbenutzers.
                charset:    UTF8                            # Die Kodierung, die die Datenbank verwendet.
                logging:   "%kernel.debug%"                 # Die Option sorgt dafür, das alle SQLs nicht mehr geloggt werden (Standard: %kernel.debug%). `Mehr Informationen <http://www.loremipsum.at/blog/doctrine-2-sql-profiler-in-debugleiste>`_.
                profiling: "%kernel.debug%"                 # Profiling von SQL Anfragen. Diese Option kann in der Produktion ausgeschaltet werden. (Standard: %kernel.debug%)

**Verwendung mehrerer Datenbanken**

Es folgt ein Beispiel mit zwei Datenbankverbindungen in der **doctrine.yaml**:

.. code-block:: yaml

    doctrine:
        dbal:
            default_connection: default
            connections:
                # Datenbankverbindung default
                default:
                    driver:    "%database_driver%"
                    host:      "%database_host%"
                    port:      "%database_port%"
                    dbname:    "%database_name%"
                    path:      "%database_path%"
                    user:      "%database_user%"
                    password:  "%database_password%"
                    charset:    UTF8
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"
                # Datenbankverbindung search_db
                search_db:
                    driver:    "%database2_driver%"
                    host:      "%database2_host%"
                    port:      "%database2_port%"
                    dbname:    "%database2_name%"
                    path:      "%database2_path%"
                    user:      "%database2_user%"
                    password:  "%database2_password%"
                    charset:    UTF8
                    logging:   "%kernel.debug%"
                    profiling: "%kernel.debug%"


Weitere Informationen weiter oben unter parameters.yaml.


YAML Anwendungsdateien
----------------------

Als YAML definierte Anwendungen können in dem Verzeichnis **application/config/applications** abgelegt werden. Die bekannten Beispielanwendungen “**Mapbender mobile**”, “**Mapbender Demo Map**” und “**Mapbender Demo Map basic**” liegen dort als einzelne YAML Dateien.

Sollen die drei Beispielanwendungen nicht im Mapbender sichtbar sein, so kann unter **application/config/applications** die einzelne Anwendung ausgewählt und deren Variable "published" auf "false" gesetzt werden.

.. code-block:: yaml

	parameters:
		applications:
			mapbender_mobile:
				[...]
				published: false

Nun sind die Anwendungen für Benutzer (außer dem root user) nicht sichtbar.

Weitere YAML basierende Anwendungen können einfach in dieses Verzeichnis abgelegt werden und werden automatisch von Mapbender erkannt.


Mapbender Demo Map
------------------

Dies ist die Demo-Anwendung, die für eine Desktop-Anwendung standardmäßig verwendet werden sollte.

Detaillierte Beschreibungen zu den enthaltenen Elementen finden Sie unter :ref:`elements_de`.


Mapbender Demo Map basic
------------------------

Die zweite Demoanwendung, welche folgende Unterschiede zur Hauptanwendung aufweist:

Werkzeugleiste
    Verwendet :ref:`coordinate_utility_de` anstelle von :ref:`POI_de`.

Seitenbereich
    Enthält keine im Voraus konfigurierten Elemente.

Kartenbereich
    Verwendet :ref:`coordinate_utility_de` anstelle von :ref:`scaledisplay_de` und :ref:`POI_de`.

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

Bitte gehen Sie zu :ref:`app_command_export_import_clone_de`, um entsprechende Konsolenbefehle einzusehen. Nachfolgend finden Sie einige einführende Worte darüber, was mit Anwendungen über die Konsole möglich ist.

**Export über die Konsole**

Anwendungen können als .json oder .yaml - Datei über die Konsole exportiert werden.
Jedoch kann eine YAML-Datei, die über die Konsole exportiert wurde, nicht unter application/config/application abgelegt und somit als Anwendung in Mapbender eingefügt werden.
Das YAML-Format einer Datei, die über die Konsole exportiert wurde, unterscheidet sich von dem YAML-Format der Dateien unter application/config/application.

**Import über die Konsole**

YAML-Dateien, die zuvor über die Benutzeroberfläche oder die Konsole exportiert wurden, können über die Konsole via bin/console importiert werden.


**Anwendung über die Konsole klonen**

Klont/Kopiert eine existierende Anwendung.

