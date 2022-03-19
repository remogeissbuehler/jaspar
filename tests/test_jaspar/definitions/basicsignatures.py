"""Function signatures for tests
"""
from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty, abstractstaticmethod
from argparse import ArgumentParser
import inspect
import itertools

from .. import aux
import jaspar.actions as A

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
        ["hello", "world", "--with-a-flag"],
        ["--a", "helloA", "--b", "helloB"]
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
        parser.add_argument("a", nargs="+")

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
        parser.add_argument("a", nargs="+")
        parser.add_argument("--b", default="test")

        return parser


class VarPosAndKwReq(SignatureTestCase):
    @staticmethod
    def signature(*a, b):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("a", nargs="+")
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
        # TODO: think abou this case. maybe a and b should be positional and kw since there is an explicit kw-only in the signature?
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
    # TODO: think about what this should do
    @staticmethod
    def signature(*args, **kwargs):
        pass


class VarPosAndKwReqAndVarKw(SignatureTestCase):
    # TODO: think about what this should even do
    @staticmethod
    def signature(*args, req, **kwargs):
        pass


class PositionalOnly(SignatureTestCase):
    @staticmethod
    def signature(pos, /):
        pass

    inputs = [
        ["positional"],
        ["now", "two"],
        ["--positional", "thisiswrong"],
        ["--positional"]
    ]

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("pos")

        return parser


class PositionalAndOptPos(SignatureTestCase):
    @staticmethod
    def signature(source, dest="out/", /):
        pass

    inputs = [
        ["src", "dest"],
        ["onlySrc"],
        ["someSrc", "--dest", "someDest"],
    ]

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("source")
        parser.add_argument("dest", nargs="?", default="out/")

        return parser

class PositionalOptPosAndKw(SignatureTestCase):
    @staticmethod
    def signature(source, dest="out/", /, opt=25, *, kwonly, kwonly_opt="alreadythere"):
        pass 

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("source")
        parser.add_argument("dest", nargs="?", default="out/")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("opt", nargs="?", default=25, action=A.StoreOnce)
        group.add_argument("--opt", default=25, action=A.StoreOnce)

        parser.add_argument("--kwonly", required=True)
        parser.add_argument("--kwonly-opt", default="alreadythere")

        return parser
    
    inputs = [ 
        ["src/", "build/", "13", "--kwonly", "test"],
        ["src/", "build/", "13", "--kwonly", "test", "--kwonly-opt", "1"],
        ["src/", "build/", "--opt=17", "--kwonly", "test", "--kwonly-opt", "1"],
        ["src/", "--opt=17", "--kwonly", "test", "--kwonly-opt", "1"],
        ["src/", "--kwonly", "test"],

        # negative examples
        ["--opt", "52", "--kwonly", "sthelse"],
        ["src/", "dest/"],
        ["src/", "--dest=build/", "--opt", "17", "--kwonly=5"]
    ]

class PositionalOnlyAndOptPositionalOrKw(SignatureTestCase):
    @staticmethod
    def signature(source, /, dest="out/"):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("source")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("dest", nargs="?", default="out/", action=A.StoreOnce)
        group.add_argument("--dest", default="out/", action=A.StoreOnce)

        return parser

    inptus = [ 
        ["src/", "build/"],
        ["src/"],
        ["src/", "--dest=build/"],
        ["--dest=build/", "home"],
        ["--dest", "dist/", "src"],

        ["src", "build", "--dest=sthelse"],
        ["--dest", "build", "source", "--dest", "anotherbuild"]
    ]

class PositionalOnlyAndOptKw(SignatureTestCase):
    @staticmethod
    def signature(source, /, *, dest="out/"):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("source")

        parser.add_argument("--dest", default="out/")

        return parser

    inptus = [ 
        ["src/", "build/"],
        ["src/"],
        ["src/", "--dest=build/"],
        ["--dest=build/", "home"],
        ["--dest", "dist/", "src"],

        ["src", "build", "--dest=sthelse"],
        ["--dest", "build", "source", "--dest", "anotherbuild"]
    ]

class PostionalOnlyAndPositionalOrKw(SignatureTestCase):
    @staticmethod
    def signature(source, /, dest):
        pass

    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("source")

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("dest", nargs="?", action=A.StoreOnce)
        group.add_argument("--dest", action=A.StoreOnce)

        return parser

    inptus = [ 
        ["src/", "build/"],
        ["src/"],
        ["src/", "--dest=build/"],
        ["--dest=build/", "home"],
        ["--dest", "dist/", "src"],

        ["src", "build", "--dest=sthelse"],
        ["--dest", "build", "source", "--dest", "anotherbuild"]
    ]



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


def get_data(inputs=True):
    if inputs:
        return (
            (case.signature, case.get_reference_parser(), inputs)
            for case in testcases
            if aux.hasattrs(case, "signature", "get_reference_parser", "inputs")
            for inputs in case.inputs + input_everywhere
        )
    else:
        return (
            (case.signature, case.get_reference_parser())
            for case in testcases
            if aux.hasattrs(case, "signature", "get_reference_parser") and case.get_reference_parser() is not None

        )
