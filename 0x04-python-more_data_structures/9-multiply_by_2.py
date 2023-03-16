#!/usr/bin/python3

def double(a):
    return a * 2


def multiply_by_2(a_dictionary):
    new_dic = {}
    for key in a_dictionary:
        new_dic[key] = double(a_dictionary[key])
    return new_dic
