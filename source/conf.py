# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import pathlib
import tomllib

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList


def get_version() -> str:
    pyproject = pathlib.Path("../pyproject.toml")
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
breathe_default_members = ("members", "undoc-members")
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
numfig_format = {"figure": "Figure %s", "table": "Table %s"}
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
        "font-stack": "montserrat, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji",
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
        \definecolor{org}{RGB}{237,120,0}
        \definecolor{gry}{RGB}{ 157,157,156}
        \newcommand{\docutilsrolectypered}[1]{{\color{ctypered} #1}}
        \newcommand{\docutilsrolered}[1]{{\color{red} #1}}
        \newcommand{\docutilsrolecronoblue}[1]{{\color{cronoblue} #1}}
        \setcounter{tocdepth}{4}
    """,
    "extraclassoptions": r"openany",
    "tableofcontents": r"\tableofcontents",
    "maketitle": r"""
        \thispagestyle{empty}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (0,0)   { \includegraphics[width=\textwidth]{cronologic.pdf}};
        \end{tikzpicture}

        \begin{minipage}{0.83\textwidth}
        \begin{tabular}{l}

        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (-8.3,1){\fontsize{20}{2}\selectfont
        \cronoheaderfont
        {\textcolor{org}{Ndigo5G-PCIe}}};

        \draw[align=center] node at (-8.3,0){\fontsize{20}{2}\selectfont
        \sffamily \textcolor{org}{USER GUIDE}};
        \end{tikzpicture}
        \\ \vspace{5pt}
        %{\efbox{
        %\hspace{-10pt}
        \includegraphics[width=120mm,height=150mm,keepaspectratio]{Title5G.pdf}
        %}}
        \\
        \end{tabular}
        \end{minipage}
        \begin{minipage}{0\textwidth}
        \vspace{25pt}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (0,-5){
        \fontsize{100}{2}\selectfont
        \bfseries \textcolor{org}{ \rotatebox{90}{Ndigo5G-PCIe}}};
        \end{tikzpicture}
        \end{minipage}

        \vspace{-25pt}
        \begin{minipage}{0\textwidth}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (-3,-18){\fontsize{20}{2}\selectfont
        \sffamily \textcolor{gry}{~\url{www.cronologic.de}}};
        \end{tikzpicture}
        \end{minipage}
        \newpage
    """,
    "releasename": "Rev.",
    "makeindex": "",
    "printindex": "",
}
latex_theme = "manual"  # manual (book class) or howto (article class)
latex_additional_files = [
    "cronologicug.sty",
    "extraplaceins.sty",
    "cronologic.pdf",
    "Title5G.pdf",
]


class PassThroughOptions(dict):
    """
    Dictionary subclass allowing dynamic acceptance of any directive option.
    """

    def __contains__(self, key):
        return True

    def __getitem__(self, key):
        if key in ("no-latex-header", "hide-initializer"):
            return directives.flag
        return directives.unchanged


class LatexTocDoxygenBase(Directive):
    """
    Base directive wrapping Breathe doxygen directives to inject LaTeX TOC entries.

    Available Options:
        :no-latex-header: (flag) If present, disables the LaTeX raw block generation.
        :toclevel: (string) The LaTeX TOC level to use. Defaults to 'subsection'.
        :hide-initializer: (flag) Temporarily disables breathe_show_define_initializer.
        *Any other options provided are passed through to the underlying doxygen directive.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = PassThroughOptions()

    def run(self):
        name = self.arguments[0]
        escaped_name = name.replace("_", r"\_")
        no_latex = "no-latex-header" in self.options
        toclevel = self.options.get("toclevel", "subsection")
        hide_initializer = "hide-initializer" in self.options

        rst = []
        if not no_latex:
            rst.extend(
                [
                    ".. raw:: latex",
                    "",
                    "    \\phantomsection",
                    f"    \\addcontentsline{{toc}}{{{toclevel}}}{{{escaped_name}}}",
                    "",
                ]
            )

        rst.append(f".. {self.doxy_type}:: {name}")  # ty: ignore[unresolved-attribute]

        for k, v in self.options.items():
            if k not in ("no-latex-header", "toclevel", "hide-initializer"):
                rst.append(f"   :{k}:" if v is None else f"   :{k}: {v}")

        if self.content:
            rst.append("")
            rst.extend(f"   {line}" for line in self.content)

        node = nodes.Element()
        env = self.state.document.settings.env

        orig_initializer_setting = getattr(
            env.config, "breathe_show_define_initializer", False
        )

        if hide_initializer:
            env.config.breathe_show_define_initializer = False

        try:
            self.state.nested_parse(
                StringList(rst, source=self.state.document.current_source),
                self.content_offset,
                node,
            )
        finally:
            if hide_initializer:
                env.config.breathe_show_define_initializer = orig_initializer_setting

        return node.children


class LatexTocDoxygenFunction(LatexTocDoxygenBase):
    """
    Sphinx directive wrapping doxygenfunction with LaTeX TOC injection.
    """

    doxy_type = "doxygenfunction"


class LatexTocDoxygenStruct(LatexTocDoxygenBase):
    """
    Sphinx directive wrapping doxygenstruct with LaTeX TOC injection.
    """

    doxy_type = "doxygenstruct"


class LatexTocDoxygenDefine(LatexTocDoxygenBase):
    """
    Sphinx directive wrapping doxygendefine with LaTeX TOC injection.
    """

    doxy_type = "doxygendefine"


class LatexTocDoxygenTypedef(LatexTocDoxygenBase):
    """
    Sphinx directive wrapping doxygentypedef with LaTeX TOC injection.
    """

    doxy_type = "doxygentypedef"


def setup(app):
    """
    Registers the custom LaTeX TOC doxygen directives with the Sphinx application.
    """
    app.add_directive("latex-toc-doxygenfunction", LatexTocDoxygenFunction)
    app.add_directive("latex-toc-doxygenstruct", LatexTocDoxygenStruct)
    app.add_directive("latex-toc-doxygendefine", LatexTocDoxygenDefine)
    app.add_directive("latex-toc-doxygentypedef", LatexTocDoxygenTypedef)
    return {"version": "1.0", "parallel_read_safe": True}
