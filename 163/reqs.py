from operator import methodcaller
from packaging import version

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
                   if version.parse(entry[1]) > version.parse(oldreqs[entry[0]])]
    return upgradereqs


other_old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
other_new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""
changed_dependencies(other_old_reqs, other_new_reqs)
