#!/usr/bin/python3
"""Pascal's Triangle Implimentation"""


def pascal_triangle(n):
    """Genrates the triangle"""
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        last = pascal[-1]
        temp = [1]
        for i in range(len(last) - 1):
            temp.append(last[i] + last[i + 1])
        temp.append(1)
        pascal.append(temp)
    return pascal
