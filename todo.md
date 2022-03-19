#  TODOs

# Testing
- [ ] more extensive tests

# Features
## Module parsing
- [ ] define and make multiple function with main setup work

## Function signature support
- [ ] add support for type annotations
- [ ] add default behaviour for bools (store_true)
- [ ] add support for `**kwargs` varargs (via custom action)
- [ ] maybe add support for config via custom jaspar type hints:
```python
from jaspar.typehintconfig import NotRequired, Action

class MyCustomAction(argparse.Action):
    ...

def foo(bar: NotRequired[str], baz: Action[MyCustomAction]):
    pass
```

## 'UX'
- [ ] add support for global / local config changes
  - [ ] choose between strict / smart parsing mode

# Code Quality
- [ ] refactor `jaspar.__init__.py` and the parser