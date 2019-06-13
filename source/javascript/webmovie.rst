Webmovie
------------------

#. jQuery Plugin

    .. code-block:: javascript

        $.fn.webmovie()

#. jQuery data key

    **IU_WIDGET.WEBMOVIE**

    * Example

    .. code-block:: javascript

        var Webmovie = $('#id').data(IU_WIDGET.WEBMOVIE)

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


3. WebMovie(Vimeo & Youtube) lazy initialization

    .. code-block:: javascript
        :emphasize-lines: 1,2

        window.IUEditor.initVimeoInElement(element)
        window.IUEditor.initYoutubeInElement(element)

        // lazy initialization example

        // 1. init Vimeo in myDiv element
        var $myDiv = $('#myDiv');
        window.IUEditor.initVimeoInElement($myDiv);
        // or
        window.IUEditor.initVimeoInElement($myDiv[0]);

        // 2. init Youtube in myDiv element
        var $myDiv = $('#myDiv');
        window.IUEditor.initYoutubeInElement($myDiv);
        // or
        window.IUEditor.initYoutubeInElement($myDiv[0]);
