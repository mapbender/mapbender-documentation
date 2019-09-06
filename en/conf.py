# -*- coding: utf-8 -*-

import sys, os

sys.path.insert(0, os.path.abspath('..'))
from conf import *

extensions = [
    'notfound.extension'
]

language = 'en'
master_doc = 'index'

html_static_path = ['../_static']
html_theme_path = ['../_templates']
html_theme = "sphinx_rtd_theme"
html_logo = '../_static/mapbender_logo.png'
html_favicon = '../_static/mapbender.ico'

# not found page 404
notfound_template = '../404.rst'

# Override RTD_Theme CSS
# https://github.com/rtfd/sphinx_rtd_theme/issues/117
html_context = {
    'css_files': [
        '../_static/theme_overrides.css',  # overrides for wide tables in RTD theme
    ],
    'display_github': True, # Add 'Edit on Github' link instead of 'View page source'
    'github_user': 'mapbender',
    'github_repo': 'mapbender-documentation',
    'github_version': 'master/'
}

# -- Project information -----------------------------------------------------

project       = u'Mapbender Documentation'
title         = project
author        = u'The Mapbender Team'
copyright     = u'2019, The Mapbender Team'
description   = u'Mapbender Documentation'
product       = u'Mapbender'
contributor   = u'WhereGroup GmbH'
filename      = u'Mapbender_doc'
documentclass = 'manual'

# -- Options for LaTeX output ------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        filename + '.tex',
        title,
        author,
        documentclass
    )
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        title,
        author,
        product,
        description,
        'Miscellaneous'
    ),
]

# -- Options for Epub output -------------------------------------------------

# The basename for the epub file. It defaults to the project name.
epub_basename = 'Mapbender_EN'

# Bibliographic Dublin Core info.
epub_title = project
epub_description = description
epub_author = author
epub_contributor = contributor
epub_language = language

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
