# -*- coding: utf-8 -*-
#
# Mapbender documentation build configuration file, created by
# sphinx-quickstart on Sun Jul  8 00:08:58 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinxcontrib.phpdomain'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Mapbender'
copyright = u'2022, The Mapbender Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# Mapbender uses three digits.
version = '3.3.0'
# The full version, including alpha/beta/rc tags.
release = '3.3.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Internationalization configuration ----------------------------------------
# -- Options for sphinx-intl ---------------------------------------------------

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# -- Lexer configuration ---------------------------------------------------

import sys
import os
import shlex
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
from pygments.lexers.templates import TwigHtmlLexer
from pygments.lexers.templates import TwigLexer
from pygments.lexers.data import YamlLexer
from pygments.lexers.sql import PostgresLexer
from pygments.lexers.resource import ResourceLexer

# Symfony Extension Start
#sys.path.append(os.path.abspath('_exts'))

# enable highlighting for PHP code not between ``<?php ... ?>`` by default
lexers['php']      = PhpLexer(startinline=True, linenos=1)
lexers['twig']     = TwigHtmlLexer()
lexers['postgres'] = PostgresLexer()
lexers['yaml']     = YamlLexer()
lexers['resource'] = ResourceLexer()

# use PHP as the primary domain
primary_domain = 'php'
highlight_language = 'php'

# ...
# add the extensions to the list of extensions

# set url for API links
api_url = 'http://api.symfony.com/master/%s'
# Symfony Extension End

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_theme']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Mapbender Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Mapbender Documentation'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/mapbender_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/mapbender3.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Mapbenderdoc'


# -- Options for LaTeX output --------------------------------------------------
# see: https://www.sphinx-doc.org/en/master/latex.html for settings

latex_engine = 'xelatex' # also possible lualatex, pdflatex, latex

_PREAMBLE = r"""
    \usepackage[T1]{fontenc}
    \usepackage[titles]{tocloft}
    \usepackage{textcomp}
    \inputencoding{utf8}
    \setmainfont{Ubuntu}
    \setsansfont{Ubuntu}
    \setmonofont{Ubuntu Mono}
"""

_PREAMPLE_PDFLATEX = """
    \DeclareUnicodeCharacter{25CF}{$\bullet$}
    \DeclareUnicodeCharacter{251C}{\mbox{\kern.23em
      \vrule height2.2exdepth1exwidth.4pt\vrule height2.2ptdepth-1.8ptwidth.23em}}
    \DeclareUnicodeCharacter{2500}{\mbox{\vrule height2.2ptdepth-1.8ptwidth.5em}}
    \DeclareUnicodeCharacter{2514}{\mbox{\kern.23em
      \vrule height2.2exdepth-1.8ptwidth.4pt\vrule height2.2ptdepth-1.8ptwidth.23em}}
"""

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': _PREAMBLE,

    'inputenc' : '\\usepackage[utf8]{inputenc}',
    'utf8extra': ''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        'de/index',
        'Mapbender_de.tex',
        u'Mapbender  Dokumentation',
        u'Das Mapbender Team',
        'manual'
    ),
    (
        'en/index',
        'Mapbender_en.tex',
        u'Mapbender  Documentation',
        u'The Mapbender Team',
        'manual'
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'mapbender', u'Mapbender Documentation', [u'The Mapbender Team'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        'de/index',
        'Mapbender DE',
        u'Mapbender Dokumentation',
        u'Das Mapbender Team',
        'Mapbender',
        'Ein KartenCMS',
        'Miscellaneous'
    ),
    (
        'en/index',
        'Mapbender EN',
        u'Mapbender Documentation',
        u'The Mapbender Team',
        'Mapbender',
        'A mapclient CMS',
        'Miscellaneous'
    ),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# Override RTD_Theme CSS
# https://github.com/rtfd/sphinx_rtd_theme/issues/117
html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # overrides for wide tables in RTD theme
    ],
    'display_github': True, # Add 'Edit on Github' link instead of 'View page source'
    'github_user': 'mapbender',
    'github_repo': 'mapbender-documentation',
    'github_version': 'master/'
}

# -- Options for epub output ------------------------------------------------

# The basename for the epub file. It defaults to the project name.
#epub_basename

# The HTML theme for the epub output. Since the default themes are not optimized for small screen space, using the same theme for HTML and epub output is usually not wise. This defaults to 'epub', a theme designed to save visual space.
#epub_theme

# A dictionary of options that influence the look and feel of the selected theme. These are theme-specific. For the options understood by the builtin themes, see this section.
#epub_theme_options

# The title of the document. It defaults to the html_title option but can be set independently for epub creation.
#epub_title

# The author of the document. This is put in the Dublin Core metadata. The default value is 'unknown'.
#epub_author

# The language of the document. This is put in the Dublin Core metadata. The default is the language option or 'en' if unset.
#epub_language

# The publisher of the document. This is put in the Dublin Core metadata. You may use any sensible string, e.g. the project homepage. The default value is 'unknown'.
#epub_publisher

# The copyright of the document. It defaults to the copyright option but can be set independently for epub creation.
#epub_copyright

# An identifier for the document. This is put in the Dublin Core metadata. For published documents this is the ISBN number, but you can also use an alternative scheme, e.g. the project homepage. The default value is 'unknown'.
#epub_identifier

# The publication scheme for the epub_identifier. This is put in the Dublin Core metadata. For published books the scheme is 'ISBN'. If you use the project homepage, 'URL' seems reasonable. The default value is 'unknown'.
#epub_scheme

# A unique identifier for the document. This is put in the Dublin Core metadata. You may use a random string. The default value is 'unknown'.
#epub_uid

# The cover page information. This is a tuple containing the filenames of the cover image and the html template. The rendered html cover page is inserted as the first item in the spine in content.opf. If the template filename is empty, no html cover page is created. No cover at all is created if the tuple is empty. Examples:
#epub_cover = ('_static/cover.png', 'epub-cover.html')
#epub_cover = ('_static/cover.png', '')
#epub_cover = ()

# Meta data for the guide element of content.opf. This is a sequence of tuples containing the type, the uri and the title of the optional guide information. See the OPF documentation at http://idpf.org/epub for details. If possible, default entries for the cover and toc types are automatically inserted. However, the types can be explicitely overwritten if the default entries are not appropriate. Example:
# epub_guide = (('cover', 'cover.html', u'Cover Page'),)

# Additional files that should be inserted before the text generated by Sphinx. It is a list of tuples containing the file name and the title. If the title is empty, no entry is added to toc.ncx. Example:
epub_pre_files = [
    ('index.html', 'Welcome'),
]

# Additional files that should be inserted after the text generated by Sphinx. It is a list of tuples containing the file name and the title. This option can be used to add an appendix. If the title is empty, no entry is added to toc.ncx. The default value is [].
epub_post_files = []

# A list of files that are generated/copied in the build directory but should not be included in the epub file. The default value is [].
epub_exclude_files = []

# The depth of the table of contents in the file toc.ncx. It should be an integer greater than zero. The default value is 3. Note: A deeply nested table of contents may be difficult to navigate.
#epub_tocdepth

# This flag determines if a toc entry is inserted again at the beginning of it’s nested toc listing. This allows easier navitation to the top of a chapter, but can be confusing because it mixes entries of differnet depth in one list. The default value is True.
#epub_tocdup

# This setting control the scope of the epub table of contents. The setting can have the following values:
#epub_tocscope

# This flag determines if sphinx should try to fix image formats that are not supported by some epub readers. At the moment palette images with a small color table are upgraded. You need the Python Image Library (PIL) installed to use this option. The default value is False because the automatic conversion may lose information.
#epub_fix_images

# This option specifies the maximum width of images. If it is set to a value greater than zero, images with a width larger than the given value are scaled accordingly. If it is zero, no scaling is performed. The default value is 0. You need the Python Image Library (PIL) installed to use this option.
#epub_max_image_width

# Control whether to display URL addresses. This is very useful for readers that have no other means to display the linked URL. The settings can have the following values:
#epub_show_urls

# If true, add an index to the epub document. It defaults to the html_use_index option but can be set independently for epub creation.
#epub_use_index
