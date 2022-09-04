#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return None
    v = a_dictionary.get(list(a_dictionary)[0])
    k = list(a_dictionary)[0]
    for key, value in a_dictionary.items():
        if value >= v:
            v = value
            k = key
    return k
