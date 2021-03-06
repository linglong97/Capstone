def arbitrary_value_from_dict(d):
    """
    :param d: non-empty dictionary d
    :return: an arbitrary value from d
    """
    assert (not d == {})
    return next(iter(d.values()))


def limit_list_size(a, length):
    """
    :param a: a list of size n
    :param length: size to limit a to
    reduces the size of the larger of a to MAX_NUMBER_DATA_POINTS
    if the list exceed that size by deleting from the end
    :return: a
    """

    if len(a) > length:
        return a[-length:]

    return a


def synchronize_list(a, b):
    """
    :param a: a list of size n
    :param b: a list of size m
    reduces the size of the larger of a or b by deleting from the end
    :return: tuple a, b
    """

    if len(a) > len(b):
        return a[-len(b):], b
    elif len(a) < len(b):
        return a, b[-len(a):]
    return a, b
