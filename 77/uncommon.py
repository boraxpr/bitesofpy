def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    checker = 0
    for my_city in my_cities:
        for other_city in other_cities:
            if my_city == other_city:
                checker += 1
    return my_cities.__len__() - checker + other_cities.__len__() - checker


# print(uncommon_cities(['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin'],
#                       ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']))
