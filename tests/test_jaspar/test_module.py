import inspect
from weakref import ref

import pytest

import jaspar.parser as jp
from .definitions import modules
from . import aux


GENERAL_INPUTS = [
    [],
    ["--help"],
    ["-h"]
]

def _get_data():
    return (
        (module, input)
        for _, module in inspect.getmembers(modules)
        if inspect.ismodule(module)
        for input in module.INPUTS + GENERAL_INPUTS
        
    )


@pytest.mark.parametrize(
    'module,input',
    _get_data()
)
def test_module(module, input, capfd):
    parser, _ = jp.parse_module(module)
    reference = module._get_reference_parser()

    if reference is None:
        pytest.skip()

    aux.compare_parsed_args(parser, reference, input, capfd)

@pytest.mark.parametrize(
    'module',
    (module for _, module in inspect.getmembers(modules) if inspect.ismodule(module))
)
def test_helpstrings(module, capfd):
    parser, _ = jp.parse_module(module)
    reference = module._get_reference_parser()

    if reference is None:
        pytest.skip()
    
    aux.compare_help_strings(parser, reference, capfd)
