#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_to_del = []

    for i in a_dictionary:
        if a_dictionary.get(i) == value:
            key_to_del.append(i)
    for i in key_to_del:
        del a_dictionary[i]

    return a_dictionary
