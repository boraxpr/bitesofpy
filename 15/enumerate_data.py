names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for key, name in enumerate(names):
        outputkey = key + 1
        print(str(outputkey)+". "+"{:11}{}".format(names[key], countries[key]))


# enumerate_names_countries()