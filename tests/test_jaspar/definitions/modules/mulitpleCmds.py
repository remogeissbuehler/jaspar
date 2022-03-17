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

def _nocmdforthat():
    pass

if __name__ == "__main__":
    jaspar.read_args()