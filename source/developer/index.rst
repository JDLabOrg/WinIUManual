Developer View
================

Developer view is a panel where you can view and modify the code applied to the design or modify the code of the project.
You can open the developer mode panel via the view menu.

.. image:: /_static/developer/dev_screen.png

You can add code in the left panel and see the preview code in the right panel.

ID & Class
``````````````````````

.. thumbnail:: /_static/developer/dev_01.png
    :width: 100%
    :group: developer
    :title: ID & Class

You can change a Html ID and add classes.

.. code-block:: html
    :caption: Example

    <!-- Your Input  -->
    class1 class2 class3
    <!-- Result -->
    <div class="class1 class2 class3"></div>

Attribute
``````````````````

.. thumbnail:: /_static/developer/dev_02.png
    :width: 100%
    :group: developer
    :title: Attribute

.. code-block:: html
    :caption: Example

    <!-- Your Input  -->
    attr="value1" attr="value2" single_value
    <!-- Result -->
    <div attr="value1" attr="value2" single_value></div>


Inline style code
``````````````````````````

.. thumbnail:: /_static/developer/dev_03.png
    :width: 100%
    :group: developer
    :title: Inline style code

.. code-block:: css
    :caption: Example

    /* Your Input */
    color:blue; background-color:lightblue;

.. code-block:: html

    <!-- Result -->
    <div style="color:blue; background-color:lightblue;"></div>


Comment before element
```````````````````````````````

.. thumbnail:: /_static/developer/dev_04.png
    :width: 100%
    :group: developer
    :title: Comment before element

.. code-block:: html
    :caption: Example
    :emphasize-lines: 5-6

    <!-- Your input -->
    This element is blahblah

    <!-- Result -->
    <!-- This element is blahblah -->
    <div></div>


Comment after element
```````````````````````````````

.. thumbnail:: /_static/developer/dev_05.png
    :width: 100%
    :group: developer
    :title: Comment after element

.. code-block:: html
    :caption: Example
    :emphasize-lines: 5-6

    <!-- Your input -->
    The end of this element

    <!-- Result -->
    <div></div>
    <!-- The end of this element-->
