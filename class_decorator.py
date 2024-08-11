import functools
import time
from functools import update_wrapper


class DelayStart:

    def __init__(self, func, *, duration=1):
        update_wrapper(self, func)
        self.func = func
        self.duration = duration

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} second before starting...')
        time.sleep(1)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delayed_start(**kwargs):
    return functools.partial(DelayStart, **kwargs)


@delayed_start(duration=2)
def hello():
    print('Hello, World.')

# print(hello)
# print(type(hello))
# print(hello.__name__)
hello()
# hello.eager_call()