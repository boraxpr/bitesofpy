import numpy as np
import pandas as pd


def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    try:
        return ser.get(idx)
    except KeyError:
        raise KeyError


def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser[start:end]


def get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser.loc[start:end]


def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    data = []
    if even_index:
        for key, val in ser.items():
            if key % 2 == 0:
                data.append(val)
        newser = pd.Series(data=data, index=[x for x in range(len(data)*2) if x % 2 == 0])
    else:
        for key, val in ser.items():
            if key % 2 != 0:
                data.append(val)
        newser = pd.Series(data=data, index=[x for x in range(len(data)*2) if x % 2 != 0])
    return newser
