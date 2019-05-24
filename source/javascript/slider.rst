Slider
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.slide()

#. jQuery data key

    **IU_WIDGET.SLIDER**

    * Example

    .. code-block:: javascript

        var Slider = $('#id').data(IU_WIDGET.SLIDER)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.setValue(value)`
          - Set slider value
        * - :code:`.render()`
          - Render a point and textfield with current value
        * - :code:`.renderPoint()`
          - Render a point
        * - :code:`.renderTextField()`
          - Render a textfield

#. Method Detail

    .. list-table::
        :header-rows: 1

        * - Method
          - Param
          - Type
          - Description
          - Default
        * - :code:`.setValue(value)`
          - value
          - number
          - slider value between min and max
          - attribute **data-iu-slide-default-value**

#. Example

    .. code-block:: javascript

        //get slider object
        var Slider = $('#id').data(IU_WIDGET.POPUP);

        //change value to 80, range in (0, 100)
        Slider.setValue(80);

        //redraw slider
        Slider.render();
