def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if type(value) is not float and type(value) is not int:
        raise TypeError
    if fmt != "cm" and fmt != "in":
        raise ValueError
    if fmt == "cm":
        r = value*2.54
        return r.__round__(4)
    elif fmt == "in":
        r = value/2.54
        return r.__round__(4)
