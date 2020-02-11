import secrets
import string


def gen_key(parts=4, chars_per_part=8):
    key = []
    for part in range(parts):
        p = ""
        for char in range(chars_per_part):
            c = secrets.choice(string.ascii_uppercase+string.digits)
            p = p + c
        key.append(p)

    return "-".join(key)


print(gen_key())