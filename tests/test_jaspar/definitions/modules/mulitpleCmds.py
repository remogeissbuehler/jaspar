def test():
    print("=== This is just a test ===")

def repeat(n: int, horizontal=False):
    text = "Repeat"
    if horizontal:
        text = n * text
    for _ in range(n):
        print("Repeated!")

def _nocmdforthat():
    pass

