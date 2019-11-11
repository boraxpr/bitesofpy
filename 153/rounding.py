def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    values = []
    if up:
        for each in transactions:
            each = each + 1
            values.append(int(each))
    if not up:
        for each in transactions:
            values.append(int(each))
    return values


# print(round_up_or_down(transactions=[1.1, 2.2, 3.2, 4.7], up=True))
