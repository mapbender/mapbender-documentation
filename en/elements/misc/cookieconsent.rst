.. _cookieconsent:

Cookie Banner
=============

Applications support displaying a cookie banner which is customized via the Mapbender configuration file ``parameters.yaml``. We use the code from `Cookie Consent <https://cookieconsent.insites.com/>`_ without making an additional call to the internet.

The banner is displayed in any application on the first run.

.. image:: ../../../figures/cookiebanner.png
           :scale: 80

After this banner is dismissed it doesn't appear again until you have deleted the cookie in your web browser. Mapbender depends on cookies and stores its PHP-session there.


Configuration
-------------

Configuration takes place in the *parameters.yaml* file and accounts for the whole Mapbender instance. Please add the parameter ``mapbender.cookieconsent`` with the value ``true`` or ``false``. If the parameter is missing or the value is set to ``false``, the banner will not be displayed in your applications.

Example:

.. code-block:: yaml

    #Mapbender Cookie Consent Message
    mapbender.cookieconsent: true


.. tip:: After changing these parameters you have to clean the contents of the cache-directory (``var/cache/\*``).