import time
from functools import wraps


def run_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('func: {} run time: {}'.format(func.__name__, end - start))
        return result

    return wrapper
