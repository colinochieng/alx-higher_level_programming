#!/usr/bin/python3

def weight_average(my_list=[]):
    ls1 = []
    ls2 = []
    sum_mul = 0
    weight = 0

    if len(my_list) == 0:
        return (0)
    for i in my_list:
        j, k = i
        ls1.append(j)
        ls2.append(k)

    for j, k in zip(ls1, ls2):
        sum_mul += j * k
    for j in ls2:
        weight += j

    return sum_mul / weight
