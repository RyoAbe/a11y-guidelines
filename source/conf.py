# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import datetime

# -- Project information -----------------------------------------------------

project = 'freeeアクセシビリティー・ガイドライン'
copyright = '2020-2021, freee株式会社'
author = 'freee株式会社'
version = 'Ver. 202110.2'
release = version
publishedDate = u'2021年10月18日'

if 'internal' in tags:
  publishedDate = datetime.datetime.now().strftime("%Y-%m-%d")
  release = u"INTERNAL {ver} ({date})".format(
    ver = version,
    date = publishedDate
  )

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinxcontrib.trimblank',
        'sphinx.ext.todo',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
  "inc/*",
  "checks/inc/*",
  "info/inc/*",
  "intro/ChangeLog/*"
]

# substitution definitions:
rst_prolog = u"""
.. |published_date| replace:: {pubdate}

.. include:: /WCAG21-SC-defs.txt
.. include:: /misc-defs.txt
""".format(
  pubdate = publishedDate
)


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
   "collapse_navigation": "false",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False
html_show_sphinx = False
html_permalinks = False

linkcheck_ignore = [r'http://localhost:\d+/']

def setup(app):
  app.add_css_file('a11y-gl.css')

[extensions]

if 'internal' in tags:
  todo_include_todos = True
  todo_link_only = True
