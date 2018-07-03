from setuptools import setup, find_packages
from io import open


with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="{{cookiecutter.python_module}}",
    py_modules=["{{cookiecutter.python_module}}"],
    version="0.1.0",
    description="Code for the {{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}} transformer in FME",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    url="{{cookiecutter.fme_hub_url}}",
    keywords="fme fmepy transformer",
    classifiers=[
        "DO NOT UPLOAD TO PYPI",
        "Framework :: FME",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=False,
)