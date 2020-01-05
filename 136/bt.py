"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}

# print(Bloodtype.A_NEG.value)
# complete :

# print(type(Bloodtype.AB_POS.value))


def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """

    if type(donor) is int and type(recipient) is int:
        if donor not in [0, 1, 2, 3, 4, 5, 6, 7] or recipient not in [0, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        elif donor == Bloodtype.ZERO_NEG.value:
            return True
        elif donor == Bloodtype.ZERO_POS.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.A_POS.value, Bloodtype.B_POS.value, Bloodtype.ZERO_POS.value]:
            return True
        elif donor == Bloodtype.B_NEG.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.AB_NEG.value, Bloodtype.B_POS.value, Bloodtype.B_NEG.value]:
            return True
        elif donor == Bloodtype.B_POS.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.B_POS.value]:
            return True
        elif donor == Bloodtype.A_NEG.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.AB_NEG.value, Bloodtype.A_POS.value, Bloodtype.A_NEG.value]:
            return True
        elif donor == Bloodtype.A_POS.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.A_POS.value]:
            return True
        elif donor == Bloodtype.AB_NEG.value and recipient in [Bloodtype.AB_POS.value, Bloodtype.AB_NEG.value]:
            return True
        elif donor == Bloodtype.AB_POS.value and recipient == Bloodtype.AB_POS.value:
            return True
        else:
            return False
    elif type(donor) is str and type(recipient) is str:
        if donor not in blood_type_text.keys() or recipient not in blood_type_text.keys():
            raise ValueError
        elif donor == "0-":
            return True
        elif donor == "0+" and recipient in ["AB+", "A+", "B+", "0+"]:
            return True
        elif donor == "B-" and recipient in ["AB+", "AB-", "B+", "B-"]:
            return True
        elif donor == "B+" and recipient in ["AB+", "B+"]:
            return True
        elif donor == "A-" and recipient in ["AB+", "AB-", "A+", "A-"]:
            return True
        elif donor == "A+" and recipient in ["AB+", "A+"]:
            return True
        elif donor == "AB-" and recipient in ["AB+", "AB-"]:
            return True
        elif donor == "AB+" and recipient == "AB+":
            return True
        else:
            return False
    elif type(donor) is Bloodtype and type(recipient) is Bloodtype:
        if donor not in blood_type_text.values() or recipient not in blood_type_text.values():
            raise ValueError
        elif donor == blood_type_text.get("0-"):
            return True
        elif donor == blood_type_text.get("0+") and recipient in [blood_type_text.get("AB+"), blood_type_text.get("A+"),
                                                                  blood_type_text.get("B+"), blood_type_text.get("O+")]:
            return True
        elif donor == blood_type_text.get("B-") and recipient in [blood_type_text.get("AB+"),
                                                                  blood_type_text.get("AB-"),
                                                                  blood_type_text.get("B+"),
                                                                  blood_type_text.get("B-")]:
            return True
        elif donor == blood_type_text.get("B+") and recipient in [blood_type_text.get("AB+"),
                                                                  blood_type_text.get("B+")]:
            return True
        elif donor == blood_type_text.get("A-") and recipient in [blood_type_text.get("AB+"),
                                                                  blood_type_text.get("AB-"),
                                                                  blood_type_text.get("A+"),
                                                                  blood_type_text.get("A-")]:
            return True
        elif donor == blood_type_text.get("A+") and recipient in [blood_type_text.get("AB+"),
                                                                  blood_type_text.get("A+")]:
            return True
        elif donor == blood_type_text.get("AB-") and recipient in [blood_type_text.get("AB+"),
                                                                   blood_type_text.get("AB-")]:
            return True
        elif donor == blood_type_text.get("AB+") and recipient == blood_type_text.get("AB+"):
            return True
        else:
            return False
    else:
        raise TypeError

# print(check_bt(7, 1))
# hint


def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )