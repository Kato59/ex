def parse_day(s):
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    s_lower = s.lower() 
    for i, day in enumerate(days):
        if s_lower.startswith(day):
            return i + 1
    return -1
