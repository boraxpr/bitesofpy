from operator import methodcaller
from distutils.version import StrictVersion

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    oldreqslines = old_reqs.split()
    newreqslines = new_reqs.split()
    oldreqs = {entry[0]: entry[1] for entry in map(methodcaller("split", "=="), oldreqslines)}
    newreqs = {entry[0]: entry[1] for entry in map(methodcaller("split", "=="), newreqslines)}
    upgradereqs = [entry[0] for entry in newreqs.items()
                   if StrictVersion(entry[1]) > StrictVersion(oldreqs[entry[0]])]
    return upgradereqs
