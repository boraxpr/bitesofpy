def positive_divide(numerator, denominator):
    if type(numerator) != int and type(denominator) != int:
        raise TypeError
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        return 0
    if result < 0:
        raise ValueError
    return result