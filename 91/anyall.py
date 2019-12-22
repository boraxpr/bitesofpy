import string

VOWELS = 'aeiou'
PYTHON = 'python'

# print("ee".__len__())


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    input_str = str(input_str)
    input_str = input_str.lower()
    str_len = input_str.__len__()
    ccount = 0

    for char in input_str:
        if char in VOWELS:
            ccount += 1
    if ccount == str_len:
        return True
    else:
        return False


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    input_str = str(input_str)
    input_str = input_str.lower()
    str_len = input_str.__len__()
    ccount = 0

    for char in input_str:
        if char in PYTHON:
            ccount += 1
    if ccount != 0:
        return True
    else:
        return False
    pass


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    input_str = str(input_str)
    str_len = input_str.__len__()
    ccount = 0

    for char in input_str:
        if char in string.digits:
            ccount += 1
    if ccount != 0:
        return True
    else:
        return False