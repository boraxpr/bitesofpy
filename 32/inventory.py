import copy
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    items_copy = copy.deepcopy(items)
    return items_copy[:]

# duplicate_items(items)