import string


def simple_calculator(calculation:str):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    num1, operator, num2 = calculation.split(" ")
    if not num1.lstrip("-").isdigit() and not num2.lstrip("-").isdigit():
        raise ValueError
    if operator == "+":
        return int(num1)+int(num2)
    elif operator == "-":
        return int(num1)-int(num2)
    elif operator == "*":
        return int(num1)*int(num2)
    elif operator == "/" and num2 == "0":
        # return float(num1)/float(num2)
        raise ValueError
    elif operator == "/" and num2 != "0":
        return round(float(num1)/float(num2),ndigits=2)
    else:
        raise ValueError

