def duplicate(value, n):
    """Generate a list with the given value repeated n times.

    Args:
        value: The value to be duplicated.
        n (int): The number of times to duplicate the value.

    Returns:
        list: A list containing the duplicated values.
    """
    if n <= 0:
        return []
    return [value] * n
