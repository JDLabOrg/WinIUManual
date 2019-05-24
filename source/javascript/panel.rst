Panel
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.panel()

#. jQuery data key

    **IU_WIDGET.PANEL**

    * Example

    .. code-block:: javascript

        var Panel = $('#id').data(IU_WIDGET.PANEL)

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
        * -  :code:`.show()`
          - Show panel
        * - :code:`.close()`
          - Close panel
        * - :code:`.toggle()`
          - Change show/hide state