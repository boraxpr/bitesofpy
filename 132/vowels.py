VOWELS = list('aeiou')
text="""Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms."""

def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    # print(type(text))
    words = []
    for line in text.splitlines():
        line = [word.lower() for word in line.split(" ") if len(word) > 0]
        words.append(line)
    listofwords = []
    for list in words:
        listofwords += list
    result = []
    for word in listofwords:
        point = 0
        for ch in word:
            if ch in VOWELS:
                point+=1
        result.append((word,point))
    result.sort(key=lambda x:x[1])
    return result[-1]

print(get_word_max_vowels(text))
