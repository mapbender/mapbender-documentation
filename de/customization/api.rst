.. _api_de:

API
***

Mapbender bietet eine API, über die Clients verschiedene Befehle ausführen können.

Mit der API kann Mapbender verwaltet werden, ohne die Webadministrationsschnittstelle verwenden zu müssen. Die REST-API bietet Befehle, um beispielsweise Informationen über Dienste zu erhalten, und sie bietet auch Befehle, um Dienste zu veröffentlichen oder zu aktualisieren.

.. image:: ../../figures/customization/api.png
     :width: 100%


Dokumentation
-------------

Die API-Dokumentation ist in jede Mapbender-Installation integriert und über http://localhost/mapbender/api/doc/ öffentlich zugänglich.

In der Dokumentation finden Sie Beispiele für jeden Endpunkt. Bitte beachten Sie, dass Sie sich anmelden und autorisieren müssen, um die Beispiele auszuführen zu können. Außerdem benötigen Sie das Recht „API“ (siehe ACL).

Sie können die Dokumentation in der Mapbender-Demo erreichen unter: 

https://demo.mapbender.org/api/doc/

Weitere Informationen zur Developer Dokumentation finden Sie hier:

https://github.com/mapbender/mapbender/blob/develop/docs/api/setup.md


Apache Autorisierung
--------------------

Apache leitet per default den Authorization Header aus Sicherheitsgründen nicht an den Client weiter. Dies ist für die Nutzung der API aber notwendig. Es muss daher folgendes im VirtualHost oder der Konfiguration gesetzt werden:

.. code-block:: apacheconf
     
   SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1 


Upload Directory ändern
-----------------------

Um das Upload Directory zu ändern, können Sie den "api_upload_dir" Parameter in der paramter.yaml Datei anpassen


API-Seite für den öffentlichen Zugriff sperren
----------------------------------------------

Um den öffentlichen Zugriff der API-Seite zu sperren, können Sie in der security.yaml Datei folgende Paramter anpassen. Ändern Sie hierbei 

.. code-block:: yaml

   { path: ^/api/doc, roles: PUBLIC_ACCESS }

in

.. code-block:: yaml

   { path: ^/api/doc, roles: ROLE_ADMIN }

um.