#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    ls = [a_dictionary.get(key) for key in a_dictionary]
    maxim = lambda a, b: a if a > b else b
    i = ls[0]
    for j in ls:
        k = maxim(i, j)
        i = j
    for ke, v in a_dictionary.items():
        if v == k:
            return ke
