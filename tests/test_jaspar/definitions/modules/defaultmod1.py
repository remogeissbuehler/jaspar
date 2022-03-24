from tabnanny import verbose
import jaspar
from argparse import ArgumentParser


INPUTS = [
    ["source", "--verbose"],
    ["arg1", "arg2", "--no-verbose"],
    ["xyz", "anotherone"],
    ["--verbose"],

    ["--verbose", "True"],
    ["--verbose=True", "abc", "def"],
    ["1", "2", "3", "--verbose=False"],
]


def default(*args, verbose=False):
    if verbose:
        print(*args)


def _get_reference_parser():
    parser = ArgumentParser()
    parser.add_argument("args", nargs="+")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", action='store_true', dest='verbose')
    group.add_argument("--no-verbose", action="store_false", dest='verbose')
    
    parser.set_defaults(verbose=False)
    parser.set_defaults(_func=default)

    return parser
    

if __name__ == "__main__":
    jaspar.read_args()