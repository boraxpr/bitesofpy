import string

import pandas as pd
from numpy import int64

# print([x for x in range(1, 27, 1)])
def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    return pd.Series(data=[1, 2, 3, 4, 5], dtype=int, name="Fred")


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    return pd.Series(data=[x/1000 for x in range(1001)], dtype=float)


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    return pd.Series(data=[x for x in range(1, 27, 1)], index=[c for c in string.ascii_lowercase], dtype=int64)


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    return pd.Series(data=[c for c in string.ascii_uppercase], index=[x for x in range(101, 127, 1)], dtype=object)