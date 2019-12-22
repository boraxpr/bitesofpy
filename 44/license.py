import secrets
import string


def gen_key(parts=4, chars_per_part=8):
    key = ""
    for part in range(parts):
        # print(part.__str__() + " " + parts.__str__())
        p = ""
        for char in range(chars_per_part):
            c = secrets.choice(string.ascii_uppercase+string.digits)
            p = p + c
        if part != parts-1:
            p = p + "-"
        key = key + p
    return key


print(gen_key())