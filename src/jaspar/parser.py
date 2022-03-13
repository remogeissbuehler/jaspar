from enum import Enum
import inspect
from argparse import ArgumentParser
from inspect import _ParameterKind
from typing import Callable
from venv import create

from . import config as C
from . import actions as A


class CmdLineArgType(Enum):
    POSTIONAL = 0b01
    FLAG = 0b10
    BOTH = 0b11


def create_argument(
    parser: ArgumentParser,
    arg_type: CmdLineArgType,
    name: str,
    **options
):
    if arg_type == CmdLineArgType.POSTIONAL:
        if not options.pop("required", True) and 'nargs' not in options:
            options['nargs'] = '?'

        parser.add_argument(name, **options)
    elif arg_type == CmdLineArgType.FLAG:
        parser.add_argument("--" + name, **options)
    else:
        g = parser.add_mutually_exclusive_group(options.get("required", False))
        g.add_argument(name, nargs="?", action=A.StoreOnce)
        g.add_argument("--" + name, action=A.StoreOnce)


def parse_parameter(
    parser: ArgumentParser,
    param: inspect.Parameter,
    create_both: bool
) -> None:
    """Takes the signature of a function and adds the parameters to the parser.

    Example: Takes a parameter "b = None" and does `parser.add_argument("--b", default=None)`

    :param parser: The parser to add the parameter to
    :type parser: ArgumentParser
    :param param: The parameter of the function signature with its properties.
    :type param: inspect.Parameter
    :param create_both: Whether or not to create both a positional and a flag argument 
                        for a POSITIONAL_OR_KEYWORD parameter.
    """
    name = param.name.replace("_", "-")
    has_default = param.default != inspect._empty

    arg_type = None
    if param.kind == _ParameterKind.KEYWORD_ONLY:
        arg_type = CmdLineArgType.FLAG
    elif param.kind in [
        _ParameterKind.POSITIONAL_ONLY,
        _ParameterKind.VAR_POSITIONAL
    ]:
        arg_type = CmdLineArgType.POSTIONAL
    elif param.kind == _ParameterKind.POSITIONAL_OR_KEYWORD:
        if has_default:
            arg_type = CmdLineArgType.FLAG
        else:
            arg_type = CmdLineArgType.POSTIONAL

        if create_both:
            arg_type = CmdLineArgType.POSTIONAL

    options = dict()

    # take default argument if present
    options['default'] = None if not has_default else param.default
    options['required'] = not has_default

    if param.kind == _ParameterKind.VAR_POSITIONAL:
        options['nargs'] = '*'

    create_argument(parser, arg_type, name, **options)


def parse_signature(parser: ArgumentParser, signature: inspect.Signature):
    has_positional_only = any(
        param.kind == _ParameterKind.POSITIONAL_ONLY
        for param in signature.parameters.values()
    )

    create_both = C.POSITIONAL_OR_KEYWORD_MODE == C.PositionalOrKeywordMode.STRICT
    create_both = create_both or has_positional_only
    for param in signature.parameters.values():
        parse_parameter(parser, param, create_both)

    return parser


def parse_main_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()


def parse_subcommand_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()


def parse_function(parser: ArgumentParser, f: Callable):
    raise NotImplementedError()
