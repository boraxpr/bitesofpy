import string


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    nonasciis = list()
    for word in str(text).split(" "):
        for ch in word:
            if ch not in string.ascii_letters and ch not in string.punctuation and ch not in string.digits:
                nonasciis.append(word)
                break

    return nonasciis


print(extract_non_ascii_words("An preost wes on leoden, Laȝamon was ihoten"))
