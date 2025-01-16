import pytest
from duplicate import duplicate

@pytest.mark.parametrize("input_data, expected", [
    (["abc", 5], ["abc", "abc", "abc", "abc", "abc"]),
    (["abc", 1], ["abc"]),
    (["abc", -1], []),
    (["abc", 0], []),
    (["", 0], []),
])
def test_duplicate(input_data, expected):
    assert duplicate(*input_data) == expected
