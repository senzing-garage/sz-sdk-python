# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = "sz-sdk-python"
copyright = "2025, Senzing"
author = "senzing"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]


# -- Customization -----------------------------------------------------------

sys.path.insert(0, os.path.abspath("../../src"))


extensions = [
    "autodocsumm",  # to generate tables of functions, attributes, methods, etc.
    "sphinx_toolbox.collapse",  # support collapsable sections
    "sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",  # to read Google-style or Numpy-style docstrings
    "sphinxext.remoteliteralinclude",  # extends literalinclude to be able to pull files from URLs
    "sphinx.ext.viewcode",  # to allow viewing the source code in the web page
]

exclude_patterns = ["*.py"]

html_theme = "sphinx_rtd_theme"
# autodoc_inherit_docstrings = False  # don't include docstrings from the parent class
# autodoc_typehints = "description"   # Show types only in descriptions, not in signatures

# Methods that are not to be documented. Intended to be internal use or experimental
doc_excludes = ("find_interesting_entities_by_entity_id", "find_interesting_entities_by_record_id", "get_feature")


def autodoc_skip_member(app, what, name, obj, skip, options):
    return True if name in doc_excludes else None


def setup(app):
    app.connect("autodoc-skip-member", autodoc_skip_member)
