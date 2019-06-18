Project Setting
===================================================
project setting is a function that allows you to change settings for information about the project, media query, code, and so on.

.. Check thumbnail option here : https://pythonhosted.org/sphinxcontrib-images/

Site Information
------------------
.. thumbnail:: /_static/setting/setting_01.png
    :width: 100%
    :group: setting
    :title: Site Information

Site Information is the menu to set project file name, favicon, and other items (meta tags).

- If you choose a project, meta tags are applied to all the pages in the project.
- If you choose a single page, meta tags are applied to the selected page.

Media Query
--------------
.. thumbnail:: /_static/setting/setting_02.png
    :width: 100%
    :group: setting
    :title: Media Query

Media Query is a menu that sets options related to the size of the project or the event.

- Add new size

    .. image:: /_static/setting/add_size.png

    You can add a size. If you can check duplicated from, all css values are copied from the selected size.

Build
--------------
.. thumbnail:: /_static/setting/setting_03.png
    :width: 100%
    :group: setting
    :title: Build

Build is a menu for setting options such as path, resource path, port, etc. to build the project.

- Build path - The directory of your project output : html files
- Resource path - The directory of your project output and resources : css, js and all resource files (image, video and etc.)
- Resource prefix - Prefix is inserted to all resource's link : `src="/prefix/original/path/image.png"`
- Link prefix - Prefix is inserted to the href of page link (relative link) : `href="/prefix/original/pages/index.html"`

- Environment Variables in the *build path* and *resource path*
    - **$CurrentFolder** : The parent directory of a project directory that contains the current project file(.webproj).
    - **$AppName** : The project name.
    - **$HomeFolder** : User home directory.

CSS/JS
--------------
.. thumbnail:: /_static/setting/setting_04.png
    :width: 100%
    :group: setting
    :title: CSS / Javascript

CSS/JS is a menu where you can add the css or javascript file you want to use in your project.

- If you choose a project, the css and javascript files are added to all the pages in the project.
- If you choose a single page, the css and javascript files are added to the selected page.


External API
--------------
.. thumbnail:: /_static/setting/setting_05.png
    :width: 100%
    :group: setting
    :title: External API

External API is a menu for configuring the external APIs used in the project.
