from unittest.mock import MagicMock

from {{cookiecutter.python_module}}.transformer import TransformerImpl
from fmeobjects import FMEFeature


def test_greeting():
    """
    Verify the value of the greeting attribute on the output feature
    based on a given input feature.
    """
    # Build an input feature with internal attribute for parameter.
    in_feature = FMEFeature()
    in_feature.setAttribute("___XF_FIRST_NAME", "World")

    # Create the transformer and capture its output features.
    # Then pass it the input feature.
    transformer = TransformerImpl()
    transformer.pyoutput = MagicMock(transformer.pyoutput)
    transformer.input(in_feature)

    # There should be only 1 output feature,
    # with the expected greeting attribute and value.
    assert transformer.pyoutput.call_count == 1
    out_feature = transformer.pyoutput.call_args.args[0]
    assert out_feature.getAttribute("_greeting") == "Hello, World!"
