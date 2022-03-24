import argparse
from typing import Any, Sequence, Type, Union


# class StoreOnce(argparse.Action):
#     """Action to make sure the value gets set only once.

#     This action makes sure that if multiple arguments have the same destination
#     (typically "argument" and "--argument"), the value doesn't get overridden by the
#     other argument('s default).
    
#     Note: to prevent both arguments from being specified at the same time, use
#     a mutually exclusive group. This is just to prevent the second argument overrides
#     the first's value by its default.
#     """

#     def __call__(self, parser, namespace, values, option_string=None):
#         if getattr(namespace, self.dest, self.default) == self.default:
#             # only set if the value is currently the default
#             setattr(namespace, self.dest, values)


def _get_action(action: str) -> argparse.Action:
    container = argparse.ArgumentParser()
    return container._registry_get("action", action)


def StoreOnceWrapper(Action: Union[str, Type[argparse.Action]]):
    if isinstance(Action, str):
        Action = _get_action(Action)

    class _StoreOnceWrapped(Action):
        def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Union[str, Sequence[Any], None], option_string: Union[str, None] = ...) -> None:
            if getattr(namespace, self.dest, self.default) == self.default:
                super().__call__(parser, namespace, values, option_string)
    
    return _StoreOnceWrapped
        

StoreOnce = StoreOnceWrapper("store")
StoreTrueOnce = StoreOnceWrapper("store_true")
StoreFalseOnce = StoreOnceWrapper("store_false")