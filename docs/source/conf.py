################################################
################ SECTION TO EDIT ###############
################################################

project = 'How to Document in RTD'
copyright = '2021, Emerging Technologies'
author = 'Bibhash Mitra, Prasang Gupta'
release = '0.0.1'




################################################
######## NO NEED TO EDIT AFTER THIS LINE #######
################################################

import os
import sys
sys.path.insert(0, os.path.abspath('./../../'))

extensions = [
    'sphinx.ext.autodoc',           # for generating documentation from docstrings
    'sphinx.ext.autosummary',       # generate summaries for autodoc
    'sphinx.ext.autosectionlabel',  # allow reference sections to use titles
    'sphinx.ext.intersphinx',       # link to other project documentations
    'sphinx.ext.viewcode',          # add links to python source code for documentation
    'sphinx_autodoc_typehints',     # automatically document param types
    'nbsphinx',                     # integrate with jupyter notebooks
    'sphinx.ext.napoleon',          # support for numpy and google docstrings
    'sphinx.ext.coverage',          # collect document coverage
    'sphinx_rtd_theme'              # RTD theme
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
autosummary_generate = True                 # turn on autosummary generation
autosummary_generate_overwrite = True       # turn on overwriting for subsequent builds
autoclass_content = "both"                  # add __init__ doc (ie. params) to class summaries
html_show_sourcelink = False                # remove 'view source code' from top of page (for html, not python)
autodoc_inherit_docstrings = True           # if no docstring, inherit from base class
set_type_checking_flag = True               # enable 'expensive' imports for sphinx_autodoc_typehints
nbsphinx_allow_errors = True                # continue through Jupyter errors
add_module_names = False                    # remove namespaces from class/method signatures

templates_path = ['_templates']
exclude_patterns = []

try:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_css_files = ["readthedocs-custom.css"]
except ImportError:
    html_theme = 'alabaster'
html_static_path = ['_static']