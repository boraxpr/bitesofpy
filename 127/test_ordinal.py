import pytest

from ordinal import get_ordinal_suffix


@pytest.mark.parametrize("input_argument, expected_return", [
    (0, '0th'),
    (1, '1st'),
    (2, '2nd'),
    (3, '3rd'),
    (4, '4th'),
    (9, '9th'),
    (10, '10th'),
    (11, '11th'),
    (12, '12th'),
    (13, '13th'),
    (20, '20th'),
    (21, '21st'),
    (22, '22nd'),
    (23, '23rd'),
    (24, '24th'),
    (25, '25th'),
    (30, '30th'),
    (50, '50th'),
    (51, '51st'),
    (52, '52nd'),
    (53, '53rd'),
    (54, '54th'),
    (55, '55th'),
    (99, '99th'),
    (100, '100th'),
    (101, '101st'),
    (102, '102nd'),
    (103, '103rd'),
    (104, '104th'),
    (110, '110th'),
    (111, '111th'),
    (1001, '1001st'),
    (1003, '1003rd'),
    (1111, '1111th'),
])
def test_ordinal(input_argument, expected_return):
    assert get_ordinal_suffix(input_argument) == expected_return