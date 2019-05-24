Movie
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.movie()

#. jQuery data key

    **IU_WIDGET.MOVIE**

    * Example

    .. code-block:: javascript

        var movie = $('#id').data(IU_WIDGET.MOVIE)

#. Method

    .. list-table::
        :header-rows: 1

        * - Method
          - Description
        * - :code:`.play()`
          - Play movie
        * - :code:`.pause()`
          - Pause movie
        * - :code:`.autoplay()`
          - Play movie if movie is visible in window frame, pause otherwise
