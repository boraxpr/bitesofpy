cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    all_jeeps = []
    # print(cars['Jeep'][0])
    for car in cars['Jeep']:
        all_jeeps.append(car)
    all_jeeps = ", ".join(all_jeeps)
    return all_jeeps


# print(get_all_jeeps(cars))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = list()
    for car in cars.keys():
        first_model.append(cars[car][0])
    return first_model

# print(get_first_model_each_manufacturer(cars))


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    match = list()
    for manufacturer in cars.keys():
        for car in cars[manufacturer]:
            if grep.lower() in car.lower():
                match.append(car)
    return sorted(match)
# print(get_all_matching_models(grep='CO'))


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for manufacturer in cars.keys():
        cars[manufacturer] = sorted(cars[manufacturer])
    return cars

# print(sort_car_models())
