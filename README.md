# Transformer template for FME Packages

This is a [Cookiecutter](https://cookiecutter.readthedocs.io) template
for use with [Safe Software's FME](https://safe.com).
This template is for an FME Package containing a single Python-based transformer.
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
* A Python library named `fme_mygreeter`, ready for packaging as a Python Wheel.
* A transformer named `MyGreeter` in the Integrations category,
  which calls the `fme_mygreeter` Python module.
  The transformer and its Python module have a simple example 
  of getting and setting attributes.
* A placeholder `icon.png` for the package, which can be replaced or deleted.


## Make an .fpkg

FME works with .fpkg files instead of FME Package directories.
To create an .fpkg file, use the `fme-packager` tool.
