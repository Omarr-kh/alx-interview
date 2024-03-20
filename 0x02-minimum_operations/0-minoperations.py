#!/usr/bin/python3
""" solution for minimum operations problem """


def minOperations(n):
    """ return min operations to get n 'H' """
    if (n < 2):
        return 0
    operations = 0
    copied_len = 0
    h_done = 1

    while h_done < n:
        if copied_len == 0:
            # first step: copy all and paste
            copied_len = h_done
            h_done += copied_len
            operations += 2
        elif n - h_done > 0 and (n - h_done) % h_done == 0:
            # copy all and paste
            copied_len = h_done
            h_done += copied_len
            operations += 2
        elif copied_len > 0:
            h_done += copied_len
            operations += 1
    return operations
