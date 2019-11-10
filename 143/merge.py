NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    age = dict()
    for element in group1:
        if element == name.lower():
            age['group1'] = group1[name]
    for element in group2:
        if element == name.lower():
            age['group2'] = group2[name]
    for element in group3:
        if element == name.lower():
            age['group3'] = group3[name]
    age = sorted(age.items(), reverse=True)
    return age[0][1]

# print(get_person_age("ana"))
