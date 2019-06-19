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

.. _text_detail:

Text
------
.. image:: /_static/panels/detail/prop/002_text_ellipsis.png

- Type : You can change a text tag in *<p>, <h1>* and *<h2>*
- Ellipsis : You can add ellipsis to a selected line.

See :doc:`characteristics</widgets/basic/text>`.

.. _static_image_detail:

Static image
-----------------------
.. image:: /_static/panels/detail/prop/003_static_alt.png

- Alternative text : *alt* attribute in *<img>*

See :doc:`characteristics</widgets/basic/staticImage>`.

.. _icon_button_detail:

Image and text
-----------------------
.. image:: /_static/panels/detail/prop/004_imgt_margin.png

- Image
    - Top margin
    - Bottom margin

See :doc:`characteristics</widgets/basic/iconButton>`.

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

See :doc:`characteristics</widgets/complex/googleMap>`.

.. _tweet_detail:

Tweet
-----------------------
.. image:: /_static/panels/detail/prop/006_twt.png

- Tweet message : The text message
- URL to tweet
- Button size : Medium or Large

See :doc:`characteristics</widgets/complex/tweet>`.

.. _facebook_detail:

Facebook like
-----------------------
.. image:: /_static/panels/detail/prop/007_fb.png

- Like URL
- Color scheme : Light and Dark
- Show friend's face

See :doc:`characteristics</widgets/complex/facebook>`.

.. _table_detail:

Table
-----------------------
Table Row
``````````````

.. image:: /_static/panels/detail/prop/008_table_row.png

- As a header : Use *<th>* tag instead of *<tr>*
- Row span
- Column span

See :doc:`characteristics</widgets/complex/table>`.

.. _carousel_detail:

Carousel
-----------------------
.. image:: /_static/panels/detail/prop/009_car_position.png

- Arrow
    - X position : X position from side
    - Y position : Y position from top

See :doc:`characteristics</widgets/complex/carousel>`.

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

See :doc:`characteristics</widgets/complex/videoClip>`.

.. _webmovie_detail:

Vimeo or Youtube
-----------------------
.. image:: /_static/panels/detail/prop/011_vimeo_auto.png

- Autoplay
- Loop

See :doc:`characteristics</widgets/complex/webMovie>`.

.. _slide_detail:

Slide / Range Slide
-----------------------
Slider Inner Bar
````````````````````````

.. image:: /_static/panels/detail/prop/012_slider_bar.png

- Inner bar image : You can put an image instead of color.

Slider Text
````````````````

.. image:: /_static/panels/detail/prop/012_slider_text.png

- Type : Same as :ref:`Text<text_detail>`

See :doc:`slide</widgets/programming/slide>`, :doc:`range slide</widgets/programming/rangeslide>` characteristics.

.. _switch_detail:

Switch
-----------
.. image:: /_static/panels/detail/prop/013_switch.png

- Checked : Status after build

See :doc:`characteristics</widgets/programming/switch>`.

.. _flip_switch_detail:

Flip switch
-------------
.. image:: /_static/panels/detail/prop/014_flip.png

- Checked : Status after build

See :doc:`characteristics</widgets/programming/flipswitch>`.

.. _label_detail:

Label
-------------
.. image:: /_static/panels/detail/prop/001_label_for.png

- For : Html id of a connected widget

See :doc:`characteristics</widgets/programming/label>`.

.. _button_detail:

Button
-------------
.. image:: /_static/panels/detail/prop/015_btn_type.png

- Type : default, reset and submit

See :doc:`characteristics</widgets/programming/button>`.

.. _input_text_detail:

Input text
-------------
.. image:: /_static/panels/detail/prop/016_input_txt.png

- Max : Maximum of type
- Min : Minimum of type
- Max length

See :doc:`characteristics</widgets/programming/inputText>`.

.. _input_paragraph_detail:

Input paragraph
--------------------------
.. image:: /_static/panels/detail/prop/017_input_p.png

- Max length

See :doc:`characteristics</widgets/programming/inputParagraphText>`.

.. _checkbox_detail:

Checkbox
-------------
.. image:: /_static/panels/detail/prop/018_checkbox.png

- Checked : Status after build

See :doc:`characteristics</widgets/programming/checkbox>`.

.. _radio_button_detail:

Radio button
-------------
.. image:: /_static/panels/detail/prop/019_radio_btn.png

- Checked : Status after build
- Group : Group name of a radio button

See :doc:`characteristics</widgets/programming/radiobutton>`.

.. _form_detail:

Form
-------------
.. image:: /_static/panels/detail/prop/020_form.png

- Action
- Method
- Input hiddens

See :doc:`characteristics</widgets/programming/form>`.

.. _collection_detail:

Collection
-------------
.. image:: /_static/panels/detail/prop/021_collection.png

- Item count
- Composition

See :doc:`characteristics</widgets/programming/collection>`.
