IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    # print(names[0])
    filtered_list = []
    for name in names:
        # print(name[0])
        checker = 0
        if IGNORE_CHAR.title() == name[0] or IGNORE_CHAR == name[0]:
            continue
        if QUIT_CHAR == name[0] or QUIT_CHAR.title() == name[0]:
            return filtered_list
        for char in name:
            if char.isdigit():
                checker = 1
                break
        if checker == 0:
            filtered_list.append(name)
        if name == names[-1] or names.index(name) == 5:
            return filtered_list


print(filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))