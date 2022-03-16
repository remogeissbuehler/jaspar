
import jaspar

def _print_args(*a, **kw):
    for arg in a:
        print(arg)
    for k, v in kw.items():
        print(f"{k}: {v}")

def main(source, dest="out/", *, silent=False, verbose=False):
    _print_args(source, dest, silent=silent, verbose=verbose) 


if __name__ == "__main__":
    jaspar.read_args()