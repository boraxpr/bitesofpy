VOWELS = list('aeiou')
text = """Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms."""


def count_vowels(word):
    return len([v for v in word if v in VOWELS])


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    # print(type(text))
    words = text.lower().split(" ")
    words = [(word, count_vowels(word)) for word in words]
    return max(words,key=lambda x: x[1])


print(get_word_max_vowels(text))
