def get_month_number(s):
    months = [
        'jan', 'feb', 'mar', 'apr', 'may', 'jun',
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
    ]
    s_lower = s.lower()
    for i, month in enumerate(months):
        if s_lower.startswith(month):
            return i + 1
    return -1
