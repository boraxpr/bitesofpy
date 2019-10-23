NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    nameset = set()
    for name in names:
        nameset.add(name.title())
    return list(nameset)

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    namelist = []
    # ...
    namedict = dict()
    for name in names:
        split = name.split(" ")
        namedict[split[1]] = split[0]
        namedictsorted = sorted(namedict.items(), reverse=1)
    for each  in namedictsorted:
        namelist.append(each[1]+" "+each[0])
    return namelist

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstnames = []
    # ...
    namedict = dict()
    for name in names:
        split = name.split(" ")
        namedict[split[1]] = split[0]
    for name in namedict.values():
        firstnames.append(str(name))
    return min(firstnames, key=len)

# dedup_and_title_case_names(NAMES)
# sort_by_surname_desc(NAMES)
# shortest_first_name(['brian okken', 'michael kennedy', 'trey hunner',
#                        'matt harrison', 'julian sequeira', 'dan bader',
#                        'michael kennedy', 'brian okken', 'dan bader'])