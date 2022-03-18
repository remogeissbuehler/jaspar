import jaspar
from argparse import ArgumentParser


INPUTS = [
    ["--verbose", "True"],
    ["1", "2", "3", "--verbose=False"],
    ["--verbose=True", "abc", "def"],
    ["xyz", "anotherone"],

    ["source", "--verbose"],
]


def default(*args, verbose=False):
    if verbose:
        print(*args)


def _get_reference_parser():
    parser = ArgumentParser()
    parser.add_argument("args", nargs="+")
    parser.add_argument("--verbose", default=False)

    return parser
    

if __name__ == "__main__":
    jaspar.read_args()