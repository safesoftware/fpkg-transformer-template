"""
{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}}
Python implementation.

The Python package's setup.py is configured such that 
the Python code for the transformer must be entirely in this file.
"""
# The code in this file must be compatible with both Python 2 and 3.
# FME includes the 'six' library for this purpose.
# import six

# import fmeobjects


class {{cookiecutter.transformer_name}}(object):
    """
    One instance of this class is created per instance of the transformer in the workspace.
    All instances are created at the beginning of the workspace translation.
    """

    def __init__(self):
        pass

    def input(self, feature):
        first_name = feature.getAttribute('__xformer_first_name')
        feature.setAttribute('greeting', 'Hello, {}!'.format(first_name))
        self.pyoutput(feature)

    def pyoutput(self, feature):
        # Implementation is injected by FME.
        pass
