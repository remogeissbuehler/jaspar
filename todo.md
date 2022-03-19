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
- [ ] maybe add support for config via custom jaspar type hints / general types
```python
from jaspar.typehintconfig import NotRequired, Action, Choice
from typing import Literal

class MyCustomAction(argparse.Action):
    ...

def foo(bar: NotRequired[str], 
        baz: Action[MyCustomAction],
        greeting: Choice("hello", "goodbye"),
        name: Literal["Alice", "Bob"]):
    pass
```

## 'UX'
- [ ] add support for global / local config changes
  - [ ] choose between strict / smart parsing mode
- [ ] autoparse function docstrings to provide helpstrings

# Code Quality
- [ ] refactor `jaspar.__init__.py` and the parser