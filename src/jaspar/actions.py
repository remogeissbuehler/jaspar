import argparse

class StoreOnce(argparse.Action):
    """Action to make sure the value gets set only once.

    This action makes sure that if multiple arguments have the same destination
    (typically "argument" and "--argument"), the value doesn't get overridden by the
    other argument('s default).
    
    Note: to prevent both arguments from being specified at the same time, use
    a mutually exclusive group. This is just to prevent the second argument overrides
    the first's value by its default.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        print(namespace, values)
        if getattr(namespace, self.dest, self.default) == self.default:
            # only set if the value is currently the default
            setattr(namespace, self.dest, values)