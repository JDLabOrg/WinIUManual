Javascript for Widget
======================

Javascript Version >= 2.1

Initialize
----------------

Initialize all descendents of element as IU WIDGET.
.. code-block:: javascript

    IUDOMReady($element)

- Example
    .. code-block:: javascript

        IUDOMReady($('body'))

Multiple versions of jQuery
--------------------------------

If you imported another version of jQuery, you should use `IUEditor.$` instead of `$` in order to use iueditor.js API

Widgets
----------------

.. toctree::
    transition
    carousel
    collapsible
    flip_switch
    google_map
    panel
    popup
    slider
    range_slider
    tabview
    switch
    webmovie
    movie
    others
