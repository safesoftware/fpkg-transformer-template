"""
Cookiecutter hook for template value validation.
"""
import re
import sys


def validate_parameter(parameter, regex_pattern, parameter_value):
    if not re.match(regex_pattern, parameter_value):
        print(
            "{name} needs to match {pattern}".format(
                name=parameter, pattern=regex_pattern
            )
        )
        return False
    return True


valid = True

# UID pattern from FME Packages Specification.
UID_PATTERN = r"^[a-z0-9](?!.*--)[a-z0-9-]{1,30}[a-z0-9]$"
valid &= validate_parameter("Package UID", UID_PATTERN, "{{cookiecutter.package_uid}}")
valid &= validate_parameter(
    "Publisher UID", UID_PATTERN, "{{cookiecutter.publisher_uid}}"
)

TRANSFORMER_PATTERN = r"^[A-Za-z0-9]+$"
valid &= validate_parameter(
    "Transformer name", TRANSFORMER_PATTERN, "{{cookiecutter.transformer_name}}"
)

TRANSFORMER_FILE_NAME_PATTERN = r"^[a-z0-9_]+$"
valid &= validate_parameter(
    "Transformer file name",
    TRANSFORMER_FILE_NAME_PATTERN,
    "{{cookiecutter.transformer_file_name}}",
)

PYTHON_MODULE_PREFIX_PATTERN = r"^[a-z0-9]+$"
valid &= validate_parameter(
    "Python module prefix",
    PYTHON_MODULE_PREFIX_PATTERN,
    "{{cookiecutter.python_module_prefix}}",
)

PYTHON_PACKAGE_PATTERN = r"^[A-Za-z0-9-]+$"
valid &= validate_parameter(
    "Python package name", PYTHON_PACKAGE_PATTERN, "{{cookiecutter.python_package}}"
)

PYTHON_MODULE_PATTERN = r"^[A-Za-z0-9_]+$"
valid &= validate_parameter(
    "Python module name", PYTHON_MODULE_PATTERN, "{{cookiecutter.python_module}}"
)

AUTHOR_EMAIL_PATTERN = r"^[^@]+@[^@]+$"
valid &= validate_parameter(
    "Author email", AUTHOR_EMAIL_PATTERN, "{{cookiecutter.author_email}}"
)

if not valid:
    print("Failed validation")
    sys.exit(1)
