def sum_numbers(numbers=None):

    if numbers is None:
        numbers = [i+1 for i in range(100)]
        # print(numbers)
        # print(sum(numbers))
        return sum(numbers)
    else:
        return sum(numbers)
# sum_numbers(None)



