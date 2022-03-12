"""Function signatures for tests
"""
from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty, abstractstaticmethod
from argparse import ArgumentParser
import inspect
import itertools

from .. import aux

# These functions server to test the different types of signatures that a function could have.
# 1. Types of parameters: positional / keyword / optional / required / variable length etc.

input_everywhere = [
    [],
]


class SignatureTestCase(ABC):
    @abstractstaticmethod
    def signature(*args, **kwargs):
        pass

    @abstractstaticmethod
    def get_reference_parser():
        pass


# --
class Positional(SignatureTestCase):
    @staticmethod
    def signature(a, b):
        pass

    inputs = [
        ["hello", "world"],
        ["1", "too"],
        ["onlyone"],
        ["one", "too", "many"],
        ["hello", "world", "--with-a-flag"]
    ]

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a")
        parser.add_argument("b")

        return parser


class PositionalAndKwOpt(SignatureTestCase):
    @staticmethod
    def signature(a, b, c=None):
        pass

    inputs = [
        ["hello", "world"],
        ["hello", "world", "--c", "25"],
        ["hello", "world", "--c", "test"],
        ["hello", "world", "--c", "multiple", "after", "flag"],
        ["hello"],
        ["two", "args", "--d", "something"],
    ]

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a")
        parser.add_argument("b")
        parser.add_argument("--c")

        return parser


class VarPos(SignatureTestCase):
    @staticmethod
    def signature(*a):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a", nargs="*")

        return parser

    inputs = [
        ["one"],
        ["one", "two", "three"],
        ["positional", "--with-flag"],
        ["positional", "too", "-s"]
    ]


class VarPosAndKwOpt(SignatureTestCase):
    @staticmethod
    def signature(*a, b="test"):
        pass

    inputs = [ 
        ["multiple", "arguments"],
        ["only one"],
        ["1", "2", "3", "--b", "withflag"],
        ["--b", "onlyflagwithval"],
        ["--b"],
        ["a", "d", "--b"],
        ["a", "--b", "13"]
    ]

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a", nargs="*")
        parser.add_argument("--b", default="test")

        return parser


class VarPosAndKwReq(SignatureTestCase):
    @staticmethod
    def signature(*a, b):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a", nargs="*")
        parser.add_argument("--b", required=True)
        
        return parser

    inputs = [ 
        ["some", "positionals", "--b", "andb"],
        ["--b", "onlyB"],
        ["hello", "nob"],
        ["hello"],
    ]

class PositionalAndKwReq(SignatureTestCase):
    @staticmethod
    def signature(a, b, *, c):
        pass

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a")
        parser.add_argument("b")
        parser.add_argument("--c", required=True)

        return parser

    inputs = [
        ["hello", "world", "--c", "500"],
        ["hello", "world", "--c", "BIG-C"],
        ["hello", "world", "--c2"],
        ["onlyone"],
        ["hello", "world"],
        ["hello", "world", "thirdPosition"]
    ]


class PositionalAndKwReqOpt(SignatureTestCase):
    @staticmethod
    def signature(a, b, *, c, d=None):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a")
        parser.add_argument("b")
        parser.add_argument("--c", required=True)
        parser.add_argument("--d", default=None)
        
        return parser
    
    inputs = [ 
        ["a", "b", "--c", "c", "--d", "something"],
        ["a", "b", "--c", "c"],
        ["hello", "world", "--cC"],
        ["hello", "--c", "25", "--d", "something"],
        ["hello"],
        ["hello", "world"],
        ["hello", "world", "--d", "noC"]
    ]


class VarPosAndVarKw(SignatureTestCase):
    @staticmethod
    def signature(*args, **kwargs):
        pass


class VarPosAndKwReqAndVarKw(SignatureTestCase):
    @staticmethod
    def signature(*args, req, **kwargs):
        pass


testcases = [case for case in globals().values()]

# DATA = {
#     'success': (
#         (case.signature, case.get_reference_parser(), inputs)
#         for case in testcases
#         if aux.hasattrs(case, "signature", "get_reference_parser", "good_inputs")
#         for inputs in case.good_inputs
#     ),
#     'fail': (
#         (case.signature, case.get_reference_parser(), inputs)
#         for case in testcases
#         if aux.hasattrs(case, "signature", "get_reference_parser", "fail_inputs")
#         for inputs in case.fail_inputs
#     )
# }

DATA = (
    (case.signature, case.get_reference_parser(), inputs)
    for case in testcases
    if aux.hasattrs(case, "signature", "get_reference_parser", "inputs")
    for inputs in case.inputs + input_everywhere
)
