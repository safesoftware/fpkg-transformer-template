"""
{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}} implementation.
"""
from fmeobjects import FMEFeature
from ._vendor.fmetools.plugins import FMEEnhancedTransformer


class TransformerImpl(FMEEnhancedTransformer):
    """
    The Python implementation of the {{cookiecutter.transformer_name}} transformer.
    Each instance of the transformer in the workspace has an instance of this class.
    """

    def __init__(self):
        super(TransformerImpl, self).__init__()

    def receive_feature(self, feature: FMEFeature):
        """
        Receive an input feature.
        """
        # The FMX file supplies all parameters as attributes on the input feature.
        first_name = feature.getAttribute("___XF_FIRST_NAME")

        # Set the output attribute, and output the feature.
        feature.setAttribute("_greeting", "Hello, {}!".format(first_name))
        self.pyoutput(feature)
