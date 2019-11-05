from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if list1 is list2:
        return Equality.SAME_REFERENCE

    if list1 == list2:
        return Equality.SAME_ORDERED

    if not list1 == list2 and sorted(list1) == sorted(list2):
        return Equality.SAME_UNORDERED
    set1 = set(list1).__reduce__()
    set2 = set(list2).__reduce__()
    if set1 == set2:
        return Equality.SAME_UNORDERED_DEDUPED
    return Equality.NO_EQUALITY

# check_equality([],[])
# set1 = set([3,2,2,2,2,2])
# print(set1)