#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double = lambda a: a * 2
    new_dic = {}
    for key in a_dictionary:
        new_dic[key] = double(a_dictionary[key])
    return new_dic
