.. _migration:

Migration Guide
###############

.. hint::
    
    This page gives migration instructions on specific Mapbender versions. For general tips on updating, see the :ref:`installation_update` page instead.

.. note::
    
    For in-depth information from the Mapbender development team, also see the `Upgrading Guide on GitHub <https://github.com/mapbender/mapbender/blob/master/UPGRADING.md>`_.
    

Migration to Mapbender 4
************************

* For Mapbender 4, all ``.yml`` file extensions were transformed into ``.yaml``. When migrating, the corresponding syntax must be adjusted accordingly.


Migration to Mapbender 3.3.4
****************************

* Please update the database schema. Run:

.. code-block:: bash

    bin/console doctrine:schema:update --force

* Next, you need to configure CSRF tokens to be used during login to the **csrf_token_generator** form_login section in ``security.yaml`` as follows:

.. code-block:: yaml

    form_login:
        check_path: /user/login/check
        login_path: /user/login
        csrf_token_generator: security.csrf.token_manager

* For productive environments, it is important to install an SSL certificate. After that, set the ``parameters.cookie_secure`` variable in your ``parameters.yaml`` to ``true``. This ensures that the Login cookie is only transmitted over secure connections.

Migration to Mapbender 3.3
**************************

* Make sure you have PHP >= 7.4 or PHP 8.x
* Provide a backup of your database. 
* Update your database schema to 3.3 with bin/console doctrine:schema:update --force
* doctrine.yaml: Please note that in the doctrine connection configuration variables must be set with quotes, for example '%database_driver%'
* CAUTION: Please note that the eye at application is used from (3.2.x) onwards to make the application available for the anonymous user (public access). Before 3.2.x, the eye/checkbox at security was used to publish an application.  

To update from 3.2.x to 3.3.x should be quite easy.

.. note:: 
    
    If you update from a version < 3.2, you have to follow the steps described at the `Migration to Mapbender 3.2 <#Migration to Mapbender 3.2>`_ section below.


















Migration to Mapbender 3.2
**************************

You can migrate older Mapbender installations to Mapbender 3.2.

Check the :ref:`installation_update` Guide.

* Make sure you have PHP >= 7.1.0 and PHP < 8 
* Provide a backup of your database. 
* Update your database schema to 3.2 with bin/console doctrine:schema:update --force
* CAUTION: Please note that the eye at application is from (3.2.x) used to make the application available for the anonymous user (public access). Before the eye /checkbox at security was used to publish an application.  

Some elements may not work after the update and may need a closer look.


Update map_engine_code
======================

If it makes sense, update all applications to map_engine_code current.

    Update mb_core_application set map_engine_code = 'current';


SearchRouter
============

In the Workshop bundle, you can find a `Demo <https://github.com/mapbender/mapbender-workshop/blob/master/app/config/applications/mapbender_demo_nrw.yml>`_.

1. deprecated empty: use placeholder instead

2. For text and choice you have to define the full class-path.

You also find information at `Best Practices Page <https://github.com/mapbender/mapbender/wiki/Best-practices:-form-types#inversion-of-choices>`_.

You can update the configuration with the following SQL.

.. code-block:: sql

    Update mb_core_element set configuration =
    replace(configuration,'s:6:"choice"','s:53:"Symfony\Component\Form\Extension\Core\Type\ChoiceType"')
        where class = 'Mapbender\CoreBundle\Element\SearchRouter';

    Update mb_core_element set configuration =
    replace(configuration,'s:4:"text"','s:51:"Symfony\Component\Form\Extension\Core\Type\TextType"')
    where class = 'Mapbender\CoreBundle\Element\SearchRouter';

    Select configuration from mb_core_element where class = 'Mapbender\CoreBundle\Element\SearchRouter';


3. For choice: Please note that key or value are passed flipped that means value and the key- see also `Best Practices Page <https://github.com/mapbender/mapbender/wiki/Best-practices:-form-types#inversion-of-choices>`_

.. code-block:: sql
    
    choices:
        Bonn - this is the value not the key: Bonn
        Cologne - this is the value not the key: Cologne
        Siegburg - this is the value not the key: Siegburg


Migrating SimpleSearch
======================

SimpleSearch element was improved. You can now define the projection of the result that comes from the Solr Service. Mapbender will then transform the result to the projection of the map.

SimpleSearch Supports Nominatim, Photon from version 3.2.5 - see workshop demo applications


1. Define sourceSrs in your SimpleSearch definition. If not defined, the default ('EPSG:4326') should be chosen. You can find an example at `this Configuration file <https://github.com/mapbender/mapbender-workshop/blob/release/3.2/application/config/applications/mapbender_demo_nrw.yaml>`_

                     sourceSrs: 'EPSG:25832'

2. query_ws_replace: From version 3.2.8 on, set query_ws_replace or modify the code as described in `this issue comment <https://github.com/mapbender/mapbender/issues/1391#issuecomment-968645508>`_	     

                     query_ws_replace: +


Migrating BaseSourceSwitcher
============================

Please note that on start of an application, all WMS are activated where the root layer is activated.

Before 3.2, it was possible to activate all BaseSources, where only the first WMS was visible on start.


Template / CSS
==============

CSS change. Plus, there will be a big redesign in backend and frontend in the upcoming versions.

* Check the workshop Bundle for the changes
* Define your template as desktop-template


Migrating Digitizer
===================

Digitizer is available for Mapbender >= 3.2.2. The new Digitizer Version is 1.4. Some functionality is not updated to 1.4 already (e.g. cluster).

* See `list of deprecated features <https://github.com/mapbender/mapbender-digitizer/releases/tag/1.4>`_
* See also `digitizer php file <https://github.com/mapbender/mapbender-digitizer/blob/1.4/Element/Digitizer.php>`_
* You can find a demo in the `Workshop bundle <https://github.com/mapbender/mapbender-workshop/blob/release/3.2/application/config/applications/mapbender_digitize_demo.yaml>`_
* maxResults - is supported again to limit the number of features that are loaded to the application (if not defined all features will be used) (digitizer >=1.4.9)
* For font definitions, see `issue 1308 <https://github.com/mapbender/mapbender/issues/1308>`_
    * fontSize: 38 definition without px 
    * labelxOffset: 18 (not supported in 3.2.3)
    * labelYOffset: 18 (not supported in 3.2.3)
* Types that are not supported in 3.2.4
    * upload
    * select with multiselect
    * coordinates
* Clustering not implemented in 3.2.x
* Style definition is limited not all OL2 styles can be defined
* Support styling features with icons (interpret externalGraphic, graphicWidth, graphicHeight properties) (Mapbender >=3.2.7)
* Support data placeholder syntax in externalGraphic (e.g. "/bundles/projectbundle/images/${type}.png") (Mapbender >=3.2.7)
* Save NULL for empty fields, works for int/float/decimal columns but not for double precision (Mapbender >= 3.2.6, see `issue 1355 <https://github.com/mapbender/mapbender/issues/1355>`_)
* Save NULL for empty fields for text fields does not work. Mapbender saves '' instead (see `issue 1385 <https://github.com/mapbender/mapbender/issues/1385>`_)
* supports printable: true


There is a new style called unsaved.

.. code-block:: yaml

    unsaved:
        strokeWidth: 3
        strokeColor: "#f0f0f0"
        fillColor:   "#ffff"
        fillOpacity: 0.5
        pointRadius: 6
        label: 'Neu - bitte speichern'
        fontColor: red
        fontFamily: 'Arial, Courier New, monospace'
        fontColor: red
        fontSize: 38
        fontWeight: bold


WMS Layer visibility
====================

Make sure that your WMS provides a proper extent for all supported EPSG-codes (this is used and saved in table mb_wms_wmslayersource Spalten latlonbounds und boundingboxes). 
Else it can happen that a layer is not requested for the given extent of your map.


Notice on the Sketch element
============================

Redlining was renamed to Sketch (>= 3.2.3).

.. code-block:: bash

	Update  public.mb_core_element set class = 'Mapbender\CoreBundle\Element\Sketch',
	title = 'mb.core.sketch.class.title'
		where class = 'Mapbender\CoreBundle\Element\Redlining';
		
		
FeatureInfo
===========

* showOriginal deprecated - parameter not available anymore (from 3.2.3).
* highlighting: true - new >= 3.2.3 highlights the geometry if you have WKT integrated in the featureinfo result - see `issue 1287 <https://github.com/mapbender/mapbender/issues/1287>`_ and also this `FeatureInfo blog post <https://wheregroup.com/blog/details/mapbender-featureinfo-mit-highlighting-der-treffer-geometrie/>`_


Print - Print queue
===================

* Mapbender supports print queue
* see `Queue blog post <https://wheregroup.com/blog/details/mapbender-druckauftraege-verwalten-und-wiederverwenden-einrichtung-der-warteschleife/>`_

