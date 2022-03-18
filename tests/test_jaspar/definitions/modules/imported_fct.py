from argparse import ArgumentParser
from typing import get_type_hints
from warnings import warn

import jaspar


def test(msg=""):
    print("=== This is just a test ===")
    print(f"--- {msg} ---")


def _get_reference_parser():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    test_p = subparsers.add_parser("test")
    test_p.add_argument("--msg", default="")
    test_p.set_defaults(_func=test)

    return parser


INPUTS = [
    ["test"],
    ["test", "--msg=Hello"],
    ["test", "--msg", "'Hello World, it's me'"],

    ["warn"],
    ["warn", "somemsg"],
    ["get_type_hints"],
    ["test", "Message"]
]


def _nocmdforthat():
    pass


if __name__ == "__main__":
    jaspar.read_args()
