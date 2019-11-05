def get_index_different_char(chars):
    result = []
    Al = 0
    nonAl = 0
    for char in chars:
        char = str(char)
        if char.isalnum():
            # result.append(chars.index(char))
            Al += 1
            if Al > 1:
                break
        else:
            nonAl += 1
            if nonAl > 1:
                break
    # print(Al.__str__()+" "+nonAl.__str__())
    if Al == 2:
        for char in chars:
            charS = str(char)
            if not charS.isalnum():
                result.append(chars.index(char))
    else:
        for char in chars:
            charS = str(char)
            if charS.isalnum():
                result.append(chars.index(char))
    return result


print(get_index_different_char(
        [2, '.', ',', '!']))
#
# A = ["1","3","A"]
# print(A.index("A"))
