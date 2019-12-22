def get_profile(**kwargs):
    # print(kwargs.__len__())
    if 'name' in kwargs and 'profession' in kwargs and kwargs.__len__() == 2:
        name = kwargs['name']
        profession = kwargs['profession']
        return str(name + " is a " + profession)
    elif 'name' in kwargs and 'profession' in kwargs and kwargs.__len__() != 2:
        raise TypeError
    elif 'name' not in kwargs and 'profession' not in kwargs and kwargs.__len__() != 0:
        raise TypeError
    elif 'name' in kwargs and 'profession' not in kwargs:
        name = kwargs['name']
        return str(name + " is a " + "programmer")
    elif 'name' not in kwargs and 'profession' in kwargs:
        profession = kwargs['profession']
        return str("julian" + " is a " + profession)
    elif 'name' not in kwargs and 'profession' not in kwargs and kwargs.__len__() == 0:
        return str("julian is a programmer")
    else:
        raise TypeError


# print(get_profile(name="z", profession="z", flag="d"))