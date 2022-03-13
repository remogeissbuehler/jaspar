
import jaspar

def _print_args(*a, **kw):
    for arg in a:
        print(a)
    for k, v in kw.items():
        print(f"{k}: {v}")

def main(source, dest="out/", *, silent=False, verbose=False):
    _print_args(source, dest, silent=silent, verbose=verbose) 