def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    words = [word1, word2]

    def lower_replace(word: str):
        return word.replace(" ", "").lower()
    words = list(map(lower_replace, words))
    if len(words[0]) != len(words[1]):
        return False
    char_sets = [set(word) for word in words]
    return char_sets[0] == char_sets[1]
