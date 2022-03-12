import inspect
from argparse import ArgumentParser
from inspect import _ParameterKind
from typing import Callable


def parse_parameter(parser: ArgumentParser, param: inspect.Parameter):
    name = param.name
    is_required = param.default == inspect._empty
    is_positional = param.kind in [
        _ParameterKind.POSITIONAL_ONLY,
        _ParameterKind.POSITIONAL_OR_KEYWORD,
        _ParameterKind.VAR_POSITIONAL
    ]
    is_varpos = param.kind == _ParameterKind.VAR_POSITIONAL

    becomes_flag = not is_required or not is_positional
    if becomes_flag:
        name = "--" + name

    options = dict()

    # take default argument if present
    options['default'] = None if param.default == inspect._empty else param.default
    
    # required can only be set for flags, i.e. non-positional arguments
    if becomes_flag:
        options['required'] = is_required or not becomes_flag

    if is_varpos:
        options['nargs'] = '*'
    

    parser.add_argument(name, **options)
    


def parse_signature(parser: ArgumentParser, signature: inspect.Signature):
    for param in signature.parameters.values():
        parse_parameter(parser, param)
    
    return parser


def parse_main_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()


def parse_subcommand_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()


def parse_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()
