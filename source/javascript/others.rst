Widgets without further methods
---------------------------------------

* File : iu.widget.js

File Upload
````````````````````

#. Description
    * **File Upload Widget**
    * When clicking event, connect *Upload Button* with *File Name*

#. jQuery Plugin
    .. code-block:: javascript
        :emphasize-lines: 1

        $.fn.activateFileUpload

        // Example
        $('#file-upload-id').activateFileUpload()

Enable Hover Effect
``````````````````````````
#. Description
    * Widget has mouse-over styles
    * Mimic **:hover** selector
    * When occuring mouse over event, activate *iux-hover* class

#. jQuery Plugin
    .. code-block:: javascript
        :emphasize-lines: 1

        $.fn.activateHover

        // Example
        $('#widget-has-mouse-over-id').activateHover()

Enable Link to Scroll Effect
``````````````````````````````````````

#. Description
    * Widget has id link (page#id)
    * When clicking event on link, smooth scroll to position at link's element

#. jQuery Plugin
    .. code-block:: javascript
        :emphasize-lines: 1

        $.fn.activateScrollLink

        // Example
		$('#widget-has-element-link').activateScrollLink()

Full Section
````````````````````````

#. Description
    * Section has enable full size
    * When resizing window, section's height will be equal to window's height

#. jQuery Plugin
    .. code-block:: javascript
        :emphasize-lines: 1

        $.fn.iufullsection

    	// Example
		$('#section-is-enabled-fullsize').iufullsection()





