from argparse import ArgumentParser
import jaspar

def main(source="src", target="out/", verbose=False):
    # TODO: disallow positional arguments for main if there are subcommands,
    #       as they clash with each other.
    if verbose:
        print("==  Function Main  ==")
        print(" Argument values:")
    print(f"{source=}")
    print(f"{target=}")

    if verbose:
        print("==/ Function Main /==")

# def main():
#     print("== Function Main == ")


def show(file):
    print(f"-------------------{file}---------------------------------")
    with open(file, "r") as f:
        for line in f:
            print(line, end='')
        print()
    print(f"-----------------------------------------------------" + (len(file) * "-"))


def create(file, show_file=False):
    with open(file, "x"):
        file.write("This was newly created")
        print("File created")
    if show_file:
        show(file)


def _get_reference_parser():
    return None


INPUTS = [ 
    ["someSrc/"],
    ["someSrc/", "--target=build"],
    ["someSrc/", "--verbose", "False"],
    ["show", "~/.zshrc"],
    ["create", "/tmp/atempfile.txt"],
    ["create", "/tmp/btempfile.txt", "--show-file=True"],

    ["someSrc", "--target=.", "--show-file=False"],
    ["show", "--verbose=True"],
    [""]
]

if __name__ == "__main__":
    jaspar.read_args()