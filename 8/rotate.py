def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    toAdd = ""
    if n == 0:
        return string
    elif n>0:
        if n > len(string):
            return string
        for i in range(n):
            # print("i " + i.__str__())
            toAdd = toAdd + string[0]
            # print("Toadd " + toAdd)
            string = string[1 : :]
            # print("str " + string)
            # print(string)
        string = string+toAdd
        return string
    elif n<0:
        for i in range(n, 0 , 1):
            # print("i " + i.__str__())
            toAdd = string[len(string)-1] + toAdd
            # print("Toadd " + toAdd)
            string = string[: -1 :]
            # print("str " + string)
        # print(toAdd)
        string = toAdd+string
        return string

# print(rotate("hello", -2))
# print("zxc".__len__())
# print("zxc"[2])