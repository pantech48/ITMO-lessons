from collections import namedtuple


def return_namedtuple(*args):
    Named = namedtuple('Named', args)
    def decorator(func):
        def wrapper(*args, **kwargs):
            var_func = func(*args, **kwargs)
            if isinstance(var_func, tuple):
                return Named(*var_func)
            return var_func
        return wrapper
    return decorator

