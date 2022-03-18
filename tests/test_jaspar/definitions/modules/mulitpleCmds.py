from argparse import ArgumentParser
import warnings
import jaspar

def test():
    print("=== This is just a test ===")

def repeat(n: int, horizontal=False):
    # TODO: make automatic int parsing work
    # TODO: make automatic bool parsing work
    if isinstance(n, str):
        warnings.warn("n is string!!")
        n = int(n)
    text = "Repeat"
    if horizontal:
        text = n * text
    for _ in range(n):
        print(text)


def copy(source, dest="copy", /, both=False, *, recursive, verbose=False):
    if verbose:
        print("COPYING")
    if recursive:
        print("in order to understand recursion, one must understand recursion")
    
    print(f"copying from {source} to {dest}")


def _get_reference_parser():
    parser = ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest", nargs="?", default="copy")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("both", nargs="?", default=False)
    group.add_argument("--both", required=False, default=False)

    parser.add_argument("--recursive", required=True)
    parser.add_argument("--verbose", default=True)

    return parser


INPUTS = [ 
    ["src", "--recursive=False"],
    ["src", "dst", "--recursive", "True"],
    ["src", "--both", "True", "--recursive=1"],
    ["src", "dst", "both", "--recursive", "False"],

    ["src", "--dest", "somePlace", "--recursive"],
    ["src"]
]


def _nocmdforthat():
    pass

if __name__ == "__main__":
    jaspar.read_args()