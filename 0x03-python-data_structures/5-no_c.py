#!/usr/bin/python3

def no_c(my_string):
    stri = ''
    for j in my_string:
        if j == 'c' or j == 'C':
            continue
        else:
            stri += j
    return (stri)
