.. _basedata:

Base data
#########

Base data determines the fundamental information and settings of an application. They can be configured through a mask in the application settings in the :ref:`backend`. You can find more details on application creation under :ref:`Quickstart <quickstart>`.


Settings
--------

* **Title**: The application's name.

* **URL Title**: How the application is shown in the URL field. No special characters allowed.

* **Thumbnail**: Uploadable image file from the file directory that will be displayed in the application overview. Click on **Select File**.

* **Description**: Text input field that can store the application's description, if provided.

* **Persistent map state**: Stores the state of specific map parameters and settings across sessions. For more information, please see :ref:`Share Elements <persistent_map_view>`.

* **Show Splashscreen**: Shows a splashscreen on application startup to indicate the loading time.

  .. image:: /figures/mapbender_create_application.png
     :width: 80%


Configuring the Splashscreen
----------------------------

The splashscreen enhances your application's appearance by displaying an image logo alongside the application's title.
To configure the splashscreen image, follow the steps below:

1. Open the ``parameters.yaml`` file located in your Mapbender installation. For more on the file itself, see :ref:`yaml`.
2. Create or look for the key ``branding.splashscreen_image``.
3. Define the splashscreen image using one of the following methods:

   - **File Path**: Specify a single file path relative to the `application/public` directory in your Mapbender installation.

   .. code-block:: yaml

    parameters:
      branding.splashscreen_image: path/relative/to/public/myimage.png


   - **Array**: Utilize an array format where keys correspond to the application's slug. This allows you to customize the splashscreen image for each application. Use the key ``default`` to provide a fallback image for applications not explicitly defined.   

   .. code-block:: yaml

    parameters:
      branding.splashscreen_image:
        sample_application: path/relative/to/public/sample_application.png
        another_application: path/relative/to/public/another_application.png
        default: path/relative/to/public/myimage.png


If the splashscreen image is not configured, the logo (``branding.logo``) will be used for all applications.

Moreover, the appearance of the splashscreen is customizable via CSS variables. Please switch to :ref:`CSS` for an example.  