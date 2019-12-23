import decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    d = decimal.Decimal(number).quantize(decimal.Decimal('1.'), rounding=decimal.ROUND_HALF_EVEN)
    return d

# print(round_even(3.5))