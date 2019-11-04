IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    # print(names[0])
    filtered_list = []
    for name in names:
        # print(name[0])
        namekun = list(name)
        # checker = 0
        if IGNORE_CHAR.title() == name[0] or IGNORE_CHAR == name[0]:
            continue
        if QUIT_CHAR == name[0]:
            return filtered_list
        if any(char.isdigit() for char in name):
            continue
        filtered_list.append(name)

    return filtered_list.__str__()


print(filter_names(['t1im', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))