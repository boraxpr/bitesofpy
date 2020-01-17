from functools import reduce


def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    listoflang = [programmers[dev] for dev in programmers]
    return reduce(set.intersection, map(set, listoflang))

# print(common_languages(dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
#                 tim=['Python', 'Haskell', 'C++', 'JS'],
#                 sara=['Perl', 'C', 'Java', 'Python', 'JS'],
#                 paul=['C++', 'JS', 'Python'])))