import django
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
# django.setup()


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Projet_JO_Doc_Tech'
copyright = '2023, Thomas Quezet'
author = 'Thomas Quezet'
release = 'V1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.doctest','sphinx.ext.autodoc','sphinxcontrib_django','sphinx.ext.todo','sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []

language = '[fr]'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

django_settings = 'shop.settings'
django_show_db_tables=True
