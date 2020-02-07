from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*numbers):

        num_checker = [type(num) for num in numbers if num > 0]
        set_length = len(set(num_checker))

        #If there is more than 1 type in the arguements then raise TypeError
        if set_length > 1:
            raise TypeError
        #If there is some number < 0 then raise ValueError
        if len([*numbers]) != len(num_checker):
            raise ValueError
        return func(*numbers)
    return wrapped

    # complete this decorator
