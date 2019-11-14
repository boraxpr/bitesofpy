def countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while True:
            yield num
            num -= 1
            if num < 1 or num > 100:
                raise StopIteration




