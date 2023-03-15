#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_list = []
    for i in matrix:
        sq_idx = list(map(lambda a: a ** 2, i))
        sq_list.append(sq_idx)
    return sq_list
