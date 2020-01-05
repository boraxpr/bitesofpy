wordsx = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
words = ['abc55', 'B1te', 'hope', 'how4', 'it', "Let's", 'see', 'this', 'this', 'works', '1sorts,', '22', '4', '55abc']


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # numbers = list()
    words.sort(key=lambda x: x.lower())
    words.sort(key=lambda x: x[0].isdigit())
    # for key, word in enumerate(words):
    #     if word[0].isdigit():
    #         numbers.append(word)
    #         words.pop(key)
    return words


print(sort_words_case_insensitively(words))