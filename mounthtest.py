import pytest
from month import get_month_number

@pytest.mark.parametrize("input_data, expected", [
    (["january"], 1),
    (["february"], 2),
    (["feb"], 2),
    (["February"], 2),
    (["Feb"], 2),
    (["abc"], -1),
    ([""], -1),
])
def test_get_month_number(input_data, expected):
    assert get_month_number(*input_data) == expected
