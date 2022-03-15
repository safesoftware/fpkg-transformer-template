"""
{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}} implementation.
"""
from fmeobjects import FMEFeature
from ._vendor.fmetools.plugins import FMEEnhancedTransformer


class {{cookiecutter.transformer_name}}(FMEEnhancedTransformer):
    """
    This is the Python implementation of the transformer.
    Each instance of the transformer in the workspace has an instance of this class.
    """

    def __init__(self):
        pass

    def input(self, feature: FMEFeature):
        """
        Receive an input feature.
        """
        # The FMX file supplies all parameters as attributes on the input feature.
        first_name = feature.getAttribute("___XF_FIRST_NAME")

        # Set the output attribute, and output the feature.
        feature.setAttribute("_greeting", "Hello, {}!".format(first_name))
        self.pyoutput(feature)
