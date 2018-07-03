# {{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}}

_This doc appears when the transformer is selected in the Workbench Quick Add pane._

The {{cookiecutter.transformer_name}} transformer takes a first name as input,
and outputs a greeting for that person.

This transformer is part of the
[{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}} FME Package]({{cookiecutter.fme_hub_url}}).


## Inputs:

* **First Name**: The first name of who to greet. Default: "World".

## Outputs attributes:

* **greeting**: This attribute contains the greeting message.
  It looks something like "Hello, [first name]!".
