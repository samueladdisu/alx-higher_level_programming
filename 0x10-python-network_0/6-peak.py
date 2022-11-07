#!/usr/bin/python3
"""
Find peak module
"""


def find_peak(list_of_integers):
    """ find peak """
    ls = list_of_integers
    if len(ls) == 0:
        return None
    elif len(ls) == 1:
        return ls[0]
    else:
        i = 0
        le = len(ls)
        max = ls[0]
        while True:
            if max < ls[i]:
                max = ls[i]
            i += 1
            if i >= le:
                break
    return max
