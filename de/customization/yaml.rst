.. _yaml_de:

YAML Konfiguration (Konfigurations - und Anwendungsdateien)
###########################################################

YAML Konfigurationsdateien
==========================

Die folgenden Konfigurationsdateien sind zu finden unter application/app/config.

parameters.yml
--------------
Hier werden grundlegenede Parameter von Mapbender bestimmt, beispielsweise die Datenbank des MB-Repositories und Datenbanken, auf denen die einzelnen Elemente verweisen (z.B. für die Suche, die Digitalisierung, etc.). Hier wird die Standardsprache der Oberfläche festgelegt, sowie Cookie- und Proxy-Einstellungen definiert.

* **Datenbank**: Parameter, die mit database beginnen, definieren die Datenbankverbindung.
  Ihre Datenbankkonfiguration könnte in der parameters.yml könnte folgendermaßen aussehen, wenn Sie PostgreSQL verwenden:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:
    database_user:     postgres
    database_password: geheim

  Mehr Informationen dazu finden Sie im Kapitel :ref:`database_de`.

* **Proxy-Einstellungen**:
  Sofern Sie einen Proxy verwenden, müssen Sie diesen in der Datei parameters.yml im Bereich OWSProxy Configuration angeben.

  Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml
    
    # OWSProxy Configuration
        ows_proxy3_logging: false
        ows_proxy3_obfuscate_client_ip: true
        ows_proxy3_host: myproxy
        ows_proxy3_port: 8080
        ows_proxy3_connecttimeout: 60
        ows_proxy3_timeout: 90
        ows_proxy3_user: ~
        ows_proxy3_password: ~
        ows_proxy3_noproxy:
            - 192.168.1.123

* **Mailer**: Die Mailerangaben starten mit mailer. Nutzen Sie z.B. smtp oder sendmail.

* **Spracheinstellung**: Sie können eine Sprache (locale) für Ihre Anwendung angeben (Standardwert ist en). 
  Folgende Sprachcodes sind verfügbar:
    * en für Englisch (Standard),
    * de für Deutsch,
    * es für Spanisch,
    * it für Italienisch,
    * nl für Niederländisch,
    * pt für Portugiesisch,
    * ru für Russisch.
  Unter http://doc.mapbender.org/en/book/translation.html erfahren Sie mehr über die Anpassung von Übersetzungen und wie neue  Sprachen hinzugefügt werden können.

* **Mapbender Logo**:
  Das Logo (Standard ist das Mapbender Logo) kann in der Datei parameters.yml angepasst werden. Diese Änderung wirkt sich global   auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.logo:     neues_logo.jpg

Die Datei des neuen Logos muss unter application/web eingefügt werden.
  
* **Projektname**:
  Der Projektname (Standard ist das Mapbender) kann in der Datei parameters.yml angepasst werden. Diese Änderung wirkt sich global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.project_name:     Example    

**Wichtiger Hinweis:** Achten Sie darauf keine Tabulatoren für Einrückungen zu verwenden. Verwenden Sie stattdessen Leerzeichen.


config.yml
----------
Diese Datei enthält grundlegende Architektur-Vorgaben von MB. Gleichzeitig sind hier die Parameter für die parameters.yml als Platzhalter definiert. Wichtig: Jede Datenbank, die in der parameters.yml definiert wird, muss auch als Platzhalter in der config.yml stehen. Desweiteren legt die Datei fest, welche Konfigurationen für den produktiven Modus und den Entwicklermodus verwendet werden sollen.

* **fom_user.selfregistration**: Um die Selbstregistrierung zu de/aktivieren, passen Sie den fom_user.selfregistration Parameter an.   Sie müssen unter self_registration_groups eine/mehrere Gruppen angeeben, so dass selbstregistriere Anwender automatisch (bei der Registrierung) diesen Gruppen zugewiesen werden. Über die Gruppe bekommen Sie dann entsprechend Rechte zugewiesen.
* **fom_user.reset_password**: Über diesen Parameter kann die Möglichkeit de/aktiviert werden, das Passwort neu zu setzen.
* **framework.session.cookie_httponly**: Stellen Sie für HTTP-only session cookies sicher, dass der Parameter framework.session.cookie_httponly auf true steht.


YAML Anwendungsdateien
======================

Als YAML definierte Anwendungen können in dem Verzeichnis **app/config/applications** abgelegt werden. Die bekannten Beispielanwendungen “**Mapbender mobile**”, “**Mapbender Demo Map**” und “**Mapbender Demo Map basic**” liegen dort als einzelne YAML Dateien. 
Weitere YAML basierende Anwendungen können einfach in dieses Verzeichnis abgelegt werden und werden automatisch von Mapbender erkannt.


Export/Import von YAML Anwendungsdateien über die Benutzeroberfläche
--------------------------------------------------------------------

**Export**

Sie können eine Anwendung unter **Anwendungen --> Exportieren** als JSON oder YAML exportieren.

.. image:: ../../figures/export.png


**Import**

Unter **Anwendungen --> Importieren** kann die Exportdatei in eine Mapbender-Installation importiert werden.

.. image:: ../../figures/export.png



Export/Import von YAML Anwendungsdateien über die Konsole
---------------------------------------------------------

**Export über die Konsole**

Anwendungen können als json oder yml über die Konsole exportiert werden.
Jedoch kann die YAML-Datei die über die Konsole exportiert wurde nicht unter app/config/application abgelegt und somit als Anwendung in Mapbender eingefügt werden.
Das YAML Format einer Datei die über die Konsole exportiert wurde unterscheidet sich von dem YAML Format der Dateien unter app/config/application. Ersteres wurde von einer Maschine erzeugt, letzteres von einem Programmierer. 


**Import über die Konsole**

YAML-Dateien die zuvor über die Benutzeroberfläche exportiert wurden, können über die Konsole importiert werden.

.. code-block:: bash

    $ app/console mapbender:application:import ~/Downloads/export.json 

~/Downloads/export.json ist der Dateipfad.


**Hilfe zu den Befehlen**

.. code-block:: bash

    $ app/console mapbender:application:import --help
    
.. code-block:: bash

    $ app/console mapbender:application:export --help

