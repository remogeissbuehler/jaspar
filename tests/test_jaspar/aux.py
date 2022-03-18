from argparse import ArgumentParser
from typing import Callable, List

import pytest

def add_data_to_fct(**kwargs):
    """Adds data to a function.

    For every key in the kwargs dictionary, a corresponding key with an underscore _ prepended will be added
    to the function object.

    Example:
    @_add_data_to_fct(input=["hello", "world"])
    def somefunction(somearg):
        pass

    will set somefunction._input = ["hello", "world"]
    """
    def decorator(function: Callable):
        for key in kwargs:
            setattr(function, "_" + key, kwargs[key]) 
            
        return function
    
    return decorator


def hasattrs(obj, *attrs):
    for attr in attrs:
        if not hasattr(obj, attr): return False

    return True


def compare_parsers(parser: ArgumentParser, reference: ArgumentParser, inputs: List[str], capfd):
    try:
        reference_args = reference.parse_args(inputs)
    except SystemExit:
        ref_captured = capfd.readouterr()
        with pytest.raises(SystemExit):
            parser.parse_args(inputs)
            assert capfd.readouterr() == ref_captured
        return

    args = parser.parse_args(inputs)

    assert reference_args == args