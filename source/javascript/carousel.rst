Carousel
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.carousel()

#. jQuery data key

    **IU_WIDGET.CAROUSEL**

    * Example

    .. code-block:: javascript

        var Carousel = $('#id').data(IU_WIDGET.CAROUSEL)

#. Option

    .. list-table::
        :widths: 100 400
        :header-rows: 1

        * - Member
          - description
        * - :code:`.callbackMove`
          - Callback function when the animation has finished

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - description
        * - :code:`.reload()`
          - Reload carousel
        * - :code:`.destroy()`
          - Destroy carousel
        * - :code:`.pause()`
          - Pause carousel if carousel is set autoplay
        * - :code:`.start()`
          - Start carousel if carousel is set autoplay
        * - :code:`.moveNext()`
          - Go to next item
        * - :code:`.movePrev()`
          - Go to prev item
        * - :code:`.moveCurrent()`
          - Reset to current item
        * - :code:`.move(index, translateX)`
          - Go to (index) item with translateX value

#. Method Detail

    .. list-table::
        :header-rows: 1
        :stub-columns: 1

        * - Method
          - Param
          - Type
          - Description
        * - :code:`.move(index, translateX)`
          - toIndex
          - number
          - index of carousel item
        * -
          - translateX
          - number
          - css : translateX