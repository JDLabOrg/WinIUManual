Transition
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.transition()

#. jQuery data key

    **IU_WIDGET.TRANSITION**

    * Example

    .. code-block:: javascript

        var Transition = $('#id').data(IU_WIDGET.TRANSITION)

#. Option

    .. list-table::
        :header-rows: 1

        * - Member
          - Description
        * - :code:`.callbackShow`
          - Callback function when the animation (show) has finished. The second item is shown.
        * - :code:`.callbackClose`
          - Callback function when the animation (close) has finished. The second item is closed.

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