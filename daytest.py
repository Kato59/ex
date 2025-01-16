def parse_day(s):
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    s_lower = s.lower().strip()  # Convert input to lowercase and trim whitespace
    for i, day in enumerate(days):
        if s_lower.startswith(day):
            return i + 1
    return -1

import pytest

@pytest.mark.parametrize("input_data, expected", [
    (["friday"], 6),
    (["Friday"], 6),
    (["Fri"], 6),
    (["monday"], 2),
    (["Mon"], 2),
    (["abc"], -1),
    ([""], -1),
    (["   fri"], 6),
])
def test_parse_day(input_data, expected):
    assert parse_day(*input_data) == expected
