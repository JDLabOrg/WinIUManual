Collapsible
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.collapsible()

#. jQuery data key

    **IU_WIDGET.COLLAPSIBLE**

    * Example

    .. code-block:: javascript

        var Collapsible = $('#id').data(IU_WIDGET.COLLAPSIBLE)

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
        * - :code:`.toggle(state)`
          - Change content's show/hide state

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
          - Show if state is true, hide otherwise