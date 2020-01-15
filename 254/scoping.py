num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    sum_of_numbers = sum(numbers)
    num_hundreds += sum_of_numbers // 100
    return sum_of_numbers


# sum_of_numbers, num_hundreds = sum_numbers()


