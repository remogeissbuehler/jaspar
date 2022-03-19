
from modulefinder import Module

from . import parser as P
import inspect
from inspect import _ParameterKind


def read_args(module: Module = None):
    if module is None:
        import sys
        module = sys.modules["__main__"]
    parser, signatures = P.parse_module(module)
    args = parser.parse_args()

    signature = signatures[args._func.__module__ + "." + args._func.__name__]

    # TODO make this work with subcommands
    fn_params = signature.parameters.values()
    
    # TODO: make some in-depth tests that this always has the right order
    fn_args = (
        getattr(args, param.name) 
        for param in fn_params
        if param.kind in [_ParameterKind.POSITIONAL_ONLY, _ParameterKind.VAR_POSITIONAL]
    )

    fn_kwargs = dict(
        (param.name, getattr(args, param.name))
        for param in fn_params
        if param.kind not in [_ParameterKind.POSITIONAL_ONLY, _ParameterKind.VAR_POSITIONAL]
    )


    args._func(*fn_args, **fn_kwargs)
