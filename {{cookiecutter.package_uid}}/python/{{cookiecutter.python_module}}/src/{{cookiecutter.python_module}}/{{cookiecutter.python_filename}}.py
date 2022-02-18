"""
{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}} implementation.
"""
from fmeobjects import FMEFeature


class {{cookiecutter.transformer_name}}:
    """
    Each instance of the transformer in the workspace has an instance of this class.
    All instances are created at the beginning of the workspace translation.
    """

    def __init__(self):
        pass

    def input(self, feature: FMEFeature):
        """
        Receive an input feature.
        """
        # The FMX file supplies all parameters as attributes on the input feature.
        # After getting the values of these attributes, they need to be removed,
        # so they don't show up on output features.
        first_name = feature.getAttribute("__xformer_first_name")
        feature.removeAttribute("__xformer_first_name")

        # Set the output attribute, and output the feature.
        feature.setAttribute("_greeting", "Hello, {}!".format(first_name))
        self.pyoutput(feature)

    def pyoutput(self, feature: FMEFeature):
        """
        Emit an output feature.
        """
        # Implementation is injected by FME.
        pass
