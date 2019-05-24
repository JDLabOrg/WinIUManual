Range Slider
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.rangeslider()

#. jQuery data key

    **IU_WIDGET.RANGE_SLIDER**

    * Example

    .. code-block:: javascript

        var RangeSlider = $('#id').data(IU_WIDGET.RANGE_SLIDER)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.changeStartValue(value)`
          - Set start value
        * - :code:`.changeEndValue(value)`
          - Set end value
        * - :code:`.render()`
          - Render innerBar and textfields with current values
        * - :code:`.renderInnerBar(updateLeft)`
          - Render innberBar
        * - :code:`.renderStartTextField()`
          - Render a start textfield
        * - :code:`.renderEndTextField()`
          - Render a end textfield

#. Method Detail

    .. list-table::
        :header-rows: 1

        * - Method
          - Param
          - Type
          - Description
          - Default
        * - :code:`.changeStartValue(value)`
          - value
          - number
          - slider value between min and end
          - attribute **data-iu-range-slide-default-start-value**
        * - :code:`.changeEndValue(value)`
          - value
          - number
          - slider value between start and max
          - attribute **data-iu-range-slide-default-end-value**
        * - :code:`.renderInnerBar(updateLeft)`
          - updateLeft
          - bool
          - if updateLeft is true, update innerBar left
          - false

