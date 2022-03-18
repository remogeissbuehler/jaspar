import jaspar


def default(*args, verbose=False):
    if verbose:
        print(*args)
    

if __name__ == "__main__":
    jaspar.read_args()