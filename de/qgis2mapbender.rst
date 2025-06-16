.. _qgis2mapbender_de:

QGIS2Mapbender Plugin
*********************

Beschreibung
============

QGIS2Mapbender ist ein QGIS-Plugin, mit dem ein QGIS Server Projekt auf einen Server übertragen werden kann und anschließend der QGIS Server WMS in Mapbender veröffentlicht werden kann.

Sie finden den QGIS2Mapbender im QGIS Python Plugins Repository: https://plugins.qgis.org/plugins/QGIS2Mapbender

.. image:: ../../../figures/qgis2mapbender.png
     :scale: 70

Installation und Anforderungen
==============================

Bitte beachten Sie, dass QGIS2Mapbender Version >= 1.0.0 eine Mapbender Version >= 4.1.2 benötigt.

Installation des Plugins
------------------------

QGIS2Mapbender wird im QGIS Plugin Repository veröffentlicht. Die Installation ist direkt aus dem QGIS Plugin Repository über den QGIS Plugin Manager möglich. Klicken Sie dazu auf den Menüpunkt Plugins ► Verwalten und Installieren von Plugins. Alternativ kann eine Version auch hier heruntergeladen werden. Der gezippte Ordner kann manuell installiert werden. Klicken Sie auf den Menüpunkt Plugins ► Plugins verwalten und installieren. Wählen Sie im Dialog Plugin-Manager die Option Nicht installiert und laden Sie das Zip hoch.

Anforderungen an Ihr lokales System
-----------------------------------

* Das QGIS-Projekt muss im selben Ordner wie die Daten gespeichert sein. Bitte beachten Sie, dass zusammen mit dem QGIS-Projekt auch alle Dateien in dem Ordner, der das QGIS-Projekt enthält, auf den Server hochgeladen werden.

Anforderungen an Ihren Server
-----------------------------

* QGIS Server ist auf Ihrem Server installiert.
* Mapbender ist auf Ihrem Server installiert und konfiguriert.

Voraussetzungen für Ihre Mapbender-Installation
-----------------------------------------------

*Apache*

* Konfigurieren Sie die Apache-Autorisierung und das Mapbender-Upload-Verzeichnis api_upload_dir (siehe https://doc.mapbender.org/en/customization/api.html)

*PHP*

* Konfigurieren Sie die folgenden Parameter in der php.ini so, dass sie den Eigenschaften der Projekte entsprechen, die Sie auf den Server hochladen möchten. Denken Sie daran, dass der Ordner, der Ihr Projekt und Ihre Daten enthält, beim Hochladen auf den Server gezippt wird.
    
    * upload_max_filesize - die maximale Größe einer hochgeladenen Datei.
    * post_max_size - maximale Größe aller Daten, die über eine POST-Anfrage gesendet werden; der Wert sollte gleich oder größer als upload_max_filesize sein.
    * max_execution_tine - hier wird die maximale Zeit in Sekunden festgelegt, die ein Skript für die Analyse der Eingabedaten benötigt.


*Mapbender*

* Anwendung: Erstellen Sie mindestens eine Vorlageanwendung in Mapbender (die kopiert und zur Veröffentlichung eines neuen WMS verwendet werden kann) oder eine Anwendung, die direkt zur Veröffentlichung eines neuen WMS verwendet wird.

* Die Anwendungen sollten mindestens eine Instanz einer Karte und ein Layerset enthalten.

Hinweis: Das Feld „layerset“ in QGIS2Mapbender ist die ID oder der Name des zu verwendenden Layersets. Die Voreinstellung ist „main“ oder das erste Layerset in der Anwendung.

* Benutzer/Gruppen: Alle Mapbender-Benutzer, die berechtigt sein sollen, QGIS2Mapbender zu benutzen, benötigen spezielle Rechte. Es gibt nur eine Ausnahme und das ist der Mapbender-Superuser mit der ID 1, bei dem diese Berechtigung automatisch vergeben wird.

    * Der Benutzer/die Gruppe benötigt die globale Berechtigung access_api und upload_files, um alle Operationen auf der API durchführen und Dateien hochladen zu können.
    * Der Benutzer/die Gruppe benötigt die globale Berechtigung view_sources.
    * Der Benutzer/die Gruppe benötigt das globale Recht create_applications, um eine Anwendung zu kopieren.
    * Benutzer/Gruppe muss das Recht view_applications haben, um eine Anwendung zu kopieren.
    * Benutzer/Gruppe benötigt das globale Recht edit_applications, um eine Anwendung mit einer neuen Quelle zu aktualisieren.
    * Benutzer/Gruppe benötigt das globale Recht edit_soruces, um eine neue Quelle zu erstellen (veröffentlichen).
    * Der Benutzer/die Gruppe benötigt das globale Recht update_soruces, um eine Quelle neu zu laden.

Konfigurieren der Verbindung zum Server
---------------------------------------

Die folgende Abbildung zeigt eine typische Konfiguration der Verbindung zum Server.

.. image:: ../../../figures/qgis2mapbender_server_configuration.png
     :scale: 70

Einige Anmerkungen zur Standardkonfiguration:




Docker
------

* QGIS Server und Mapbender können als Docker Container betrieben werden. Bitte stellen Sie sicher, dass das Mapbender Upload-Verzeichnis api_upload_dir den gleichen Pfad wie das QGIS Server Projektverzeichnis hat, da es im QGIS Server Request als Pfad im MAP Parameter verwendet wird.
* Ein Standard QGIS Projekt (Umgebung: QGIS_PROJECT_FILE) sollte nicht angegeben werden.

Unterstützung
=============

info@wheregroup.com

Lizenz
======

Das Plugin ist unter der beigefügten GNU General Public License lizenziert: