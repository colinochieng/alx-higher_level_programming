#!/usr/bin/python3

def no_c(my_string):
    stri = ''
    for j in my_string:
       if j != 'c' and j != 'C':
          stri += j
    return (stri)
