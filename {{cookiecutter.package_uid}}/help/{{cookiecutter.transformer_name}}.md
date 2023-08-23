# {{cookiecutter.transformer_name}} ({{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}})
The {{cookiecutter.transformer_name}} transformer takes a first name as input,
and outputs a greeting for that person.

[//]: # (This file is the main documentation for the transformer)
[//]: # (and should fully describe its functionality and parameters.)

This transformer is part of the FME Package `{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}`.

## Typical uses
To set an attribute that contains a customizable greeting.

## How does it work?
Sets an attribute named `_greeting` with a value of `Hello, [FIRST NAME]!`.

## Configuration
### Input Ports
#### Input
This transformer accepts any feature.
### Output Ports
#### Output
- **_greeting:** The greeting based on the given parameters.

#### <Rejected>
Features that cause the operation to fail are output through this port.
Rejected features have `fme_rejection_code` and `fme_rejection_message` attributes
which specify the reason for the failure.

**Note:** If the input feature has an existing value for `fme_rejection_code`, the value will be removed.

**Rejected Feature Handling:** Can be set to either terminate the translation or
continue running when it encounters a rejected feature.
This setting is available both as a default [FME option](https://docs.safe.com/fme/html/FME_Desktop_Documentation/FME_Workbench/Workbench/options_workspace_defaults.htm)
and as a [workspace parameter](https://docs.safe.com/fme/html/FME_Desktop_Documentation/FME_Workbench/Workbench/workspace_parameters.htm).

### Parameters
#### Options
- **First Name:** First name to be greeted by. Defaults to "World".
