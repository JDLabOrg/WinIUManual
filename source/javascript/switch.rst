Switch
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.pgswitch()

#. jQuery data key

    **IU_WIDGET.SWITCH**

    * Example

    .. code-block:: javascript

        var Switch = $('#id').data(IU_WIDGET.SWITCH)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.toggle(state)`
          - Change 1st item to 2nd item

#. Method Detail

    .. list-table::
        :header-rows: 1

        * - Method
          - Param
          - Type
          - Description
        * - :code:`.toggle(state)`
          - state
          - bool
          - Show 2nd item if state is true, hide 2nd item otherwise