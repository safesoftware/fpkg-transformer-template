# Transformer template for FME Packages

This is a [Cookiecutter](https://cookiecutter.readthedocs.io) template
for use with [Safe Software's FME](https://safe.com).
This template is for an FME Package containing a single Python-based
transformer for FME 2023 and newer.
It prompts for some values and generates an FME Package directory structure.


## Usage

First, install Cookiecutter:

```
$ pip install cookiecutter
```

Then, tell Cookiecutter to load this template:

```
$ cookiecutter https://github.com/safesoftware/fpkg-transformer-template.git
```

You'll be prompted to enter a series of values to fill in the template.
`cookiecutter.json` contains all the things you'll be asked.

The template includes some basic validation to ensure that the supplied parameters
don't result in an invalid package structure.


## Contents

The template lays down a directory with the name of your `package_uid`.
Inside are the contents of an FME Package, ready to be extended.

If all default parameters of the template were accepted, this results in:

* An FME Package with `publisher_uid` of `example` and `package_uid` of `my-package`.
* A Python library named `fme_demogreeter`, ready for packaging as a Python Wheel.
* A transformer named `DemoGreeter` in the Integrations category,
  which calls the `fme_demogreeter` Python module.
  The transformer and its Python module have a simple example 
  of getting and setting attributes.
* A placeholder `icon.png` for the package, which can be replaced or deleted.


## Next steps

1. **Install Python dev dependencies:**
  In a terminal, navigate to the Python package directory and run `pip install -e .[dev]`.
2. **Vendorize fmetools**: This template's Python code requires a private copy of the [fmetools] library.
   Install it by running `python-vendorize` in the Python package directory.
   This installs fmetools based on the settings in vendorize.toml.
3. **Make an .fpkg:** FME Package projects need to be converted to .fpkg files for use with FME Workbench.
   To create an .fpkg file, use the [fme-packager] tool.

[fmetools]: https://pypi.org/project/fmetools/
[fme-packager]: https://pypi.org/project/fme-packager/

## Make an .fpkg

FME works with .fpkg files instead of FME Package directories.
To create an .fpkg file, use the `fme-packager` tool.
