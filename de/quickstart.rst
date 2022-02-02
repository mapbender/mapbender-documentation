.. _quickstart_de:

:Author: OSGeo-Live
:Author: Astrid Emde
:Version: osgeo-live8.5
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)
:Thanks: mapbender-user list
:Date: |date|

  .. |mapbender-button-show| image:: ../figures/mapbender_button_show.png

  .. |mapbender-button-copy| image:: ../figures/mapbender_button_copy.png

  .. |mapbender-button-publish| image:: ../figures/mapbender_button_publish.png

  .. |mapbender-button-edit| image:: ../figures/mapbender_button_edit.png

  .. |mapbender-button-delete| image:: ../figures/mapbender_button_delete.png

  .. |mapbender-button-add| image:: ../figures/mapbender_button_add.png

  .. |mapbender-button-key| image:: ../figures/mapbender_button_key.png


.. image:: ../_static/mapbender_logo.png
  :scale: 100 %
  :alt: project logo
  :align: right


##################################################
Mapbender Quickstart: Erste Schritte mit Mapbender
##################################################

Mapbender ist ein web-basiertes Geoportal Framework zum Veröffentlichen, Registrieren, Anzeigen, Navigieren und Überwachen von Diensten, mit der Möglichkeit Dienste gesichert anzubieten.

Administrationsoberflächen ermöglichen es Administratoren, Karten- und Datendienste zu verwalten und zu kategorisieren. Über die Administration können einzelnen Benutzern und Gruppen Zugriffe gewährt werden.

Mapbender wurde unter Verwendung moderner Webtechnologien komplett neu geschrieben. Die Grundlage bildet das Symfony Framework. Auf der Clientseite finden Sie OpenLayers.

Mit dieser neuen Code-Grundlage wird die Mapbender Idee eines Geoportal Frameworks fortgesetzt.

  * Anwendungen können direkt im Browser erstellt, konfiguriert und gestylt werden.
  * Dienste wie WMS können in einem Service Repository verwaltet und mit Anwendungen verbunden werden.
  * Das Rechtemanagement ist sowohl für einzelne Benutzer als auch Gruppen einfach zu verwalten, egal ob sie in einer Datenbank oder über LDAP gespeichert werden.
  * Der Administrator braucht keine Zeile Code zu schreiben, da die Konfiguration über die webbasierte Administrationsoberfläche erfolgt.
  * Suchen (SQL oder Solr) können konfiguriert werden.
  * Anwendungen zur Digitalisierung können aufgebaut werden.
  * Ein Mobiles Template kann für das Erstellen von Anwendungen für Smartphones und Tablets verwendet werden.

Sie brauchen nichts weiter als einen Standard Webbrowser für diesen Schnellstart (Quickstart).

Dieser Quickstart beschreibt, wie Sie:

  * Mapbender starten
  * eine Anwendung erstellen
  * einen Web Map Service (OGC WMS) laden
  * WMS konfigurieren
  * eine individuelle Anwendung erstellen
  * Benutzer und Gruppen anlegen und Anwendungen zuweisen

Eine Mapbender Anwendung kann wie folgt aussehen:

  .. image:: ../figures/mapbender3_basic_application.png


Installation
===============

Hinweise zur Installation von Mapbender finden Sie unter `Installation <installation.html>`_.


Starten Sie Mapbender
================================================================================

#. Wählen Sie ``Mapbender`` aus dem Startmenü (sofern vorher eine solche Verknüpfung erstellt wurde) oder besuchen Sie http://localhost/mapbender/app.php (Adresse kann etwas abweichen, je nachdem wie der Apache Alias in der Datei /etc/apache2/sites-available/mapbender.conf erstellt wurde, nähere Informationen dazu unter `Installation <installation.html>`_)


#. Die Anwendung braucht eine kurze Zeit, um zu starten.

Falls Sie Schwierigkeiten haben, Mapbender zu starten, überprüfen Sie, ob der Apache Web Server und die PostgreSQL Datenbank laufen.



Starten Sie Mapbender im Entwicklungsmodus über app_dev.php
==============================================================
Symfony bietet einen Entwicklungsmodus mit einer Reihe von Informationen über die Anwendung an (Logging, Fehlermeldungen, Datenbankabfragen, Speicherverbrauch, Zeit und mehr). Dieser Modus ist nur über localhost verfügbar.

  .. image:: ../figures/mapbender_app_dev.png

#. Start des Entwicklungsmodus: http://localhost/mapbender/app_dev.php

#. Schauen Sie sich an, welche Information im Entwicklungsmodus angezeigt werden.



Die Willkommensseite
================================================================================

#. Die Willkommensseite listet die öffentlichen Anwendungen auf, die von allen Benutzern aufgerufen werden können. Die Anwendungen werden mit Vorschaubild, Titel und Beschreibung aufgelistet.

#. Sie können die Anwendung per Klick auf den Titel, das Vorschaubild oder den Startbutton aufrufen.

#. Bevor Sie Mapbender administrieren können, müssen Sie sich anmelden.

#. Klicken Sie auf den Link **Anmelden** oben rechts, um die Loginseite aufzurufen.

#. Sie können sich mit dem Benutzer anmelden, der während der Installation erzeugt wurde. Er kann ``root`` heißen mit dem Kennwort ``root`` (Dies ist der Standardbenutzer/Kennwort nach der Installation von Mapbender auf der OSGeo-Live. Bitte ändern Sie das Kennwort, wenn Sie eine Produktivumgebung betreiben. Löschen Sie den Benutzer ``root`` nicht.).


Nach erfolgreicher Anmeldung werden Sie zur ``Mapbender Administration`` weiter geleitet.


Anwendungsübersicht
================================================================================
Nach der Anmeldung werden Sie zur Anwendungsübersicht (``Anwendungen/ Applications``) mit einer Liste der für Sie freigegebenen Anwendungen weiter geleitet.

Die Anwendungsübersicht bietet folgende Funktionen:

 * Titel und Beschreibung
 * Vorschaubild zur Anwendung (sofern bereitgestellt)
 * |mapbender-button-show| Link zur Anwendung
 * |mapbender-button-copy| Button, um die Anwendung zu kopieren
 * |mapbender-button-edit| Button, um die Anwendung zu bearbeiten
 * |mapbender-button-publish| Button zum Veröffentlichen der Anwendung
 * |mapbender-button-delete| Button, um die Anwendung zu löschen
 * mit dem Filtertextfeld kann nach Anwendungen gesucht werden


  .. image:: ../figures/mapbender3_application_overview.png


Erstellen Sie eine eigene Anwendung
================================================================================

Erstellen Sie eine neue Anwendung, indem Sie einen Titel, eine Beschreibung sowie einen URL-Titel eingeben. Anschließend können Sie die Anwendung bearbeiten und Elemente, Themen, Stil (CSS-Editor) und Sicherheitseinstellungen zu verwalten.

#. Wählen Sie ``Anwendungen --> Neue Anwendung (Applications --> New Application)``

#. Geben Sie einen Titel und eine Beschreibung der Anwendung ein

#. Geben Sie einen URL-Titel an, der in der URL benutzt wird, um die Anwendung zu starten. Er kann identisch zum Titel sein und sollte keine Leer- und Sonderzeichen enthalten.

#. Laden Sie eine Bilddatei und definieren so ein Vorschaubild für die Anwendungsübersicht.

#. Wählen Sie eine Layoutvorlage für die Anwendung. Die Vorlage bestimmt den Aufbau der Anwendung. Mapbender stellt Ihnen einige Vorlagen (Templates) zur Verfügung (Fullscreen, Classic,...). Sie können aber auch eigene Vorlagen anlegen.

#. Betätigen Sie die Schaltfläche **Speichern (Create)**, um die Anwendung zu erzeugen.

#. Über den ``Bearbeiten-Button`` |mapbender-button-edit| neben der Anwendung können Sie nun weitere Bearbeitungen durchführen.


Ihre Anwendung wurde erstellt. Jetzt brauchen Sie Elemente (z.B. Kartenelement, Navigation, Legende) und Kartendienste, um die Anwendung mit Leben zu füllen.


  .. image:: ../figures/mapbender_create_application.png


.. tip:: Beachten Sie, dass derzeit die Layout-, Icon- und Farbanpassungen online über den CSS_Editor oder in css- und twig-Dateien erfolgen. Lesen Sie dazu die Dokumentation unter `Wie werden eigene Vorlagen (templates) erzeugt? <customization/templates.html>`_.


Kopieren und Umbenennen einer Anwendung
================================================================================
Sie können eine neue Anwendung auch durch Kopieren einer vorhandenen erzeugen. Jede Anwendung, auf die Sie schreibend zugreifen können, verfügt über den Button Anwendung duplizieren |mapbender-button-copy|. Beim Kopieren wird die Anwendung mitsamt der Dienste kopiert. Die kopierte Anwendung erhält einen abgeleiteten Namen, den Sie im nächsten Schritt anpassen können.



Löschen einer Anwendung
================================================================================
Sie können eine Anwendung aus der Liste ``Anwendungen`` über den |mapbender-button-delete|-Button löschen. Es wird lediglich die Anwendung gelöscht. Die Dienste sind weiterhin im Dienste-Repository vorhanden.



Exportieren und Importieren von Anwendungen und Daten
================================================================================

Weitere Informationen im Kapitel :ref:`yaml_de`.


Verwaltung von Datenquellen
=================================
Mapbender soll verschiedene Dienste wie OGC WMS, OGC WMTS oder OGC WFS verwalten. Jeder Service muss dabei anders verwaltet werden. In der Administration ist dabei für jede Quelle eine eigene Administrationsmöglichkeit (im Moment lediglich WMS) vorgesehen.


Service Repository (Datenquellen)
====================================

#. Gehen Sie auf ``Datenquelle (Services)`` und schauen sich die Dienstquellen an.

#. Sie bekommen einen Überblick über die Dienste, die bereits in Mapbender geladen wurden.

#. Typ (z.B. WMS), Titel und Beschreibung bieten eine erste Information über den Dienst.

#. Per Klick auf den |mapbender-button-show| ``Anzeigen-Button`` bekommen Sie weitere Informationen über die Quelle.

#. Über den ``Button`` |mapbender-button-delete| können Sie die Datenquelle aus Ihrem Repository löschen.


Laden von Web Map Services
================================================================================
Sie können OGC Web Map Services (WMS) in Ihre Anwendung laden. Mapbender unterstützt dabei die Versionen 1.1.1 und 1.3.0.

Ein WMS liefert ein XML, wenn das getCapabilities-Dokument angefordert wird. Diese Information wird von Mapbender ausgelesen. Der Client erhält alle notwendigen Informationen über den Dienst aus diesem XML.

.. tip:: Sie sollten das Capabilities-Dokument zuerst in Ihrem Browser überprüfen, bevor Sie versuchen, den Dienst in Mapbender zu laden.

#. Wählen Sie ``Datenquelle --> Neue Datenquelle (Sources --> Add Source)`` oder nutzen sie den |mapbender-button-add| ``Button`` um eine neue Datenquelle hinzuzufügen. Geben Sie den Link zur WMS getCapabilities URL in das Textfeld ``Dienste-URL`` (``Service URL``) ein.

#. Geben Sie Benutzername und Kennwort ein, sofern der Dienst eine Authentifizierung benötigt.

#. Über die Auswahl ``nur valid (only valid)`` können Sie Dienste laden, die dem WMS Schema folgen. Dienste, die diesem Schema nicht folgen, könnten vielleicht Probleme in der Anzeige hervorrufen.

#. Klicken Sie **Laden (Load)**, um den Dienst in das Repository zu laden.

#. Nach erfolgreicher Registrierung des Dienstes zeigt Mapbender eine Übersicht der Informationen an, die der Dienst geliefert hat.

  .. image:: ../figures/mapbender_wms_load.png


Hier sind einige Beispiel WMS:

Germany demo

http://wms.wheregroup.com/cgi-bin/germany_workshop.xml?VERSION=1.1.1&REQUEST=GetCapabilities&SERVICE=WMS

WhereGroup OSM WMS

http://osm-demo.wheregroup.com/service

Omniscale OSM WMS (siehe auch http://osm.omniscale.de/)
http://osm.omniscale.net/proxy/service?


.. NOCH NICHT IMPLEMENTIERT
  .. tip:: Erzeugen Sie eine Containeranwendung und laden Sie jeden WMS nur einmal hier hinein. Sie können die WMS aus diesem Container in andere Anwendungen übernehmen. Wenn Sie diesen WMS aktualisieren werden mögliche Änderungen in allen Anwendungen übernommen, die diesen WMS beinhalten. Sie können einen WMS einfach von einer Anwendung zu einer anderen über den Menüeintrag *Link WMS to application* kopieren.


Fügen Sie Dienste zur Anwendung hinzu
===========================================
Nach dem erfolgreichen Hochladen eines WMS möchten Sie diesen zu einer Anwendung hinzufügen.

#. Wählen Sie  ``Anwendungen -->`` |mapbender-button-edit| ``Editier-Button --> Layerset``.

#. Wählen Sie den ``Button`` |mapbender-button-add|, um ein Layerset hinzuzufügen. Ein Layerset präsentiert mehrere Layer (mögliche Namen können "main" für die Hauptkarte und "overview" für die Übersichtskarte sein)

#. Jetzt können Sie Dienste zum Layerset hinzufügen.

#. Wählen Sie den ``Button`` |mapbender-button-add|, um dem neuen Layerset Dienste hinzuzufügen.

#. Sie können die Reihenfolge der Dienste und der Ebenen über drag & drop ändern.


  .. image:: ../figures/mapbender_add_source_to_application.png

Konfiguration von Diensten
================================================================================
Sie können Dienste für Ihre Anwendung konfigurieren. Vielleicht möchten Sie nicht alle Ebenen anzeigen oder Sie möchten die Reihenfolge oder den Titel der Ebenen ändern, die Info-Abfrage für einzelne Ebenen verhindern oder den Minimal-/Maximalmaßstab ändern.

#. Wählen Sie  ``Anwendung -->`` |mapbender-button-edit| ``Editier-Button --> Layerset --> Editier-Button``, um eine Instanz zu konfigurieren.

#. Sie sehen eine Tabelle mit den Layern des Dienstes.

#. Sie können die Reihenfolge der Layer über drag & drop ändern.


.. image:: ../figures/mapbender_wms_application_settings.png


**Dienstekonfiguration:**

* Titel: Name der bei der Anwendung angezeigt wird
* Opacity: wählen Sie die Opazität (Deckkraft) in Prozent
* Format: wählen Sie das Format für den getMap-Requests
* Infoformat: wählen Sie das Format für getFeatureInfo-Requests (text/html für die Ausgabe als HTML wird empfohlen)
* Exceptionformat: wählen Sie das Format für Fehlermeldungen
* Kachel-Puffer (Tile buffer): Dieser Parameter gilt für Dienste, die gekachelt angefordert werden und gibt an, ob weitere umgebende Kacheln abgerufen werden sollen. Damit sind diese bei einer Pan-Bewegung schon heruntergeladen und sichtbar. Je höher der Wert, desto mehr umgebende Kacheln werden abgerufen. Default: 0.
* BBOX-Faktor: Dieser Parameter gilt für Dienste, die nicht-gekachelt angefordert werden. Hier kann man angeben, wie groß das zurückgegebene Bild sein soll. Ein Wert größer 1 wird ein größeres Kartenbild anfordern. Default: 1.25 und kann auf 1 gesetzt werden.
* BaseSource: soll der Dienst als BaseSource behandelt werden (BaseSources können beim Ebenenbaum ein-/ausgeblendet werden)
* Proxy: bei Aktivierung wird der Dienst über Mapbender als Proxy angefordert
* Transparenz: Standard ist aktiviert, deaktiviert wird der Dienst ohne transparenten Hintergrund angefordert (getMap-Request mit TRANSPARENT=FALSE)
* Gekachelt (Tiled): Dienst wird in Kacheln angefordert, Standard ist nicht gekachelt (kann bei großer Karte sehr hilfreich sein, wenn der Dienst die Kartengröße nicht unterstützt)


**Vendor Specific Parameter:**

In einer Layerset Instanz können Vendor Specific Parameter angegeben werden,
die an den WMS Request angefügt werden. Die Umsetzung folgt den Angaben der
multi-dimensionalen Daten in der WMS Spezifikation.

In Mapbender können die Vendor Specific Parameter genutzt werden, z.B. um
Benutzer und Gruppeninformation des angemeldeten Benutzers an die WMS Anfrage zu
hängen. Es können auch feste Werte übermittelt werden.

Das folgende Beispiel zeigt die Definition eines Parameters „group“, der als
Inhalt die Gruppe des gerade in Mapbender angemeldeten Nutzers weitergibt.

.. image:: ../figures/mapbender_vendor_specific_parameter.png

* Vstype: Mapbender spezifische Variablen: Gruppe (groups), User (users), Simple.
* Name: Parameter Name im WMS Request.
* Default: Standardwert.
* Hidden: Wenn der Wert gesetzt ist, werden die Anfragen serverseitig versendet, so dass die Parameter nicht direkt sichtbar sind.

Momentan eignet sich das Element, um Benutzer und Gruppeninformationen
weiterzugeben, z.B. für Benutzer die $id$ und für Gruppen den Parameter
$groups$.


**Layerkonfiguration:**

* Titel - Layertitel der Service Information (der Titel ist anpassbar)
* Aktiv an/aus (active on/off) - aktiviert/ deaktiviert ein Thema in dieser Anwendung
* Auswählen erlauben (select allow) - Layer wird angezeigt und ist auswählbar im Ebenenbaum
* Auswählen an (select on) - Layer ist bei Anwendungsstart aktiv
* Info erlauben (info allow) - Infoabfrage wird für diesen Layer zugelassen
* Info an (info on) - Layer Infoabfrage wird beim Start aktiviert
* Minimaler/ Maximaler Maßstab (minsc / maxsc) - Maßstabsbereich, in dem der Layer angezeigt wird.
* Aufklappen (toggle) - aufklappen beim Start der Anwendung
* Sortieren (reorder) - Ebenen können über drag&drop in der Anwendung verschoben werden
* ... -> öffnet einen Dialog mit weiteren Informationen
* name - Layername der Service Information (wird beim getMap-Request verwendet und ist nicht veränderbar)
* Style - wenn ein WMS mehr als einen Stil anbietet, können Sie einen anderen Stil als den standard (default) Stil wählen.



Fügen Sie Elemente zu Ihrer Anwendung hinzu
=================================================
Mapbender bietet eine Reihe von Elementen (Modulen) an, aus denen Sie Ihre Anwendung aufbauen können. Ihre Anwendung verfügt wiederum über verschiedene Bereiche (Toolbar, Sidepane, Content, Footer), die Sie mit Elementen bestücken können.

  .. image:: ../figures/mapbender_application_add_element.png

#. Wählen Sie ``Anwendungen -->`` |mapbender-button-edit| ``Editier-Button --> Layouts --> Button`` |mapbender-button-add|, um eine Übersicht über die Mapbender-Elemente zu erhalten.

#. Wählen Sie ein Element aus der Liste aus.

#. Beachten Sie die verschiedenen Bereiche Ihrer Anwendung. Stellen Sie sicher, dass Sie das Element zum richtigen Bereich hinzufügen.

#. Konfigurieren Sie das Element. Hinweis: Wenn Sie ein Element z.B. **Karte (map)** auswählen, sehen Sie lediglich die Optionen für dieses Element und können es entsprechend konfigurieren.

#. Sie können die Position der Elemente über drag & drop ändern.

#. Schauen Sie sich Ihre Anwendung an. Öffnen Sie Ihre Anwendung über den Button |mapbender-button-show|.

Jetzt sollten sie eine Idee davon haben, wie einfach es ist, eine Mapbender-Anwendung ohne Codes zu verändern.


  .. image:: ../figures/mapbender_application_elements.png

Beispiele für Elemente, die Mapbender anbietet:

* Über Mapbender-Dialog (About Dialog)- zeigt Informationen über Mapbender an
* Aktivitätsanzeige (Activity Indicator) - zeigt HTTP-Aktivität an
* Hintergrund wechseln (BaseSourceSwitcher) - Hintergründe können definiert und gewechselt werden
* Button
* Koordinatenanzeige (Coordinates Display) - zeigt Mausposition in den Kartenkoordinaten an
* Copyright- zeigt Nutzungsbedingungen an
* Feature Info - Informationsausgabe (getFeatureInfo)
* GPS-Position - Button zur Anzeige der GPS-Position
* HTML - Element zur freien Definition von HTML zur Einbindung von Bilder, Texten, Links
* Bildexport (Image Export) - Bild kann als png oder jpg exportiert werden
* Legende - Anzeige der Legende der Dienste und Themen
* Layertree - Ebenenbaum
* Karte (Map)
* Meetingpoint (POI) - Treffpunkt wird mit Hinweistexten generiert und über eine URL verschickt
* Übersicht (Overview) - zeigt eine kleine Übersichtskarte
* Druck (PrintClient) - Druckdialog
* Linien- und Flächenmessung (Ruler Line/Area) - Linien- und Flächenzeichnung, Dialog der Messung
* Maßstabsauswahl (Scale Selector) - Auswahl des Maßstabs über eine Auswahlbox
* Maßstabsleiste (ScaleBar) - Anzeige des aktuellen Maßstabs
* Einfache Suche (SimpleSearch) - Einfache Suche über SOLR
* Suche (Search Router) - konfigurierbare Suche über SQL
* SRS Auswahl (Spatial Reference System Selector) - Auswahl der Projektion (SRS) über eine Auswahlbox
* Navigation Toolbar (Zoombar)
* WMS Loader - Laden von OGC WMS Diensten über ein Textfeld (getCapabilities-URL)
* WMC Editor - Speichern von Themenplänen
* WMC Loader - Laden von Themenplänen
* WMC List - Laden von Themenplänen über eine Auswahlbox

Sie finden detaillierte Informationen zu jedem Element in der `Mapbender Dokumentation <index.html>`_.


Versuchen Sie es selber
================================================================================

* Fügen Sie ein Kartenelement (Map-Element) zum content-Bereich Ihrer Anwendung hinzu.
* Fügen Sie ein Ebenenbaum (Layertree) zum content-Bereich Ihrer Anwendung hinzu.
* Fügen Sie einen Button in die Toolbar, der den Layertree öffnet.
* Fügen Sie das Navigationswerkzeug (Navigation Toolbar) in den content-Bereich hinzu
* Fügen Sie ein Copyright-Element hinzu und ändern Sie den Copyright-Text.
* Fügen Sie eine SRS Auswahl (SRS Selector) in den Footer-Bereich ein.



Benutzer- und Gruppenverwaltung
=================================
Der Zugriff auf eine Mapbender Anwendung benötigt Authentifizierung. Nur öffentliche Anwendungen können von allen Anwendern genutzt werden.

Ein Benutzer kann die Berechtigungen bekommen, um auf eine oder mehrere Anwendungen und Dienste zuzugreifen.

.. NOCH NICHT IMPLEMENTIERT
  Es gibt keinen vorgegebenen Unterschied zwischen Rollen wie ``guest``, ``operator`` oder ``administrator``. Die ``role`` eines Benutzers beruht auf den Funktionen und des Diensten, aud die der Benutzer durch diese Anwendung Zugriff hat.


Benutzer anlegen
================================================================================

#. Um einen Benutzer anzulegen, gehen Sie zu ``Benutzerverwaltung --> Benutzer --> Neuer Benutzer (User control --> User --> New User)`` oder wählen Sie den ``Button`` |mapbender-button-add|.

#. Wählen Sie einen Namen und ein Kennwort für Ihren Benutzer.

#. Geben Sie eine E-Mail-Adresse für den Benutzer an.

#. Speichern Sie Ihren neuen Benutzer.

#. Weitere Angaben zum Benutzer können im Reiter ``Profil`` erfolgen.


  .. image:: ../figures/mapbender_create_user.png



Gruppen anlegen
================================================================================
#. Erzeugen Sie eine Gruppe über  ``Gruppen --> Neue Gruppen (Group --> New Group)``.

#. Wählen Sie einen Namen und eine Beschreibung für Ihre Gruppe.

#. Speichern Sie Ihre neue Gruppe.


Benutzer einer Gruppe zuweisen
================================================================================

#. Weisen Sie einen Benutzer einer Gruppe über `` Benutzer --> Gruppen (Users --> Groups)`` zu.

#. Wählen Sie einen oder mehrere Benutzer über ``Benutzer (Users)`` aus, die Sie der Gruppe zuweisen wollen.

#. Weisen Sie einen Benutzer über ``Benutzer -->`` |mapbender-button-edit| ``Editier-Button--> Gruppen`` einer Gruppe zu.


  .. image:: ../figures/mapbender_assign_user_to_group.png


Rechte
========
Mapbender bietet verschiedene Rechte an, die Sie vergeben können. Diese beruhen auf dem Symfony ACL System http://symfony.com/doc/2.1/cookbook/security/acl_advanced.html#built-in-permission-map

* view - anzeigen
* edit - editieren
* delete - löschen
* operator - kann anzeigen, editieren und löschen
* master - kann anzeigen, editieren und löschen und diese Rechte außerdem weitergeben
* owner - Besitzer, darf alles. Darf master und owner Recht vergeben.


Weisen Sie einem Benutzer über ``Benutzer --> Benutzer bearbeiten --> Sicherheit (Users --> Edit your User --> Security)`` Rechte zu.

  .. image:: ../figures/mapbender_roles.png


Zuweisen einer Anwendung zu einem Benutzer/einer Gruppe
============================================================
#. Bearbeiten Sie Ihre Anwendung über ``Anwendungen --> Editier-Button`` |mapbender-button-edit|

#. Wählen Sie ``Sicherheit (Security)``

#. Veröffentlichen Sie Ihre Anwendung über die Auswahl **aktiviert** unter ``Sicherheit`` oder den Button zur Veröffentlichung |mapbender-button-publish| bei der Anwendungsübersicht

#. Setzen Sie Berechtigungen wie view, edit, delete, operator, master, owner

#. Weisen Sie eine Anwendung einem Benutzern/einer Gruppe zu

#. Testen Sie die Konfiguration!

#. Melden Sie sich über ``Logout`` ab.

#. Melden Sie sich unter der neuen Benutzerbezeichnung an

  .. image:: ../figures/mapbender_security.png


Zuweisen einzelner Elemente zu Benutzern/Gruppen
============================================================
Standardmäßig stehen alle Elemente den Benutzern/Gruppen zur Verfügung, die Zugriff auf eine Anwendung haben. Der Zugriff kann darüberhinaus für einzelne Elemente noch genauer definiert werden, so dass diese nur bestimmten Benutzern/Gruppen zur Verfügung stehen.

#. Bearbeiten Sie Ihre Anwendung über ``Anwendungen -->`` |mapbender-button-edit| ``Editier-Button``

#. Wählen Sie ``Layouts``

#. Jedes Element verfügt über einen |mapbender-button-key| ``-Button``

#. Wählen Sie den |mapbender-button-key| ``-Button`` zu dem Element, das nur ausgewählten Benutzern/Gruppen zur Verfügung stehen soll

#. Setzen Sie Berechtigungen wie view, edit, delete, operator, master, owner

#. Weisen Sie das Element Benutzern/Gruppen zu

#. Testen Sie die Konfiguration!


Anwendung beim Start positionieren
============================================================
Sie können eine Anwendung beim Start positionieren. Dies kann über einen Punkt oder ein Rechteck erfolgen. Beim Start können dabei auch Texte zur Anzeige mitgegeben werden. Diese Funktionalität nutzt das Element Treffpunkt (Meetingpoint).

Sie können dabei einen oder mehrere Punkte (POIS) in der URL übergeben. Jeder Punkt verfügt dabei über die folgenden Parameter:

- Punkt (point): Koordinatenpaar, die Werte werden mit Komma getrennt (zwingend)
- Beschriftung (label): Beschriftung, die angezeigt werden soll (optional)
- Maßstab (scale): Maßstab, in dem der Punkt angezeigt werden soll (optional, Angabe ist nur bei der Anzeige eines Punktes sinnvoll)

Wenn Sie mehr als einen Punkt im Aufruf übergeben, zoomt die Karte auf 150% der POI-Boundingbox.

Format für die Übergabe eines einzelnen Punktes:

* ?poi[point]=363374,5621936&poi[label]=Hello World&poi[scale]=5000

* http://demo.mapbender.org/application/mapbender_user?poi[point]=363374,5621936&poi[label]=Hello World&poi[scale]=5000

  .. image:: ../figures/mapbender_position_poi_label.png


Für die Übergabe vieler Punkte wird das folgende Format verwendet:

* ?poi[0][point]=363374,5621936&poi[0][label]=Hello&poi[1][point]=366761,5623022&poi[1][label]=World



Weitere Aufgaben
================================================================================

Hier sind weitere Aufgaben, die Sie ausprobieren können:

#. Versuchen Sie, einige WMS in Ihre Anwendung zu laden. Versuchen Sie Ihre WMS zu konfigurieren.

#. Versuchen Sie eine eigene Anwendung zu erzeugen.


Was kommt als Nächstes?
================================================================================

Dies waren nur die ersten Schritte mit Mapbender. Es gibt viele weitere Funktionen, die Sie ausprobieren können.

Mapbender Webseite

  https://mapbender.org/

Sie finden Tutorials unter

  https://doc.mapbender.org

Beteiligen Sie sich

	https://mapbender.org/community/
