#!/usr/bin/python3
""" UTF-8 validation. """


def validUTF8(data):
    """ Checks if a list of integers are valid UTF-8. """
    offset = 0
    n = len(data)
    for i in range(n):
        if offset > 0:
            offset -= 1
            continue

        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False

        elif data[i] <= 0x7f:
            offset = 0

        elif data[i] & 0b11111000 == 0b11110000:
            extent = 4
            if n - i >= extent:
                next_bye = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + extent],
                ))
                if not all(next_bye):
                    return False
                offset = extent - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            extent = 3
            if n - i >= extent:
                next_bye = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + extent],
                ))
                if not all(next_bye):
                    return False
                offset = extent - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            extent = 2
            if n - i >= extent:
                next_bye = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + extent],
                ))
                if not all(next_bye):
                    return False
                offset = extent - 1
            else:
                return False
        else:
            return False
    return True
