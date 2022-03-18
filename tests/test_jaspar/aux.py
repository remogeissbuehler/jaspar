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


def _format_capfd(ref, cap) -> str:
    return f"{ref[0]}\n\t+++\n{ref[1]}\n\n -- is not --\n\n{cap[0]}\n\t+++\n{cap[1]}"


def compare_parsed_args(parser: ArgumentParser, reference: ArgumentParser, inputs: List[str], capfd):
    try:
        reference_args = reference.parse_args(inputs)
    except SystemExit:
        ref_captured = capfd.readouterr()
        with pytest.raises(SystemExit):
            parser.parse_args(inputs)
            captured = capfd.readouterr()
            assert captured == ref_captured, f"{_format_capfd(ref_captured, captured)}"
        return

    args = parser.parse_args(inputs)

    assert reference_args == args, f"{reference_args} != {args}"


def compare_help_strings(parser: ArgumentParser, reference: ArgumentParser, capfd):
    reference.print_help()
    ref = capfd.readouterr()

    parser.print_help()
    actual = capfd.readouterr()

    assert ref == actual, _format_capfd(ref, actual)