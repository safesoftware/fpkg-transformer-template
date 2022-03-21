from {{cookiecutter.python_module}}.transformer import TransformerImpl
from fmeobjects import FMEFeature


class MockTransformer(TransformerImpl):
    """
    This is a subclass of the transformer under test,
    but with its pyoutput() features saved to an out_features member,
    where they can be recovered for validation.
    """
    def __init__(self):
        super().__init__()
        self.out_features = []

    def pyoutput(self, feature):
        self.out_features.append(feature)


def test_greeting():
    """
    Verify the value of the greeting attribute on the output feature
    based on a given input feature.
    """
    # Build an input feature with internal attribute for parameter.
    in_feature = FMEFeature()
    in_feature.setAttribute("___XF_FIRST_NAME", "World")

    # Create the transformer and pass it the input feature.
    transformer = MockTransformer()
    transformer.input(in_feature)

    # There should be only 1 output feature,
    # with the expected greeting attribute and value.
    assert len(transformer.out_features) == 1
    out_feature = transformer.out_features[0]
    assert out_feature.getAttribute("_greeting") == "Hello, World!"
