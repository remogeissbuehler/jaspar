
from argparse import ArgumentParser
import jaspar

def _print_args(*a, **kw):
    for arg in a:
        print(arg)
    for k, v in kw.items():
        print(f"{k}: {v}")


def main(source, dest="out/", silent=False, verbose=False):
    _print_args(source, dest, silent=silent, verbose=verbose) 


def _get_reference_parser():
    parser = ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--dest", default="out/")
    parser.add_argument("--silent", default=False)
    parser.add_argument("--verbose", default=False)
    parser.set_defaults(_func=main)

    return parser


INPUTS = [ 
    ["src/"],
    ["src/", "--dest=build/"],
    ["someSrc/", "--silent=True"],
    ["someSrc/", "--verbose=False", "--dest", "someplace"],

    ["someSrc/", "--verbose", "--dest", "someplace"],
    ["--dest", "/bin"]
]


if __name__ == "__main__":
    jaspar.read_args()