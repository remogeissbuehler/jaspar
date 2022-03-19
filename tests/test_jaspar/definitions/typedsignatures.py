"""Function signatures for tests
"""
from argparse import ArgumentParser

from .. import aux
from .basicsignatures import SignatureTestCase
import jaspar.types as jT


input_everywhere = [
    [],
]

class BasicNumbers(SignatureTestCase):
    @staticmethod
    def signature(num: int, pi=3.14):
        pass

    inputs = [
        ["15"],
        ["3", "--pi=0.5"],
        ["-5"],
        ["--pi", "3", "0"],

        ["1.5"],
        ["5", "--pi=hello"]
    ]

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("num", type=int)
        parser.add_argument("--pi", type=float, default=3.14)

        return parser


class BasicBoolFlags(SignatureTestCase):
    @staticmethod
    def signature(some_flag=True, verbose=False):
        pass

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("--some-flag", action="store_true", dest="some_flag")
        parser.add_argument("--no-some-flag", action="store_false", dest="some_flag")
        parser.set_defaults(some_flag=True)

        parser.add_argument("--verbose", action="store_true", dest="verbose")
        parser.add_argument("--no-verbose", action="store_false", dest="verbose")
        parser.set_defaults(verbose=False)

        return parser

    inputs = [ 
        ["--some-flag"],
        ["--no-some-flag"],
        ["--verbose"],
        ["--no-verbose"],
        ["--no-some-flag", "--verbose"]
    ]

class BoolPositional(SignatureTestCase):
    @staticmethod
    def signature(exec: bool):
        pass 

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("exec", type=jT.str2bool)

        return parser 

    inputs = [ 
        ["True"], ["yes"], ["on"],
        ["False"], ["no"], ["off"]
    ]

class BoolKwRequired(SignatureTestCase):
    @staticmethod
    def signature(*, required_flag: bool):
        pass

    @staticmethod
    def get_reference_parser():
        parser = ArgumentParser()
        parser.add_argument("--required-flag", required=True, type=jT.str2bool)

        return parser
        

testcases = [case for case in globals().values()]


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
