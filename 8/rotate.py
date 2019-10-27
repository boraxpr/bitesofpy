def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    toAdd = ""
    if n == 0:
        return string
    elif n>0:
        for i in range(n):
            print("i " + i.__str__())
            toAdd = toAdd.__add__(string[0])
            print("Toadd " + toAdd)
            string = string.replace(string[0], "", 1)
            print("str " + string)
            # print(string)
        string = string+toAdd
        return string
    elif n<0:
        for i in range(abs(n)):
            print("i " + i.__str__())
            toAdd = string[len(string)-1]+toAdd
            print("Toadd " + toAdd)
            string = string.replace(string[len(string)-1], "",1)
            print("str " + string)
        string = toAdd+string
        return string

# print(rotate("hello",-2))
# print("zxc".__len__())
# print("zxc"[2])