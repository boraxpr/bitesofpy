def get_ordinal_suffix(number):
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    suffixes = {0: "th", 1: "st", 2: "nd", 3: "rd", 4:"th", 5:"th"
        , 6:"th", 7:"th", 8:"th", 9:"th", 11: "th", 12: "th", 13:"th"}
    #For teen numbers exceptions 11,12,13
    if number == 11 or number == 12 or number == 13:
        return str(number) + suffixes.get(number)
    #For 111,1111,11111...
    elif number % 100 == 11:
        return str(number) + suffixes.get(number % 100)
    #For all other numbers
    elif number % 10 in suffixes.keys():
        return str(number) + suffixes.get(number % 10)

