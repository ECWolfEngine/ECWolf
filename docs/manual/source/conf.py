# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

sys.path.append(os.path.abspath('_exts'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ECWolf'
copyright = '2026, ECWolf Team. Content is available under GNU Free Documentation License 1.3+ unless otherwise noted.'
author = 'ECWolf Team'
release = '1.5pre'

rst_prolog = f"""
.. |project| replace:: {project}
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['markup', 'sphinx.ext.extlinks', 'zdirective', 'zpygments']

exclude_patterns = ['_templates']

primary_domain = 'decorate'

extlinks = {
	'zd': ('https://zdoom.org/wiki/%s', '%s')
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_css_files = ['scriptref.css']
