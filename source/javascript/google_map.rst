Google Map
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.googlemap()

#. jQuery data key

    **IU_WIDGET.GOOGLEMAP**

    * Example

    .. code-block:: javascript

        var Map = $('#id').data(IU_WIDGET.GOOGLEMAP)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.resize()`
          - Move map position to center

#. Google map lazy initialization

    .. code-block:: javascript
        :emphasize-lines: 1

        window.IUEditor.initGoogleMapInElement(element)

        // lazy initialization example
        // init google-map in myDiv element
        var $myDiv = $('#myDiv');
        window.IUEditor.initGoogleMapInElement($myDiv);
        // or
        // window.IUEditor.initGoogleMapInElement($myDiv[0]);