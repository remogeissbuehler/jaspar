import inspect
from argparse import ArgumentParser

import jaspar.parser as jp
import pytest

from . import definitions as defs
from . import aux


@pytest.mark.parametrize(
    "signature_fct,reference_parser,inputs",
    defs.signatures.get_data()
)
def test_parse_signature(signature_fct, reference_parser, inputs, capfd):
    signature = inspect.signature(signature_fct)
    parser = jp.parse_signature(ArgumentParser(), signature)

    aux.compare_parsed_args(parser, reference_parser, inputs, capfd)

@pytest.mark.parametrize(
    "signature_fct,reference_parser",
    defs.signatures.get_data(inputs=False)
)
def test_parse_signature_help_message(signature_fct, reference_parser, capfd):
    signature = inspect.signature(signature_fct)
    parser = jp.parse_signature(ArgumentParser(), signature)

    aux.compare_help_strings(parser, reference_parser, capfd) 
