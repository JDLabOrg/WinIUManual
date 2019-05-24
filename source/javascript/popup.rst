Popup
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.popup()

#. jQuery data key

    **IU_WIDGET.POPUP**

    * Example

    .. code-block:: javascript

        var Popup = $('#id').data(IU_WIDGET.POPUP)

#. Option

    .. list-table::
        :header-rows: 1

        * - Member
          - Description
        * - :code:`.callbackShow`
          - Callback function when the animation has finished
        * - :code:`.callbackClose`
          - Callback function when the animation has finished

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.show()`
          - Show panel
        * - :code:`.close()`
          - Close panel
        * - :code:`.toggle()`
          - Change show/hide state