from typing import Callable


def add_data_to_fct(**kwargs):
    """Adds data to a function.

    For every key in the kwargs dictionary, a corresponding key with an underscore _ prepended will be added
    to the function object.

    Example:
    @_add_data_to_fct(input=["hello", "world"])
    def somefunction(somearg):
        pass

    will set somefunction._input = ["hello", "world"]
    """
    def decorator(function: Callable):
        for key in kwargs:
            setattr(function, "_" + key, kwargs[key]) 
            
        return function
    
    return decorator

def hasattrs(obj, *attrs):
    for attr in attrs:
        if not hasattr(obj, attr): return False

    return True