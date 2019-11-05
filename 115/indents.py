def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    counts = 0
    for char in text:
        if char.isspace() and char != "\t" and char !="\n":
            counts += 1
        elif char.isalpha():
            break
    return counts

# print(count_indents("\t\toxzcxc"))
# "ddd dd dd".