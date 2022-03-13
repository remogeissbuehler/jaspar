from enum import Enum


class PositionalOrKeywordMode(Enum):

    # tries to map the function parameter properties to CL arguments
    # as strictly as possible
    STRICT = 0,

    # tries to find a good compromise.
    # Namely, positional_or_keyword are treated as 
    #   - positional when they don't have a default (==> pos. arg)
    #   - keyword when they have a default (==> --flag arg)
    # 
    # Except if there are positional_only parameters present, in which 
    # case we assume the user explicitly wants to differentiate.
    # In that case they are treated as both.
    SMART_COMPROMISE = 1
