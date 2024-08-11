import time
from functools import wraps
from random import random


class timer:
    """decorator,print cost time"""

    def __init__(self, print_args):
        self.print_args = print_args

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
            print('time cost: {} seconds'.format(time.perf_counter() - st))
            return ret

        return decorated


@timer(print_args=True)
def random_sleep():
    time.sleep(random())


# _deco = timer(print_args=True)
# random_sleep = _deco(random_sleep)
random_sleep()
