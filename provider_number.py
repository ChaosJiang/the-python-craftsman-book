import random

import wrapt as wrapt


def provide_number(min_num, max_num):
    """ decorator, randomly generate a number between [min_num, max_num]"""

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            return func(num, *args, **kwargs)

        return decorated

    return wrapper


@provide_number(1, 100)
def print_random_number(num):
    print(num)


print_random_number()
