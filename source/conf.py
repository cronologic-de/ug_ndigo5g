# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import pathlib
import tomllib


def get_version() -> str:
    pyproject = pathlib.Path("./pyproject.toml")
    if pyproject.exists():
        with pyproject.open("rb") as f:
            data = tomllib.load(f)
        return data.get("project", {}).get("version")
    return "0.0.0"


project = "Ndigo5G-10 User Guide"
copyright = "2026, cronologic GmbH & Co. KG"
author = "cronologic GmbH & Co. KG"
version = get_version()
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "breathe",
]

breathe_projects = {"ndigo5g_api": os.fspath("./doxygen/xml/")}
breathe_default_project = "ndigo5g_api"
breathe_show_include = False
breathe_show_define_initializer = True

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

toc_object_entries_show_parents = "hide"

with open("global.rst", "r") as f:
    prolog_file = f.read()
rst_prolog = f"""
{prolog_file}

.. |version| replace:: {release}
"""

templates_path = ["_templates"]
exclude_patterns = ["global.rst"]

numfig = True
numfig_format = {"figure": "Figure %s:", "table": "Table %s:"}
numfig_secnum_depth = 1
primary_domain = "cpp"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

cronoblue = "#376EB5"
cronolightblue = "#569fd6"
cronoorange = "#ED7807"
cronolightorange = "rgb(237, 120, 7, 0.2)"
cronogrey = "#737372"
cronolightgrey = "#acacac"
cronoverylightgrey = "#dcdcdc"

html_theme = "furo"
html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": cronolightblue,
        "color-brand-content": cronolightblue,
        "color-api-name": cronoorange,
        "color-sidebar-brand-text": cronolightblue,
        "color-highlight-on-target": cronolightorange,
        "color-foreground-primary": cronolightgrey,
        "color-headers": cronoverylightgrey,
        "color-first-header": cronoorange,
    },
    "light_css_variables": {
        "font-stack": "Montserrat, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji",
        "font-stack--monospace": "Consolas, Monaco, Liberation Mono, Lucida Console, monospace",
        "color-foreground-primary": cronogrey,
        "color-headers": "#000000",
        "color-first-header": cronoorange,
        "color-brand-primary": cronoblue,
        "color-brand-content": cronoblue,
        "color-api-name": cronoorange,
        "color-sidebar-brand-text": cronoblue,
        "color-admonition-title--attention": cronoorange,
        "color-admonition-title-background--attention": cronolightorange,
        "color-highlight-on-target": cronolightorange,
        "sidebar-caption-space-above": "0",
    },
    "top_of_page_buttons": [],
}

html_favicon = "_static/cronologic_favicon.svg"
html_title = f"{project}"
html_logo = "_static/cronologic.svg"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# latex_toplevel_sectioning = "section"

latex_engine = "lualatex"
latex_xindy_use = False
latex_table_style = ["booktabs"]
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg": "",
    "preamble": r"""
        \usepackage[
            sphinx,
            noframe=false,
            webpage=https://docs.cronologic.de/ndigo5g,
        ]
        {cronologicug}
        \definecolor{ctypered}{RGB}{142,33,0} % C-type auto highlighting color
        \newcommand{\docutilsrolectypered}[1]{{\color{ctypered} #1}}
        \newcommand{\docutilsrolered}[1]{{\color{red} #1}}
        \newcommand{\docutilsrolecronoblue}[1]{{\color{cronoblue} #1}}
        \setcounter{tocdepth}{4}
    """,
    "extraclassoptions": r"openany",
    "tableofcontents": r"\tableofcontents",
    "maketitle": r"%\includepdf[pages={1}]{Ndigo6G-12_Front_Page.pdf}",
    "releasename": "Rev.",
    "makeindex": "",
    "printindex": "",
}
latex_theme = "manual"  # manual (book class) or howto (article class)
latex_additional_files = [
    "cronologicug.sty",
    "extraplaceins.sty",
]
