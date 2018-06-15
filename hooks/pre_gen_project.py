"""
Cookiecutter hook for template value validation.
"""
from __future__ import print_function
import re
import sys


failed = False


def print2(msg):
    print(msg)
    failed = True


UID_PATTERN = r'^[a-z0-9](?!.*--)[a-z0-9-]{1,30}[a-z0-9]$'
if not re.match(UID_PATTERN, '{{cookiecutter.publisher_uid}}'):
    print2('Publisher UID needs to match ' + UID_PATTERN)
if not re.match(UID_PATTERN, '{{cookiecutter.package_uid}}'):
    print2('Package UID needs to match ' + UID_PATTERN)


TRANSFORMER_PATTERN = r'^[A-Za-z0-9]$'
if not re.match(TRANSFORMER_PATTERN, '{{cookiecutter.transformer_name}}'):
    print2('Transformer name needs to match ' + TRANSFORMER_PATTERN)


if failed:
    print('Failed validation')
    sys.exit(1)
