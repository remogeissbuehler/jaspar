import jaspar 

@jaspar.config(
    args = {
        'required': True
    }
)
def somefunction(*args):
    pass

@jaspar.config(
    source = {
        'nargs': '+',
        'default': "src/"
    },
    target = {
        'default': "out/"
    }
)
def anotherfunction(source, target=None):
    pass

if __name__ == "__main__":
    print(jaspar._configs)