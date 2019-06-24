Detail
=============================
Detail property provides functionality for fine-tuning widgets.

.. thumbnail:: /_static/panels/detail/detail.png
  :width: 40%
  :group: panels
  :title: Detail

The circular UI in front is a UI that tells the property to apply the media query.
On the first column, if the circle is orange, the value is in the current media query.
Otherwise, the value is from other media queries or default value (cascading value).
You can clear current value by clicking the circle.

----

.. _section_detail:

Section
-------------
.. image:: /_static/panels/detail/prop/022_section.png

- Set section full-height : Section height is same as the height of web browser (js).

.. _text_detail:

Text
------
.. image:: /_static/panels/detail/prop/002_text_ellipsis.png

- Type : You can change a text tag in *<p>, <h1>* and *<h2>*
- Ellipsis : You can add ellipsis to a selected line.

See :ref:`basic<text_basic>`.

.. _static_image_detail:

Static image
-----------------------
.. image:: /_static/panels/detail/prop/003_static_alt.png

- Alternative text : *alt* attribute in *<img>*

See :ref:`basic<staticImg_basic>`.

.. _icon_button_detail:

Image and text
-----------------------
.. image:: /_static/panels/detail/prop/004_imgt_margin.png

- Image
    - Top margin
    - Bottom margin

See :ref:`basic<iconButton_basic>`.

.. _google_map_detail:

Google map
-----------------------
.. image:: /_static/panels/detail/prop/005_google.png

- Map
    - Google map API key : You can get from google map. It should be set in project setting.
    - Longitude : The longitude of your location
    - Latitude : The latitude of your location
- Control
    - Zoom level : 1~18
    - Zoom control : Show a zoom control or not
    - Street Control : Show a street control or not
- Marker
    - Use : Show a marker or not
    - Image : You can change a marker image.
    - Title : The popup message when clicking a marker
- Map style
    - Color theme

See :ref:`complex<googleMap_complex>`.

.. _tweet_detail:

Tweet
-----------------------
.. image:: /_static/panels/detail/prop/006_twt.png

- Tweet message : The text message
- URL to tweet
- Button size : Medium or Large

See :ref:`complex<tweet_complex>`.

.. _facebook_detail:

Facebook like
-----------------------
.. image:: /_static/panels/detail/prop/007_fb.png

- Like URL
- Color scheme : Light and Dark
- Show friend's face

See :ref:`complex<fb_complex>`.

.. _table_detail:

Table
-----------------------
.. image:: /_static/panels/detail/prop/008_table.png

Table Row
``````````````

.. image:: /_static/panels/detail/prop/008_table_row.png

- As a header : Use *<th>* tag instead of *<tr>*
- Row span
- Column span

See :ref:`complex<table_complex>`.

.. _carousel_detail:

Carousel
-----------------------
.. image:: /_static/panels/detail/prop/009_car_position.png

- Arrow
    - X position : X position from side
    - Y position : Y position from top

See :ref:`complex<carousel_complex>`.

.. _video_detail:

Video
-----------------------
.. image:: /_static/panels/detail/prop/010_video_attrib.png

- Video
    - Alternative text
- Attribute
    - Loop
    - Muted
    - Autoplay : Autoplay is only work when muted.

See :ref:`complex<clip_complex>`.

.. _webmovie_detail:

Vimeo or Youtube
-----------------------
.. image:: /_static/panels/detail/prop/011_vimeo_auto.png

- Autoplay
- Loop

See :ref:`complex<webMovie_complex>`.

.. _slider_detail:

Slider / Range Slider
-----------------------
Slider Inner Bar
````````````````````````

.. image:: /_static/panels/detail/prop/012_slider_bar.png

- Inner bar image : You can put an image instead of color.

Slider Text
````````````````

.. image:: /_static/panels/detail/prop/012_slider_text_new.png

- Type : Same as :ref:`Text<text_detail>`
- Text name

See :ref:`slider programming<slider_program>` characteristics.

Range slider Text
````````````````````

.. image:: /_static/panels/detail/prop/012_range_text_2.png

- Type : Same as :ref:`Text<text_detail>`
- Start text name
- End text name

See :ref:`range slider programming<rangeSlider_program>` characteristics.

.. _switch_detail:

Switch
-----------
.. image:: /_static/panels/detail/prop/013_switch_2.png

- Checked : Status after build
- Name

See :ref:`programming<switch_program>`.

.. _flip_switch_detail:

Flip switch
-------------
.. image:: /_static/panels/detail/prop/013_switch_2.png

- Checked : Status after build
- Name

See :ref:`programming<flip_program>`.

.. _label_detail:

Label
-------------
.. image:: /_static/panels/detail/prop/001_label_for.png

- For : Html id of a connected widget
- Text

See :ref:`programming<label_program>`.

.. _button_detail:

Button
-------------
.. image:: /_static/panels/detail/prop/015_btn_type.png

- Type : default, reset and submit

See :ref:`programming<button_program>`.

.. _input_text_detail:

Input text
-------------
.. image:: /_static/panels/detail/prop/016_input_txt_2.png

- Max : Maximum of type
- Min : Minimum of type
- Max length

See :ref:`programming<inputText_program>`.

.. _input_paragraph_detail:

Input paragraph
--------------------------
.. image:: /_static/panels/detail/prop/017_input_p_2.png

- Max length

See :ref:`programming<inputParagraph_program>`.

.. _checkbox_detail:

Checkbox
-------------
.. image:: /_static/panels/detail/prop/018_checkbox_2.png

- Checked : Status after build
- Name

See :ref:`programming<checkbox_program>`.

.. _radio_button_detail:

Radio button
-------------
.. image:: /_static/panels/detail/prop/019_radio_btn_2.png

- Checked : Status after build
- Group : Group name of a radio button
- Name

See :ref:`programming<radioButton_program>`.

.. _form_detail:

Form
-------------
.. image:: /_static/panels/detail/prop/020_form_2.png

- Action
- Method
- Input hiddens
- Name

See :ref:`programming<form_program>`.

.. _collection_detail:

Collection
-------------
.. image:: /_static/panels/detail/prop/021_collection.png

- Item count
- Composition

See :ref:`programming<collection_program>`.

File upload
-------------
.. image:: /_static/panels/detail/prop/023_file_upload.png

- Name

See :ref:`programming<fileUpload_program>`.

Select
-------------
.. image:: /_static/panels/detail/prop/024_select.png

- Option
- Name

See :ref:`programming<select_program>`.

Header/Footer
-------------
.. image:: /_static/panels/detail/prop/025_header.png

- Composition

See :doc:`characteristics</navigation/structure>`.
