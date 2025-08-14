# Configuration file for the Sphinx documentation builder.

import os
import sys

folder_paths = ['../../splice-api/app','../../splice-cli/src/splice_cli','../../splice-lib/src/splice_lib','../../splice-pipeline/src/splice_pipeline','../../splice-tests','../../splice-ui/src/splice_ui','../../splice-api','../../splice-lib/src','../../splice-cli/src','../../splice-pipeline/src','../../splice-ui/src']

for path in folder_paths:
    sys.path.insert(0, os.path.abspath(path))


# -- Project information

project = 'SPLICE test'
copyright = '2025, Me'
author = 'Me'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

autosummary_generate = True
