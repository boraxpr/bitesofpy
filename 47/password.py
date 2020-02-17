import re
import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    length_check = len(password) in range(6, 13)
    digit_check = any([char.isdigit() for char in password])
    lower_check = len([char for char in password if char.islower()]) >= 2
    upper_check = any([char.isupper() for char in password])
    punctuation_check = any([char for char in password if char in PUNCTUATION_CHARS])
    # re.escape is used in case of there is an re metacharacters in password
    # Metacharacters include . ^ $ * + ? { } [ ] \ | ( )
    # In this exercise, Regex is needed because used_passwords,
    # even when converted to string, contain brackets, commas and quotations
    # just like a set ex.{'PassWord@1', 'PyBit$s9'}
    r = re.findall(re.escape(password), str(used_passwords))
    used_check = not any(r)
    if all([length_check, digit_check, lower_check, upper_check, punctuation_check, used_check]):
        used_passwords.add(password)
        return True
    else:
        return False


