import distutils.util

def str2bool(s: str) -> bool:
    return bool(distutils.util.strtobool(s))