.. _systemrequirements_de:

Systemvoraussetzungen und Download
##################################

Systemvoraussetzungen
*********************

Mapbender benötigt die folgenden Komponenten:

* PHP 5.6 (neueste Bugfix-Version) oder neuer (php5) 
* PHP CLI Interpreter (php5-cli) 
* PHP SQLite Erweiterung (php5-sqlite) 
* PHP cURL Erweiterung (php5-curl) 
* PHP Internationalisierungserweiterung (php5-intl)
* PHP GD für den Druck (php5-gd)
* PHP Multibyte String (php5-mbstring)
* PHP FileInfo für den Druck zur Prüfung der Bilder
* APACHE mod_rewrite
* OpenSSL
* Für die Entwicklung, speziell durch das phantomjs Hilfspaket, wird außerdem die BZ2 Extension benötigt (php-bz2)

Für Suse SLES müssen Sie bei PHP 7 zusätzlich noch installieren (extra Pakete unter SLES):
* php7-zlib
* php7-fileinfo

Unterstützung PostgreSQL:
* PostgreSQL Version 10 wird noch nicht unterstützt (Doctrine/DBAL 2.7 enthält PostgreSQL 10 Unterstützung).


PHP 7
-----

Mapbender unterstützt auch PHP 7. Sie benötigen die oben beschriebenen PHP-Bibliotheken für PHP 7 und zusätzlich die folgenden:

* PHP Zip (php-zip)
* PHP BZ2 (php-bz2)
* PHP XML (php-xml)


Datenbanken
-----------

Um optional eine andere Datenbank als die vorkonfigurierte SQLite zu verwenden, wird eine PHP-Erweiterung benötigt, die von Doctrine unterstützt wird: `Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. Für PostgreSQL beispielsweise php5-pgsql.

Beachten Sie, dass die SQLite Erweiterung auf jeden Fall benötigt wird. Sie benötigen diese, um im Entwicklermodus zu arbeiten oder um Profiler-Daten zu erzeugen sowie um Fehler zu analysieren.


Systemvoraussetzungen Windows
******************************

Auch unter Windows benötigen Sie `PHP <http://www.php.net/>`_ und damit einen PHP-fähigen Webserver wie `Apache <http://httpd.apache.org/>`_.

Wir haben gute Erfahrungen mit den 64-bit Downloads von Apache und PHP gemacht.

* `Apache Download <http://www.apachelounge.com/download/>`_: Die Downloads der Apache Lounge sind für verschiedene Versionen von Windows angepasst. Für neuere Versionen wählen Sie die "VC11" oder "VC14" Variante (benötigt die Visual C++ Redistributable für Visual Studio 2012 bzw. 2015) und die Win64 Version (64-bit).

* `PHP Download <http://windows.php.net/download#php-5.6>`_: Wählen Sie die "Non Thread Safe" Variante des PHP Downloads. als x64 Paket (64-bit).


Anmerkungen zu Windows
----------------------

Die Apache Downloads unterscheiden sich nach der Version von Visual Studio, mit der sie kompiliert worden sind und damit nach der geeigneten Version der Microsoft Visual C++ Redistributable. Bei neueren Windows Versionen ist das in der Regel unproblematisch. Es gibt drei unterschiedliche Varianten:

* **VC 14**: Benötigt Visual C++ Redistributable for Visual Studio 2015.
* **VC 11**: Benötigt Visual C++ Redistributable for Visual Studio 2012. PHP baut i.d.R. noch auf dieser Version auf.
* **VC 10**: Benötigt Visual C++ Redistributable for Visual Studio 2008 SP1.

Zusätzlich gibt es 32- und 64-bit Versionen von Apache für Windows. 



Download von Mapbender
**********************

Installationspakete von Mapbender werden als komprimierte Pakete ausgegeben und sind auf der `Download-Seite <http://mapbender.org/download>`_ verfügbar.

Nach dem Herunterladen extrahieren Sie die komprimierten Pakete in ein Verzeichnis Ihrer Wahl. In dieser Installationsbeschreibung wird davon ausgegangen, dass die Dateien unter

* **/var/www** (für Linux) oder
* **C:/** (für Windows, nicht empfehlenswert, der Einfachheit halber) ausgepackt werden.

Benennen Sie für die weitere Installationsanleitung das entpackte Verzechnis (z.B.: "mapbender3-3.0.5.2") nach "mapbender" um.

Die weiteren Schritte der Installation finden Sie in den folgenden Kapiteln:

* `Installation für Ubuntu und Debian <installation_ubuntu.html>`_
* `Installation auf Windows <installation_windows.html>`_

Für den schnellen Test können Sie auch die `Installation im Symfony eigenen Webserver <installation_symfony.html>`_ durchführen. Die `Git-basierte Installation <installation_git.html>`_ benötigt diese Download Pakete nicht, sondern lädt sich Mapbender von den Git-Quellen. Dafür sind dort zusätzlich Schritte notwendig.


Verzeichnisstruktur
-------------------

Nach dem Entpacken des TAR.GZ- bzw des ZIP-Archivs finden Sie in dem Mapbender-Verzeichnis folgende Unterverzeichnisse:

.. code-block:: bash
                
                .
                ├── app
                ├── bin
                ├── fom
                ├── mapbender
                ├── owsproxy
                ├── src
                ├── vendor
                └── web
