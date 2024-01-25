# ug_ndigo5g

Userguide for the cronologic Ndigo5G digitizer. 

This is a [Sphinx](https://www.sphinx-doc.org/) project that creates the
userguides for the
[Ndigo5G-10 and Ndigo5G-8](https://www.cronologic.de/product/ndigo5g-10),
gigasample PCIe digitizer boards by
[cronologic GmbH & Co. KG](https://www.cronologic.de/).

## Setup and installation
A Python installation is necessary to compile the user guide.

Optionally, create and activate a virtual environment
```powershell
python -m venv .venv
. .\.venv\Scripts\activate
``` 

Install the requirements of the project
```powershell
pip install -r requirements.txt
```


After that, run
```powershell
make html
```
   or
```powershell
make latexpdf
```
to compile the project as html or pdf. The html (pdf) output is in
`build/html/` (`build/latex/`).


## License
This documentation is licensed under an [Creative Commons Attribution-NonDerivatices 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/).
You are free to copy and redistribute the material in any medium or format for any purpose, even commercially unchanged if you give appropriate credit to cronologic GmbH & Co. KG. A link to [this repository](https://github.com/cronologic-de/ug_ndigo5g) or the [product page](https://www.cronologic.de/products/adcs/cronologic-ndigo5g-10) is sufficient.

If you decide to contribute to this repository you transfer non-exclusive but unlimited rights to your edit to cronologic GmbH & Co. KG.

![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

The file [extraplaceins.sty](extraplaceins.sty) is in the public domain.
