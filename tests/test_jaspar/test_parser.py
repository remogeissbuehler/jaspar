import inspect
from argparse import ArgumentParser

import jaspar.parser as jp
import pytest

from . import definitions as defs


@pytest.mark.parametrize(
    "signature_fct,reference_parser,inputs",
    defs.signatures.get_data()
)
def test_parse_signature(signature_fct, reference_parser, inputs, capfd):
    signature = inspect.signature(signature_fct)
    parser = jp.parse_signature(ArgumentParser(), signature)

    try:
        reference_args = reference_parser.parse_args(inputs)
    except SystemExit:
        ref_captured = capfd.readouterr()
        with pytest.raises(SystemExit):
            parser.parse_args(inputs)
            assert capfd.readouterr() == ref_captured
        return

    args = parser.parse_args(inputs)

    assert reference_args == args

@pytest.mark.parametrize(
    "signature_fct,reference_parser",
    defs.signatures.get_data(inputs=False)
)
def test_parse_signature_help_message(signature_fct, reference_parser, capfd):
    signature = inspect.signature(signature_fct)
    parser = jp.parse_signature(ArgumentParser(), signature)

    reference_parser.print_help()
    ref = capfd.readouterr()

    parser.print_help()
    actual = capfd.readouterr()

    assert ref == actual
