"""
{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}} implementation.
"""
from fmeobjects import FMEFeature
from ._vendor.fmetools.plugins import FMEEnhancedTransformer
from ._vendor.fmetools.paramparsing import TransformerParameterParser


class TransformerImpl(FMEEnhancedTransformer):
    """
    The Python implementation of the {{cookiecutter.transformer_name}} transformer.
    Each instance of the transformer in the workspace has an instance of this class.
    """

    def __init__(self):
        super(TransformerImpl, self).__init__()
        # Load the transformer parameter definitions.
        self.params = TransformerParameterParser("{{cookiecutter.publisher_uid}}.{{cookiecutter.package_uid}}.{{cookiecutter.transformer_name}}")

    def receive_feature(self, feature: FMEFeature):
        """
        Receive an input feature.
        """
        # Pass internal attributes on feature into parameter parser.
        # Then get the parsed value of the First Name parameter.
        # By default, these methods assume a prefix of '___XF_'.
        self.params.set_all(feature)
        first_name = self.params.get("FIRST_NAME")

        # Set the output attribute, and output the feature.
        feature.setAttribute("_greeting", "Hello, {}!".format(first_name))
        self.pyoutput(feature)

{%- if cookiecutter.group_based_transformer == "y" %}

    def process_group(self):
        # TODO: Implement as described in overriden method's docstring
        # Group-Based Transformers accumulate features in receive_feature().
        # When FME calls this method, process the accumulated features, output results,
        # and clear the accumulated features in preparation for the next group, if any.
        pass
{%- endif %}
