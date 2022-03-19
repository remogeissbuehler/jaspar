from argparse import ArgumentParser
import warnings
import jaspar

import jaspar.actions as A

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

    # TODO: adapt for new typing specs

    parser = ArgumentParser()

    subp = parser.add_subparsers(required=True, dest="_command") 
    
    copy_ = subp.add_parser("copy")
    copy_.add_argument("source")
    copy_.add_argument("dest", nargs="?", default="copy")

    g1 = copy_.add_mutually_exclusive_group(required=False)
    g1.add_argument("both", nargs="?", default=False, action=A.StoreOnce)
    g1.add_argument("--both", default=False, action=A.StoreOnce)

    copy_.add_argument("--recursive", required=True)
    copy_.add_argument("--verbose", default=False, required=False)
    copy_.set_defaults(_func=copy)
    
    repeat_ = subp.add_parser("repeat")
    repeat_.add_argument("n")
    repeat_.add_argument("--horizontal", default=False)
    repeat_.set_defaults(_func=repeat)

    test_ = subp.add_parser("test")
    test_.set_defaults(_func=test)

    return parser

# TODO: fix inputs here
test_inputs = [
    ["test"],

    ["test", "--with-a-flag"]
]

repeat_inputs = [ 
    ["repeat", "5"],
    ["repeat", "--horizontal=True", "7"],
    ["repeat", "3", "--horizontal", "True"],

    ["repeat"]
]


copy_inputs = [ 
    ["copy", "src", "--recursive=False"],
    ["copy", "src", "dst", "--recursive", "True"],
    ["copy", "src", "--both", "True", "--recursive=1"],
    ["copy", "src", "dst", "both", "--recursive", "False"],

    ["copy", "src", "--dest", "somePlace", "--recursive"],
    ["copy", "src"]
]


gen_inputs = [
    ["src", "dest"],
    ["25"],
    ["_nocmdforthat"]
]

INPUTS = test_inputs + repeat_inputs + copy_inputs + gen_inputs


def _nocmdforthat():
    pass

if __name__ == "__main__":
    jaspar.read_args()