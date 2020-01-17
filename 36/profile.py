def get_profile(name, age, *args,**kwargs):
    if type(age) != int:
        raise ValueError
    if len(args) > 5:
        raise ValueError
    result = dict()
    sports = list()
    awards = dict()
    if len(args) != 0:
        for sport in args:
            sports.append(sport)
        sports.sort()
        result.update({'sports': sports})

    if len(kwargs) != 0:
        result.update({'awards': awards})
        for award in kwargs:
            result['awards'].update({award: kwargs[award]})
    result.update({'name':name, 'age':age})
    return result
print(get_profile("jeff", 3))