# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import requests

# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# Readthe docs Environment variables
IS_ENABLED_NAMO = os.environ.get('PROJECT') == 'NAMO'

if IS_ENABLED_NAMO:
    project = 'Windows Namo WebEditor ONE'
    copyright = '2019, NamoEditor'
    author = 'NamoEditor'
    project_name = 'Namo WebEditor ONE'
else:
    project = 'Windows IUEditor'
    copyright = '2019, JDLab'
    author = 'JDLab'
    project_name = 'IUEditor'

build_context = {
    'project_name': project_name
}
# rst_epilog = '.. |program_name| replace:: {0}'.format(program_name)

# -- General configuration ---------------------------------------------------
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinxcontrib.images',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# image options
# ref : https://pythonhosted.org/sphinxcontrib-images/
images_config = {

}


from jinja2 import Template


# Custom render
# https://www.ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
def rst_jinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    src = source[0]
    template = Template(src)
    source[0] = template.render(app.config.build_context)


def setup(app):
    app.add_config_value('build_context', build_context, True)
    app.connect("source-read", rst_jinja)
    app.add_stylesheet('css/custom.css')


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

