def countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while True:
        yield num
        num -= 1
        if num == 100 or num == 0:
            return



