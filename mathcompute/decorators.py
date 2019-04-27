import functools
import time


def time_calc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ans = func(*args, **kwargs)
        end = time.time()
        return (end - start), ans, func.__name__

    return wrapper
