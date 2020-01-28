def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""

    # list of the words that occurs more than once
    duplicated = [word for word in set(words) if words.count(word) > 1]
    # list of first occurence position of duplicated words
    pos = [words.index(dupword) for dupword in duplicated]
    return sorted(pos)