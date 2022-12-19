from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    numbers = Counter(numbers)
    # you code ...
    return numbers.most_common()[0][0], numbers.most_common()[-1][0]
