Flip Switch
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.flipswitch()

#. jQuery data key

    **IU_WIDGET.FLIPSWITCH**

    * Example

    .. code-block:: javascript

        var Switch = $('#id').data(IU_WIDGET.FLIPSWITCH)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.toggle(state, duration)`
          - Change show/hide state

#. Method Detail

    .. list-table::
        :header-rows: 1
        :stub-columns: 1
        :widths: 1 1 1 5 1
        :class: prevent-responsive-table

        * - Method
          - Param
          - Type
          - Description
          - Default
        * - :code:`.toggle(state)`
          - state
          - bool
          - Show if state is true, hide otherwise
          -
        * -
          - duration
          - number
          - Duration with animation
          - 300ms
