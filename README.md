# ug_ndigo5g

HTML/PDF User Guide for the cronologic **Ndigo5G-10** analog-to-digital
converter.

This is a Sphinx project that creates the User Guide for the
[Ndigo5G](https://www.cronologic.de/product/ndigo5g-10), highspeed digitizer.
from [cronologic GmbH & Co. KG](https://www.cronologic.de).

Find the documentation online at
[docs.cronologic.de/ndigo5g](https://docs.cronologic.de/ndigo5g).

## Prerequisites

Python is necessary for creating the HTML output.

Python and LuaLaTeX are necessary for creating the LaTeX/PDF output.

Dependencies are managed using [uv](https://docs.astral.sh/uv).

### Fonts for LaTeX

The `fontspec` package is used for the LaTeX output. It may complain that fonts
are missing from your system.

The following fonts are required for the LaTeX output and are included in the
listed packages.

- Montserrat (main font):
  [montserrat](https://ctan.org/tex-archive/fonts/montserrat)
- TeX Gyre Adventor (headings font): [tex-gyre](https://ctan.org/pkg/tex-gyre)
- Latin Modern Math (math font): [lm-math](https://ctan.org/pkg/lm-math)
- Latin Modern Mono Light (monospaced font): [lm](https://ctan.org/pkg/lm)
- KerkisSans (expanded Greek letters): [kerkis](https://ctan.org/pkg/kerkis)

## Building

Run

```shell
make html
```

or

```shell
make latexpdf
```

to compile the project as HTML or PDF. The HTML (PDF) output is in `build/html/`
(`build/latex/`).

Alternatively, if you do not have make, use the [make.bat](make.bat) script
instead.

## License

See [LICENSE](LICENSE).
