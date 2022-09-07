#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list is None or my_list == {}:
        return 0
    Num, denom = 0, 0
    for t in my_list:
        Num = Num + t[0] * t[1]
        denom = denom + t[1]
    if denom == 0:
        return 0
    return Num / denom
