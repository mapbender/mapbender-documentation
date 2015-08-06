.. _systemrequirements:

Systemvoraussetzungen und Download
##################################

Systemvoraussetzungen
***************

Mapbender3 benötigt die folgenden Komponenten:

* >= PHP 5.4 (php5) 
* PHP CLI Interpreter (php5-cli) 
* PHP SQLite Erweiterung (php5-sqlite) 
* PHP cURL Erweiterung (php5-curl) 
* PHP Alternative PHP Cache (php-apc)
* PHP Internationalisierungserweiterung (php5-intl)
* PHP GD für den Druck (php5-gd)
* PHP FileInfo für den Druck zur Prüfung der Bilder
* APACHE mod_rewrite
* OpenSSL

Um optional eine andere Datenbank als die vorkonfigurierte SQLite zu verwenden, wird eine PHP-Erweiterung benötigt, die von Doctrine unterstützt wird: `Doctrine <http://www.doctrine-project.org/projects/dbal.html>`_. Für PostgreSQL beispielsweise php5-pgsql.

Beachten Sie, dass die SQLite Erweiterung auf jeden Fall benötigt wird. Sie benötigen diese, um im Entwicklermodus zu arbeiten oder um Profiler-Daten zu erzeugen sowie um Fehler zu analysieren.


Systemvoraussetzungen Windows
******************************

Auch unter Windows benötigen Sie `PHP <http://www.php.net/>`_ und damit einen PHP-fähigen Webserver wie `Apache <http://httpd.apache.org/>`_.

Wir haben gute Erfahrungen mit den 64-bit Downloads von Apache und PHP gemacht.

* `Apache Download <http://www.apachelounge.com/download/>`_: Die Downloads der Apache Lounge sind für verschiedene Versionen von Windows angepasst. Für neuere Versionen wählen Sie die "VC14" Variante (benötigt die Visual C++ Redistributable für Visual Studio 2015) und die Win64 Version (64-bit).

  
* `PHP Download <http://windows.php.net/download#php-5.6>`_: Wählen Sie die "Thread Safe" Variante des PHP Downloads. als x64 Paket (64-bit).


Anmerkungen zu Windows
----------------------

Die Apache Downloads unterscheiden sich nach der Version von Visual Studio, mit der sie kompiliert worden sind und damit nach der geeigneten Version der Microsoft Visual C++ Redistributable. Bei neueren Windows Versionen ist das in der Regel unproblematisch. Es gibt drei unterschiedliche Varianten:

* **VC 14**: Benötigt Visual C++ Redistributable for Visual Studio 2015.
* **VC 11**: Benötigt Visual C++ Redistributable for Visual Studio 2012.
* **VC 10**: Benötigt Visual C++ Redistributable for Visual Studio 2008 SP1.

Zusätzlich gibt es 32- und 64-bit Versionen von Apache für Windows. 



Download von Mapbender3
********** 

Installationspakete von Mapbender3 werden als komprimierte Pakete ausgegeben und sind auf der Download-Seite verfügbar unter http://mapbender3.org/download.

Nach dem Herunterladen extrahieren Sie die komprimierten Pakete in ein Verzeichnis Ihrer Wahl. In dieser Installationsbeschreibung wird davon ausgegangen, dass die Dateien unter /var/www ausgepackt werden.
