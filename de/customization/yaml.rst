.. _yaml_de:

YAML Konfiguration (Konfigurations - und Anwendungsdateien)
===========================================================

Die folgenden Konfigurationsdateien sind zu finden unter application/app/config.

parameters.yml
--------------

Hier werden grundlegende Parameter von Mapbender bestimmt:

* **Datenbank**: 
  Die Datenbankkonfiguration in der parameters.yml sieht folgendermaßen aus, wenn PostgreSQL verwendet wird:

.. code-block:: yaml

    database_driver:   pdo_pgsql
    database_host:     localhost
    database_port:     5432
    database_name:     mapbender
    database_path:
    database_user:     postgres
    database_password: geheim

 Weitere Informationen im Kapitel :ref:`database_de`.

* **Proxy-Einstellungen**:
  Wenn ein Proxy verwendet wird, muss dieser in der Datei parameters.yml im Bereich OWSProxy Configuration angegeben werden.

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

* **Mailer**: Die Mailerangaben starten mit mailer (z.B. smtp oder sendmail).

  Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml
   
        mailer_transport:  smtp
        mailer_host:       localhost
        mailer_user:       ~
        mailer_password:   ~
        
  Ein Mailer wird für die Funktionen 'Self-Registration' und 'Passwort zurücksetzen' benötigt.
  Weitere Informationen im Kapitel :ref:`users_de`.

* **Spracheinstellung**: Die Sprache (locale) der Mapbender Installation kann angepasst werden, jedoch nicht die einer  einzelnen Anwendung. 

  Folgende Sprachcodes sind verfügbar:
    * en für Englisch (Standard),
    * de für Deutsch,
    * es für Spanisch,
    * it für Italienisch,
    * nl für Niederländisch,
    * pt für Portugiesisch,
    * ru für Russisch.
    
  Eine Konfiguration könnte wie folgt aussehen:

.. code-block:: yaml
   
   # locale en, de, it, es, ru, nl, pt are available
    fallback_locale:   en
    locale:            en
    secret:            ThisTokenIsNotSoSecretChangeIt
    
  Weitere Informationen unter http://doc.mapbender.org/en/book/translation.html
  
* **Mapbender Logo**:
  Das Logo (Standard ist das Mapbender Logo) kann in der Datei parameters.yml angepasst werden. Diese Änderung wirkt sich  global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.logo:     neues_logo.jpg

  Die Datei des neuen Logos muss unter application/web eingefügt werden.
  
* **Projektname**:
  Der Projektname (Standard: Mapbender) kann in der Datei parameters.yml angepasst werden. Diese Änderung wirkt sich global auf die gesamte Mapbender Installation aus.

.. code-block:: yaml

    branding.project_name:     Example    


**Wichtiger Hinweis:** In der parameters.yml dürfen **keine Tabulatoren für Einrückungen** verwendet werden.


config.yml
----------

Diese Datei enthält grundlegende Architektur-Vorgaben von Mapbender. Gleichzeitig sind hier die Parameter für die parameters.yml als Platzhalter definiert. Wichtig: Jede Datenbank, die in der parameters.yml definiert wird, muss auch als Platzhalter in der config.yml stehen. Des Weiteren legt die Datei fest, welche Konfigurationen für den produktiven Modus und den Entwicklermodus verwendet werden sollen.

* **fom_user.selfregistration**: Um die Selbstregistrierung zu de/aktivieren, passen Sie den fom_user.selfregistration Parameter an.   Sie müssen unter self_registration_groups eine/mehrere Gruppen angeben, so dass selbstregistriere Anwender automatisch (bei der Registrierung) diesen Gruppen zugewiesen werden. Über die Gruppe bekommen Sie dann entsprechend Rechte zugewiesen.
* **fom_user.reset_password**: Über diesen Parameter kann die Möglichkeit de/aktiviert werden, das Passwort neu zu setzen.
* **framework.session.cookie_httponly**: Stellen Sie für HTTP-only session cookies sicher, dass der Parameter framework.session.cookie_httponly auf true steht.


YAML Anwendungsdateien
----------------------

Als YAML definierte Anwendungen können in dem Verzeichnis **app/config/applications** abgelegt werden. Die bekannten Beispielanwendungen “**Mapbender mobile**”, “**Mapbender Demo Map**” und “**Mapbender Demo Map basic**” liegen dort als einzelne YAML Dateien. 
Weitere YAML basierende Anwendungen können einfach in dieses Verzeichnis abgelegt werden und werden automatisch von Mapbender erkannt.


Mapbender Demo Map
------------------

Folgende Funktionen sind vorimplementiert:

Toolbar
    * Layer tree (Button)
    * Featureinfo (Button)
    * Print client (Button)
    * Image Export (Button)
    * Legend (Button)
    * WMS loader (Button)
    * GPS Position
    * measure (line und area) (Buttons)
    * about (About dialog)
    * POI (Button)

Sidepane
    * Layer tree
    * Redlining
    * Coordinates utility
    * About Mapbender (HTML)

Content
    * Map
    * Navigation toolbar
    * Legend
    * Featureinfo
    * WMS loader
    * Image export
    * Print client
    * line 
    * area
    * Scale bar
    * Layer tree
    * Overview
    * Scale display
    * POI

Footer
    * Activity Indicator
    * mb.core.coordinates.class.title
    * SRS selector
    * Scale selector
    * © OpenStreetMap contributors (Button)
    * HTML-powered by Mapbender (HTML)

Ausführliche Beschreibungen der einzelnen Funktionen unter https://doc.mapbender.org/de/functions.html



Mapbender Demo Map basic
------------------------

Unterschiede zu Mapbender Demo Map:

Toolbar  
    Die Toolbar unterscheidet sich kaum von der in der Mapbender Demo Map Anwendung. Statt 'POI' ist 'Coordinates utility'      eingebunden.

Sidepane  
    Hier sind keine Funktionen vorimplementiert.

Content  
    Statt der Funktionen 'Scale display' und 'POI' ist die Funktion 'Coordinates utility' eingebunden.

Ausführliche Beschreibungen der einzelnen Funktionen unter https://doc.mapbender.org/de/functions.html



Mapbender mobile 
----------------

Die Beispielanwendung kann als Mobile Template für die Erstellung von Anwendungen für Smatphones oder Tablets verwendet werden.

Folgende Funktionen sind vorimplementiert:

Footer
    * Themes (Button)
    * Base source switcher (Button)
    * GPS Position
    * Imprint (Button)
    * help (Button)
    * about (Button)

Content
    * Map
    * Navigation toolbar

Mobilepane
    * Themes (Layer tree)
    * Featureinfo
    * Imprint (HTML)
    * help (HTML)
    * Base source switcher
    * about (HTML)



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

Anwendungen können als datei.json oder datei.yml über die Konsole exportiert werden.
Jedoch kann eine YAML-Datei die über die Konsole exportiert wurde nicht unter app/config/application abgelegt und somit als Anwendung in Mapbender eingefügt werden.
Das YAML Format einer Datei, die über die Konsole exportiert wurde, unterscheidet sich von dem YAML Format der Dateien unter app/config/application. Ersteres wurde von einer Maschine erzeugt, letzteres von einem Programmierer. 


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

