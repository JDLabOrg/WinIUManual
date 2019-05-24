Tab View
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.tabview()

#. jQuery data key

    **IU_WIDGET.TABVIEW**

    * Example

    .. code-block:: javascript

        var Tabview = $('#id').data(IU_WIDGET.TABVIEW)

#. Option

    .. list-table::
        :header-rows: 1

        * - Member
          - Description
        * - .callbackSelect
          - Callback function when the animation has finished

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.select(index)`
          - Select a index'th tab item

#. Method Detail

    .. list-table::
        :header-rows: 1

        * - Method
          - Param
          - Type
          - Description
        * - :code:`.select(index)`
          - index
          - number
          - tab index in range (0, tabcount-1)