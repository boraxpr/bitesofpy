import pytest
from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize(
    "test_input, expected",
    [(15,"Fizz Buzz"), (45,"Fizz Buzz"),
     (3, "Fizz"), (9, "Fizz"), (12, "Fizz"),
     (5, "Buzz"), (10, "Buzz"), (20, "Buzz"),
     (25, "Buzz"),(30, "Buzz"), (35, "Buzz")]
)
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected