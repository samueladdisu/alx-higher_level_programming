#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is None or a_dictionary == {}:
        return a_dictionary
    del_key = []
    for k, v in a_dictionary.items():
        if v == value:
            del_key.append(k)
    for k in del_key:
        del a_dictionary[k]
    return a_dictionary
