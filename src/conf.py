# -*- coding: utf-8 -*-
#
# CellML specifications build configuration file, created by
# sphinx-quickstart on Mon Jun  9 21:58:16 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import datetime

date_today = datetime.datetime.today()

unofficial = True

if unofficial:
  tags.add('unofficial')

build_type = os.environ['CELLML_SPEC_BUILD'] if 'CELLML_SPEC_BUILD' in os.environ else 'Normative'
if build_type not in ('Normative', 'Full'):
    raise ValueError('Build type must be "Normative" or "Full".')

def manage_index(direction, base_dir=''):
    files = ['master_index.rst', 'index.rst']
    if build_type == 'Normative':
        files = ['normative_only_index.rst', 'index.rst']

    files = [os.path.join(base_dir, files[0]),
             os.path.join(base_dir, files[1])]
    if direction == 'out':
        files.reverse()

    os.rename(os.path.abspath(files[0]), os.path.abspath(files[1]))


def tex_document_name():
    name = 'cellml2_specification'
    if build_type == 'Normative':
        name = 'cellml2_normative_specification'

    return name


def define_excluded_patterns():
    exclude_patterns = ['normative_only_index.rst',
                        'reference/libcellml/*.rst',
                        'reference/formal_section*',
                        'reference/informative/informB9_reset1.rst',
                        'reference/informative/informC07_effect_of_units_on_variables.rst',
                        'reference/informative/informC08_interpretation_of_mathematics.rst',
                        'reference/informative/informC11_interpretation_of_variable_resets.rst',
                        'reference/formal_only/*', ]
    if build_type == 'Normative':
        exclude_patterns = ['master_index.rst',
                            'reference/index_section*',
                            'reference/formal_and_informative/*.rst',
                            'reference/informative/*.rst',
                            'reference/libcellml/*.rst', ]

    return exclude_patterns


manage_index('in')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '3.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'hoverxref.extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['static/templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

autosectionlabel_prefix_document = True

# These are the shorthand for external links.  Use them in the other pages as:
#   :shortcut:`Shortcut text <extra string if needed>` NB space before <
# Declare below as:
#   'shortcut': ('http://linkhere/%s',''), NB have to put the string insertion %s to make it work
#   OR, where you want to print out the URL to the rendered version:
#   'shortcut': ('http://linkhere%s', None) then use :shortcut:`/` in the text to display full URL, including the trailing slash.
extlinks = {
    'buildbot': ('https://buildbot.net%s', ''),
    'calvin_and_hobbes': ('https://www.gocomics.com/calvinandhobbes/%s', ''),
    'cellml1to2': ('https://github.com/hsorby/cellml1to2%s', ''),
    'cellml2namespace': ('http://www.cellml.org/cellml/2.0%s', None),
    'cellml2spec_display': ('https://cellml.org/specifications/cellml_2.0%s', None),
    'cellsolver': ('https://github.com/hsorby/cellsolver%s', ''),
    'cmake': ('https://cmake.org/%s', ''),
    'doxygen': ('http://www.doxygen.nl/%s', ''),
    'euler_method': ('https://en.wikipedia.org/wiki/Euler_method%s', ''),
    'git': ('https://git-scm.com/%s', ''),
    'github': ('https://github.com/%s', ''),
    'google_styleguide': ('https://google.github.io/styleguide/cppguide.html/%s', ''),
    'libcellml': ('https://libcellml.org/%s', ''),
    'libcellml_repo': ('https://github.com/cellml/libcellml.git%s', ''),
    'libxml2': ('http://www.xmlsoft.org/%s', ''),

    # These should be identical: one for links, one for full URL display
    'mathml2':         ('https://www.w3.org/TR/2003/REC-MathML2-20031021%s', ''),
    'mathml2_display': ('https://www.w3.org/TR/2003/REC-MathML2-20031021%s', None),

    'mathml2help': ('https://www.w3.org/TR/MathML2/chapter4.html%s', ''),

    # This will get MathML added to the end so it becomes http://www.w3.org/1998/Math/MathML
    # in the final display, to avoid trailing slashes.
    'mathml2namespace': ('http://www.w3.org/1998/Math/%s', None),

    'namespace_help': ('https://www.w3schools.com/xml/xml_namespaces.asp%s', ''),
    'opencor': ('https://opencor.ws/%s', ''),
    'pmr': ('https://models.physiomeproject.org/welcome/%s', ''),
    'python': ('https://www.python.org/%s', ''),

    # These should be identical: one for links, one for full URL display
    'rfc2119':         ('https://www.ietf.org/rfc/rfc2119.txt%s', ''),
    'rfc2119_display': ('https://www.ietf.org/rfc/%s', None),

    'sphinx': ('http://sphinx-doc.org/%s', ''),
    'swig': ('http://www.swig.org/%s', ''),
    'unicode': ('http://www.fileformat.info/info/unicode/char/%s/index.htm', 'U+'),

    # These should be identical: one for links, one for full URL display
    'unicode13':         ('https://www.unicode.org/versions/Unicode13.0.0%s', ''),
    'unicode13_display': ('https://www.unicode.org/versions/Unicode13.0.0%s', None),

    # These should be identical: one for links, one for full URL display
    'xlink':         ('https://www.w3.org/TR/2001/REC-xlink-20010627%s', ''),
    'xlink_display': ('https://www.w3.org/TR/2001/REC-xlink-20010627%s', None),

    'xml_help': ('https://www.w3.org/XML/%s', ''),

    # These should be identical: one for links, one for full URL display
    'xml_1_1':         ('https://www.w3.org/TR/xml11%s', ''),
    'xml_1_1_display': ('https://www.w3.org/TR/xml11%s', None),

    # These should be identical: one for links, one for full URL display
    'xml_infoset':         ('https://www.w3.org/TR/2004/REC-xml-infoset-20040204/%s', ''),
    'xml_infoset_display': ('https://www.w3.org/TR/xml-infoset%s', None),

    'xml_namespace_1_1':         ('https://www.w3.org/TR/2006/REC-xml-names11-20060816%s', ''),
    'xml_namespace_1_1_display': ('https://www.w3.org/TR/2006/REC-xml-names11-20060816%s', None),

}

# Making a passive role with which to decorate hardcoded references to sections. These
# will need to be manually changed if the numbering is ever altered, and can be located
# more easily by searching for the "hardcodedref" tag.
rst_prolog = """
.. role:: hardcodedref
"""

# General information about the project.
project = u'CellML'
copyright = u'2019-{0}, CellML Editors and Contributors'.format(
    date_today.year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0'
if unofficial:
    version += '-unofficial'
    release += '-unofficial'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = define_excluded_patterns()

# The reST default role (used for this markup: `text`) to use for all
# documents.
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

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, enable figure numbering
numfig = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = '@SPHINX_THEME@'
html_theme = 'sphinx_rtd_theme'
# html_theme = 'bizstyle'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navigation_depth': 2,
}

# Pass options through to the template
html_context = {
  'unofficial': unofficial,
}

# Automagically convert all :ref: blocks to show a tooltip using the hoverxref
# extension.
hoverxref_auto_ref = True
hoverxref_roles = ['term', 'code']

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['@SPHINX_THEME_DIR@']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
# html_style = 'css/theme.css'

html_static_path = ['static/']
html_css_files = ['css/cellml.css']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

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
htmlhelp_basename = 'CellMLdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Removing the blank pages between chapters
    'extraclassoptions': 'openany,twoside',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
% Preamble set from Sphinx configuration
\usepackage[titles]{tocloft}
\usepackage{textgreek}
\usepackage{amssymb}

% Stop cross-references from showing up in italics
\protected\def\sphinxcrossref#1{#1}
'''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '{0}.tex'.format(tex_document_name()), u'CellML Normative Specification',
     u'CellML 2.0 Editors and Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#    ('index', 'cellml', u'CellML 2.0 Documentation', [u'CellML Editors'], 1)
# ]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#    ('index', 'CellML', u'CellML Documentation',
#     u'CellML 2.0 Editors', 'CellML 2.0', 'CellML 2.0 Normative Specification.',
#     'Miscellaneous'),
# ]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

def build_finished_handler(app, exception):
    manage_index('out', base_dir=app.confdir)


def setup(app):
    app.connect('build-finished', build_finished_handler)
    app.add_css_file('css/cellml.css')
