#!/usr/bin/python3
i = 122


while i != 96:
    if i % 2 == 1:
        j = i - 32
    else:
        j = i
    print('{:c}'.format(j), end="")
    i = i - 1
