#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double = lambda a: a * 2
    new_dic = {}
    for key in a_dictionary:
        result = double(a_dictionary[key])
        new_dic[key] = result
    return new_dic
