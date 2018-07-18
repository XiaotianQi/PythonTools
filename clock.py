import time
import functools

def clock(func):
    @functools.wraps
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, v) for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) --> %r' % (t1, name, arg_str, result))
        return result
    return clocked